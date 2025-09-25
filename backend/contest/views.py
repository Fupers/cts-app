from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Contestant
from .serializers import ContestantSerializer
from django.core.mail import send_mail
import random
from .tasks import send_verification_email, send_winner_email
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from .tokens import account_token
from rest_framework_simplejwt.views import TokenObtainPairView

# registrar concursante
class RegisterContestantView(generics.CreateAPIView):
  serializer_class = ContestantSerializer
  permission_classes = [AllowAny]

  def post(self, request, *args, **kwargs):
    email = request.data.get('email')

    if Contestant.objects.filter(email=email).exists():
      return Response({'error': 'Este email ya está registrado.'}, status=status.HTTP_400_BAD_REQUEST)

    response = super().post(request, *args, **kwargs)
    send_verification_email.delay(response.data['id'])

    return response

# lista de concursantes
class ContestantListView(generics.ListAPIView):
  queryset = Contestant.objects.all().order_by('-created_at')
  serializer_class = ContestantSerializer
  permission_classes = [IsAdminUser]

# verificar concursante
class VerifyAccountView(APIView):
  permission_classes = [AllowAny]
  
  def post(self, request, *args, **kwargs):
    token = request.data.get("token")
    password = request.data.get("password")

    if not token or not password:
      return Response(
        {"error": "Token y contraseña son requeridos"},
        status=status.HTTP_400_BAD_REQUEST
      )

    # validar token
    user_id = account_token.check_token(token)
    if not user_id:
      return Response(
        {"error": "Token inválido o expirado"},
        status=status.HTTP_400_BAD_REQUEST
      )

    contestant = get_object_or_404(Contestant, id=user_id)
    contestant.password = make_password(password)
    contestant.is_verified = True
    contestant.save()

    return Response(
      {"message": "Cuenta activada correctamente"},
      status=status.HTTP_200_OK
    )

# generar ganador
class DrawWinnerView(APIView):
  permission_classes = [IsAdminUser]

  def post(self, request, *args, **kwargs):
    verified = Contestant.objects.filter(is_verified=True)
    if not verified.exists():
      return Response(
        {"error": "No hay concursantes verificados"},
        status=status.HTTP_400_BAD_REQUEST
      )

    # Selecciona al azar un ganador
    winner = random.choice(list(verified))

    # No enviamos correo aquí
    return Response(
      {
        "id": winner.id,
        "name": winner.name,
        "email": winner.email
      },
      status=status.HTTP_200_OK
  )

# notificar al ganador
class NotifyWinnerView(APIView):
  permission_classes = [IsAdminUser]

  def post(self, request, *args, **kwargs):
    winner_id = request.data.get("winner_id")

    if not winner_id:
      return Response(
        {"error": "Se requiere el ID del ganador"},
        status=status.HTTP_400_BAD_REQUEST
      )

    try:
      winner = Contestant.objects.get(id=winner_id, is_verified=True)
    except Contestant.DoesNotExist:
      return Response(
        {"error": "Ganador no encontrado o no verificado"},
        status=status.HTTP_404_NOT_FOUND
      )

    # Aquí enviamos correo solo al presionar "Mandar correo"
    send_winner_email.delay(winner.id)

    return Response(
      {"message": f"Correo enviado a {winner.email}"},
      status=status.HTTP_200_OK
    )
from celery import shared_task
from django.core.mail import send_mail
from .models import Contestant
from django.conf import settings
from .tokens import account_token

# Mandar correo de verificacion
@shared_task
def send_verification_email(user_id):
    contestant = Contestant.objects.get(id=user_id)
    token = account_token.generate_token(user_id)
    verification_url = f"http://localhost:5173/verify/{token}"

    send_mail(
        "Verifica tu cuenta",
        f"Hola {contestant.name}, haz clic aquí para activar tu cuenta: {verification_url}",
        settings.DEFAULT_FROM_EMAIL,
        [contestant.email],
        fail_silently=False,
    )

# Mandar correo de ganador
@shared_task
def send_winner_email(user_id):
    winner = Contestant.objects.get(id=user_id)
    subject = "¡Felicidades, eres el ganador!"
    message = f"Hola {winner.name},\n\nHas sido seleccionado como ganador del sorteo Felicidades!"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [winner.email],
        fail_silently=False,
    )

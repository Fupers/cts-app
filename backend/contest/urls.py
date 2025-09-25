from django.urls import path
from .views import RegisterContestantView, ContestantListView, VerifyAccountView, DrawWinnerView, NotifyWinnerView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
  path('contest/register/', RegisterContestantView.as_view(), name='register'),
  path('admin/contest/', ContestantListView.as_view(), name='contestant-list'),
  path('contest/verify/', VerifyAccountView.as_view(), name='verify'),
  path("admin/draw_winner/", DrawWinnerView.as_view(), name="draw_winner"),
  path("admin/notify_winner/", NotifyWinnerView.as_view(), name="notify_winner"),
  path('admin/login/', TokenObtainPairView.as_view(), name='admin-login'),
]
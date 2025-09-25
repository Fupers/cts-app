from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class ContestantManager(BaseUserManager):
  def create_user(self, email, name, phone, password=None):
    if not email:
      raise ValueError("El email es obligatorio")

    email = self.normalize_email(email)
    user = self.model(email=email, name=name, phone=phone)

    if password:
      user.set_password(password)

    user.save(using=self._db)
    return user

class Contestant(AbstractBaseUser):
  name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=20)
  is_verified = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  objects = ContestantManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'phone']

  def __str__(self):
    return self.email
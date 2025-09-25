from itsdangerous import URLSafeTimedSerializer
from django.conf import settings

serializer = URLSafeTimedSerializer(settings.SECRET_KEY)

class AccountToken:
  def generate_token(self, user_id):
    return serializer.dumps(user_id, salt="email-verify")

  def check_token(self, token, max_age=3600):
    try:
      return serializer.loads(token, salt="email-verify", max_age=max_age)
    except Exception:
      return None

account_token = AccountToken()

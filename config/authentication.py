from rest_framework.authentication import BaseAuthentication
from django.conf import settings
import jwt
from users.models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("jwt-auth") # jwt token 

        if not token:
            return None
        
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        user_id = decoded.get('id')
        user = User.objects.get(id=user_id)

        return (user, None)
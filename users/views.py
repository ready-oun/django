from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password

# api/v1/users [POST] ==> 유저 생성 API

class Users(APIView):
    def post(self, request):
        # pswd => verification is needed and hash save needed
        # the other => other datas except pswd

        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)

        try:
            validate_password(password)

        except:
            raise ParseError("Invalid password")
        
        if serializer.is_valid():
            user = serializer.save() # create a new user
            user.set_password(password) # hashing pswd
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)

# api/v1/users/myinfo [GET, PUT] ==> update datas        
class MyInfo(APIView):
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)

        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)

            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
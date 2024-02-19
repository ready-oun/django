from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.authentication import TokenAuthentication # 사용자 인증: 어떤 유저인지 식별하기 위한 API
from rest_framework.permissions import IsAuthenticated # 권한 부여: 인증된 유저들만 볼 수 있는 페이지 

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
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

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
# api/v1/login
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ParseError()
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

# api/v1/logout
class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("header :", request.headers)
        logout(request)

        return Response(status=status.HTTP_200_OK)
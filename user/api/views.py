from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.api.serializers import UserSerializer, UserLoginSerializer


class RegisterUserAPI(generics.CreateAPIView):
    """
    RegisterUserAPI api to register a new user to the system
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"result": serializer.data, "message": "Done", "status": True}, status=201)
        return Response({"message": serializer.errors, "status": False}, status=400)


class LoginUserAPI(APIView):
    """
    LoginUserAPI api to log the user to be allowed to use the system
    """
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            return Response({"result": serializer.data, "message": "Done", "status": True}, status=201)
        return Response({"message": serializer.errors, "status": False}, status=400)

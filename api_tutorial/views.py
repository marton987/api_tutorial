from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from api_tutorial.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User ViewSet
    POST: Creates a new User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        """
        Creates a new User
        :return: ({Object}) Returns the new user object, or an error
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = User.objects.create(**serializer.validated_data, is_active=False)
            return Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Please provide all required fields.',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

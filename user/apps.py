from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from sales.models import Sale


def groups_creation():
    employee, exists = Group.objects.get_or_create(name='employee')

    permission_for_groups(employee)

    return(exists)


def permission_for_groups(*groups):
    for group in groups:
        permissions = []

        if 'employee' == group.name:
            content_type = ContentType.objects.get_for_model(Sale)

            permissions.extend([
                Permission.objects.get(codename='add_sale'),
            ]
            )

        for permission in permissions:
            group.permissions.add(permission)


class AccountView(APIView):
    groups_creation()

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        token = request.META['HTTP_AUTHORIZATION'].strip('Token ')
        user = UserSerializer(Token.objects.get(key=token).user).data

        if user['is_superuser']: 
            if serializer.data['is_staff'] == True:
                user = User.objects.create_user(**request.data)
                user.groups.add(Group.objects.get(name='seller'))

                serializer = UserSerializer(user)

                return Response(serializer.data, status.HTTP_201_CREATED)

        
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data['username'], password=request.data['password'])

        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key})

        return Response(status=status.HTTP_401_UNAUTHORIZED)

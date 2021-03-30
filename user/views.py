# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User, Group, Permission
# from django.contrib.auth import authenticate
# from django.contrib.contenttypes.models import ContentType

# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token

# from .serializers import UserSerializer

# from sales.models import Sale

# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


# if not User.objects.filter(username='gerente').exists():
#     User.objects.create_superuser('gerente', '', '1234')



# class LoginView(APIView):
#     def post(self, request):
#         print(request.data['username'])
#         user = authenticate(
#             username=request.data['username'],password=request.data['password'])
        
#         if user is not None:
#             token = Token.objects.get_or_create(user=user)[0]
#             return Response({'token': token.key})


#         return Response(status=status.HTTP_401_UNAUTHORIZED)

# class RedirectView(APIView):
#     def get(self,request):
#         return redirect('/menu/')

# class LoginPage(APIView):
#     def get(self, request):
#         return render(request, 'login.html')

# class UserCategoryView(APIView):
#     def post(self,request):
#         token = dict(request.data)['token'][0]
#         try:
#             user = UserSerializer(Token.objects.get(key=token).user).data
#             if user['is_superuser'] == True:
#                 return Response('super_user')
#         except:
#             return Response('')
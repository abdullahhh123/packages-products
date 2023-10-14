from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
# from api.serializers 
from package.api.serailizers import UserSerialzer , PackageSerializer , SubscriptionSerializer
from rest_framework.response import Response
from .models import User , Package
# python3 -m pip install pyJWT to be installed
import jwt , datetime
from collections import OrderedDict , defaultdict
from django.forms.models import model_to_dict

# python3 -m pip install django-cors-headers to be installed

# Create your views here.



class RegisterView(APIView):
    def post(self , request,**kwargs):
        # self.http_method_names.append("GET")
        serializer = UserSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self,request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User Not Found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload , 'secret' , algorithm='HS256')
        respone = Response()

        ## Setting this token to the cookies
        respone.set_cookie(key='jwt' , value=token , httponly=True)

        respone.data = {"jwt":token}
        return respone
    

class UserView(APIView):
    def get(self , request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token , 'secret' , algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerialzer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self , request):
        response = Response()
        response.delete_cookie('jwt')
        response.date = {
            'message':'logged out successfuly'
        }
        return response
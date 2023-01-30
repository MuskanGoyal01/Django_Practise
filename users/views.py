from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer

from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
@api_view(["POST"])
def Register_Users(request):
    print(request.data)
    serializer = RegistrationSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def LogIn_Users(request):
    print(request.data)

    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()

    if user is None:
        raise AuthenticationFailed("User not found!")

    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect Password!")

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        "jwt": token
    }

    return response


@api_view(["GET"])
def view_user(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed("Unauthenticated!")

    try:
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")

    user = User.objects.filter(id=payload['id']).first()
    serializer = RegistrationSerializer(user)

    return Response(serializer.data)


@api_view(["POST"])
def LogOut_Users(request):
    print(request.data)

    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'Logged out Successfully.'
    }

    return response


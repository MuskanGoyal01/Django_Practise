from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegistrationSerializer
from ..api.views import MyTokenObtainPairSerializer

# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def Register_Users(request):
    try:
        data = []
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            account.save()
            token = Token.objects.get_or_create(user=account)[0].key
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username
            data["token"] = token

        else:
            data = serializer.errors


        return Response(data)
    except IntegrityError as e:
        account=User.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})

    except KeyError as e:
        print(e)
        raise ValidationError({"400": f'Field {str(e)} missing'})


from rest_framework import authentication
from gustavo.models import Gordinho
from .serializers import GordinhoSerializer
from rest_framework import viewsets


class GordinhoViewSet(viewsets.ModelViewSet):
    serializer_class = GordinhoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Gordinho.objects.all()

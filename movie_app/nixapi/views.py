from rest_framework.viewsets import ModelViewSet
from movie_app.models import Movies
from .SER import NIXSER
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class NIXAPI(ModelViewSet):
    serializer_class = NIXSER
    queryset = Movies.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]



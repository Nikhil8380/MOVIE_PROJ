from rest_framework import serializers
from rest_framework.response import Response
from movie_app.models import Movies

class NIXSER(serializers.ModelSerializer):
    class Meta():
        model=Movies
        fields='__all__'
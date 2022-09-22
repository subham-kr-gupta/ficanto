from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        user_obj = User.objects.all()
        serializer = UserSerializer(user_obj, many=True)  # We have multiple data that's why many=True
        return Response({'status': 200, "data": serializer.data, "message": "User List"})

    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            print(serializer.errors)
            return Response({'status': 403, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 201, 'data': serializer.data})

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response({'status': 200, 'data': serializer.data})

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
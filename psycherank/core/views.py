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
    queryset = User.objects.all()
    
    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)  # We have multiple data that's why many=True
        return Response({'status': 200, "data": serializer.data, "message": "User List"})

    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            print(serializer.errors)
            return Response({'status': 403, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 201, 'data': serializer.data})

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response({'status': 200, 'data': serializer.data})

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 201, 'data': serializer.data})
        
        return Response({'status': 403, 'message': 'Something went wrong'})


    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        return Response({'status': 204, 'data': 'User deleted!!'})


class QuestionnaireViewSet(viewsets.ViewSet):
    queryset = Questionnaire.objects.all()
    
    def list(self, request):
        serializer = QuestionnaireSerializer(self.queryset, many=True)  # We have multiple data that's why many=True
        return Response({'status': 200, "data": serializer.data})

    def create(self, request):
        serializer = QuestionnaireSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            print(serializer.errors)
            return Response({'status': 403, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 201, 'data': serializer.data})

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = QuestionnaireSerializer(item)
        return Response({'status': 200, 'data': serializer.data})

    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = QuestionnaireSerializer(item, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 201, 'data': serializer.data})
        
        return Response({'status': 403, 'message': 'Something went wrong'})


    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response({'status': 204, 'data': 'Item deleted!!'})


class AssessmentViewSet(viewsets.ViewSet):
    queryset = Assessment.objects.all()
    
    def list(self, request):
        serializer = AssessmentSerializer(self.queryset, many=True)  # We have multiple data that's why many=True
        return Response({'status': 200, "data": serializer.data})

    def create(self, request):
        serializer = AssessmentSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            print(serializer.errors)
            return Response({'status': 403, 'message': 'Something went wrong'})

        serializer.save()
        return Response({'status': 201, 'data': serializer.data})

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = AssessmentSerializer(item)
        return Response({'status': 200, 'data': serializer.data})

    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = AssessmentSerializer(item, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': 201, 'data': serializer.data})
        
        return Response({'status': 403, 'message': 'Something went wrong'})


    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response({'status': 204, 'data': 'Item deleted!!'})


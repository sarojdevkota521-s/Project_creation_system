from django.shortcuts import render
from .models import Project

from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from .serializers import ProjectSerializer

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()  
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return Project.objects.all().select_related('creator')
        return Project.objects.all()
        
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.creator != self.request.user:
            raise PermissionDenied("You cannot edit this project.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise PermissionDenied("You cannot delete this project.")
        instance.delete()

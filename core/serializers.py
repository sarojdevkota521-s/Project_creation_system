from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['creator']

    
    # user can view their project all details but not others
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     request = self.context.get('request')

    #     if request and instance.creator != request.user:
    #         allowed_fields = ['title', 'description']
        
    #         keys = list(representation.keys())
    #         for key in keys:
    #             if key not in allowed_fields:
    #                 representation.pop(key)
                    
    #     return representation
        
from django.shortcuts import render
from django.http import HttpResponse
from dogs.models import DogDB, BreedDB
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

def index(request):
    return HttpResponse("Hello, world.")

class BreedDBSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    size = serializers.CharField(max_length=30)
    friendliness = serializers.IntegerField()
    trainability = serializers.IntegerField() 
    sheddingamount = serializers.IntegerField()
    exerciseneeds = serializers.IntegerField() 
    
    def create(self, validated_data):
        return BreedDB.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        instance.save()
        return instance
    
class BreedDBViewSet(viewsets.ModelViewSet):

    queryset = BreedDB.objects.all()
    serializer_class = BreedDBSerializer
    
    def list(self, request):
        serializer = BreedDBSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = BreedDBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = BreedDBSerializer(item)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = BreedDBSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DogDBSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(default=1)
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField(default=1)
    breed = serializers.PrimaryKeyRelatedField(queryset=BreedDB.objects.all())
    gender = serializers.CharField(max_length=30)
    color = serializers.CharField(max_length=30)
    favoritefood = serializers.CharField(max_length=30)
    favoritetoy = serializers.CharField(max_length=30)
    
    def create(self, validated_data):
        return DogDB.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()
        return instance

class DogDBViewSet(viewsets.ModelViewSet):

    queryset = DogDB.objects.all()
    serializer_class = DogDBSerializer
    
    def list(self, request):
        serializer = DogDBSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = DogDBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = DogDBSerializer(item)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = DogDBSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

from django.shortcuts import render

from django.http import Http404,HttpResponse
from .models import Persons
from .serializers import PersonSerializer
from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response    
class PersonList(APIView):
    def get(self,request):
        person=Persons.objects.all()
        serializer = PersonSerializer(person,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_CREATED)
        
    


class PersonDetail(APIView):
    def get_person(self,pk):
        try:
            return Persons.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,reuqest,pk):
        person = self.get_person(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self,request,pk):
        person = self.get_person(pk)
        serializer = PersonSerializer(person,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_CREATED)
    
    def delete(self,request,pk):
        person = self.get_person(pk)
        person.delete()
        return Response(status.HTTP_404_CREATED)


               
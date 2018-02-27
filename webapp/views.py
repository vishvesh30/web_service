from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import employees
from .serializers import employeeSerializer


@api_view(['GET', 'POST', ])
def get_list(request):
    if request.method == 'GET':
        print("in data")
        employees1 = employees.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', ])
def employeedetail(request, emp_id):
    print("in id")
    if request.method == 'GET':
        print("emp:-" + emp_id)
        employees1 = employees.objects.get(emp_id=emp_id)
        serializer = employeeSerializer(employees1,many=False)
        return Response(serializer.data)

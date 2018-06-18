from django.http import HttpResponse
from period.models import AcademicPeriod
from .serializers import AcademicPeriodSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def periods(request):
    if request.method == 'GET':
        periods = AcademicPeriod.objects.all()
        serializer = AcademicPeriodSerializer(periods, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AcademicPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        AcademicPeriod.objects.all().delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def period_detail(request, pk):
    try:
        period = AcademicPeriod.objects.get(pk=pk)
    except AcademicPeriod.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AcademicPeriodSerializer(period)
        return Response(serializer.data)

    if request.method == 'POST':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AcademicPeriodSerializer(period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        period.delete()
        return Response(status=status.HTTP_200_OK)

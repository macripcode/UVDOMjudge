from django.http import HttpResponse
from course.models import Course
from .serializers import CourseSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def courses(request):

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        Course.objects.all().delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    if request.method == 'POST':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def filter_period(request, id_academic_period):
    try:
        courses = Course.objects.filter(academic_period=id_academic_period)
    except Course.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        courses.delete()
        return Response(status=status.HTTP_200_OK)




        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def filter_professor(request, id_professor):
    if request.method == 'GET':
        courses = Course.objects.filter(professor_course=id_professor)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def filter_signature(request, id_signature):
    if request.method == 'GET':
        courses = Course.objects.raw('select * from api.course_course where code_course like \'%' + id_signature+ '%\';')

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        return Response(status=status.HTTP_404_NOT_FOUND)


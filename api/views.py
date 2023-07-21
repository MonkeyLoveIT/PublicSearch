from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from firstapp.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@swagger_auto_schema(
    method='post',
    request_body=BookSerializer(many=True),
    responses={
        201: 'Created',
        400: 'Bad Request',
    },
    operation_summary="Import Data",
    operation_description="Import multiple book records.",
)
@api_view(['POST'])
def import_data(request):
    if request.method == 'POST':
        data_list = request.data
        serializer = BookSerializer(data=data_list, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
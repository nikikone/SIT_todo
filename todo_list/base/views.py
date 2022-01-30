"""Документация."""
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from .models import ToDo, File
from .serializers import ToDoSerializer, FileSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
import mimetypes


def taskList(request):
    """Документация."""
    return HttpResponse('To Do list')
# Create your views here.


class FileView(APIView):
    """Документация."""

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """Документация."""
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """Документация."""
        response = []
        for e in File.objects.all():
            file_obj = {
                "name": e.file.name,
                "size": str(e.file.size) + 'b',
            }
            response.append(file_obj)
        return Response(response, status=status.HTTP_200_OK)


class FileViewDetail(APIView):
    """Документация."""

    def get(self, *args, **kwargs):
        """Документация."""
        response = 0
        file_path = ""
        name_file = ""
        for e in File.objects.all():
            if e.file.name == self.kwargs['pk']:
                file_path = '.' + e.file.url
                name_file = e.file.name
                response = 1
                break
        # return Response(File.objects.all(), status=status.HTTP_200_OK)
        if response > 0:
            FilePointer = open(file_path, 'rb')
            file_type = mimetypes.guess_type(name_file)
            response = HttpResponse(FilePointer, content_type=file_type[0])
            response['Content-Disposition'] = 'attachment; filename=' + name_file
            return response
        response = "Not Found"
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    def delete(self, *args, **kwargs):
        """Документация."""
        for e in File.objects.all():
            if e.file.name == self.kwargs['pk']:
                response = e.delete()
                return Response(response, status=status.HTTP_200_OK)
        response = "File not Found"
        return Response(response, status=status.HTTP_404_NOT_FOUND)


class UserList(generics.ListAPIView):
    """Документация."""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Документация."""
        user = self.request.user
        serializer.save(user=user)


class UserDetail(generics.RetrieveAPIView):
    """Документация."""

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class ToDoList(generics.ListCreateAPIView):
    """Документация."""

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Документация."""
        return ToDo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Документация."""
        # todo = self.request.todo
        serializer.save(owner=self.request.user)


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    """Документация."""

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthenticated]

    def get_queryset(self):
        """Документация."""
        return ToDo.objects.filter(owner=self.request.user)

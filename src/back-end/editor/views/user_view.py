from django.shortcuts import redirect
from django.http.response import Http404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import CustomUser
from ..serializers import UserSerializer


class UserList(generics.ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(APIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        obj = CustomUser.objects.filter(pk=user.id)
        return Response(serializer.data)

    def put(self, request):
        user = CustomUser.objects.filter(pk=self.request.user.id)
        serializer = UserSerializer(user[0], data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view()
def success_email_confirm(request, key):
    front_url = 'http://localhost:4001/login'
    return redirect(front_url)


@api_view()
def redirect_front_login(request):
    front_url = 'http://localhost:4001/login'
    return redirect(front_url)


@api_view()
def redirect_front_register(request):
    front_url = 'http://localhost:4001/signin'
    return redirect(front_url)

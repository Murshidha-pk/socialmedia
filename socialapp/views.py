from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from socialapp.serializers import UserSerializer,PostSerializer

from socialapp.models import Post

from rest_framework import authentication,permissions
# Create your views here.

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

#for authtoke

#installed app > rest_framework.authtoken > migrate
#urls > Obtainauthtoken > import from rest_framework.authtoken.views import Obtainauthtoken

class PostCreateListView(ListAPIView,CreateAPIView):

    queryset=Post.objects.all()       #for working list

    serializer_class=PostSerializer    #for working create

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

#from create (django provide) when save for owner > overriding
    def perform_create(self, serializer):
        
        serializer.save(owner=self.request.user)

class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    
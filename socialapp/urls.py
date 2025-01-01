from django.urls import path

from socialapp import views

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[

    path('signup/',views.SignUpView.as_view()),

    path('token/',ObtainAuthToken.as_view()),

    path('posts/',views.PostCreateListView.as_view()),

    path('posts/<int:pk>/',views.PostRetrieveUpdateDestroyView.as_view()),

    path('posts/<int:pk>/add-like/',views.PostLikeView.as_view()),

    path('posts/<int:pk>/add-comment/',views.PostCommentView.as_view()),

    path('profile/change/',views.UserProfileView.as_view()),

    

]
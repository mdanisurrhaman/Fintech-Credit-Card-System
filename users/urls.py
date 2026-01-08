from django.urls import path
from .views import RegisterView, ProtectedView
from .views import LogoutAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('protected/', ProtectedView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

]

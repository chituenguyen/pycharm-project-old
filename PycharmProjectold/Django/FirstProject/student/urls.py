from django.urls import path,include
from . import views,models
from .models import student
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.generics import RetrieveAPIView,ListAPIView


urlpatterns=[
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('travel', views.travel, name='travel'),
]
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = ['id','name','birthday','email','course_student']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.student.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('student', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from django.urls import include, path
from rest_framework import routers
from . import views

router1 = routers.DefaultRouter()
router1.register(r'quiz', views.QuizViewSet)

router2 = routers.DefaultRouter()
router2.register(r'questions', views.QuestionsViewSet)

urlpatterns = [
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
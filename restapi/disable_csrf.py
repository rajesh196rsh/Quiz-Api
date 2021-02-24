from rest_framework import serializers
from .models import quiz, questions

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = quiz 
        fields = ('id','name','description')


class QuestionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = questions
        fields = ('id','name','options','correct_option','quiz','points')
        

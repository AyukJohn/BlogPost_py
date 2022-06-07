# from curses import meta
from rest_framework import serializers
from .models import AboutMe


class AboutMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutMe
        fields = ['id', 'aboutMe', 'aboutBlog', 'mySkills', 'myProjects', 'img']
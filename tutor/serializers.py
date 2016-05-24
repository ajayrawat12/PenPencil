"""Ser."""

from rest_framework import serializers
from tutor.models import TutorProfile


class TutorSerializer(serializers.ModelSerializer):
    """DOC."""

    class Meta:
        """DOC."""

        model = TutorProfile
        fields = ('username', 'password', 'age', 'email', 'name')

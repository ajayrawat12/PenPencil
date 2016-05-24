"""views for REST."""
#from django.shortcuts import HttpResponseRedirect
from rest_framework import generics
#from rest_framework import mixins
from .models import TutorProfile
from .serializers import TutorSerializer
# from django.shortcuts import render_to_response
# from django.core.context_processors import csrf
#import ipdb


class TutorList(generics.ListCreateAPIView):
    """List all tutor."""

    queryset = TutorProfile.objects.all()
    serializer_class = TutorSerializer


class TutorDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a tutor instance."""

    queryset = TutorProfile.objects.all()
    serializer_class = TutorSerializer

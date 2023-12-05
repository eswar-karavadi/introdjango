from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status


# Create your views here.
reviews = [
            'app dev is great',
            'you should join',
            'hello world',
            'welcome to intro to django'
        ]

class AppDevClubReviewsView(APIView):
    def get(self, request):
        return Response({'reviews': reviews})

class AppDevClubReviewsAdd(APIView):
    def post(self, request):
        user_review = request.POST['user_review']
        reviews.append(user_review)
        return Response({'status': 'Review added successfully'})
from django.shortcuts import render
from .models import Reviews
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

# api/v1/reviews [GET]
class ReviewsList(APIView):
    def get(self, request):
        reviews = Reviews.objects.all()
        # reviews == django obj, so it needs to be jsonified => need werializers 
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

# api/v1/review_id [GET]
class ReviewDetail(APIView):
    def get(self, request, review_id):
        try: 
            review = Reviews.objects.get(id=review_id)
        except:
            raise NotFound
        
        serializer = ReviewSerializer(review)

        return Response(serializer.data)
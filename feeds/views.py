from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
from .serializers import FeedSerializer
from rest_framework.exceptions import NotFound

# api/v1/feeds [POST]

class Feeds(APIView):
    # 전체 게시글 데이터 조회
    def get(self, request):
        feeds = Feed.objects.all() # 객체 
        # 객체 -> JSON (serialize)
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        # 역직렬화 : 클라이언트가 보내준 json -> obj
        serializer = FeedSerializer(data=request.data)

        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            # print("post serializer", serializer)

            serializer = FeedSerializer(feed)

            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)

class FeedDetail(APIView):
    def get_object(self, feed_id):
        try: 
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound 

    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        # feed(obj) => json : serializer 
        serializer = FeedSerializer(feed)

        return Response(serializer.data)
from rest_framework.serializers import ModelSerializer
from .models import Reviews
from users.serializers import FeedUserSerializer

class ReviewSerializer(ModelSerializer):
    user = FeedUserSerializer()
    class Meta:
        model = Reviews
        fields = '__all__'
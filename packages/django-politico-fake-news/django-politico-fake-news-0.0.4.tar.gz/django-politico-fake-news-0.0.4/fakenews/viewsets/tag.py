from .base import TokenAuthedViewSet

from taggit.models import Tag
from fakenews.serializers import TagSerializer


class TagViewset(TokenAuthedViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'value'
    throttle_classes = []

from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from fakenews.models import Claim
from .share import ShareSerializer


class ClaimSerializer(TaggitSerializer, serializers.ModelSerializer):
    disinformation_type = serializers.SerializerMethodField()
    share_set = ShareSerializer(many=True, read_only=True)
    tags = TagListSerializerField(read_only=True)

    def get_disinformation_type(self, obj):
        return obj.disinformation_type.pk

    class Meta:
        model = Claim
        fields = (
            "disinformation_type",
            "text",
            "short_text",
            "canoncial_url",
            "archive_url",
            "share_set",
            "tags"
        )

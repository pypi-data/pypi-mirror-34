from rest_framework import serializers
from fakenews.models import FactCheck

from .claim import ClaimSerializer
from .user import UserSerializer


class FactCheckSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    claim_reviewed = ClaimSerializer()
    author = UserSerializer()

    def get_author(self, obj):
        return obj.author.last_name

    def get_claim_reviewed(self, obj):
        return obj.claim_reviewed.text

    class Meta:
        model = FactCheck
        fields = "__all__"


class FactCheckListSerializer(serializers.ModelSerializer):
    claim_reviewed = serializers.SerializerMethodField()
    disinformation_type = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    def get_claim_reviewed(self, obj):
        return obj.claim_reviewed.short_text

    def get_disinformation_type(self, obj):
        return obj.claim_reviewed.disinformation_type.label

    def get_author(self, obj):
        return obj.author.__str__()

    def get_tags(self, obj):
        output = []
        for tag in obj.claim_reviewed.tags.all():
            output.append(tag.slug)

        output = list(set(output))
        return output

    class Meta:
        model = FactCheck
        fields = (
            "id",
            "claim_reviewed",
            "disinformation_type",
            "publish_date",
            "author",
            "tags"
        )

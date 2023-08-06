from .base import TokenAuthedViewSet

from fakenews.models import FactCheck
from fakenews.serializers import FactCheckSerializer, FactCheckListSerializer


class FactCheckViewset(TokenAuthedViewSet):
    queryset = FactCheck.objects.all()
    serializer_class = FactCheckSerializer
    lookup_field = 'pk'
    throttle_classes = []

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'list':
            return FactCheckListSerializer
        return FactCheckSerializer

    def get_queryset(self):
        queryset = FactCheck.objects.all()

        # Filter by disinformation_type
        disinformation_type = self.request.query_params.get(
            'disinformation_type',
            None
        )
        if disinformation_type:
            queryset = queryset.filter(
                claim_reviewed__disinformation_type__label=disinformation_type
            )

        # Filter by tags on the claim
        tags = self.request.query_params.get('tags', None)
        if tags:
            tags = tags.split(',')
            queryset = queryset.filter(
                claim_reviewed__tags__slug__in=tags
            ).distinct()

        return queryset

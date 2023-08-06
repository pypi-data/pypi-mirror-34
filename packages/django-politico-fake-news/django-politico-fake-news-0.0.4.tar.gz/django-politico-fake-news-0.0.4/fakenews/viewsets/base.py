from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..authentication import TokenAPIAuthentication


class TokenAuthedViewSet(ModelViewSet):
    """
    ViewSet class that restricts views to our bots token.
    Also disables the default pagination.
    """
    authentication_classes = (TokenAPIAuthentication,)
    permission_classes = (IsAuthenticated,)
    paginator = None

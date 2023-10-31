import logging

from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST

from users.views import login_required

from .models import (
    ConsumerGroup,
    ProducerGroup,
)

logger = logging.getLogger(__name__)


# pyright issues
# A user request is an authenticated user
class UserRequest(HttpRequest):
    user: User

# Create your views here.


@login_required
@require_POST
def create_consumer_group(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"details": "success"})


@login_required
@require_POST
def create_producer_group(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"details": "success"})


@login_required
@require_POST
def create_community(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"details": "success"})


@login_required
@require_POST
def send_invitation(request: UserRequest) -> JsonResponse:
    return JsonResponse({})


@login_required
@require_POST
def accept_invitation(request: UserRequest) -> JsonResponse:
    return JsonResponse({})


@login_required
@require_POST
def reject_invitation(request: UserRequest) -> JsonResponse:
    return JsonResponse({})


@login_required
def get_invitations_for_user(request: UserRequest) -> JsonResponse:
    return JsonResponse({})


@login_required
def get_user_groups(request: UserRequest) -> JsonResponse:
    producer_groups_qs = ProducerGroup.objects.filter(users__pk=request.user.pk)
    consumer_groups_qs = ConsumerGroup.objects.filter(users__pk=request.user.pk)
    communities = []
    producer_groups = [group.name for group in producer_groups_qs]
    consumer_groups = [group.name for group in consumer_groups_qs]
    return JsonResponse(
        {
            "producer_groups": producer_groups,
            "consumer_groups": consumer_groups,
            "communities": communities,
        }
    )

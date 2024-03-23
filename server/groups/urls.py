from django.urls import path

from . import views

urlpatterns = [
    path(
        "create-consumer-group",
        views.create_consumer_group,
        name="api-create-consumer-group",
    ),
    path(
        "create-producer-group",
        views.create_producer_group,
        name="api-create-producer-group",
    ),
    path("create-community-group", views.create_community, name="api-create-community"),
    path("send-invitation", views.send_invitation, name="api-send-invitation"),
    path("accept-invitation", views.accept_invitation),
    path("reject-invitation", views.reject_invitation),
    path("get-invitations-for-user", views.get_invitations_for_user),
    path("get-user-groups", views.get_user_groups),
]

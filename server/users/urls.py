from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view, name="api-login"),
    path("logout/", views.logout_view, name="api-logout"),
    path("session/", views.session_view, name="api-session"),
    path("whoami/", views.whoami, name="api-whoami"),
    path("create-account/", views.create_account, name="api-create-account"),
    path("recover-password/", views.recover_password, name="api-recover-password"),
    path("update-password/", views.update_password, name="api-update-password"),
    path(
        "activate-account/<slug:email_token>",
        views.activate_account,
        name="api-activate-account",
    ),
    path("trigger-error/", views.trigger_error),
    path("say-hello/", views.say_hello),
]

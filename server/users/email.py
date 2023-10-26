from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_email(recipient: str, username: str, email_token: str, locale: str):
    """Sends confirmation email"""
    app_url = settings.APP_URL

    if locale == "en-US":
        message = """
        Hello %(username)s, we need to confirm your email.

        Please click in the link bellow:

        %(app_url)sapi/activate-account/%(email_token)s

        If you have not asked for an account in this platform you can ignore this message.

        Greetings,
        %(app_url)s
        """ % {
            "username": username,
            "app_url": app_url,
            "email_token": email_token,
        }

        subject = "Confirm your email"

        send_mail(subject, message, None, [recipient])
    elif locale == "pt-BR":
        message = """
        Olá %(username)s, precisamos confirmar o seu e-mail.

        Por favor, clique no link abaixo:

        %(app_url)sapi/activate-account/%(email_token)s

        Se você não solicitou uma conta nesta plataforma, pode ignorar esta mensagem.

        Saudações,
        %(app_url)s
        """ % {
            "username": username,
            "app_url": app_url,
            "email_token": email_token,
        }

        subject = "Confirm your email"

        send_mail(subject, message, None, [recipient])
    else:
        raise Exception(f"Unknown locale: {locale}")


def send_update_password_email(recipient: str, username: str, email_token: str, locale: str):
    """Sends update password link"""
    app_url = settings.APP_URL

    if locale == "en-US":
        message = """
        Hi %(username)s, you have requested to reset your password.

        Please click in the link bellow:

        %(app_url)supdate_password.html#id=%(email_token)s

        If you have not asked for an account in this platform you can ignore this message.

        Greetings,
        %(app_url)s
        """ % {
            "username": username,
            "app_url": app_url,
            "email_token": email_token,
        }

        subject = "Update password"
        send_mail(subject, message, None, [recipient])
    elif locale == "pt-BR":
        message = """
        Olá %(username)s, você solicitou a redefinição da sua senha.

        Por favor, clique no link abaixo:

        %(app_url)supdate_password.html#id=%(email_token)s

        Se você não solicitou uma conta nesta plataforma, pode ignorar esta mensagem.

        Atenciosamente,
        %(app_url)s
        """ % {
            "username": username,
            "app_url": app_url,
            "email_token": email_token,
        }

        subject = "Atualização de senha"

        send_mail(subject, message, None, [recipient])
    else:
        raise Exception(f"Unknown locale: {locale}")

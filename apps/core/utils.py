from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings


def site_email(to, template, context, subject):
    template = template
    subject = subject
    to = to
    from_email = settings.SENDER_EMAIL
    #context = Context(context)

    html_message = get_template('emails/' + template + '.html').render(context)
    message = strip_tags(html_message)

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=to,
        html_message=html_message
    )
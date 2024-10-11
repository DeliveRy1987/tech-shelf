from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_signup_confirmation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'アカウント登録完了のお知らせ'
        message = f'ご登録いただきありがとうございます、{instance.username}さん！'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, email_from, recipient_list)

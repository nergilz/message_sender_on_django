from django.db import models

class Message_db(models.Model):
    msg_email = models.EmailField(verbose_name='email')
    msg_message = models.TextField(verbose_name='message')
    msg_status = models.BooleanField(verbose_name='status')


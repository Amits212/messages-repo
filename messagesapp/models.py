from django.db import models


class Message(models.Model):
    message = models.TextField()
    subject = models.CharField(max_length=100)
    # In order to check if message is already read
    message_already_read = models.BooleanField(default=False)
    sender = models.ForeignKey('auth.User', related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey('auth.User', related_name='received_messages', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

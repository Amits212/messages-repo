from django.apps import AppConfig


class MessagesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messagesapp'
# To ensure that the signals are set up and ready to handle events as soon as the application starts
    def ready(self):
        import messagesapp.signals
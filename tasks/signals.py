from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from tasks.models import Ingeniero

@receiver(pre_delete, sender=Ingeniero)
def delete_user(sender, instance, **kwargs):
    user = User.objects.get(username=instance.user.username)
    user.delete()
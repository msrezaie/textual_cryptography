from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from . models import CryptodenUser

# instance represents the instance/object of the sender, in this case the sender would be the object of the CryptodenUser model
# Define a signal handler function for creating a CryptodenUser instance when a new User is created
def createCryptodenUser(sender, instance, created, **kwargs):
    # Check if a new User instance was just created
    if created:
        # Create a new CryptodenUser instance with the same attributes as the User instance
        cryptodenUser = CryptodenUser.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
        )

# Define a signal handler function for deleting the associated User instance when a CryptodenUser instance is deleted
def deleteCryptodenUser(sender, instance, **kwargs):
    # Get the User instance associated with the deleted CryptodenUser instance
    user = instance.user
    # Delete the User instance
    user.delete()

# Connect the createCryptodenUser function to the post_save signal of the User model
post_save.connect(createCryptodenUser, sender=User)

# Connect the deleteCryptodenUser function to the post_delete signal of the CryptodenUser model
post_delete.connect(deleteCryptodenUser, sender=CryptodenUser)
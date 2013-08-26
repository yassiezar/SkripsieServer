from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	balance = models.DecimalField(max_digits=8, decimal_places=2, default=1000)

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.user																																																																																																																																																																																																																																																																																																																																								

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
User.profile = property(lambda u: u.get_profile() )


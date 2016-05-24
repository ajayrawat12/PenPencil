from django.db import models

# Create your models here.

class TutorProfile(models.Model):
    """docstring for registered users, saving registered users."""

    #highlighted = models.TextField()

    username = models.CharField(max_length=30, blank=False, null=False,
                                verbose_name='User_Name', default='dev')

    password = models.CharField(max_length=20, blank=False, null=False, default='dev')

    email = models.EmailField(blank=False, null=False, verbose_name='Email')

    age = models.IntegerField(blank=True, null=True,)

    name = models.CharField(blank=True, null=True, max_length=20)



    def __unicode__(self):
        """UNICODE."""
        return self.username

    class Meta:
        """Class Info."""

        verbose_name = 'TutorProfile'
        verbose_name_plural = "TutorProfile's"

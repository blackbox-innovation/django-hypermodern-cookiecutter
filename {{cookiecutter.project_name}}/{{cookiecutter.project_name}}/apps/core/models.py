import logging
import uuid

from allauth.account.models import EmailAddress
from allauth.account.signals import email_confirmed
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


logger = logging.getLogger(__name__)



class TimestampedUUIDModel(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True



# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username/
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the maybe given email and password."""
        if not email:
            raise ValueError("Cannot create not-candidate user without email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


@receiver(email_confirmed)
def update_user_email(sender, request, email_address, **kwargs):
    # Once the email address is confirmed, make new email_address primary.
    # This also sets user.email to the new email address.
    # email_address is an instance of allauth.account.models.EmailAddress
    email_address.set_as_primary()
    # Get rid of old email addresses
    EmailAddress.objects.filter(user=email_address.user).exclude(primary=True).delete()


class User(AbstractUser, TimestampedUUIDModel):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False, verbose_name=_("email"), unique=True, null=True)

    first_name = models.CharField(
        max_length=30,
        blank=False,
        verbose_name=_("first name"),
    )
    last_name = models.CharField(
        max_length=35,
        blank=False,
        verbose_name=_("last name"),
    )
  
    def __str__(self):
        return f"{self.get_full_name()} {f'<{self.email}>' if self.email else ''}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "users"

    objects = UserManager()


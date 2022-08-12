from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class Guest(AbstractBaseUser, models.Model):
    username_validator = UnicodeUsernameValidator()

    username = models.EmailField(
        max_length=150,
        unique=True,
        help_text=(
            "Required. email will be used as username. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )

    first_name = models.CharField(("first name"), max_length=150, blank=True)

    last_name = models.CharField(("last name"), max_length=150, blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class Booking(models.Model):
    stay = models.CharField(max_length=30)
    check_in = models.DateField()
    check_out = models.DateField()
    user = models.ForeignKey(Guest, on_delete=models.PROTECT)

    def get_username(self):
        return self.user.username
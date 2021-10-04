from re import T
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import EmailValidator
from django.contrib.auth.models import UserManager
from utils import UserTypeChoices, GenderChoices
from django.utils.translation import ugettext_lazy as _

def national_id(instance, filename):
    return f"national_id/{instance.id}/{filename}"

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and -/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        blank=True,
        null=True
    )

    first_name = models.CharField('first name',
                                  max_length=150,
                                  null=True)

    last_name = models.CharField('last name',
                                 max_length=150,
                                 null=True)

    email = models.EmailField('email address', validators=[EmailValidator], unique=True)

    phone = models.CharField(max_length=20, null=True)

    gender = models.SmallIntegerField(choices=GenderChoices.choices, default=GenderChoices.MALE)

    type = models.SmallIntegerField(choices=UserTypeChoices.choices, default=UserTypeChoices.REPRESENTATIVE)

    national_id = models.ImageField(upload_to=national_id, blank=True, null=True)

    is_staff = models.BooleanField(
        'staff status',
        default=False,
    )

    is_active = models.BooleanField(
        'active',
        default=True,
    )

    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True
        db_table = 'users'
        unique_together = [('username','phone'), ]

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_user_type(self):
        """ Return user type as a String """
        return self.get_type_display()

    def get_gender(self):
        return self.get_gender_display()

    def get_identity(self):
        return f'[{self.get_type_display()}]: {self.first_name} {self.last_name}'

    @property
    def total_revenu(self):
        if self.type in [UserTypeChoices.ADMIN, UserTypeChoices.MANAGER]:
            return None
        return None

class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image

# A custom user model needs a user manager
class UserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, directorate, password=None):
        if not email:
            raise ValueError("Users must have a valid email address")
        if not username:
            raise ValueError("Users must have a unique username")
        if not firstname:
            raise ValueError("Users must have a first name")
        if not lastname:
            raise ValueError("Users must have a last name")
        if not directorate:
            raise ValueError("Users must indicate their directorate")

        user = self.model(
                email = self.normalize_email(email),
                username = username,
                firstname = firstname,
                lastname = lastname,
                directorate = directorate,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, firstname, lastname, directorate, password):
            user = self.create_user(
                    email = self.normalize_email(email),
                    username = username,
                    firstname = firstname,
                    lastname = lastname,
                    directorate = directorate,
                    password=password,
                )
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)


DIRECTORATES = ('', 'EED', 'WED', 'Other')

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    directorate = models.CharField(max_length=20, choices=[(d, d) for d in DIRECTORATES])
    # These are required for the AbstractBaseUser class by Django
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # In a custom field, we need to set the field by which
    # users log in with. Here we want to use email.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'directorate']

    # Tell the user model where the user manager is
    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email

    # These functions are required in a custom user model
    # This sets permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 500:
            output_size = (350, 450)
            img.thumbnail(output_size)
            img.save(self.image.path)

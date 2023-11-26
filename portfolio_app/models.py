from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=200, default=timezone.now)
    contact_email = models.CharField(max_length=200, default=timezone.now)
    is_active = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])


class Project(models.Model):
    title = models.CharField(max_length=200, default=timezone.now)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default = None, null = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

class Student(models.Model):
    #List of choices for majrs
    MAJOR =(

        ('F', 'Fountain'),
        ('M', 'Morrison'),
        ('L', 'Lyons')
    )#end of major

    name = models.CharField(max_length=200)
    """email = models.CharField("UCCS Email", max_length=200)"""
    major = models.CharField(max_length=200, choices=MAJOR)#, blank = True)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, null = True, default = None, blank = True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )
        
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Add related_name argument here
        related_query_name='user',
    )

    def __str__(self):
        return self.email
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
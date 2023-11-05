from django.db import models
from django.urls import reverse
from django.utils import timezone

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

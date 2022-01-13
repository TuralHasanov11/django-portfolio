from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Experience(models.Model):
    company = models.CharField(max_length=255, null=False, blank=True)
    position = models.CharField(max_length=255, null=False, blank=True)
    text = models.TextField(null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company

    @property
    def dateFrom(self):
        return self.date_from.date()

    @property
    def dateTo(self):
        return self.date_to.date()

class Project(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True, unique=True)
    url = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    technologies = models.ManyToManyField(Skill, through='ProjectTechnology')

    def __str__(self):
        return self.name

class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    

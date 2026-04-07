from django.db import models

# Create your models here.

class TechstackBackend(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class TechstackFrontend(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class TechstackDatabases(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class TechstackTools(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=225)
    link = models.URLField(null=True, blank=True)
    gitlink = models.URLField(null=True, blank=True)
    description = models.TextField()
    svg_icon = models.TextField()
    database = models.ManyToManyField(TechstackDatabases, related_name='db_projects')
    frontend = models.ManyToManyField(TechstackFrontend, related_name='front_projects')
    backend = models.ManyToManyField(TechstackBackend, related_name='back_projects')
    tools = models.ManyToManyField(TechstackTools, related_name='tool_projects')

    def __str__(self):
        return self.name








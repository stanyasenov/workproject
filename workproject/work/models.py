from django.db import models


class Programmer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    title = models.CharField(max_length=30)
    wage = models.IntegerField()


class Module(models.Model):
    name = models.CharField(max_length=50, unique=True)
    source_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    planned_finish_by_date = models.DateTimeField()
    actual_finish_by_date = models.DateTimeField(blank=True, null=True)

    user = models.ForeignKey(Programmer, on_delete=models.CASCADE)


class Stage(models.Model):
    finish_by_date = models.DateTimeField()

    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    admin_programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    working_programmer = models.ManyToManyField(Programmer, related_name='working_programmer')



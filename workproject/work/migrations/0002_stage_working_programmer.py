# Generated by Django 4.1 on 2022-08-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='working_programmer',
            field=models.ManyToManyField(related_name='working_programmer', to='work.programmer'),
        ),
    ]

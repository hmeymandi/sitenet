# Generated by Django 3.2.6 on 2021-09-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_alter_restmodel_accept'),
    ]

    operations = [
        migrations.AddField(
            model_name='restmodel',
            name='timeavg',
            field=models.CharField(default='sumtime1', max_length=250),
        ),
    ]

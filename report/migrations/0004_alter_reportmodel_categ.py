# Generated by Django 3.2.6 on 2021-09-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20210829_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportmodel',
            name='categ',
            field=models.ManyToManyField(related_name='info', to='report.Informationmodel', verbose_name='دسته بندیُ'),
        ),
    ]
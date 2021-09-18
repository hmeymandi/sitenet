# Generated by Django 3.2.6 on 2021-08-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210820_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='کاربر عادی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='مدیر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_authe',
            field=models.BooleanField(default=True, verbose_name='سرشیفت'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='سرپرست'),
        ),
    ]
# Generated by Django 3.2.6 on 2021-09-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_authe',
            field=models.BooleanField(default=True, verbose_name='سرشیفت'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='سرپرست'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_nazer',
            field=models.BooleanField(default=False, verbose_name='ناظر'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
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
    ]

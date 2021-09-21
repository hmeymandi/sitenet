# Generated by Django 3.2.6 on 2021-09-20 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest', '0005_auto_20210916_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restmodel',
            name='time1',
            field=models.TimeField(verbose_name='شروع مرخصی'),
        ),
        migrations.AlterField(
            model_name='restmodel',
            name='time2',
            field=models.TimeField(verbose_name='پایان مرخصی'),
        ),
        migrations.AlterField(
            model_name='restmodel',
            name='type',
            field=models.CharField(choices=[('h', 'ساعتی'), ('d', 'روزانه')], default='h', max_length=20, verbose_name='نوع مرخصی'),
        ),
        migrations.CreateModel(
            name='Repmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ثبت')),
                ('name', models.CharField(max_length=150, verbose_name='نام قطعه')),
                ('station', models.CharField(max_length=50, verbose_name='نام ایستگاه')),
                ('subj', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری')),
            ],
            options={
                'verbose_name': ' سیستم قطعات معیوب',
                'verbose_name_plural': 'سیستم قطعات معیوب',
            },
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_alter_reportmodel_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informationmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True, verbose_name='نمایش')),
                ('position', models.IntegerField(verbose_name='موقیعت')),
            ],
            options={
                'verbose_name': 'اطلاعات',
                'verbose_name_plural': 'اطلاعات',
                'ordering': ['position'],
            },
        ),
        migrations.AlterField(
            model_name='reportmodel',
            name='acepet',
            field=models.CharField(choices=[('تایید نشده', 'تایید نشده'), ('تایید سر شیفت', 'تایید سر شیفت'), ('تایید نهایی', 'تایید نهایی')], default='تایید نشده', max_length=30, verbose_name='وضیعت'),
        ),
        migrations.AddField(
            model_name='reportmodel',
            name='categ',
            field=models.ManyToManyField(to='report.Informationmodel', verbose_name='دسته بندیُ'),
        ),
    ]
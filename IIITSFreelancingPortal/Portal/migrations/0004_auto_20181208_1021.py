# Generated by Django 2.1.1 on 2018-12-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0003_auto_20181208_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='mention',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_link',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='e_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='f_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]

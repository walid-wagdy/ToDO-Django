# Generated by Django 3.1 on 2020-08-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_todolist_date_when'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='desc',
            field=models.CharField(default='Description here', max_length=10000),
            preserve_default=False,
        ),
    ]
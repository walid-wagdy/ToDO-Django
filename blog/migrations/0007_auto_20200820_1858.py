# Generated by Django 3.1 on 2020-08-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_todolist_date_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.3 on 2023-10-31 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

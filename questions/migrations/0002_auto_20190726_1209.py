# Generated by Django 2.2.3 on 2019-07-26 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
    ]

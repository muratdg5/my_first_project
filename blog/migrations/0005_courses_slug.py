# Generated by Django 4.1.5 on 2023-03-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_courses_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]

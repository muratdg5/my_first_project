# Generated by Django 4.1.5 on 2023-01-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('title_two', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('like', models.IntegerField()),
                ('like_two', models.IntegerField()),
                ('image', models.ImageField(upload_to='courses')),
                ('image_teacher', models.ImageField(upload_to='trainers')),
                ('is_home', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexCounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_student', models.CharField(max_length=100)),
                ('name_student_sayi', models.IntegerField()),
                ('name_courses', models.CharField(max_length=100)),
                ('name_courses_sayi', models.IntegerField()),
                ('name_trainers', models.CharField(max_length=100)),
                ('name_trainers_sayi', models.IntegerField()),
                ('is_home', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('text_one', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('button1', models.CharField(max_length=100)),
                ('is_home', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('text_one', models.CharField(max_length=200)),
                ('text_two', models.CharField(max_length=200)),
                ('text_three', models.CharField(max_length=200)),
                ('description_one', models.TextField()),
                ('image', models.ImageField(upload_to='index')),
                ('is_home', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexWhysection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('button1', models.CharField(max_length=100)),
                ('is_home', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='trainers')),
                ('is_home', models.BooleanField()),
            ],
        ),
    ]

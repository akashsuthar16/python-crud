# Generated by Django 2.0 on 2021-08-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='fname', max_length=255)),
                ('uname', models.CharField(default='uname', max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]

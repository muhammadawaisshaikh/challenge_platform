# Generated by Django 2.0.13 on 2020-05-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_roomadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('staff_only', models.BooleanField(default=False)),
            ],
        ),
    ]

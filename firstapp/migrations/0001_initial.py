# Generated by Django 4.0.1 on 2022-03-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=200)),
                ('uemail', models.EmailField(max_length=254)),
                ('uage', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('read', models.CharField(max_length=50)),
            ],
        ),
    ]
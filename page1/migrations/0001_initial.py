# Generated by Django 5.0.2 on 2024-02-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('empId', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]

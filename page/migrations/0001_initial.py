# Generated by Django 3.1.5 on 2021-02-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digit', models.CharField(max_length=200)),
                ('string', models.CharField(max_length=200)),
                ('aplha', models.CharField(max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2022-04-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choach', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('em', models.CharField(max_length=100)),
            ],
        ),
    ]

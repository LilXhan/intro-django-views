# Generated by Django 4.1.4 on 2023-01-04 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_personproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidationPersonProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.person',),
        ),
        migrations.AddField(
            model_name='person',
            name='salary',
            field=models.FloatField(default=0.0),
        ),
    ]

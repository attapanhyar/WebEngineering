# Generated by Django 3.2.4 on 2021-06-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_remove_facultdata_senior'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultdata',
            name='senior',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

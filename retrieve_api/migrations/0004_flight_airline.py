# Generated by Django 3.2.9 on 2021-12-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retrieve_api', '0003_auto_20211206_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='airline',
            field=models.CharField(default='AA', max_length=2),
            preserve_default=False,
        ),
    ]

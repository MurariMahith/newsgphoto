# Generated by Django 3.0.7 on 2020-07-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200728_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='username',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]

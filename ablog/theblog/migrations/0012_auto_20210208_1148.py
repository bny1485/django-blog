# Generated by Django 3.1.5 on 2021-02-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_auto_20210207_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='facebook_url',
            new_name='twitter_url',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]

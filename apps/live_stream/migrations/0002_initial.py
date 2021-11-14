# Generated by Django 3.2.9 on 2021-11-14 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('live_stream', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='live_stream_viewers',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='user.useraccountmodel'),
        ),
        migrations.AddField(
            model_name='host_user_links',
            name='host_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.useraccountmodel'),
        ),
    ]

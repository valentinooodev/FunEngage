# Generated by Django 3.2.9 on 2021-11-14 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master_data', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='related_links',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
        migrations.AddField(
            model_name='push_notifications',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.useraccountmodel'),
        ),
        migrations.AddField(
            model_name='push_notification_trans_contents',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
        migrations.AddField(
            model_name='push_notification_master_contents',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
        migrations.AddField(
            model_name='mgmt_portal_user',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
        migrations.AddField(
            model_name='email_notification_trans_contents',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
        migrations.AddField(
            model_name='email_notification_master_contents',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
        migrations.AddField(
            model_name='box_notifications',
            name='box_notification_master_content_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.box_notification_master_contents'),
        ),
        migrations.AddField(
            model_name='box_notifications',
            name='box_notification_transaction_content_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='master_data.box_notification_transaction_contents'),
        ),
        migrations.AddField(
            model_name='box_notifications',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.useraccountmodel'),
        ),
        migrations.AddField(
            model_name='box_notification_transaction_contents',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
        migrations.AddField(
            model_name='box_notification_master_contents',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.clients'),
        ),
    ]

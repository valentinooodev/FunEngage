# Generated by Django 3.2.9 on 2021-11-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box_Notification_Master_Contents',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('box_notification_master_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('timing_type', models.SmallIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('memo', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Box_Notification_Transaction_Contents',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('box_notification_transaction_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('from_type', models.SmallIntegerField()),
                ('from_user_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('to_user_ids', models.TextField(null=True)),
                ('scheduled_at', models.DateTimeField()),
                ('is_delivered', models.SmallIntegerField()),
                ('delivered_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Box_Notifications',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_read', models.SmallIntegerField()),
                ('read_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device_Tokens',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('platform', models.SmallIntegerField()),
                ('token', models.CharField(max_length=255)),
                ('invalidated_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email_Authns',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.SmallIntegerField()),
                ('email', models.CharField(max_length=254)),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email_Notification_Master_Contents',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('email_notification_master_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('timing_type', models.SmallIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('memo', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email_Notification_Trans_Contents',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('email_notification_trans_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('to_user_ids', models.TextField(null=True)),
                ('scheduled_at', models.DateTimeField(null=True)),
                ('is_delivered', models.SmallIntegerField()),
                ('delivered_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email_Notifications',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('to_email', models.CharField(max_length=254)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('scheduled_at', models.DateTimeField()),
                ('status', models.SmallIntegerField()),
                ('sent_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mgmt_Portal_user',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('mgmt_portal_user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.SmallIntegerField()),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('remember_token', models.CharField(max_length=255, null=True)),
                ('is_archived', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Password_Resets',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.SmallIntegerField()),
                ('email', models.CharField(max_length=254)),
                ('token', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('prefecture_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('display_order', models.SmallIntegerField()),
                ('is_default', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Push_Notification_Master_Contents',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('push_notification_master_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('timing_type', models.SmallIntegerField()),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.CharField(max_length=255)),
                ('internal_url', models.CharField(max_length=255, null=True)),
                ('memo', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Push_Notification_Trans_Contents',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('push_notification_trans_content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.CharField(max_length=255)),
                ('internal_url', models.CharField(max_length=255, null=True)),
                ('to_user_ids', models.TextField(null=True)),
                ('scheduled_at', models.DateTimeField()),
                ('is_delivered', models.SmallIntegerField()),
                ('delivered_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Push_Notifications',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('to_platform', models.SmallIntegerField()),
                ('to_token', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.CharField(max_length=255)),
                ('internal_url', models.CharField(max_length=255, null=True)),
                ('scheduled_at', models.DateTimeField()),
                ('status', models.SmallIntegerField()),
                ('sent_at', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Refresh_Tokens',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('refresh_token_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('mgmt_portal_user_id', models.IntegerField(null=True)),
                ('encrypted_refresh_token', models.CharField(max_length=255)),
                ('expires_in', models.DateTimeField()),
                ('is_blacklisted', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Related_Links',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('is_deleted', models.BooleanField(default=False, null=True, verbose_name='削除フラグ')),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('link_url', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('dir_path', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('display_order', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

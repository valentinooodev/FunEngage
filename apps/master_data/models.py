from django.core.validators import MaxValueValidator
from django.db import models
# from django.contrib.auth.models import AbstractUser
from commons.models import BaseModel


class Prefectures(BaseModel):
    prefecture_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    display_order = models.SmallIntegerField()
    is_default = models.SmallIntegerField()


# class user(AbstractUser):
#     user_id = models.IntegerField(primary_key=True)
#     client_id = models.ForeignKey(Clients, on_delete=models.PROTECT, default=1)
#     user_type = models.SmallIntegerField()
#     login_type = models.CharField(max_length=45)
#     email = models.EmailField(max_length=254, null=True)
#     password = models.CharField(max_length=255, null=True)
#     remember_token = models.CharField(max_length=255, null=True)
#     facebook_id = models.CharField(max_length=255, null=True)
#     twitter_id = models.CharField(max_length=255, null=True)
#     apple_id = models.CharField(max_length=255, null=True)
#     last_name_kanji = models.CharField(max_length=255)
#     first_name_kanji = models.CharField(max_length=255)
#     last_name_kana = models.CharField(max_length=255)
#     first_name_kana = models.CharField(max_length=255)
#     nickname = models.CharField(max_length=255)
#     sex = models.SmallIntegerField()
#     is_sex_public = models.SmallIntegerField()
#     date_of_birth = models.DateField()
#     is_date_of_birth_public = models.SmallIntegerField()
#     phone = models.CharField(max_length=45, null=True)
#     zip_code = models.CharField(max_length=8, null=True)
#     prefecture_id = models.ForeignKey(Prefectures, on_delete=models.PROTECT, default=1, null=True)
#     city = models.CharField(max_length=255, null=True)
#     subsequent_address = models.CharField(max_length=255, null=True)
#     biography = models.TextField(null=True)
#     points_balance = models.DecimalField(max_digits=15, decimal_places=0)
#     points_received = models.DecimalField(max_digits=15, decimal_places=0)
#     stamps_balance = models.DecimalField(max_digits=15, decimal_places=0)
#     econtext_cus_id = models.CharField(max_length=255, null=True)
#     delux_membership = models.CharField(max_length=255, null=True)
#     host_user_type = models.SmallIntegerField()
#     is_authenticated = models.SmallIntegerField()
#     is_archived = models.SmallIntegerField()


class Box_Notification_Master_Contents(BaseModel):
    box_notification_master_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    memo = models.CharField(max_length=255, null=True)


class Box_Notification_Transaction_Contents(BaseModel):
    box_notification_transaction_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    from_type = models.SmallIntegerField()
    from_user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField()
    is_delivered = models.SmallIntegerField()
    delivered_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Box_Notifications(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.CASCADE)
    box_notification_master_content_id = models.ForeignKey(Box_Notification_Master_Contents, on_delete=models.CASCADE,
                                                           null=True)
    box_notification_transaction_content_id = models.ForeignKey(Box_Notification_Transaction_Contents,
                                                                on_delete=models.CASCADE, null=True)
    is_read = models.SmallIntegerField()
    read_at = models.DateTimeField(null=True)


class Email_Notification_Master_Contents(BaseModel):
    email_notification_master_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    memo = models.CharField(max_length=255)


class Email_Notification_Trans_Contents(BaseModel):
    email_notification_trans_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(null=True)
    is_delivered = models.SmallIntegerField()
    delivered_at = models.DateTimeField(null=True)


class Email_Notifications(BaseModel):
    id = models.BigIntegerField(primary_key=True)
    to_email = models.CharField(max_length=254)
    title = models.CharField(max_length=255)
    body = models.TextField()
    scheduled_at = models.DateTimeField()
    status = models.SmallIntegerField()
    sent_at = models.DateTimeField(null=True)


class Push_Notification_Master_Contents(BaseModel):
    push_notification_master_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField()
    title = models.CharField(max_length=255, null=True)
    body = models.CharField(max_length=255)
    internal_url = models.CharField(max_length=255, null=True)
    memo = models.CharField(max_length=255, null=True)


class Push_Notification_Trans_Contents(BaseModel):
    push_notification_trans_content_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    body = models.CharField(max_length=255)
    internal_url = models.CharField(max_length=255, null=True)
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField()
    is_delivered = models.SmallIntegerField()
    delivered_at = models.DateTimeField(null=True)


class Push_Notifications(BaseModel):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.CASCADE)
    to_platform = models.SmallIntegerField()
    to_token = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    body = models.CharField(max_length=255)
    internal_url = models.CharField(max_length=255, null=True)
    scheduled_at = models.DateTimeField()
    status = models.SmallIntegerField()
    sent_at = models.DateTimeField(null=True)


class Email_Authns(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_type = models.SmallIntegerField()
    email = models.CharField(max_length=254)
    token = models.CharField(max_length=255)


class Mgmt_Portal_user(BaseModel):
    mgmt_portal_user_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    user_type = models.SmallIntegerField()
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=255, null=True)
    is_archived = models.SmallIntegerField()


class Password_Resets(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_type = models.SmallIntegerField()
    email = models.CharField(max_length=254)
    token = models.CharField(max_length=255)


class Refresh_Tokens(BaseModel):
    refresh_token_id = models.BigIntegerField(primary_key=True)
    user_id = models.IntegerField(null=True)
    mgmt_portal_user_id = models.IntegerField(null=True)
    encrypted_refresh_token = models.CharField(max_length=255)
    expires_in = models.DateTimeField()
    is_blacklisted = models.SmallIntegerField()


class Device_Tokens(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    platform = models.SmallIntegerField()
    token = models.CharField(max_length=255)
    invalidated_at = models.DateTimeField(null=True)


class Related_Links(BaseModel):
    id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    dir_path = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()


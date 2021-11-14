from django.db import models

from commons.models import BaseModel


# from apps.master_data.models import Clients, Prefectures


# class ClientModel(BaseModel):
#     client_id = models.IntegerField(primary_key=True, null=False)
#     name = models.CharField(max_length=255, null=False)
#     seconds_delivered_per_month = models.IntegerField(null=False)
#     is_archived = models.BooleanField()
#
#     class Meta:
#         db_table = 'clients'
#
#


class Clients(BaseModel):
    client_id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    seconds_delivered_per_month = models.DecimalField(max_digits=15, decimal_places=0, null=False)
    is_archived = models.SmallIntegerField(null=False)

    def __str__(self):
        return self.name


class UserAccountModel(BaseModel):
    user_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.PROTECT, default=1)
    user_type = models.SmallIntegerField()
    login_type = models.CharField(max_length=45)
    email = models.EmailField(max_length=254, null=True)
    password = models.CharField(max_length=255, null=True)
    remember_token = models.CharField(max_length=255, null=True)
    facebook_id = models.CharField(max_length=255, null=True)
    twitter_id = models.CharField(max_length=255, null=True)
    apple_id = models.CharField(max_length=255, null=True)
    last_name_kanji = models.CharField(max_length=255)
    first_name_kanji = models.CharField(max_length=255)
    last_name_kana = models.CharField(max_length=255)
    first_name_kana = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    sex = models.SmallIntegerField()
    is_sex_public = models.SmallIntegerField()
    date_of_birth = models.DateField()
    is_date_of_birth_public = models.SmallIntegerField()
    phone = models.CharField(max_length=45, null=True)
    zip_code = models.CharField(max_length=8, null=True)
    prefecture_id = models.ForeignKey(to='master_data.Prefectures', on_delete=models.PROTECT, default=1, null=True)
    city = models.CharField(max_length=255, null=True)
    subsequent_address = models.CharField(max_length=255, null=True)
    biography = models.TextField(null=True)
    points_balance = models.DecimalField(max_digits=15, decimal_places=0)
    points_received = models.DecimalField(max_digits=15, decimal_places=0)
    stamps_balance = models.DecimalField(max_digits=15, decimal_places=0)
    econtext_cus_id = models.CharField(max_length=255, null=True)
    delux_membership = models.CharField(max_length=255, null=True)
    host_user_type = models.SmallIntegerField()
    is_authenticated = models.SmallIntegerField()
    is_archived = models.SmallIntegerField()

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'user_custom'


class Additional_Profile_Items(BaseModel):
    additional_profile_item_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()


class User_Additional_Profile(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE)
    additional_profile_item_id = models.ForeignKey(Additional_Profile_Items, on_delete=models.CASCADE)
    body = models.TextField()


class Follows(BaseModel):
    from_user_id = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE, related_name='related1')
    to_user_id = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE, related_name='related2')


class Stamp_Code(BaseModel):
    stamp_code_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    stamp_code = models.CharField(max_length=6)
    stamps_granted = models.DecimalField(max_digits=15, decimal_places=0)
    number_of_applicable_user = models.IntegerField(null=True)
    number_of_applied_user = models.IntegerField()
    expires_in = models.DateTimeField()


class User_Stamps(BaseModel):
    user_stamps_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE)
    type = models.SmallIntegerField()
    deposit_reason = models.SmallIntegerField(null=True)
    withdrawal_reason = models.SmallIntegerField(null=True)
    stamps = models.DecimalField(max_digits=15, decimal_places=0)
    transacted_at = models.DateTimeField()
    stamps_balance = models.DecimalField(max_digits=15, decimal_places=0)


class Stamp_Receipt_Histories(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_stamp_id = models.ForeignKey(User_Stamps, on_delete=models.CASCADE)
    live_stream_id = models.IntegerField(null=True)
    stamp_code_id = models.IntegerField(null=True)
    received_at = models.DateTimeField()


class Stamp_Spending_Histories(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_stamp_id = models.ForeignKey(User_Stamps, on_delete=models.CASCADE)
    spent_for = models.SmallIntegerField()
    spent_at = models.DateTimeField()


class Rankings(BaseModel):
    ranking_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    type = models.SmallIntegerField()
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


class Ranking_Summaries(BaseModel):
    id = models.BigIntegerField(primary_key=True)
    ranking_id = models.ForeignKey(Rankings, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserAccountModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=0)
    target_date = models.DateField()

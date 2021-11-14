from django.db import models
from commons.models import BaseModel


class Points_Packages(BaseModel):
    points_package_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.PROTECT, default=1)
    apple_product_id = models.CharField(max_length=255, null=True)
    google_product_id = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=0)
    points = models.DecimalField(max_digits=15, decimal_places=0)
    display_order = models.SmallIntegerField()


class User_Points(BaseModel):
    user_point_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    type = models.SmallIntegerField()
    deposit_reason = models.SmallIntegerField(null=True)
    withdrawal_reason = models.SmallIntegerField(null=True)
    points = models.DecimalField(max_digits=15, decimal_places=0)
    transacted_at = models.DateTimeField()
    points_balance = models.DecimalField(max_digits=15, decimal_places=0)



class Points_Package_Purchase_Histories(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_point_id = models.ForeignKey(User_Points, on_delete=models.PROTECT, default=1)
    points_package_id = models.ForeignKey(Points_Packages, on_delete=models.PROTECT, default=1)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=0)
    purchased_at = models.DateTimeField()
    apple_trans_id = models.CharField(max_length=255)
    google_trans_id = models.CharField(max_length=255)
    apple_receipt = models.TextField()
    google_receipt = models.TextField()


class Gifts(BaseModel):
    gift_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=255)
    points_spent = models.DecimalField(max_digits=15, decimal_places=0)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()


class User_Gifts(BaseModel):
    user_gift_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    gift_id = models.ForeignKey(Gifts, on_delete=models.PROTECT, default=1)
    status = models.SmallIntegerField()
    used_at = models.DateTimeField(null=True)


class Gift_Tipping_Histories(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_gift_id = models.ForeignKey(User_Gifts, on_delete=models.PROTECT, default=1)
    to_user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    points_equivalent = models.DecimalField(max_digits=15, decimal_places=0)
    tipped_at = models.DateTimeField



class Point_Spending_Histories(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_point_id = models.ForeignKey(User_Points, on_delete=models.PROTECT, default=1)
    user_gift_id = models.ForeignKey(User_Gifts, on_delete=models.PROTECT, default=1)
    spend_at = models.DateTimeField()


class Gift_Purchased_Histories(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_gift_id = models.ForeignKey(User_Gifts, on_delete=models.CASCADE, default=1)
    user_point_id = models.ForeignKey(User_Points, on_delete=models.CASCADE, default=1, )
    points_spent = models.DecimalField(max_digits=15, decimal_places=0)
    purchased_at = models.DateTimeField()

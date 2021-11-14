from django.db import models
from commons.models import BaseModel


class Events(BaseModel):
    event_id = models.IntegerField(primary_key=True, unique=True)
    client_id = models.ForeignKey(to='user.Clients', on_delete=models.PROTECT, default=1)
    type = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_private = models.SmallIntegerField()
    private_key = models.CharField(max_length=255, null=True)
    is_archived = models.SmallIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Events'
        db_table = 'event'


class Event_Authorized_user(BaseModel):
    event_id = models.ForeignKey(to='user.Clients', on_delete=models.PROTECT, default=1)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return f'{self.event_id} - {self.user_id}'


class Performances(BaseModel):
    performance_id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(Events, on_delete=models.PROTECT, default=1)
    streaming_method = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    capacity = models.IntegerField(null=True)
    ticket_available_flag = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Tickets(BaseModel):
    ticket_id = models.IntegerField(primary_key=True)
    performance_id = models.ForeignKey(Events, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=0)
    points_required = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    expiration_datetime = models.DateTimeField()
    drawing_flag = models.SmallIntegerField()
    drawing_application_datetime = models.DateTimeField(null=True)
    drawing_status = models.SmallIntegerField()
    stamp_available_flag = models.SmallIntegerField()
    max_number_of_tickets = models.IntegerField()
    number_of_issued_tickets = models.IntegerField()
    is_seat_id_assigned = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Drawings(BaseModel):
    ticket_id = models.ForeignKey(to='event.Tickets', on_delete=models.PROTECT, default=1)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    is_elected = models.SmallIntegerField()
    is_purchased = models.SmallIntegerField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return f'ticket:{self.ticket_id} - user:{self.user_id}'


class User_Tickets(BaseModel):
    user_ticket_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    ticket_id = models.ForeignKey(Tickets, on_delete=models.PROTECT, default=1)
    is_settled = models.IntegerField()
    seat_id = models.CharField(max_length=255, null=True)
    expires_in = models.DateTimeField()
    status = models.SmallIntegerField()
    used_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Ticket_Purchased_Reservations(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    ticket_id = models.ForeignKey(Tickets, on_delete=models.PROTECT, default=1)
    order_id = models.CharField(max_length=100, null=True)
    number_of_tickets = models.IntegerField()
    reservation_at = models.DateTimeField()
    is_purchased = models.SmallIntegerField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Ticket_Purchase_Histories(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_ticket_id = models.ForeignKey(User_Tickets, on_delete=models.PROTECT, default=1)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=0)
    point_amount = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    order_id = models.CharField(max_length=100, null=True)
    payment_type = models.CharField(max_length=15, null=True)
    purchased_at = models.DateTimeField()
    settled_at = models.DateTimeField(null=True)
    receipt_number = models.CharField(max_length=32)
    haraikomi_url = models.CharField(max_length=255)


class Image_Paths(BaseModel):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.CASCADE, null=True,
                                related_name='img_path_related')
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE, null=True, related_name='img_path_related')
    box_notification_trans_content_id = models.ForeignKey('master_data.Box_Notification_Transaction_Contents',
                                                          on_delete=models.PROTECT, null=True,
                                                          related_name='img_path_related')
    file_name = models.CharField(max_length=255)
    dir_path = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()

    def __str__(self):
        return f'uid:{self.user_id} - event:{self.event_id} - trans_content:{self.box_notification_trans_content_id}'

    def __unicode__(self):
        return self.image_url

    def save(self, *args, **kwargs):
        self.image_url = self.dir_path + self.file_name
        super(Image_Paths, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Image Paths'

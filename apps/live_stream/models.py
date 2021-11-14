from django.db import models
from commons.models import BaseModel


class Live_Streams(BaseModel):
    live_stream_id = models.IntegerField(primary_key=True)
    ivs_arn = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField()
    host_user_id = models.IntegerField()
    performance_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255, null=True)
    ingest_endpoint = models.CharField(max_length=255)
    stream_key = models.CharField(max_length=255)
    playback_url = models.CharField(max_length=255)
    comment_available_flag = models.SmallIntegerField()
    tipping_available_flag = models.SmallIntegerField()
    stamps_granted = models.DecimalField(max_digits=15, decimal_places=0)
    release_datetime = models.DateTimeField()
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    total_number_of_viewers = models.IntegerField(null=True)
    seconds_delivered = models.DecimalField(max_digits=15, decimal_places=0)
    channel_id_sd = models.CharField(max_length=255, null=True)
    channel_id_fhd = models.CharField(max_length=255, null=True)
    input_id_sd = models.CharField(max_length=255, null=True)
    input_id_fhd = models.CharField(max_length=255, null=True)
    video_url_sd = models.CharField(max_length=255, null=True)
    video_url_fhd = models.CharField(max_length=255, null=True)


class Live_Stream_Viewers(BaseModel):
    live_stream_id = models.ForeignKey(Live_Streams, on_delete=models.PROTECT)
    user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.PROTECT, default=1)
    viewed_at = models.DateTimeField()


class Host_User_Links(BaseModel):
    id = models.IntegerField(primary_key=True)
    host_user_id = models.ForeignKey(to='user.UserAccountModel', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.TextField()


class Sent_Relations(BaseModel):
    id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(to='event.Events', on_delete=models.PROTECT, null=True)
    live_stream_id = models.IntegerField(null=True)
    email_notification_trans_content_id = models.IntegerField(null=True)
    push_notification_trans_content_id = models.IntegerField(null=True)



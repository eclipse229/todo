from django.db import models
from django.utils import timezone


# Create your models here.
class Checker(models.Model):
    ''' This is the basic model of the scheduling checker application
    it contains : activity_id ; name of the activity;Time and date of the activity
    ; name of person or place that is related to the activity and
    side notes about the activity '''
    STATUS_CHOICE = (
        ('completed','Completed'),
        ('uncompleted','Uncompleted')
    )
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    related_to_person = models.CharField(max_length=50)
    related_to_place = models.CharField(max_length=100)
    activity_note = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,
                              default='uncompleted')

    class meta:
        ordering = ('date',)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('checker:details',
                        args=[self.date.id,
                              self.date.title,])

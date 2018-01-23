from django.db import models

# Create your models here.



class Reservation(models.Model):
    name = models.CharField(max_lenght=150)
    mobile_number = models.CharField(max_lenght=15)
    party_size = models.CharField(max_lenght=10)
    comments = models.TextField(max_lenght=255)
    time = models.DateTimeField()
    time_zone = models.DateZoneField(default='UK')

    task_id = models.CharField(max_lenght=50, blank=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Reservations {0} - {1}'.format(self.pk, self.name)

    def et_absolute_url(self):
        return reverse('view_reservation', args=[str(self.id)])

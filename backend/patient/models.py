from django.db import models
from django.contrib.postgres.fields import JSONField

# sample status

SAMPLE_STATUS = (
    ('normal','ORDINAIRE'),
    ('ugent', 'URGENT'),
    ('priority','PRIORITAIRE'),
    ('extern','EXTERNE'),
)


class Patient(models.Model):

    barcode = models.CharField(max_length=100)
    qr = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    group = models.CharField(max_length=100)
    sample_status = models.CharField(max_length=50, choices=SAMPLE_STATUS, default='normal')
    doctor = models.CharField(max_length=100)
    analysis = models.TextField()
    attachments = models.TextField()
    sampling_date = models.DateTimeField()
    rdv = models.DateTimeField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = ("Patient")
        verbose_name_plural = ("Patients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})

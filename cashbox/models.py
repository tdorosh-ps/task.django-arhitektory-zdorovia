from django.db import models
from django.utils import timezone

# Create your models here.


class Client(models.Model):
    name = models.CharField("Ім'я", max_length=255)
    contact = models.CharField("Контакт", max_length=100)
    notes = models.TextField("Примітки", blank=True)

    def __str__(self):
        return f"{self.name} {self.contact}"


class Service(models.Model):
    name = models.CharField("Назва", max_length=255)
    price = models.DecimalField("Вартість", max_digits=7, decimal_places=2)
    notes = models.TextField("Примітки", blank=True)

    def __str__(self):
        return f"{self.name} {self.price}"


class Session(models.Model):
    service = models.ForeignKey(
        Service,
        verbose_name="Процедура",
        on_delete=models.PROTECT
    )
    specialist = models.ForeignKey(
        'Specialist',
        verbose_name="Фахівець",
        on_delete=models.PROTECT
    )
    client = models.ForeignKey(
        Client,
        verbose_name="Клієнт",
        on_delete=models.PROTECT
    )
    order = models.PositiveSmallIntegerField("Порядковий номер")
    appointment = models.OneToOneField(
        'Appointment',
        verbose_name="Запис на прийом",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        "Дата проведення сеансу",
        default=timezone.now
    )
    notes = models.TextField("Примітки", blank=True)

    def __str__(self):
        return f"{self.service} {self.client} {self.order}"


class Specialist(models.Model):
    name = models.CharField("Ім'я", max_length=255)
    contact = models.CharField("Контакт", max_length=100, blank=True)
    notes = models.TextField("Примітки", blank=True)
    clients = models.ManyToManyField(
        Client,
        verbose_name="Клієнти",
        blank=True
    )

    def __str__(self):
        return f"{self.name} {self.contact}"


class Income(models.Model):
    session = models.OneToOneField(
        Session,
        verbose_name="Сеанс",
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField("Сума")

    def __str__(self):
        return f"{self.session} {self.amount}"


class Cost(models.Model):
    amount = models.PositiveIntegerField("Сума")
    specialist = models.ForeignKey(
        'Specialist',
        verbose_name="Фахівець",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField("Дата операції", default=timezone.now)
    notes = models.TextField("Примітки", blank=True)

    def __str__(self):
        return f"{self.notes} {self.amount}"


class Appointment(models.Model):
    service = models.ForeignKey(
        Service,
        verbose_name="Процедура",
        on_delete=models.PROTECT
    )
    specialist = models.ForeignKey(
        'Specialist',
        verbose_name="Фахівець",
        on_delete=models.PROTECT
    )
    client = models.ForeignKey(
        Client,
        verbose_name="Клієнт",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        "Дата запису на прийом",
        default=timezone.now
    )
    notes = models.TextField("Примітки", blank=True)

    def __str__(self):
        return f"{self.service} {self.timestamp}"

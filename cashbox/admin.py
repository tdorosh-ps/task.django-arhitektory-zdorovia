from django.contrib import admin

from .models import (
    Client,
    Specialist,
    Service,
    Session,
    Income,
    Cost,
    Appointment
)

# Register your models here.


admin.site.register(Client)
admin.site.register(Specialist)
admin.site.register(Service)
admin.site.register(Session)
admin.site.register(Income)
admin.site.register(Cost)
admin.site.register(Appointment)

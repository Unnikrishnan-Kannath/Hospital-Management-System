from django.contrib import admin

# Register your models here.
from .models import doctor
from .models import prescription
from .models import patient
from .models import pharmacy

# Register your models here.
class doctorAdmin(admin.ModelAdmin):
    search_fields=('name','email','specialisation')  
admin.site.register(doctor,doctorAdmin)

class prescriptionAdmin(admin.ModelAdmin):
    search_fields=('name',)
admin.site.register(prescription,prescriptionAdmin)

class patientAdmin(admin.ModelAdmin):
    search_fields=('full_name','doctor')
admin.site.register(patient,patientAdmin)

class pharmacyAdmin(admin.ModelAdmin):
    search_fields=('user_name',)
admin.site.register(pharmacy,pharmacyAdmin)
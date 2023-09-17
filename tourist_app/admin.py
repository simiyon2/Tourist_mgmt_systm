from django.contrib import admin

from tourist_app.models import reg,londonfield,chinafield,singaporefield,japanfield,thailandfield,indonesiafield,malaysiafield,contactfield,payment
from tourist_app.models import bookingfield,payment_one,payment_two,payment_three,payment_four,payment_five,payment_six,payment_seven
# @admin.register(login)
# class PersonAdmin(admin.ModelAdmin):
#     pass

@admin.register(reg)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(londonfield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(chinafield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(singaporefield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(japanfield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(thailandfield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(indonesiafield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(malaysiafield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(contactfield)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(payment)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(payment_one)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(payment_two)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(payment_three)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(payment_four)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(payment_five)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(payment_six)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(payment_seven)
class CourseAdmin(admin.ModelAdmin):
    pass
 
@admin.register(bookingfield)
class CourseAdmin(admin.ModelAdmin):
    pass
 

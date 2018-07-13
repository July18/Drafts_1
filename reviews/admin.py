from django.contrib import admin
from .models import Wine, Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_diplay = ('wine','user_name','comment','rating','pub_date')
    list_filter = ['wine','pub_date','user_name']
    search_fields = ['comment']

admin.site.register(Wine)
admin.site.register(Review,ReviewAdmin)
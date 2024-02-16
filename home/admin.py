from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import FooterItem
from .models import DishCategory, Dish, Chef, Events, Gallery, Reservation

admin.site.register(FooterItem)
# admin.site.register(Chef)
# admin.site.register(Events)
# admin.site.register(Gallery)
# admin.site.register(Reservation)

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'slug', 'ingredients', 'description', 'price', 'is_visible', 'position', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('ingredients', 'price', 'is_visible', 'position')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'ingredients', 'description')
    # list_select_related = ('category',)


    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Dish photo'

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'surname', 'appointment', 'description', 'position', 'is_visible')
    list_editable = ('name', 'surname', 'appointment', 'description', 'position', 'is_visible')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Chef photo'

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'price', 'description', 'is_visible', 'position')
    list_editable = ('name', 'price', 'description', 'is_visible', 'position')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Event photo'

@admin.register(Gallery)
class GalleriesAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'is_visible', 'position')
    list_editable = ('name', 'is_visible', 'position')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Gallery photo'

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'time', 'number_people', 'is_conformed', 'phone', 'email')
    list_editable = ('name', 'date', 'time', 'number_people', 'is_conformed')
    list_filter = ('date', )

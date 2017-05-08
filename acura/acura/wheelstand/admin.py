from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Models, Trim, ModelsShown, Accessories, Location, Colours, Interiors, Engines, Gallery, Transmission, Features, ExteriorColour, InteriorColour


class GalleryInline(admin.TabularInline):
    model = Gallery
#    list_display = ('name_en', 'base_price', 'freight_DPI')
    verbose_name = "Image"
    verbose_name_plural = "Gallery"
    readonly_fields = ('image_thumb',)


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ('url', 'link', 'md5')

    def get_model_perms(self, request):
        return {}


class ModelsAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline,
    ]
    readonly_fields = ('image_thumb',)
    list_display = ('name_en', 'base_price', 'freight_DPI')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr'), 'year', ('subhead_en', 'subhead_fr'), ('disclaimer_en', 'disclaimer_fr')),
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb', ('overview_image_text_en', 'overview_image_text_fr')),
        }),
        (_('Prices'), {
            'fields': ('base_price', 'freight_DPI'),
        }),
        (_('Special Offers & Promotions'), {
            'fields': (('line1_en', 'line1_fr'), ('line2_en', 'line2_fr'), ('line3_en', 'line3_fr'), ('line4_en', 'line4_fr'), ('line5_en', 'line5_fr'), ('line6_en', 'line6_fr'), ('line7_en', 'line7_fr'), ('line8_en', 'line8_fr'), ('line9_en', 'line9_fr'), 'percentage', 'price')
        }),

        (_('Special Offers & Promotions - Second City'), {
            'fields': (('line10_en', 'line10_fr'), 'line10_city', ('line11_en', 'line11_fr'), 'line11_city', ('line12_en', 'line12_fr'), 'line12_city', ('line13_en', 'line13_fr'), 'line13_city', ('line14_en', 'line14_fr'), 'line14_city', ('line15_en', 'line15_fr'), 'line15_city', ('line16_en', 'line16_fr'), 'line16_city', ('line17_en', 'line17_fr'), 'line17_city', ('line18_en', 'line18_fr'), 'line18_city')
        }),

    )


class ExteriorColourGalleryInline(admin.StackedInline):
    model = ExteriorColour
    readonly_fields = ('image_thumb',)


class InteriorColourGalleryInline(admin.StackedInline):
    model = InteriorColour
    readonly_fields = ('image_thumb',)


class TransmissionInline(admin.StackedInline):
    model = Transmission


class TrimAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'model', 'heading_en', 'engine', 'get_interiors')
    readonly_fields = ('image_thumb',)
    inlines = [ExteriorColourGalleryInline, TransmissionInline]
    filter_horizontal = ('interiors',)
    fieldsets = (
        (_('General'), {
            'fields': ('model', ('name_en', 'name_fr'), 'order'),
        }),
        (_('Details'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
        (_('Highlights'), {
            'fields': (('heading_en', 'heading_fr'), ('description_en', 'description_fr')),
        }),
        (_('Options'), {
            'fields': ('engine',),
        }),

#        (_('Fuel'), {
#            'fields': ('fuel_city', 'fuel_highway', 'fuel_combined',),
#        }),

#        (_('Colours'), {
#            'fields': ('colour',),
#        }),
#        (_('Interiors'), {
#            'fields': ('interiors',),
#        }),
#        (_('Transmissions'), {
#            'fields': ('transmission', ),
#        }),
        (_('Features'), {
            'fields': ( ('highlights_en', 'highlights_fr'),('features_en', 'features_fr',)),
        }),
    )



class ModelsShownAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'trim', 'wheels_en', 'get_locations')
    filter_horizontal = ('location', 'accessory')
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('models_shown_price', 'vehicle', 'trim', 'wheels_en', 'wheels_fr', 'drivetrain', 'price_override', ('disclaimer_en', 'disclaimer_fr'),   ('transmission_en', 'transmission_fr'), 'fuel_city', 'fuel_highway', 'fuel_combined'),
        }),

        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),

        (_('Selected accessories'), {
            'fields': ('accessory',),
        }),
        (_('Locations'), {
            'fields': ('location',),
        }),
    )


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'base_price')

    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',), 'base_price'),
        }),
    )


class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'language', 'description_en', 'description_fr'),
        }),
    )

class ColoursAdmin(admin.ModelAdmin):
    list_display = ('name', 'hexcode')
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'hexcode'),
        }),
    )


class InteriorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'link', 'get_trims')
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('name',)
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
    )
'''
class InteriorsAdmin(admin.ModelAdmin):
    fields = (('url', 'image_thumb'))
    readonly_fields = ('image_thumb',)
'''


class EnginesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'displacement', 'horsePower', 'torque', 'get_trims')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',)),
        }),
        (_('Details'), {
            'fields': (('engine_en', 'engine_fr',), ('horsePower_en', 'horsePower_fr',),  ('horsePowerLast_en', 'horsePowerLast_fr',), 'displacement', ('emissions_en', 'emissions_fr',), ('bore_and_stroke_en', 'bore_and_stroke_fr'), ('recommended_fuel_en', 'recommended_fuel_fr',), 'hyBridPowerTrain', 'hybridHorsePower', 'hybridTorque', 'activeControl', 'idelStop', 'vcm', ('compressionRatio_en', 'compressionRatio_fr',), 'driveByWire' ),
        }),
    )


class TransmissionAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'abberviation', 'selected')
    fieldsets = (
        (_('General'), {
            'fields': (('name_en', 'name_fr',)),
        }),
        (_('Details'), {
            'fields': ('abberviation', 'MSRP', 'selected', 'colour_name'),
        }),
    )


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr')
    fieldsets = (
        (_('General'), {
            'fields': ('name_en', 'name_fr')
        }),
    )


class InteriorColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'selected', 'image_thumb')
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'selected', 'url', 'image_thumb')
        }),
    )


class ExteriorColourAdmin(admin.ModelAdmin):
    list_display = ('name', 'colour', 'image_thumb')
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (_('General'), {
            'fields': ('name', 'colour', 'selected')
        }),
        (_('Image'), {
            'fields': ('url', 'link', 'image_thumb'),
        }),
    )


admin.site.register(Models, ModelsAdmin)
admin.site.register(Trim, TrimAdmin)
admin.site.register(ModelsShown, ModelsShownAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Location, LocationsAdmin)
admin.site.register(Colours, ColoursAdmin)
admin.site.register(Interiors, InteriorsAdmin)
admin.site.register(Engines, EnginesAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Transmission, TransmissionAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(ExteriorColour, ExteriorColourAdmin)
admin.site.register(InteriorColour, InteriorColourAdmin)


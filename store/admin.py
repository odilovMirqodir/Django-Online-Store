from django.contrib import admin
from .models import Product, Category, Gallery, Review, Mail, FavoriteProducts, City
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'get_products_count')
    prepopulated_fields = {'slug': ('title',)}

    def get_products_count(self, obj):
        """Mahsulotni rasmlaini chiqarish admin panelga"""
        if obj.products:
            return str(len(obj.products.all()))
        else:
            return str(0)

    get_products_count.short_description = 'Tovarlar soni'


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('pk', 'title', 'category', 'quantity', 'price', 'created_at',
                    'size', 'color', 'get_photo')
    list_editable = ('price', 'quantity', 'size', 'color')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'price')
    inlines = [
        GalleryInline
    ]

    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75"')
            except:
                return '-'
        else:
            return '-'

    get_photo.short_description = "Mahsulot rasmi"

    def __delete__(self, instance):
        pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'created_at')
    readonly_fields = ('author', 'text', 'created_at')


admin.site.register(Gallery)
admin.site.register(City)
admin.site.register(Mail)
admin.site.register(FavoriteProducts)

from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product, GalleryImage

# Register your models here.


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Product,
                                                'category',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 7


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'amount']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [GalleryImageInline]
    prepopulated_fields = {'slug': ('title',)}


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['subject', 'comment', 'create_at']
#     list_filter = ['create_at']
#     readonly_fields = ('subject', 'comment',
#                        'user', 'product', 'rate', 'id')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(GalleryImage)
# admin.site.register(Comment, CommentAdmin)

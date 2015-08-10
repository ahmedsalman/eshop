from django.contrib import admin
from django.utils.text import slugify

from models import Category, Product, CategoryBanner


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'created', 'modified', 'visible', ]
    list_display_links = ('id', 'title', )
    list_editable = ('visible', )
    list_filter = ('title', 'created', 'modified', )
    list_per_page = 30
    ordering = ["created"]
    search_fields = ['id', 'title', 'banners', ]
    save_on_top = True
    readonly_fields = ['id', 'created', 'modified']
    fieldsets = [
        (None, {'fields': ['id', 'title', 'banners', 'visible']})
    ]

    def queryset(self, request):
        qs = Category.objects.all()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.select_related('created')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'slug', 'price', 'popularity')
    list_display_links = ('id', 'title', )
    list_filter = ('title', 'created', 'modified', )
    list_per_page = 30
    ordering = ["created"]
    search_fields = ['id', 'title', 'description', ]
    save_on_top = True
    readonly_fields = ['id', 'created', 'modified', 'popularity']

    fieldsets = [
        (None, {'fields': ['id', 'title', 'description', 'price', 'visible']}),
        ('Additional Information', {'fields': ['category', 'publisher',
        'manufacturer', 'brand', 'image']}),
    ]

    def queryset(self, request):
        qs = Product.objects.all()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.select_related('created')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryBanner)

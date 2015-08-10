from django.conf.urls import patterns, url

urlpatterns = patterns('product.views',
    url(r'^$',
        'home',
        name='home'),
    url(r'^thank-you/$',
        'thank_you',
        name='thank_you'),
    url(r'^checkout/$',
        'checkout',
        name='checkout'),
    url(r'^(?P<cat_slug>[-\w]+)/(?P<pro_slug>[-\w]+)/$',
        'product_page',
        name='product_page'),
    url(r'^(?P<slug>[-\w]+)/$',
        'category_view',
        name='category_view'),
)

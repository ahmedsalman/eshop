import uuid

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.shortcuts import (render_to_response,
get_object_or_404, redirect, render)
from django.template import RequestContext

from product.models import Category, Product, CategoryBanner
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.pdt.views import process_pdt
from review.forms import ReviewForm


noimage = 'http://placehold.it/150x150'


def home(request):
    categories = Category.objects.filter(visible=True).order_by('title')
    entries = Product.objects.select_related('category').filter(
        category__visible=True, visible=True).order_by('-popularity')

    banners = CategoryBanner.objects.filter(show_on_home_page=True)\
        .order_by('?')[:3]
    return render_to_response('product/index.html',
        {
            'products': entries,
            'categories': categories,
            'noimage': noimage,
            'banners': banners,
        },
        context_instance=RequestContext(request)
    )


def category_view(request, slug):
    categories = Category.objects.filter(visible=True).order_by('title')
    category = Category.objects.get(slug=slug)

    product_entries = Product.objects.select_related('category').filter(
        category__slug=slug,
        category__visible=True).order_by('-popularity')

    banners = category.banners.all().order_by('?')[:3]

    return render_to_response('product/index.html',
        {
            'products': product_entries,
            'categories': categories,
            'category': category,
            'noimage': noimage,
            'banners': banners,
        },
        context_instance=RequestContext(request)
    )


def product_page(request, cat_slug, pro_slug):
    categories = Category.objects.filter(visible=True).order_by('title')
    product = get_object_or_404(Product, slug=pro_slug,
        category__slug=cat_slug, category__visible=True)
    if product.popularity:
        product.popularity += 1
    else:
        product.popularity = 1

    product.save()

    return render_to_response('product/product_detail.html',
        {
            'product': product,
            'categories': categories,
            'reviewform': ReviewForm
        },
        context_instance=RequestContext(request)
    )


def checkout(request):

    domain = request.META['HTTP_HOST']
    protocol = 'https://' if request.is_secure() else 'http://'

    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": request.GET.get('amount'),
        "item_name": request.GET.get('name'),
        "invoice": uuid.uuid4(),
        "notify_url": protocol + domain + reverse('paypal-pdt'),
        "return_url": protocol + domain + reverse('thank_you'),
        "cancel_return": protocol + domain,
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "product/checkout.html", context)


def thank_you(request):
    pdt_obj, failed = process_pdt(request)
    context = {}
    context.update({"failed": failed, "pdt_obj": pdt_obj})
    return render(request, "product/thankyou.html", context)

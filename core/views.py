from django.shortcuts import render, get_object_or_404
from .models import Client, Product
from django.http import HttpResponse
from django.template import loader


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(
                        content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=404
    )


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(
                        content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=500
    )

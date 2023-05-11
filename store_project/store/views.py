from django.shortcuts import render


def product_list(request):
    return render(
        request,
        'store/product_list.html',
        context={'product_title': 'Range Rover'}
    )

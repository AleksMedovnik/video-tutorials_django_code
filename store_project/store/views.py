from django.shortcuts import render


def build_template(lst: list, cols: int) -> list[list]:
    return [lst[i:i + cols] for i in range(0, len(lst), cols)]


def product_list(request):
    products = [
        {'title': 'Range Rover', 'info': 'Lorem ipsum...', 'price': 150000},
        {'title': 'Land Rover Defender', 'info': 'Lorem ipsum...', 'price': 100000},
        {'title': 'Range Rover Sport', 'info': 'Lorem ipsum...', 'price': 250000},
        {'title': 'Range Rover', 'info': 'Lorem ipsum...', 'price': 150000},
        {'title': 'Land Rover Defender', 'info': 'Lorem ipsum...', 'price': 100000},
        {'title': 'Range Rover Sport', 'info': 'Lorem ipsum...', 'price': 250000},
        {'title': 'Range Rover', 'info': 'Lorem ipsum...', 'price': 150000},
        {'title': 'Land Rover Defender', 'info': 'Lorem ipsum...', 'price': 100000},
        {'title': 'Range Rover Sport', 'info': 'Lorem ipsum...', 'price': 250000},
    ]
    return render(
        request,
        'store/product_list.html',
        context={'product_list': build_template(products, 3)}
    )
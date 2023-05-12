from django.shortcuts import render


def build_template(lst: list, cols: int) -> list[list]:
    return 


# [[1, 2, 3], [4, 5, 6], [7, 8, 9,], [10]]
print(build_template([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


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
        context={'products': products}
    )

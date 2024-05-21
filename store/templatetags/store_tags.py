from django import template
from store.models import Category, FavoriteProducts

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=None)


@register.simple_tag()
def get_sorted():
    sortes = [
        {
            "title": "Narxi bo'yicha",
            "sorters": [
                ('price', "O'sish bo'yicha"),
                ('-price', "Kamayish bo'yicha"),
            ]
        },
        {
            "title": "Rangi bo'yicha",
            'sorters': [
                ('color', "A dan Z gacham"),
                ('-color', "Z dan A gacham"),
            ]
        },
        {
            "title": "O'lchami bo'yicha",
            "sorters": [
                ('size', "O'sish bo'yicha"),
                ('-size', "Kamayish bo'yicha"),
            ]
        }
    ]
    return sortes


@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)


@register.simple_tag()
def get_favourite_products(user):
    fav = FavoriteProducts.objects.filter(user=user)
    products = [i.product for i in fav]
    return products

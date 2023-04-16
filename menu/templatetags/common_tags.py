from django import template
from menu.models import Category
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, name):
    filter_lft_rgt = Category.objects.get(title=name)
    menu_items = Category.objects.filter(left__lte=filter_lft_rgt.right, left__gte=filter_lft_rgt.left+1)
    return {
        "left": context["left"],
        "right": context["right"],
        "menu_items": menu_items,
        "name": name,
    }


@register.inclusion_tag('templatetags/recursive_menu.html', takes_context=True)
def recursive_menu(context, tree, parent, left, right):

    return {
        "menu_items": tree,
        "parent": parent,
        "left": left,
        "right": right,
    }
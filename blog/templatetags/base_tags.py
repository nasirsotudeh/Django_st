from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title(data="django"):
     return data


@register.inclusion_tag("blog/partials/navbar.html")
def nav_category():
     return {
          "category": Category.objects.filter(status = True)
     }

@register.inclusion_tag("blog/partials/categorys.html")
def main_category():
     return {
          "category": Category.objects.filter(status = True)
     }
from django import template
from ..models import Company

register = template.Library()


@register.simple_tag
def count_companies():
    return Company.objects.count()
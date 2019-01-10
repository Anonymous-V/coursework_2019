from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter('wrap_div')
@stringfilter
def wrap_div(value):
    value = value.replace('<select', '<div class="ss-custom-select"><select')
    value = value.replace('</select>', '</select></div>')
    return value
from django import template
from mammoth.models import Pattern

register = template.Library()

#@register.inclusion_tag('mammoth/categories.html')
#def get_category_list(current_category=None):
#    return {'categories': Category.objects.all(), 'current_category': current_category}

#@register.inclusion_tag('mammoth/patterns.html')
#def get_pattern_list(current_pattern=None):
#    return {'patterns': Pattern.objects.all(), 'current_pattern': current_pattern}
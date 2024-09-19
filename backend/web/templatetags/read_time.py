from django import template
import math

register = template.Library()

@register.filter
def read_time(content):
    words = len(content.split())
    return math.ceil(words / 200)  # Assuming an average reading speed of 200 words per minute

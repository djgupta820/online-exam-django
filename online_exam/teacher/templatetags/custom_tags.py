from atexit import register
from django import template
import datetime

register = template.Library()

@register.simple_tag
def update(val):
    data=val
    return data

@register.simple_tag
def question():
    val = 0
    val += 1
    return val
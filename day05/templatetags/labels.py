import datetime

from . import register

@register.simple_tag
def show_name(name):
    return name

@register.simple_tag
def current_time(format_str):
    return datetime.datetime.now().strftime(format_str)

@register.simple_tag(takes_context=True)
def current_time_1(context):
    format_str = context.get('format_str')
    return datetime.datetime.now().strftime(format_str)

@register.inclusion_tag('show_tags.html', name='stags')
def show_tag(person,person1):
    items = [
        {
            'name':'test',
            'age':'18',
        }
    ]
    return {
        "items":items,
        "person":person,
        "person1":person1,
    }

@register.inclusion_tag('new_tags.html',name='stage_new')
def new_tags(new):
    return {'new':new}
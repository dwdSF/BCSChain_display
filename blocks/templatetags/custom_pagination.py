from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def page_range(context):
    ''' Template filter for custom pagination.
        The built-in doesn't work well with so many pages. '''

    c = 5
    if context['paginator'].num_pages < 2 * (c + 1):
        return list(range(1, context['paginator'].num_pages + 1))
    if context['page_obj'].number < c + 2:
        n = range(1, 12)
    elif context['page_obj'].number > context['paginator'].num_pages - (c + 1):
        n = range(context['paginator'].num_pages - 2 * c,
                  context['paginator'].num_pages + 1)
    else:
        n = range(context['page_obj'].number - c,
                  context['page_obj'].number + (c + 1))
    return list(n)

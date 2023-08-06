from django import template

register = template.Library()


@register.filter
def order_by(qs, order):
    return qs.order_by(*(order.split(",")))


@register.filter
def startswith(string, substr):
    return string.startswith(substr)


@register.filter
def visible_count(model, user):
    return model.objects.all().visible(user).count()


@register.filter
def izip(a, b):
    return zip(a, b)


@register.filter
def register_queryset(qs):
    from aristotle_mdr.utils.cached_querysets import register_queryset
    return register_queryset(qs)

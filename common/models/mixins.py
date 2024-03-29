from django.urls import reverse
from django.utils.html import format_html


class LinkMixin:
    @staticmethod
    def link_to_object(obj, model_name):
        link = reverse(f'admin:{model_name}_change', args=[obj.id])
        return format_html('<a href="{}">{}</a>', link, obj)

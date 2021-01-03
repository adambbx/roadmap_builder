from django import template

from roadmaps.services.inline import InlineStaticService

register = template.Library()


@register.inclusion_tag('roadmaps/includes/inline_js.html')
def inline_javascript(name):
    return {
        'js_content': InlineStaticService().get_inline_static(name)
    }


@register.inclusion_tag('roadmaps/includes/inline_css.html')
def inline_css(name):
    return {
        'css_content': InlineStaticService().get_inline_static(name)
    }

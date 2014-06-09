from django import template
register = template.Library()

import json
from textwrap import dedent

from django.template.defaultfilters import escape, escapejs
from django.utils.safestring import mark_safe


@register.filter
def jsdata(value, name):
    return mark_safe('\n'.join([
        '<script id="%s-json" type="application/json">' % escape(name),
        escape(json.dumps(value, indent=4)),
        '</script>',
        dedent(
            '''
            <script type="text/javascript">
                var script = document.getElementById('%(name)s-json');
                var div = document.createElement('div');
                div.innerHTML = script.innerHTML;
                var text = div.textContent || div.innerText;
                window['%(name)s'] = JSON.parse(text);
            </script>'''
        ) % dict(name=escapejs(name))
    ]))

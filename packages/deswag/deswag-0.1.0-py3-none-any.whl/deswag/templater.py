"""deswag templater classes"""
import jinja2 as jinja


class Templater():
    def __init__(self, template):
        self._template = jinja.Template(template)

    def render(self, data):
        return self._template.render(data)

from functools import wraps


def make_html(element):
    def _make_html(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{element}>{func()}</{element}>'
        return wrapper
    return _make_html

formattable_texts = dict(
    unknown_http_method='Unknown HTTP method {method}.'
)


def format_text(text_name, with_trailing_newline=True, **kwargs):
    text = formattable_texts.get(text_name).format(**kwargs)
    return text + ('\n' if with_trailing_newline else '')

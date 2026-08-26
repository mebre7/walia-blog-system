from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def highlight(text, query):
    """
    Highlight occurrences of query in text (case-insensitive).
    Wraps matches in <mark> tags with search-highlight class.
    """
    if not text or not query:
        return text

    # Escape special regex characters in the query
    escaped_query = re.escape(query)

    # Use re.IGNORECASE for case-insensitive matching
    # Replace with <mark> tag to highlight
    pattern = re.compile(escaped_query, re.IGNORECASE)
    highlighted = pattern.sub(
        lambda m: f'<mark class="search-highlight">{m.group(0)}</mark>',
        str(text)
    )

    # Mark as safe so Django renders the HTML tags
    return mark_safe(highlighted)




"""Flask configuration."""

from typing import Optional
import os
from urllib.parse import urlparse

SERVER_NAME = None

A11Y_URL = os.environ.get("ARXIV_ACCESSIBILITY_URL",
                          "mailto:web-accessibility@cornell.edu")

BASE_SERVER = os.environ.get('BASE_SERVER', 'arxiv.org')

URLS = [
    ("help", "/help", BASE_SERVER),
    ("help_identifier", "/help/arxiv_identifier", BASE_SERVER),
    ("help_trackback", "/help/trackback", BASE_SERVER),
    ("help_mathjax", "/help/mathjax", BASE_SERVER),
    ("help_social_bookmarking", "/help/social_bookmarking", BASE_SERVER),
    ("contact", "/help/contact", BASE_SERVER),
    ("search_box", "/search", BASE_SERVER),
    ("search_advanced", "/search/advanced", BASE_SERVER),
    ("account", "/user", BASE_SERVER),
    ("login", "/user/login", BASE_SERVER),
    ("logout", "/user/logout", BASE_SERVER),
    ("home", "/", BASE_SERVER),
    ("ignore_me", "/IgnoreMe", BASE_SERVER),    # Anti-robot honneypot.
    ("pdf", "/pdf/<arxiv:paper_id>", BASE_SERVER),
    ("twitter", "/arxiv", "twitter.com"),
    ("blog", "/arxiv", "blogs.cornell.edu"),
    ("wiki", "/display/arxivpub/arXiv+Public+Wiki", "confluence.cornell.edu"),
    ("library", "/", "library.cornell.edu"),
    ("acknowledgment", "/x/ALlRF", "confluence.cornell.edu")
]
"""
URLs for external services, for use with :func:`flask.url_for`.

For details, see :mod:`arxiv.base.urls`.
"""

# In order to provide something close to the config_url behavior, this will
# look for ARXIV_{endpoint}_URL variables in the environ, and update `URLS`
# accordingly.
for key, value in os.environ.items():
    if key.startswith('ARXIV_') and key.endswith('_URL'):
        endpoint = "_".join(key.split('_')[1:-1]).lower()
        o = urlparse(value)
        if not o.netloc:    # Doesn't raise an exception.
            continue
        i: Optional[int]
        try:
            i = list(zip(*URLS))[0].index(endpoint)
        except ValueError:
            i = None
        if i is not None:
            URLS[i] = (endpoint, o.path, o.netloc)

ARXIV_BUSINESS_TZ = os.environ.get("ARXIV_BUSINESS_TZ", "US/Eastern")

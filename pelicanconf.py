AUTHOR = 'Greg Hayes'
SITENAME = "Greg's Workbench"
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/gregorybhayes/"),
    ("GitHub", "https://github.com/hayesgb/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "elegant"

LANDING_PAGE_TITLE = "The Personal Microsite of Greg Hayes"
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'theme/images', 'extra/robots.txt']

PROJECTS = [
    {
        'name': 'Azure Datalake FileSystem',
        'url': 'https://github.com/fsspec/adlfs'
    },
    {
        'name': 'US-11804124-B2 -- Reducing illnesses and infections caused by ineffective cleaning by tracking and controlling cleaning efficacy',
        'url': 'https://ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11804124',
    },
    {
        "name": "US 12008504 B2 -- Food Safety Risk and Sanitation Compliance Tracking",
        "url": "https://ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12008504",
    },
    {
        "name": "US-11308788-B2 -- Hygiene management for reducing illnesses and infections caused by ineffective hygiene practices",
        "url":  "https://ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11308788",
    },
    {
        "name": "US 11104762-B2 -- Silicone-Modified Polyester Coating",
        "url": "https://ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11104762",
    },
    {
        "name": "US 8895689B2 -- Production of polymers from waste cooking oil",
        "url": "https://ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8895689"
    },
    {
        "name": "US 7393591-B2 -- High-reflectivity Polyester Coating",
        "url": "https://ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7393591",
    },
]
PROJECTS_TITLE = "Favorite Projects & Patents"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'extract_toc', 
    'series', 
    'assets', 
    'share_post'
    ]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.meta': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
        'markdown.extensions.toc': {
            'permalink': 'true',
        },
    }
}

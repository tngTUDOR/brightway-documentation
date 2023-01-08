### path setup ####################################################################################

import os
import sys

### project information ###########################################################################

project = 'Brightway'
copyright = 'Brightway Developers'

version = '2.0' # the short X.Y version.
release = '2.0' # the full version, including alpha/beta/rc tags.

### project configuration #########################################################################

needs_sphinx = '5.3.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    # native extensions
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    # iPython extensions
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    # Jupyter Notebook support
    'nbsphinx',
    # example gallery support
    'sphinx_gallery.gen_gallery',
    # Markdown support
    'myst_parser',
    # API documentation support
    'autoapi',
    # responsive web component support
    'sphinx_design',
]

templates_path = ['source/_templates']
html_static_path = ["source/_static"]
exclude_patterns = ['_build']
html_theme = "pydata_sphinx_theme"

# The master toctree document.
master_doc = 'homepage'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

### extension configuration ########################################################################

## autoapi configuration ################################################

autoapi_dirs = [
    '../brightway2-analyzer',
    '../brightway2-calc',
    '../brightway2-data',
    '../brightway2-io',
    '../brightway2-regional'
]

autoapi_template_dir = './_autoapi_templates'
autoapi_root = 'source/api'
autoapi_keep_files = False

## myst_parser configuration ############################################

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = ["colon_fence"]

## sphinx_gallery configuration ##########################################

# https://sphinx-gallery.github.io/stable/getting_started.html#create-simple-gallery
sphinx_gallery_conf = {
    'examples_dirs': './examples', # path to your example scripts
    'gallery_dirs': './source/autogenerated_examples_gallery', # path to where to save gallery generated output
    'download_all_examples': False,
    'plot_gallery': False,
    'remove_config_comments': True,
    'notebook_images': 'https://documentation.brightway.dev/en/latest/'
}

## html configuration ###################################################

html_css_files = ['css/custom.css']

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# enable https://fontawesome.com/ icons
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

# https://pydata-sphinx-theme.readthedocs.io/en/stable/
html_theme_options = {
    "header_links_before_dropdown": 7,
    "announcement": "<p>⚠️ This is the draft of the new Brightway documentation. It is work in progress! In the meantime, use the legacy documentation at docs.brightway.dev.</p>",
    "collapse_navigation": True,
    "footer_items": ["copyright"],
    "external_links": [
        {
            "url": "https://training.brightway.dev/",
            "name": "Interactive Training",
        },
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/brightway-lca",
            "icon": "fab fa-github",
        },
        {
            "name": "Conda",
            "url": "https://anaconda.org/cmutel/brightway2",
            "icon": "fab fa-python",
        },
        {
            "name": "StackOverflow",
            "url": "https://stackoverflow.com/questions/tagged/brightway",
            "icon": "fab fa-stack-overflow",
        },
        {
            "name": "Gitter",
            "url": "https://gitter.im/brightway-lca/community",
            "icon": "fab fa-gitter",
        }
    ],
    "logo": {
      "image_light": "logo/BW_all_black_transparent_landscape.svg",
      "image_dark": "logo/BW_all_white_transparent_landscape.svg"
    },
    "favicons": [
      {
         "rel": "icon",
         "sizes": "100x100",
         "href": "logo/BW_favicon_100x100.png",
      },
      {
         "rel": "apple-touch-icon",
         "sizes": "500x500",
         "href": "logo/BW_favicon_500x500.png"
      },
   ]
}


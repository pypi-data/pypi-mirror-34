Tango Articles
==============

[![Build Status](https://travis-ci.org/tBaxter/tango-articles.svg?branch=master)](https://travis-ci.org/tBaxter/tango-articles)

Tango Articles is a simple but robust reusable app for news articles and blogs entries. It can power anything from a simple blog to sophisticated full-featured news sites.

While it forms a key component of Tango, it can also be dropped into an existing non-Tango project.

## Key features
* Have as many blogs as you like running one site.
* Have as many sections as you like.
* Drag-and-drop photo ordering
* Output is compliant with hnews microformat.

##Installation:

    pip install tango-articles

or install directly from github:

    pip install git+https://github.com/tBaxter/tango-articles.git


## Usage:
Add the following to your installed apps

```python
INSTALLED_APPS = (
  # ...
  'django.contrib.sites', # if not already present
  'articles',
  'tango_shared',
  # ...
)
```

Add a `SITE_ID` to your `settings.py`

```python
# ...
SITE_ID = 1
# ...
```

Then run `python manage.py syncdb` or `python manage.py makemigrations` and `python manage.py migrate`.

`tango_shared` and [bindings for Twitter](https://github.com/sixohsix/twitter) will be installed for you.




============
Introduction
============

This Django CMS enable you to create and administrate hierarchical pages in a simple and powerful way.

Django page CMS is based around a placeholders concept. A placeholder is special template tag that
you use in your page templates. Every time you add a placeholder in your template  a field
dynamically appears in the page admin.

The project repository code repository is found at this address: http://github.com/batiste/django-page-cms

.. contents::
    :local:
    :depth: 1

Demo
====

This admin interface is no up to date, but could give you an idea of what the software is doing:

 * admin : http://pagesdemo.piquadrat.ch/admin/
 * frontend : http://pagesdemo.piquadrat.ch/pages/


Key features
============

  * :doc:`Automatic creation of localized placeholders </placeholders>`
    (content area) in admin by adding placeholders tags into page templates.
  * Django admin application integration.
  * Multilingual support.
  * `Search indexation with Django haystack <http://haystacksearch.org/>`_.
  * Fine grained rights management (publisher, hierarchy manager, language manager).
  * :ref:`Rich Text Editors <placeholder-widgets-list>` are directly available.
  * Page can be moved in the tree in a visual way.
  * The tree can be expanded/collapsed. A cookie remember your preferences.
  * Possibility to specify a different page URL for each language.
  * The frontend example provide a basic "edit in place" feature.
  * Directory-like page hierarchy (page can have the same name if they are not in the same directory).
  * Every page can have multiple alias URLs. It's especially useful to migrate websites.
  * :doc:`Possibility to integrate 3th party apps </3rd-party-apps>`.
  

Other features
==============

Here is the list of features you can enable/disable:

  * Revisions,
  * Image placeholder,
  * File browser with django-filebrowser,
  * Support for future publication start/end date,
  * Page redirection to another page,
  * Page tagging,
  * User input sanitizer (to avoid XSS),
  * `Sites framework <http://docs.djangoproject.com/en/dev/ref/contrib/sites/#ref-contrib-sites>`_

Dependencies & Compatibility
============================

  * Django 1.1.1, Django 1.0 with older release (1.0.5)
  * Python 2.3.
  * `django-haystack if used <http://haystacksearch.org/>`_
  * `django-authority for per object rights management <http://bitbucket.org/jezdez/django-authority/src/>`_.
  * `django-mptt <http://code.google.com/p/django-mptt/>`_
  * `django-tagging <http://code.google.com/p/django-tagging/>`_ (if PAGE_TAGGING = True)
  * `html5lib <http://code.google.com/p/html5lib/>`_ (if PAGE_SANITIZE_USER_INPUT = True)
  * `django-tinymce <http://code.google.com/p/django-tinymce/>`_ (if PAGE_TINYMCE = True)
  * Django page CMS is shipped with jQuery.
  * Django page CMS works well with `django-staticfiles <http://pypi.python.org/pypi/django-staticfiles/>`_
  * Compatible with MySQL, PostgreSQL, SQLite3, some issues are known with Oracle.

.. note::

    For install instruction go to the :doc:`Installation section </installation>`

Ask for help
============

`Django page CMS Google Group <http://groups.google.com/group/django-page-cms>`_

Test it
-------

To test this CMS checkout the code with subversion::

    git clone git://github.com/batiste/django-page-cms.git django-page-cms

And then, run the development server::
    
    cd example/
    python manage.py syncdb
    python manage.py build_static
    python manage.py manage.py runserver


Django Page CMS try to keep the code base stable. The test coverage is higher
than 80% and we try to keep it this way. To run the test suite::

    python setup.py test

.. note::

    If you are not admin you have to create the appropriate permissions to modify pages.
    After that you will be able to create pages.

Handling images and files
---------------------------

Django page CMS include a image placeholder for basic needs. For files browser you could use django-filebrowser:

  * http://code.google.com/p/django-filebrowser/

Once the application installed a `FileBrowseInput` will be available to use with your placeholders.

Translations
------------

This application is available in English, German, French, Spanish, Danish, Russian and Hebrew.


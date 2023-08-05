=====================================
 Sphinx Themes for Logilab Documents
=====================================

Logilab Sphinx Themes are a set of visually (c)lean, responsive, configurable
theme for the Sphinx_ documentation system. It is Python 2+3 compatible.

Installation
============

You can install the theme via pip::

  pip install logilab-sphinx-theme


Configuration
=============

Add the following to your ``conf.py``:

.. code-block:: python

   # use this to use logilab-spĥinx-themes
   html_theme = 'logilab'

.. Note:: for old sphinx versions (aka. <1.3), some more content is required:

   .. code-block:: python

      import logilab_sphinx_themes

      html_theme_path = [logilab_sphinx_themes.get_path()]
      extensions = ['logilab_sphinx_themes']
      html_theme = 'logilab'

Theme options
-------------

Primary theme options are configured in the ``html_theme_options`` variable
set in ``conf.py``. Theme options are:

- ``logo``: Relative path (from $PROJECT/_static/) to a logo image, which will
  appear in the upper left corner above the name of the project. Defaults to
  ``logilab_logo.svg``.

- ``logo_url``: URL used as link for the logo. Defaults to
  ``https://www.logilab.fr``.




For more documentation, please see
https://www.logilab.org/project/logilab-sphinx-themes

.. _Sphinx: http://www.sphinx-doc.org

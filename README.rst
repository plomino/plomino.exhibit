Description
===========

``plomino.exhibit`` allows using Exhibit to browse Plomino view data.
 
Exhibit is a Javascript framework which provides advanced text search and
filtering capabilities, with interactive maps, timelines, and other
visualizations.
More information about `Exhibit <http://www.simile-widgets.org/exhibit/>`_.

``plomino.exhibit`` adapts ``eea.daviz`` to Plomino, ``eea.daviz`` being a
Plone integration for Exhibit.
More information about `eea.daviz <http://plone.org/products/eea.daviz>`_.


Usage
=====

Add ``plomino.exhibit`` to your buildout, run the buildout, and
``plomino.exhibit``, ``eea.daviz`` and its dependencies will be deployed.

Install ``eea.daviz`` in your Plone site.

Then you can enable the *Exhibit* view on any Plomino view (using the Plone
menu *Actions* > *Enable Exhibit view*). 

Regarding Daviz configuration, see ``eea.daviz`` documentation.

All Plomino columns will be treated as *text* by default. To specify another
data type, use the following format for the column id: ``id$type`` (example:
``budget$number``).

By default, the document id is used as label. To provide a custom label,
just add a column with the id ``label``.


Credits
========

Companies
---------

|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
 

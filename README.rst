Description
===========

plomino.exhibit allows to browse Plomino view data using Exhibit.
 
Exhibit is Javascript framework providing advanced text search and filtering
functionalities, with interactive maps, timelines, and other visualizations.
More information about `Exhibit <http://www.simile-widgets.org/exhibit/>`.

plomino.exhibit adapts eea.daviz to Plomino, eea.daviz being a Plone
integration for Exhibit.
More information about `eea.daviz <http://plone.org/products/eea.daviz>`.

Usage
=====

Add plomino.exhibit to your buildout, run the buildout, it will deploy
plomino.exhibit, and also eea.daviz and its dependencies.

Install eea.daviz in your Plone site.

Then, you can enable Exhibit view on any Plomino view (using the Plone menu
"Actions" > "Enable Exhibit view"). 

Regarding Daviz configuration, see eea.daviz documentation.

All Plomino columns will be considered as text by default. To specifiy another
data type, use the following format for the column id: id$type
(example: budget$number).

By default, the document id is used as label, to provide a custom label, just
add a column with id 'label'.

Credits
========
Companies
---------
|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
 
Doctest
-------

.. testsetup::

   from sphinx_advanced import sphinx_advanced

.. note:: Sphinx docs for :mod:`~sphinx.ext.doctest`,

Example using ``doctest`` :

.. doctest::

   >> print(sphinx_advanced.help())
   Sphinx Advanced Tutorial Module


Example using ``testcode`` :

.. testcode::

   print(sphinx_advanced.help())


Example using ``testoutput`` :

.. testoutput::

   Sphinx Advanced Tutorial Module

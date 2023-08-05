.. _start-intro:


What is formulas?
*****************

Formulas implements an interpreter for excel formulas, which parses
and compile excel formulas expressions.

Moreover, it compiles excel workbooks to python and executes without
using the Excel COM server. Hence,  **Excel is not needed**.


Installation
************

To install it use (with root privileges):

::

   $ pip install formulas

Or download the last git version and use (with root privileges):

::

   $ python setup.py install


Install extras
==============

Some additional functionality is enabled installing the following
extras:

* excel: enables to compile excel workbooks to python and execute
   using: ``ExcelModel``.

* plot: enables to plot the formula ast and the excel model.

To install formulas and all extras, do:

::

   $ pip install formulas[all]

.. _end-quick:


Basic Examples
**************


Parsing
=======

An example how to parse and execute an excel formula is the following:

>>> import formulas
>>> func = formulas.Parser().ast('=(1 + 1) + B3 / A2')[1].compile()

To visualize formula model and get the input order you can do the
following:

..

   >>> list(func.inputs)
   ['A2', 'B3']
   >>> func.plot(view=False)  # Set view=True to plot in the default browser.
   SiteMap([(=((1 + 1) + (B3 / A2)), SiteMap())])

   [graph]

Finally to execute the formula and plot the workflow:

..

   >>> func(1, 5)
   OperatorArray(7.0, dtype=object)
   >>> func.plot(workflow=True, view=False)  # Set view=True to plot in the default browser.
   SiteMap([(=((1 + 1) + (B3 / A2)), SiteMap())])

   [graph]


Excel
=====

An example how to load, calculate, and write an excel workbook is the
following:

>>> import formulas
>>> fpath = 'test/test_files/excel.xlsx'
>>> xl_model = formulas.ExcelModel().loads(fpath).finish()
>>> xl_model.calculate()
Solution(...)
>>> xl_model.write()
{'EXCEL.XLSX': {Book: <openpyxl.workbook.workbook.Workbook ...>}}

To compile and execute a sub model from a workbook you can do the
following:

>>> inputs = ["'[EXCEL.XLSX]DATA'!A2"]  # input cells
>>> outputs = ["'[EXCEL.XLSX]DATA'!C2"]  # output cells
>>> func = xl_model.compile(inputs, outputs)
>>> func(2).value[0,0]
4.0

..

   >>> func.plot(view=False)  # Set view=True to plot in the default browser.
   SiteMap([(Dispatcher ..., SiteMap())])

   [graph]



**********
read_files
**********

The ``read_files`` module contains methods and classes that allow a user to read different
types of files in different ways.  Within the module a user will find functionality that 
allows them to read text files and csv files by columns and keywords.  This module
also contains functions to read sqlite databases, xml files, json files, yaml files, 
and html files

Read Text File by Keywords
==========================
This class is used to open a text file.  The member functions will look for a specific keyword
and then read the variable to the right of the keyword as a specific data type

.. autoclass:: read_files.ReadTextFileKeywords
   :members:
   
Read Columnar Data
==================

These functions will read columnar data structures in csv, txt and xlsx files
as a user defined data type.

.. autofunction:: read_files.read_csv_columns_by_headers

.. autofunction:: read_files.read_csv_columns_by_index

.. autofunction:: read_files.read_text_columns_by_headers
 
.. autofunction:: read_files.read_text_columns_by_index

.. autofunction:: read_files.read_excel_columns_by_headers

.. autofunction:: read_files.read_excel_columns_by_index
 
Read Databases
==============

The following classes and functions allow a user to read information from structured
databases

.. autoclass:: read_files.ManageSQLiteDB
   :members:

.. autofunction:: read_files.simple_sqlite_query

Misc Files
==========

This section describes funtions that can be used to read other file types to include
``xml``, ``html``, ``json``, and ``yaml`` files

.. autofunction:: read_files.read_json_file

.. autofunction:: read_files.read_xml_file

.. autofunction:: read_files.read_yaml_file

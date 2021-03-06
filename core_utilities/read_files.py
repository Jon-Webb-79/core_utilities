# Import packages here
import os
import sys
import numpy as np
import pandas as pd
from typing import List, Dict
import sqlite3
import json
from bs4 import BeautifulSoup
import yaml
#from lxml import objectify
# - If a package and a module within the package is to be imported
#   uncomment the following lines where dir is the directory containing
#   the source files.  These lines should go above the module imports
# import sys
# import os
# sys.path.insert(1, os.path.abspath(dir))
# ================================================================================
# ================================================================================
# Date:    Month Day, Year
# Purpose: Describe the purpose of functions of this file

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "1.0"
# ================================================================================
# ================================================================================
# Insert Code here


class ReadTextFileKeywords:
    """
    A class to find keywords in a text file and the the variable(s)
    to the right of the key word.  This class must inherit the
    ``FileUtilities`` class


    :param file_name: The name of the file being read to include the
                      path-link

    For the purposes of demonstrating the use of this class, assume
    a text file titled ``test_file.txt`` with the following contents.


    .. code-block:: text

        sentence: This is a short sentence!
        float: 3.1415 # this is a float comment
        double: 3.141596235941 # this is a double comment
        String: test # this is a string comment
        Integer Value: 3 # This is an integer comment
        float list: 1.2 3.4 4.5 5.6 6.7
        double list: 1.12321 344.3454453 21.434553
        integer list: 1 2 3 4 5 6 7
    """
    def __init__(self, file_name: str):
        self.file_name = file_name
        if not os.path.isfile(file_name):
            sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
# ----------------------------------------------------------------------------

    def read_double(self, key_words: str) -> np.float64:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The float value following the **key_word** on the
                      text file.  This variable is returned as a
                      np.float64 data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the first data point following the key word(s) on the text file as a float value.
        The text file can also contain a comment line following the variable
        being read.  For example we could use this class to read the double
        value 3.141596235941 in the following manner.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > double_data = dat.read_double('double:')
            > print(double_data)
            3.141596235941
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.float64(values[0])
# ----------------------------------------------------------------------------

    def read_double_list(self, key_words: str) -> List[np.float64]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      string values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as a
        numpy.float64 value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > str_data = dat.read_double_list('double list:')
            > print(str_data)
            [1.12321, 344.3454453, 21.434553]
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [np.float64(value) for value in values]
        return values
# ----------------------------------------------------------------------------

    def read_float(self, key_words: str) -> np.float32:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The float value following the **key_word** on the
                      text file.  This variable is returned as a
                      np.float32 data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the first data point following the key word(s) on the text file as a float value.
        The text file can also contain a comment line following the variable
        being read.  For example we could use this class to read the float
        value 3.1415 in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > float_data = dat.read_float('float data:')
           > print(float_data)
           3.1415
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.float32(values[0])
# ----------------------------------------------------------------------------

    def read_float_list(self, key_words: str) -> List[np.float32]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      numpy.float32 values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as a
        float value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > float_data = dat.read_float_list('float list')
            > print(float_data)
            [1.2, 3.4, 4.5, 5.6, 6.7]
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [np.float32(value) for value in values]
        return values
# ----------------------------------------------------------------------------

    def read_integer(self, key_words: str) -> np.int32:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The integer value following the **key_word** on the
                      text file.  This variable is returned as a np.int32
                      data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the first data point following the key word(s) on the text file as a
        integer value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > int_data = dat.read_float('Integer Value')
           > print(int_data)
           3
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return np.int32(values[0])
# ----------------------------------------------------------------------------

    def read_integer_list(self, key_words: str) -> List[np.int32]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      numpy.float32 values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as an
        integer value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > float_data = dat.read_integer_list('integer list:')
            > print(float_data)
            [1, 2, 3, 4, 5, 6, 7]
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [np.int32(value) for value in values]
        return values
# ----------------------------------------------------------------------------

    def read_sentence(self, key_words: str) -> str:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The data following the **key_word** on the text file.
                      The data is returned as a continuous string value

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the data following the key word(s) on the text file as a continuous string.
        The text file can also contain a comment line following the variable
        being read.  For example we could use this class to read the integer
        value `This is a short sentence!` in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > str_data = dat.read_float('sentence:')
           > print(str_data)
           'This is a short sentence!'
        """
        input_words = key_words.split()
        with open(self.file_name) as Input_File:
            lines = Input_File.readlines()
            for line in lines:
                variable = line.split()
                counter = 0
                for i in range(len(input_words)):
                    if input_words[i] != variable[i]:
                        break
                    else:
                        counter += 1
                if counter == len(input_words):
                    start = len(input_words)
                    end = len(variable)
                    word = ''
                    for i in range(start, end):
                        word = word + ' ' + variable[i]
                    return word.lstrip()
        sys.exit('{}{}{}'.format(key_words, " Keywords not found in ", self.file_name))
# ----------------------------------------------------------------------------

    def read_string(self, key_words: str) -> str:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string value following the **key_word** on the
                      text file.  This variable is returned as a str
                      data type

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the first data point following the key word(s) on the text file as a
        string value. The text file can also contain a comment line following
        the variable being read.  For example we could use this class to
        read the string value `test` in the following manner.

        .. code-block:: python

           > dat = ReadTextFileKeywords('test_file.txt')
           > str_data = dat.read_float('String:')
           > print(str_data)
           'test'
        """
        values = self.read_sentence(key_words)
        values = values.split()
        return str(values[0])
# ----------------------------------------------------------------------------

    def read_string_list(self, key_words: str) -> List[str]:
        """

        :param key_words: The key word that proceeds the data to be
                          read
        :return data: The string values following the **key_word** on the
                      text file.  This variable is returned as a List of
                      string values

        This function reads a text file and searches for a key word which
        can be a single word or a string of words.  This function will read
        the the data points following the key word(s) on the text file as a
        string value. The text file can also contain a comment line following
        the variable being read.

        .. code-block:: python

            > dat = ReadTextFileKeywords('test_file.txt')
            > str_data = dat.read_string_list('sentence:')
            > print(str_data)
            ['This', 'is', 'a', 'short', 'sentence!']
        """
        values = self.read_sentence(key_words)
        values = values.split()
        values = [str(value) for value in values]
        return values
# ================================================================================
# ================================================================================


def read_csv_columns_by_headers(file_name: str, headers: List[str],
                                data_type: List[type],
                                skip: int = 0) -> pd.DataFrame:
    """

    :param file_name: The file name to include path-link
    :param headers: A list of the names of the headers that contain
                    columns which will be read
    :param data_type: A list containing the data type of each column.  Data
                      types are limited to ``numpy.int64``, ``numpy.float64``,
                      and ``str``
    :param skip: The number of lines to be skipped before reading data
    :return df: A pandas dataframe containing all relevant information

    This function assumes the file has a comma (i.e. ,) delimiter, if
    it does not, then it is not a true .csv file and should be transformed
    to a text function and read by the xx function.  Assume we have a .csv
    file titled ``test.csv`` with the following format.

    .. list-table:: test.csv
      :widths: 6 10 6 6
      :header-rows: 1

      * - ID,
        - Inventory,
        - Weight_per,
        - Number
      * - 1,
        - Shoes,
        - 1.5,
        - 5
      * - 2,
        - t-shirt,
        - 1.8,
        - 3,
      * - 3,
        - coffee,
        - 2.1,
        - 15
      * - 4,
        - books,
        - 3.2,
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.csv'
       > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_csv_columns_by_headers(file_name, headers, dat)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40

    This function can also use the `skip` attributed read data when the
    headers are not on the first line.  For instance, assume the following csv file;

    .. list-table:: test1.csv
      :widths: 16 8 5 5
      :header-rows: 0

      * - This line is used to provide metadata for the csv file
        -
        -
        -
      * - This line is as well
        -
        -
        -
      * - ID,
        - Inventory,
        - Weight_per,
        - Number
      * - 1,
        - Shoes,
        - 1.5,
        - 5
      * - 2,
        - t-shirt,
        - 1.8,
        - 3,
      * - 3,
        - coffee,
        - 2.1,
        - 15
      * - 4,
        - books,
        - 3.2,
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test1.csv'
       > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_csv_columns_by_headers(file_name, headers, dat, skip=2)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40
    """
    if not os.path.isfile(file_name):
        sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
    dat = dict(zip(headers, data_type))
    df = pd.read_csv(file_name, usecols=headers, dtype=dat, skiprows=skip)
    return df
# ----------------------------------------------------------------------------


def read_csv_columns_by_index(file_name: str, col_index: List[int],
                              data_type: List[type], col_names: List[str],
                              skip: int = 0) -> pd.DataFrame:
    """
    :param file_name: The file name to include path-link
    :param col_index: A list of the columns to be read by number,
                      starting with column 0 as the far left column
    :param data_type: A list containing the data type of each column.  Data
                      types are limited to ``numpy.int64``, ``numpy.float64``,
                      and ``str``
    :param col_names: A list containing the names to be given to
                      each column
    :param skip: The number of lines to be skipped before reading data
    :return df: A pandas dataframe containing all relevant information

    This function assumes the file has a comma (i.e. ,) delimiter, if
    it does not, then it is not a true .csv file and should be transformed
    to a text function and read by the xx function.  Assume we have a .csv
    file titled ``test.csv`` with the following format.

    .. list-table:: test.csv
      :widths: 6 10 6 6
      :header-rows: 0

      * - 1,
        - Shoes,
        - 1.5,
        - 5
      * - 2,
        - t-shirt,
        - 1.8,
        - 3,
      * - 3,
        - coffee,
        - 2.1,
        - 15
      * - 4,
        - books,
        - 3.2,
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.csv'
       > headers = [0, 1, 2, 3]
       > names = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_csv_columns_by_index(file_name, headers, dat, names)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40

    This function can also use the `skip` attributed read data when the
    headers are not on the first line.  For instance, assume the following csv file;

    .. list-table:: test1.csv
      :widths: 16 8 5 5
      :header-rows: 0

      * - This line is used to provide metadata for the csv file
        -
        -
        -
      * - This line is as well
        -
        -
        -
      * - 1,
        - Shoes,
        - 1.5,
        - 5
      * - 2,
        - t-shirt,
        - 1.8,
        - 3,
      * - 3,
        - coffee,
        - 2.1,
        - 15
      * - 4,
        - books,
        - 3.2,
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test1.csv'
       > headers = [0, 1, 2, 3]
       > names = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_csv_columns_by_index(file_name, headers,
                                        dat, names, skip=2)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40
    """
    if not os.path.isfile(file_name):
        sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
    dat = dict(zip(col_index, data_type))
    df = pd.read_csv(file_name, usecols=col_index, names=col_names, dtype=dat,
                     skiprows=skip)
    return df
# --------------------------------------------------------------------------------


def read_text_columns_by_headers(file_name: str, headers: List[str],
                                 data_type: List[type],
                                 skip: int = 0, delimiter=r"\s+") -> pd.DataFrame:
    """

    :param file_name: The file name to include path-link
    :param headers: A list of the names of the headers that contain
                    columns which will be read
    :param data_type: A list containing the data type of each column.  Data
                      types are limited to ``numpy.int64``, ``numpy.float64``,
                      and ``str``
    :param skip: The number of lines to be skipped before reading data
    :param delimiter: The type of delimiter separating data in the text file.
                Defaulted to space delimited, where a space is one or
                more white spaces.  This function can use any delimiter,
                to include a comma separation; however, a comma delimiter
                should be a .csv file extension.
    :return df: A pandas dataframe containing all relevant information

    This function assumes the file has a space delimiter, if
    Assume we have a .csv file titled ``test.txt`` with the following
    format.

    .. list-table:: test.txt
      :widths: 6 10 6 6
      :header-rows: 1

      * - ID
        - Inventory
        - Weight_per
        - Number
      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.txt'
       > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_text_columns_by_headers(file_name, headers, dat)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40

    This function can also use the `skip` attributed read data when the
    headers are not on the first line.  For instance, assume the following csv file;

    .. list-table:: test.txt
      :widths: 16 8 5 5
      :header-rows: 0

      * - This line is used to provide metadata for the csv file
        -
        -
        -
      * - This line is as well
        -
        -
        -
      * - ID
        - Inventory
        - Weight_per
        - Number
      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.txt'
       > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_text_columns_by_headers(file_name, headers,
                                           dat, skip=2)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40
    """
    if not os.path.isfile(file_name):
        sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
    dat = dict(zip(headers, data_type))
    df = pd.read_csv(file_name, usecols=headers, dtype=dat, skiprows=skip,
                     sep=delimiter)
    return df
# --------------------------------------------------------------------------------


def read_text_columns_by_index(file_name: str, col_index: List[int],
                               data_type: List[type], col_names: List[str],
                               skip: int = 0, delimiter=r"\s+") -> pd.DataFrame:
    """

    :param file_name: The file name to include path-link
    :param col_index: A list of the columns to be read by number,
                      starting with column 0 as the far left column
    :param data_type: A list containing the data type of each column.  Data
                      types are limited to ``numpy.int64``, ``numpy.float64``,
                      and ``str``
    :param col_names: A list containing the names to be given to
                      each column
    :param skip: The number of lines to be skipped before reading data
    :param delimiter: The type of delimiter separating data in the text file.
                Defaulted to space delimited, where a space is one or
                more white spaces.  This function can use any delimiter,
                to include a comma separation; however, a comma delimiter
                should be a .csv file extension.
    :return df: A pandas dataframe containing all relevant information

    Assume we have a .txt file titled ``test.txt`` with the following format.

    .. list-table:: test.txt
      :widths: 6 10 6 6
      :header-rows: 0

      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.txt'
       > headers = [0, 1, 2, 3]
       > names = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_text_columns_by_index(file_name, headers, dat, names)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40

    This function can also use the `skip` attributed read data when the
    headers are not on the first line.  For instance, assume the following csv file;

    .. list-table:: test.txt
      :widths: 16 8 5 5
      :header-rows: 0

      * - This line is used to provide metadata for the csv file
        -
        -
        -
      * - This line is as well
        -
        -
        -
      * - ID
        - Inventory
        - Weight_per
        - Number
      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.txt'
       > headers = [0, 1, 2, 3]
       > names = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_text_columns_by_index(file_name, headers,
                                        dat, names, skip=2)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40

    """
    if not os.path.isfile(file_name):
        sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
    dat = dict(zip(col_index, data_type))
    df = pd.read_csv(file_name, usecols=col_index, names=col_names, dtype=dat,
                     skiprows=skip, sep=delimiter)
    return df
# ----------------------------------------------------------------------------


def read_excel_columns_by_headers(file_name: str, tab: str, headers: List[str],
                                  data_type: List[type], skip: int = 0) -> pd.DataFrame:
    """

    :param file_name: The file name to include path-link.  Must be an
                      .xls file format.  This code will **not** read .xlsx
    :param tab: The tab or sheet name that data will be read from
    :param headers: A list of the names of the headers that contain
                    columns which will be read
    :param data_type: A list containing the data type of each column.  Data
                      types are limited to ``numpy.int64``, ``numpy.float64``,
                      and ``str``
    :param skip: The number of lines to be skipped before reading data
    :return df: A pandas dataframe containing all relevant information

    Assume we have a .xls file titled ``test.xls`` with the following format
    in a tab titled ``primary``.

    .. list-table:: test.xls
      :widths: 6 10 6 6
      :header-rows: 1

      * - ID
        - Inventory
        - Weight_per
        - Number
      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.xls'
       > tab = "primary"
       > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_excel_columns_by_headers(file_name, tab, headers, dat)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40

    This function can also use the `skip` attributed read data when the
    headers are not on the first line.  For instance, assume the following csv file;

    .. list-table:: test.xls
      :widths: 16 8 5 5
      :header-rows: 0

      * - This line is used to provide metadata for the csv file
        -
        -
        -
      * - This line is as well
        -
        -
        -
      * - ID
        - Inventory
        - Weight_per
        - Number
      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.xls'
       > tab = "primary"
       > headers = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_excel_columns_by_headers(file_name, tab,
                                            headers, dat, skip=2)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40
    """
    if not os.path.isfile(file_name):
        sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
    dat = dict(zip(headers, data_type))
    df = pd.read_excel(file_name, sheet_name=tab, usecols=headers,
                       dtype=dat, skiprows=skip)
    return df
# ----------------------------------------------------------------------------


def read_excel_columns_by_index(file_name: str, tab: str, col_index: List[int],
                                col_names: List[str], data_type: List[type],
                                skip: int = 0) -> pd.DataFrame:
    """

    :param file_name: The file name to include path-link.  Must be an
                      .xls file format.  This code will **not** read .xlsx
    :param tab: The tab or sheet name that data will be read from
    :param col_index: A list of the columns to be read by number,
                      starting with column 0 as the far left column
    :param col_names: A list containing the names to be given to
                      each column
    :param data_type: A list containing the data type of each column.  Data
                      types are limited to ``numpy.int64``, ``numpy.float64``,
                      and ``str``
    :param skip: The number of lines to be skipped before reading data
    :return df: A pandas dataframe containing all relevant information

    Assume we have a .txt file titled ``test.xls`` with the following format.

    .. list-table:: test.xls
      :widths: 6 10 6 6
      :header-rows: 0

      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.xls'
       > tab = 'primary'
       > headers = [0, 1, 2, 3]
       > names = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_excel_columns_by_index(file_name, tab, headers, names, dat)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40

    This function can also use the `skip` attributed read data when the
    headers are not on the first line.  For instance, assume the following csv file;

    .. list-table:: test.xls
      :widths: 16 8 5 5
      :header-rows: 0

      * - This line is used to provide metadata for the csv file
        -
        -
        -
      * - This line is as well
        -
        -
        -
      * - ID
        - Inventory
        - Weight_per
        - Number
      * - 1
        - Shoes
        - 1.5
        - 5
      * - 2
        - t-shirt
        - 1.8
        - 3
      * - 3
        - coffee
        - 2.1
        - 15
      * - 4
        - books
        - 3.2
        - 48

    This file can be read via the following command

    .. code-block:: python

       > file_name = 'test.xls'
       > tab = "primary"
       > headers = [0, 1, 2, 3]
       > names = ['ID', 'Inventory', 'Weight_per', 'Number']
       > dat = [int, str, float, int]
       > df = read_excel_columns_by_index(file_name, tab, headers,
                                          names, dat, skip=2)
       > print(df)
           ID Inventory Weight_per Number
        0  1  shoes     1.5        5
        1  2  t-shirt   1.8        3
        2  3  coffee    2.1        15
        3  4  books     3.2        40
    """
    if not os.path.isfile(file_name):
        sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
    dat = dict(zip(col_index, data_type))
    df = pd.read_excel(file_name, sheet_name=tab, usecols=col_index,
                       names=col_names, dtype=dat, skiprows=skip, header=None)
    return df
# ================================================================================
# ================================================================================


class ManageSQLiteDB:
    """

    :param database: The database name to include its path-link

    This class allows users to interface with SQLite databases, open the
    database, close the database and input queries.
    """
    def __init__(self, database: str):
        self.database = database
        if not os.path.isfile(self.database):
            sys.exit('{}{}{}'.format('FATAL ERROR: ',
                                     self.database, ' does not exist'))
        self.conn = sqlite3.connect(self.database)
# ----------------------------------------------------------------------------

    def close_database_connection(self) -> None:
        """
        This function closes a database connection
        """
        self.conn.close()
        return
# ----------------------------------------------------------------------------

    def query_db(self, query: str) -> pd.DataFrame:
        """

        :param query: A SQLite query statement
        :return df: A dataframe containing the results of the
                    SQLite query

        This function will read a database in any way the user queries
        it.  Assume we have a database titled Maintenance.db which contains
        several tables, one of which is titled gas.  The gas table contains
        a history of all times a vehicle has been refueled to include how
        many gallons, the date, and the expense.

        .. code-block:: python

           > file = '../data/test/Maintenance.db'
           > db = ManageSQLiteDB(file)
           > query = "Select Date, Cost, Gallons FROM gas;"
           > df = db.query_db(query)
           > db.close_database_connection()
           > print(df)

        .. list-table:: dataframe
           :widths: 6 6 6
           :header-rows: 1

           * - Date
             - Cost
             - Gallons
           * - 2020-02-04
             - 27.88
             - 9.961
           * - 2020-02-06
             - 23.75
             - 9.619
           * - 2020-02-13
             - 28.30
             - 10.256

        """
        df = pd.read_sql_query(query, self.conn)
        return df
# ============================================================================
# ============================================================================


def simple_sqlite_query(database: str, query: str) -> pd.DataFrame:
    """

    :param database: The SQLite database name with path-link
    :param query: The SQLite query
    :return df: A dataframe containing the query results

    This function allows a user to conduct a quick SQLite database query and
    handles class instantiation and database closure for the user.  This function
    will only query the database once and will close the database after
    the function exit.  If the user wishes to make multiple queries before
    closing the database, then they should directly interface with the
    ManageSQLite class.

    Assume we have a database titled Maintenance.db which contains
    several tables, one of which is titled gas.  The gas table contains
    a history of all times a vehicle has been refueled to include how
    many gallons, the date, and the expense.

    .. code-block:: python

        > file = '../data/test/Maintenance.db'
        > query = "Select Date, Cost, Gallons FROM gas;"
        > df = db.simple_sqlite_query(file, query)
        > print(df)

    .. list-table:: dataframe
        :widths: 6 6 6
        :header-rows: 1

        * - Date
          - Cost
          - Gallons
        * - 2020-02-04
          - 27.88
          - 9.961
        * - 2020-02-06
          - 23.75
          - 9.619
        * - 2020-02-13
          - 28.30
          - 10.256
    """
    db = ManageSQLiteDB(database)
    df = db.query_db(query)
    db.close_database_connection()
    return df
# ================================================================================
# ================================================================================
# read misc files


def read_json_file(file_name: str) -> Dict:
    """

    param file_name: The name of the file being read to include the path-length
    :return db: The json string

    This function reads a .json file and captures its contents as a dictionary
    of dictionaries.  An example might look like the code snipped below, assuming
    a json file with the following information in a file titled json.json

    .. code-block:: text

        {"widget": {
         "debug": "on",
         "window": {
         "title": "Sample Konfabulator Widget",
         "name": "main_window",
         "width": 500,
         "height": 500
        },
        "image": {
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
       },
        "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
         }}

    .. code-block:: python

       > file = json.json
       > dat = read_json_file(file)
       > print(dat['widget']['debug'])
       'on'
    """
    with open(file_name) as file:
        db = json.load(file)
    return db
# --------------------------------------------------------------------------------


def read_xml_file(file_name: str):
    """

    :param file_name: The name of the xml file to be opened to include the
                      path length
    :return bs_data: The xml data as a beautiful soup object.  For more details
                     on parsing beautiful soup data see 
                     `beautiful soup <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>_`

    This function reads in a xml or an html file and returns its contents as a
    text string that can be parsed with a beautiful soup function.  Asume a
    file titled xml.xml with the contents shown below.

    .. code-block:: text

       <widget>
       <debug>on</debug>
       <window title="Sample Konfabulator Widget">
           <name>main_window</name>
           <width>500</width>
           <height>500</height>
       </window>
       <image src="Images/Sun.png" name="sun1">
           <hOffset>250</hOffset>
           <vOffset>250</vOffset>
           <alignment>center</alignment>
       </image>
       <text data="Click Here" size="36" style="bold">
           <name>text1</name>
           <hOffset>250</hOffset>
           <vOffset>100</vOffset>
           <alignment>center</alignment>
           <onMouseUp>
               sun1.opacity = (sun1.opacity / 100) * 90;
           </onMouseUp>
       </text>
       </widget>

    .. code-block:: python

       > file_name = 'xml.xml'
       > db = read_xml_file(file_name)
       > db = read_xml_file(file)
       > img_name =db.find(src="Images/Sun.png").get_text()
       > print(img_name)
       250
       250
       center
    """
    with open(file_name, 'r') as f:
        data = f.read()
    bs_data = BeautifulSoup(data, "xml")
    return bs_data
# --------------------------------------------------------------------------------


def read_yaml_file(file_name: str):
    """

    :param file_name: The name of the taml file to include the path length
    :return data: The data extracted from the yaml file

    Assume a yaml file titled test.yaml with the following structure.

    .. code-block:: text

       apples: 20
       oranges: 10
       bananas: 3
       sports:
         - soccer
         - football
         - baseball
         - cricket
         - hockey
         - table tennis
    
    The file can be read with the following code

    .. code-block:: python

        > db = read_yaml_file('test.yaml')
        > print(db['apples']
        20
        > print(db['sports'])
        ['soccer', 'football', 'baseball', 'cricket', 'hockey', 'tabble tennis']
    """
    with open(file_name) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data
# ================================================================================
# ================================================================================
# eof

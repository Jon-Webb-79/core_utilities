# Import necessary packages here
import pytest
import os
import sys
import platform
import numpy as np
from math import isclose
sys.path.insert(0, os.path.abspath('../core_utilities'))

from core_utilities.read_files import ReadTextFileKeywords
from core_utilities.read_files import read_csv_columns_by_headers
from core_utilities.read_files import read_csv_columns_by_index
from core_utilities.read_files import read_text_columns_by_headers
from core_utilities.read_files import read_text_columns_by_index
from core_utilities.read_files import read_excel_columns_by_headers
from core_utilities.read_files import read_excel_columns_by_index
from core_utilities.read_files import ManageSQLiteDB
from core_utilities.read_files import simple_sqlite_query, read_json_file
from core_utilities.read_files import read_xml_file, read_yaml_file
# ================================================================================
# ================================================================================
# Date:    Month Day, Year
# Purpose: Describe the types of testing to occur in this file.
# Instruction: This code can be run in hte following ways
#              - pytest # runs all functions beginnning with the word test in the
#                         directory
#              - pytest file_name.py # Runs all functions in file_name beginning
#                                      with the word test
#              - pytest file_name.py::test_func_name # Runs only the function
#                                                      titled test_func_name in
#                                                      the file_name.py file
#              - pytest -s # Runs tests and displays when a specific file
#                            has completed testing, and what functions failed.
#                            Also displays print statments
#              - pytest -v # Displays test results on a function by function basis
#              - pytest -p no:warnings # Runs tests and does not display warning
#                          messages
#              - pytest -s -v -p no:warnings # Displays relevant information and
#                                supports debugging
#              - pytest -s -p no:warnings # Run for record

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2021, Jon Webb Inc."
__version__ = "1.0"
# ================================================================================
# ================================================================================
# Insert Code here


plat = platform.system()
lin_plat = ['Darwin', 'Linux']


def test_file_not_found():
    """

    This function ensures that the ReadTextFileKeywords class fails
    correctly when the file cannot be found
    """
    if plat in lin_plat:
        file = '../data/test/not_file_found.txt'
    else:
        file = r'..\data\test\not_file_found.txt'
    with pytest.raises(SystemExit):
        ReadTextFileKeywords(file)
# ------------------------------------------------------------------------------


def test_read_double():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.float32
    variable.
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_double('double:')
    assert isclose(value, 3.141596235941, rel_tol=1.0e-3)
    assert isinstance(value, np.float64)
# ------------------------------------------------------------------------------


def test_read_double_list():
    """

    This function tests the ReadTextFileKeywords.read_double_list
    function to determine if it can properly read a variable
    as a list of double precision values
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    double_value = key.read_double_list('double list:')
    expected = [1.12321, 344.3454453, 21.434553]
    for  enum in enumerate(double_value):
        assert isclose(enum[1], expected[enum[0]], rel_tol=1.0e-3)
        assert isinstance(enum[1], np.float64)
# ------------------------------------------------------------------------------


def test_read_float():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.float32
    variable.
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_float('float:')
    assert isclose(value, 3.1415, rel_tol=1.0e-3)
    assert isinstance(value, np.float32)
# ------------------------------------------------------------------------------


def test_float_list():
    """

    This function tests the ReadTextFileKeywords.read_float_list
    function to determine if it can properly read a variable
    as a list of float values
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    float_value = key.read_float_list('float list:')
    expected = [1.2, 3.4, 4.5, 5.6, 6.7]
    for enum in enumerate(float_value):
        assert isclose(enum[1], expected[enum[0]], rel_tol=1.0e-3)
        assert isinstance(enum[1], np.float32)
# ------------------------------------------------------------------------------


def test_read_integer():
    """

    This function tests the ReadTextFileKeywords.read_float function to
    determine if it correctly reads in a variable as a numpy.int32
    variable.
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    value = key.read_integer('Integer Value:')
    assert value == 3
    assert isinstance(value, np.int32)
# ------------------------------------------------------------------------------


def test_read_integer_list():
    """

    This function tests the ReadTextFileKeywords.read_float_list
    function to determine if it can properly read a variable
    as a list of float values
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    int_value = key.read_integer_list('integer list:')
    expected = [1, 2, 3, 4, 5, 6, 7]
    for enum in enumerate(int_value):
        assert isclose(enum[1], expected[enum[0]], rel_tol=1.0e-3)
        assert isinstance(enum[1], np.int32)
# ------------------------------------------------------------------------------


def test_read_sentence():
    """

    This function tests the ReadTextFileKeywords.read_sentence
    function to determine if it can properly read a sentence as
    a string
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_sentence('sentence:')
    assert sentence == "This is a short sentence!"
    assert isinstance(sentence, str)
# ------------------------------------------------------------------------------


def test_read_string():
    """

    This function tests the ReadTextFileKeywords.read_string
    function to determine if it can properly read a variable
    as a single string
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_string('String:')
    assert sentence == "test"
    assert isinstance(sentence, str)
# ------------------------------------------------------------------------------


def test_read_string_list():
    """

    This function tests the ReadTextFileKeywords.read_string_list
    function to determine if it can properly read a variable
    as a list of string values
    """
    if plat in lin_plat:
        file = '../data/test/keywords.txt'
    else:
        file = r'..\data\test\keywords.txt'
    key = ReadTextFileKeywords(file)
    sentence = key.read_string_list('sentence:')
    assert sentence == ['This', 'is', 'a', 'short', 'sentence!']
    for i in sentence:
        assert isinstance(i, str)
# ================================================================================
# ================================================================================
# Test read column functions


def test_read_csv_by_headers():
    """

    This function tests the read_csv_columns_by_headers function to ensure
    it properly reads in a csv file with the headers placed at the top
    of the file
    """
    if plat in lin_plat:
        file_name = '../data/test/test1.csv'
    else:
        file_name = r'..\data\test\test1.csv'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_headers(file_name, headers, dat)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_csv_by_headers_below_start():
    """

    This function tests the read_csv_columns_by_headers function to ensure
    it properly reads in a csv file with the headers placed below the top
    of the file
    """
    if plat in lin_plat:
        file_name = '../data/test/test2.csv'
    else:
        file_name = r'..\data\test\test2.csv'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_headers(file_name, headers, dat, skip=2)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_csv_by_index():
    """

    This function tests the read_csv_columns_by_index function to ensure
    it properly reads in a csv file that has no headers and gives each
    header a name
    """
    if plat in lin_plat:
        file_name = '../data/test/test3.csv'
    else:
        file_name = r'..\data\test\test3.csv'
    headers = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_index(file_name, headers, dat, names)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_csv_by_index_below_start():
    """

    This function tests the read_csv_columns_by_index function to ensure
    it properly reads in a csv file that has no headers and gives each
    header a name.  This test uses a .csv file that has metadata on
    the first two lines before the beginning of the columnar data
    """
    if plat in lin_plat:
        file_name = '../data/test/test4.csv'
    else:
        file_name = r'..\data\test\test4.csv'
    headers = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_csv_columns_by_index(file_name, headers, dat,
                                   names, skip=2)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_header():
    """

    This function tests the read_text_columns_by_headers function to
    ensure it properly reads in a space delimited text file with
    a header in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/textcol1.txt'
    else:
        file_name = r'..\data\test\textcol1.txt'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_headers(file_name, headers, dat)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_header_below_start():
    """

    This function tests the read_text_columns_by_headers function to
    ensure it properly reads in a space delimited text file with
    a header not in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/textcol2.txt'
    else:
        file_name = r'..\data\test\textcol2.txt'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_headers(file_name, headers, dat, skip=2)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_index():
    """

    This function tests the read_text_columns_by_index function to
    ensure it properly reads in a space delimited text file with
    a header in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/textcol3.txt'
    else:
        file_name = r'..\data\test\textcol3.txt'
    headers = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_index(file_name, headers, dat, names)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_text_by_index_below_start():
    """

    This function tests the read_text_columns_by_index function to
    ensure it properly reads in a space delimited text file with
    a header not in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/textcol4.txt'
    else:
        file_name = r'..\data\test\textcol4.txt'
    headers = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]
    df = read_text_columns_by_index(file_name, headers, dat,
                                    names, skip=2)

    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_excel_by_header():
    """

    This function tests the read_excel_columns_by_headers function to
    ensure it properly reads in a space delimited text file with
    a header in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/excel_test1.xls'
    else:
        file_name = r'../data/test/excel_test1.xls'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]

    # Test read first tab
    df = read_excel_columns_by_headers(file_name, 'primary', headers, dat)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)

        # Test read second tab
    df1 = read_excel_columns_by_headers(file_name, 'secondary', headers, dat)
    new_id = np.array([5, 6, 7], dtype=int)
    inventory = np.array(['shelves', 'computers', 'mugs'], dtype=str)
    weight = np.array([15.4, 3.4, 0.6], dtype=float)
    number = np.array([4, 10, 20], dtype=int)
    for i in range(len(df1)):
        assert new_id[i] == df1['ID'][i]
        assert isinstance(df1['ID'][i], np.int64)
        assert inventory[i] == df1['Inventory'][i]
        assert isinstance(df1['Inventory'][i], str)
        assert weight[i] == df1['Weight_per'][i]
        assert isinstance(df1['Weight_per'][i], np.float64)
        assert number[i] == df1['Number'][i]
        assert isinstance(df1['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_excel_by_header_below_start():
    """

    This function tests the read_excel_columns_by_headers function to
    ensure it properly reads in a space delimited text file with
    a header not in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/excel_test2.xls'
    else:
        file_name = r'../data/test/excel_test2.xls'
    headers = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]

    # Test read first tab
    df = read_excel_columns_by_headers(file_name, 'primary', headers, dat, skip=2)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_excel_by_index():
    """

    This function tests the read_excel_columns_by_index function to
    ensure it properly reads in a space delimited text file with
    a header not in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/excel_test3.xls'
    else:
        file_name = r'../data/test/excel_test3.xls'
    col_index = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]

    # Test read first tab
    df = read_excel_columns_by_index(file_name, 'primary', col_index,
                                     names, dat)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)

        # Test read second tab
    df1 = read_excel_columns_by_index(file_name, 'secondary', col_index,
                                      names, dat)
    new_id = np.array([5, 6, 7], dtype=int)
    inventory = np.array(['shelves', 'computers', 'mugs'], dtype=str)
    weight = np.array([15.4, 3.4, 0.6], dtype=float)
    number = np.array([4, 10, 20], dtype=int)
    for i in range(len(df1)):
        assert new_id[i] == df1['ID'][i]
        assert isinstance(df1['ID'][i], np.int64)
        assert inventory[i] == df1['Inventory'][i]
        assert isinstance(df1['Inventory'][i], str)
        assert weight[i] == df1['Weight_per'][i]
        assert isinstance(df1['Weight_per'][i], np.float64)
        assert number[i] == df1['Number'][i]
        assert isinstance(df1['Number'][i], np.int64)
# ------------------------------------------------------------------------------


def test_read_excel_by_index_below_start():
    """

    This function tests the read_excel_columns_by_index function to
    ensure it properly reads in a space delimited text file with
    a header not in the top row
    """
    if plat in lin_plat:
        file_name = '../data/test/excel_test4.xls'
    else:
        file_name = r'../data/test/excel_test4.xls'
    headers = [0, 1, 2, 3]
    names = ['ID', 'Inventory', 'Weight_per', 'Number']
    dat = [np.int64, str, np.float64, np.int64]

    # Test read first tab
    df = read_excel_columns_by_index(file_name, 'primary', headers,
                                     names, dat, skip=2)
    new_id = np.array([1, 2, 3, 4], dtype=int)
    inventory = np.array(['shoes', 't-shirt', 'coffee', 'books'], dtype=str)
    weight = np.array([1.5, 1.8, 2.1, 3.2], dtype=float)
    number = np.array([5, 3, 15, 40], dtype=int)
    for i in range(len(df)):
        assert new_id[i] == df['ID'][i]
        assert isinstance(df['ID'][i], np.int64)
        assert inventory[i] == df['Inventory'][i]
        assert isinstance(df['Inventory'][i], str)
        assert weight[i] == df['Weight_per'][i]
        assert isinstance(df['Weight_per'][i], np.float64)
        assert number[i] == df['Number'][i]
        assert isinstance(df['Number'][i], np.int64)
# ================================================================================
# ================================================================================


def test_no_db_exists():
    """

    This function tests to ensure that ReadSQLiteDB correctly determines
    if a database does not exist
    """
    if plat in lin_plat:
        file = '../data/test/not_db.db'
    else:
        file = r'..\data\test\not_db.db'
    with pytest.raises(SystemExit):
        ManageSQLiteDB(file)
# ------------------------------------------------------------------------------


def test_read_database_from_class():
    """

    This function tests to ensure that ReadSQLiteDB correctly reads a
    database table
    """
    if plat in lin_plat:
        file = '../data/test/Maintenance.db'
    else:
        file = r'..\data\test\Maintenance.db'
    db = ManageSQLiteDB(file)
    query = "Select Date, Cost, Gallons FROM gas;"
    df = db.query_db(query)
    db.close_database_connection()
    assert df['Date'][0] == '2020-02-04'
    assert isclose(df['Cost'][0], 27.88, rel_tol=1.0e-3)
# ================================================================================
# ================================================================================


def test_simple_sqlite_query():
    """

    This function tests simple_sqlite_query to ensure it returns
    the proper results
    """
    if plat in lin_plat:
        file = '../data/test/Maintenance.db'
    else:
        file = r'..\data\test\Maintenance.db'
    query = "Select Date, Cost, Gallons FROM gas;"
    df = simple_sqlite_query(file, query)
    assert df['Date'][0] == '2020-02-04'
    assert isclose(df['Cost'][0], 27.88, rel_tol=1.0e-3)
# --------------------------------------------------------------------------------


def test_read_json():
    """

    This function tests the read_json_file function to ensure it returns
    the correct results
    """
    if plat in lin_plat:
        file = '../data/test/json.json'
    else:
        file = r'..\data\test\json.json'
    dat = read_json_file(file)
    assert dat['widget']['debug'] == 'on'
# --------------------------------------------------------------------------------


def test_read_xml():
    if plat in lin_plat:
        file = '../data/test/xml.xml'
    else:
        file = r'..\data\test\xml.xml'
    db = read_xml_file(file)
    img_name =db.find(src="Images/Sun.png").get_text()
    assert img_name[0:4] == '\n250'
# --------------------------------------------------------------------------------


def test_read_yaml_file():
    if plat in lin_plat:
        file = '../data/test/test.yaml'
    else:
        file = r'..\data\test\test.yaml'
    db = read_yaml_file(file)
    assert db['apples'] == 20
    assert db['oranges'] == 10
    assert db['bananas'] == 3
    dat_list = ['soccer', 'football', 'baseball', 'cricket', 'hockey', 'table tennis']
    for i in  enumerate(dat_list):
        assert i[1] == db['sports'][i[0]]
# ================================================================================
# ================================================================================
# eof

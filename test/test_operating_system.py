# Import necessary packages here

import os
import sys
import platform
import shutil
sys.path.insert(0, os.path.abspath('../core_utilities'))
from core_utilities.operating_system import OSUtilities
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


def test_change_directory():
    """

    This function tests the ability of OSUtilities.change_directory to
    properly change a directory
    """
    current = os.getcwd()
    new= current[:-5]
    util = OSUtilities()
    util.change_directory("../")
    assert new == os.getcwd()
    util.change_directory("test")
# --------------------------------------------------------------------------------


def test_copy_directory():
    """

    This function tests the ability of the OSUtilities.copy_directory function to
    copy a directory
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        directory1 = '../data/test/test_directory2'
        directory2 = '../data/test/test_directory3'
        file = '../data/test/test_directory3/test.txt'
    else:
        directory1 = r'..\data\test\test_directory2'
        directory2 = r'..\data\test\test_directory3'
        file = r'..\data\test\test_directory3\test.txt'
    util.copy_directory(directory1, directory2)
    assert os.path.isdir(directory2)
    assert os.path.isfile(file)
    if os.path.isdir(directory2):
        shutil.rmtree(directory2)
# --------------------------------------------------------------------------------


def test_copy_file():
    """

    This function tests the ability of the OSUtilities.copy_file function to correctly
    copy a file
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        file1 = '../data/test/test_file2.txt'
        file2 = '../data/test/copy_test.txt'
    else:
        file1 = r'..\data\test\test_file2.txt'
        file2 = r'..\data\test\copy_test.txt'
    util.copy_file(file1, file2)
    assert os.path.isfile(file2)
    if os.path.isfile(file2):
        os.remove(file2)
# ------------------------------------------------------------------------------


def test_count_word_occurrence():
    """

    This function tests the OSUtilities.count_occurrence_of_words_in_file
    to ensure it correctly determines the number of times a word occurs in
    a file
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        file = '../data/test/text_file.txt'
    else:
        file = r'..\data\test\text_file.txt'
    num_words = util.count_occurrence_of_word_in_file(file, 'file')
    assert num_words == 4
# ------------------------------------------------------------------------------


def test_create_directory():
    """

    This function tests the OSUtilities.create_directory command to ensure it correctly
    creates a directory
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        directory = '../data/test/test_directory3'
    else:
        directory = r'..\data\test\test_directory3'
    util.create_directory(directory)
    assert os.path.isdir(directory)
    if os.path.isdir(directory):
        os.rmdir(directory)
# ------------------------------------------------------------------------------


def test_create_file():
    """

    This function tests the OSUtilities.create_file function to ensure that it
    correctly creates an ASCII based text file
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        file = '../data/test/create_file_test.txt'
    else:
        file = r'..\data\test\create_file_test.txt'
    util.create_file(file)
    assert os.path.isfile(file)
    if os.path.isfile(file):
        os.remove(file)
# --------------------------------------------------------------------------------


def test_current_working_directory():
    """

    This function tests the OSUtilities.current_working_directory function to
    ensure it correctly determines the working directory
    """
    cwd = os.getcwd()
    cwd2 = OSUtilities.current_working_directory()
    assert cwd == cwd2
# ------------------------------------------------------------------------------


def test_delete_directory():
    """

    This function tests the OSUtilitiescreate_file function to ensure that it
    correctly creates an ASCII based text file
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        dire = '../data/test/test_directory'
    else:
        dire = r'..\data\test\test_directory'
    util.delete_directory(dire)
    assert not os.path.isdir(dire)
    if not os.path.isdir(dire):
        os.mkdir(dire)
# ------------------------------------------------------------------------------


def test_delete_file():
    """

    This function tests the OSUtilities.delete_file function to ensure that it correctly
    deletes a file
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        file = '../data/test/delete_test.txt'
    else:
        file = r'..\data\test\delete_test.txt'
    util.delete_file(file)
    assert not os.path.isfile(file)
    if not os.path.isfile(file):
        util.create_file(file)
# ------------------------------------------------------------------------------


def test_remove_populated_directory():
    """

    This function tests the OSUtilities.remove_populated_directory function to determine
    if it correctly removes a populated directory
    """
    util = OSUtilities()
    plat = platform.system()
    lin_plat = ['Darwin', 'Linux']
    if plat in lin_plat:
        directory = '../data/test/populated_dir1'
        file = '../data/test/populated_dir1/test.txt'
    else:
        directory = r'../data/test/populated_dir1'
        file = r'../data/test/populated_dir1/test.txt'
    util.delete_populated_directory(directory)
    assert not os.path.isdir(directory)
    if not os.path.isdir(directory):
        os.mkdir(directory)
        util.create_file(file)
# ================================================================================
# ================================================================================
 # eof

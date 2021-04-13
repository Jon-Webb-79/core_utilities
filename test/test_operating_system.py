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
    if plat == 'Darwin' or 'Linux':
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
    if plat == 'Darwin' or 'Linux':
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
    if plat == 'Darwin' or 'Linux':
        file = '../data/test/text_file.txt'
    else:
        file = r'..\data\test\text_file.txt'
    num_words = util.count_occurrence_of_word_in_file(file, 'file')
    assert num_words == 4
# ================================================================================
# ================================================================================
 # eof

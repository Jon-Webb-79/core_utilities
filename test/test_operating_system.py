# Import necessary packages here

import os
import sys
import platform
import shutil
from math import isclose
sys.path.insert(0, os.path.abspath('../core_utilities'))
import core_utilities.operating_system as util
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


def test_change_directory():
    """

    This function tests the ability of change_directory to
    properly change a directory
    """
    current = os.getcwd()
    new= current[:-5]
    util.change_directory("../")
    assert new == os.getcwd()
    util.change_directory("test")
# --------------------------------------------------------------------------------


def test_copy_directory():
    """

    This function tests the ability of the copy_directory function to
    copy a directory
    """
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

    This function tests the ability of the copy_file function to correctly
    copy a file
    """
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

    This function tests the count_occurrence_of_words_in_file
    to ensure it correctly determines the number of times a word occurs in
    a file
    """
    if plat in lin_plat:
        file = '../data/test/text_file.txt'
    else:
        file = r'..\data\test\text_file.txt'
    num_words = util.count_occurrence_of_word_in_file(file, 'file')
    assert num_words == 4
# ------------------------------------------------------------------------------


def test_create_directory():
    """

    This function tests the create_directory command to ensure it correctly
    creates a directory
    """
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

    This function tests the create_file function to ensure that it
    correctly creates an ASCII based text file
    """
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

    This function tests the current_working_directory function to
    ensure it correctly determines the working directory
    """
    cwd = os.getcwd()
    cwd2 = util.current_working_directory()
    assert cwd == cwd2
# ------------------------------------------------------------------------------


def test_delete_directory():
    """

    This function tests the create_file function to ensure that it
    correctly creates an ASCII based text file
    """
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

    This function tests the delete_file function to ensure that it correctly
    deletes a file
    """
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

    This function tests the remove_populated_directory function to determine
    if it correctly removes a populated directory
    """
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
# ------------------------------------------------------------------------------


def test_determine_file_size():
    """

    This function tests the determine_file_size function to determine
    if it can correctly determine the size of a file
    """
    if plat in lin_plat:
        file = '../data/test/size_test.jpg'
    else:
        file = r'..\data\test\size_test.jpg'
    file_size = util.determine_file_size(file)
    assert isclose(file_size, 26674.009, rel_tol=1.0e-3)
# ------------------------------------------------------------------------------


def test_determine_file_line_count():
    """

    This function tests the file_line_count function to ensure
    it can correctly determine how many lines are in a file
    """
    if plat in lin_plat:
        file = '../data/test/text_file.txt'
    else:
        file = r'../data/test/text_file.txt'
    lines = util.file_line_count(file)
    assert lines == 4
# ------------------------------------------------------------------------------


def test_file_word_count():
    """

    This function tests the file_word_count function to determine
    if it can correctly determine the number of words in a file
    """
    if plat in lin_plat:
        file = '../data/test/text_file.txt'
    else:
        file = r'../data/test/text_file.txt'
    words = util.file_word_count(file)
    assert words == 21
# --------------------------------------------------------------------------------


def test_move_directory():
    """

    This function test the move_file_or_directory function to ensure that it
    successfully moves directories between different locations
    """
    if plat in lin_plat:
        file1 = '../data/test/populated_dir2'
        file2 = '../data/test/move_directory2/populated_dir2'
        file3 = '../data/test/move_directory2/populated_dir2/test.txt'
    else:
        file1 = r'..\data\test\populated_dir2'
        file2 = r'..\data\test\move_directory2\populated_dir2'
        file3 = r'..\data\test\move_directory2\populated_dir2\test.txt'
    util.move_directory(file1, file2)
    assert os.path.isdir(file2)
    assert os.path.isfile(file3)
    if os.path.isdir(file2):
        util.move_directory(file2, file1)
# ------------------------------------------------------------------------------


def test_move_file():
    """

    This function test the move_file_or_directory function to ensure that it
    successfully moves files between different locations
    """
    if plat in lin_plat:
        file1 = '../data/test/move_test.txt'
        file2 = '../data/test/move_directory1/move_test2.txt'
    else:
        file1 = r'..\data\test\move_test.txt'
        file2 = r'..\data\test\move_directory1\move_test2.txt'
    util.move_file(file1, file2)
    assert os.path.isfile(file2)
    if os.path.isfile(file2):
        util.move_file(file2, file1)
# ------------------------------------------------------------------------------


def test_list_contents():
    """
    This function tests the list_contents function to ensure it returns the
    correct files and directories
    """
    if plat in lin_plat:
        directory = '../data/test/list_dir'
    else:
        directory = r'..\data\test\list_dir'
    contents = util.list_contents(directory=directory, extension='.py')
    assert 'test.py' in contents

    contents = util.list_contents(directory=directory, extension='.txt')
    expected_result = ['test1.txt', 'test2.txt', 'test3.txt']
    for i in contents:
        assert i in expected_result

    contents = util.list_contents(directory=directory)
    expected_result = ['test1.txt', 'test2.txt', 'test3.txt', 'test', 'test.py']
    for i in contents:
        assert i in expected_result
# ------------------------------------------------------------------------------


def test_copy_files_files():
    """

    This function tests the copy_files function to ensure that it
    correctly copies text file contents of a directory to a new directory
    """
    if plat in lin_plat:
        source = '../data/test/move_directory3'
        destination = '../data/test/move_directory2'
        file1 = '../data/test/move_directory2/test1.txt'
        file2 = '../data/test/move_directory2/test2.txt'
    else:
        source = r'..\data\test\move_directory3'
        destination = r'..\data\test\move_directory2'
        file1 = r'..\data\test\move_directory2\test1.txt'
        file2 = r'..\data\test\move_directory2\test2.txt'
    util.copy_files(destination, source, '.txt')
    assert os.path.isfile(file1)
    assert os.path.isfile(file2)
    os.remove(file1)
    os.remove(file2)
# ------------------------------------------------------------------------------


def test_copy_files_dirs():
    """

    This function tests the copy_files function to ensure that it
    correctly copies all directories of a directory to a new directory
    """
    if plat in lin_plat:
        source = '../data/test/move_directory3'
        destination = '../data/test/move_directory2'
        direct = '../data/test/move_directory2/test'
    else:
        source = r'..\data\test\move_directory3'
        destination = r'..\data\test\move_directory2'
        direct = r'..\data\test\move_directory2/test'
    util.copy_files(destination, source, dirs=True)
    assert os.path.isdir(direct)
    shutil.rmtree(direct)
# ------------------------------------------------------------------------------


def test_move_files_everything():
    """

    This function tests the move_files function to ensure that it
    correctly moves all contents of a directory to a new directory
    """
    if plat in lin_plat:
        source = '../data/test/move_directory3'
        destination = '../data/test/move_directory2'
        direct = '../data/test/move_directory2/test'
        file1 = '../data/test/move_directory2/test1.txt'
        file2 = '../data/test/move_directory2/test2.txt'
    else:
        source = r'..\data\test\move_directory3'
        destination = r'..\data\test\move_directory2'
        direct = r'..\data\test\move_directory2\test'
        file1 = r'..\data\test\move_directory2\test1.txt'
        file2 = r'..\data\test\move_directory2\test2.txt'

    util.move_files(destination, source)
    assert os.path.isfile(file1)
    assert os.path.isfile(file2)
    assert os.path.isdir(direct)
    util.move_files(source, destination)
# ------------------------------------------------------------------------------


def test_move_files_dirs():
    """

    This function tests the copy_files function to ensure that it
    correctly moves all directories of a directory to a new directory
    """
    if plat in lin_plat:
        source = '../data/test/move_directory3'
        destination = '../data/test/move_directory2'
        direct = '../data/test/move_directory2/test'
    else:
        source = r'..\data\test\move_directory3'
        destination = r'..\data\test\move_directory2'
        direct = r'..\data\test\move_directory2\test'
    util.move_files(destination, source, dirs=True)
    assert os.path.isdir(direct)
    util.move_files(source, destination, dirs=True)
# ------------------------------------------------------------------------------


def test_verify_directory_existence():
    """

    This function tests the verify_directory_existence function to
    ensure it can correctly identify that a file does exist
    """
    if plat in lin_plat:
        file = '../data/test/test_directory'
    else:
        file = r'..\data\test\test_directory'
    status = util.verify_directory_existence(file)
    assert status
# ------------------------------------------------------------------------------


def test_directory_existence_not_verified():
    """

    This function tests the verify_directory_existence function to
    ensure it can correctly identify that a file does exist
    """
    if plat in lin_plat:
        file = '../data/test/no_directory'
    else:
        file = r'..\data\test\no_directory'
    status = util.verify_directory_existence(file)
    assert not status
# ------------------------------------------------------------------------------


def test_verify_file_existence():
    """

    This function tests the verify_file_existence function to
    ensure it can correctly identify that a file does exist
    """
    if plat in lin_plat:
        file = '../data/test/text_file.txt'
    else:
        file = r'..\data\test\text_file.txt'
    status = util.verify_file_existence(file)
    assert status
# ------------------------------------------------------------------------------


def test_file_existence_not_verified():
    """

    This function tests the verify_file_existence function to
    ensure that it can correctly identify when a file does not exist
    """
    if plat in lin_plat:
        file = '../data/test/no_text_file.txt'
    else:
        file = r'..\data\test\no_text_file.txt'
    status = util.verify_file_existence(file)
    assert not status
# ================================================================================
# ================================================================================
 # eof

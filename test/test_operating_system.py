# Import necessary packages here

import os
import sys
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
# ================================================================================
# ================================================================================
 # eof

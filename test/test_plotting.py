# Import necessary packages here
import os
import sys
import platform
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.abspath('../core_utilities'))
from core_utilities.plotting import MatPlotDataFrame
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


def test_scatter_plot_parse_columns():
    """

    This functon tests the ability of scatter_plot_parse_column
    within the MatPlotDataFrame class to process a plot without
    failing
    """
    if plat in lin_plat:
        file = '../data/test/scatter_one.png'
    else:
        file = r'..\data\test\scatter_one.png'
    length = 20
    x = np.linspace(0, 20, num=20)
    linear = x
    squared = x ** 2.0
    lin = np.repeat('linear', 20)
    sq = np.repeat('squared', 20)

    # Combine arrays into one
    x = np.hstack((x, x))
    y = np.hstack((linear, squared))
    power = np.hstack((lin, sq))

    # Create dataframe
    dictionary = {'x': x, 'y': y, 'power': power}
    df = pd.DataFrame(dictionary)

    parsing_header = 'power'
    column_values = ['linear', 'squared']
    # Plot data
    obj = MatPlotDataFrame(1, 1)
    obj.scatter_plot_parse_column(df, 'x', 'y', parsing_header, column_values,
                                  x_label='x-axis', y_label='y-axis', title='Test',
                                  style_name='default', marker_style=['o', '^'],
                                  label_pos='upper left', grid=True)
# ================================================================================
# ================================================================================
# eof

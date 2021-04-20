# Import necessary packages here
import sys
import warnings
from typing import List
from matplotlib import rc, pyplot as plt
import pandas as pd
import numpy as np
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


class MatPlotDataFrame:
    """

    :param nrows: Number of rows of the subplot grid, defaulted to 1
    :param ncols: Number of columns of the subplot grid, defaulted to 1
    :param sharex/sharey: Controls sharing of properties among x (sharex)
                          or y (sharey) axes.
                          * True or 'all', x or y axis will be shared among all
                          subplots
                          * False or 'none', each subplot x or y-axis will be
                          independent
                          * 'row' each subplot row will share an x or y axis
                          * 'col' each subplot column will share an x or y axis
    :param squeeze: If true, extra dimensions are squeezed out from the returned
                    array of Axes.
    :param subplot_kw: Dictionary with keywords bassed to the
                       add_subplot call
    :param gridspec_kw: Dict with keywords passed to the GridSpec
                        constructor

    This class allows a user to plot data from within one or multiple data
    frame in different ways.  In addition, this class allows a user to mix
    different plotting methods into one plot
    """
    def __init__(self, nrows: int=1, ncols: int=1, sharex: bool=False,
                 sharey: bool=False, squeeze: bool=True, subplot_kw=None,
                 gridspec_kw=None):
        self.nrows = nrows
        self.ncols = ncols
        self.colors = ['lightgrey', 'deepskyblue', 'sandybrown',
                       'teal', 'limegreen', 'coral',
                       'hotpink', 'magenta', 'red',
                       'white', 'gold', 'darkgreen',
                       'turqoise', 'olive', 'orange',
                       'mediumvioletred', 'purple' , 'darkred']
        self.styles = ['o' for i in range(len(self.colors))]
        self.fig, self.ax = plt.subplots(nrows=nrows, ncols=ncols, sharex=sharex,
                                         sharey=sharey, squeeze=squeeze,
                                         subplot_kw=subplot_kw,
                                         gridspec_kw=gridspec_kw)
# --------------------------------------------------------------------------------

    def scatter_plot_parse_column(self, df: pd.DataFrame, x_header: str, y_header: str,
                                  parsing_header: str, column_values: List[str],
                                  style_name: str='default',
                                  marker_colors: List[str]=['None'],
                                  marker_style: List[str]=['None'],
                                  fill_alpha: np.float32=0.7, edge_color: str='black',
                                  x_label: str='', y_label: str='', title: str='',
                                  label_pos: str='upper right', x_scale: str='LIN',
                                  y_scale: str='LIN',
                                  label_font_size: int=18,
                                  tick_font_size: int=18, title_font_size: int=24,
                                  marker_size: int=35, marker_edge_width: np.float32=0.8,
                                  grid: bool=False, grid_style: str='-',
                                  grid_color='grey', row: int=0, col: int=0) -> None:
        """

        :param df: A pandas dataframe containing data to be plotted
        :param x_header: The column header containing data to be plotted in the
                         x-axis
        :param y_header: The column header containing data to be plotted in the
                         y-axis
        :param parsing_header: The column container containing key words that are used
                               to determine what data is plotted
        :param column_values: The keywords that exist within the column defined by parsing
                              header.  The function will filter the dataframe to only
                              contain rows where this keyword is present
        :param style_name: The plot style, defaulted to 'default'.
                           See :href `styles<https://matplotlib.org/stable/api/style_api.html>`
        :param marker_colors: A list of marker colors, where each marker color
                              corresponds to each data set.  This parameter has a
                              default color lists that can accomodate 18 different
                              data sets.  The user can override the default colors
                              with a list of their own.  Potential colors can be
                              found at :href `colors<https://matplotlib.org/stable/gallery/color/named_colors.html>`
        :param marker_style: A list of marker styles, where each marker style corresponds
                             to a data set.  This parameter has a default list of 18 circle
                             marker styles that the user can override.  Marker styles
                             can be found at :href `marker style<https://matplotlib.org/stable/api/markers_api.html>`
        :param fill_alpha: The density of the marker fill.  Defaulted to 0.7
        :param edge_color: The color of the line surrounding the marker
        :param x_label: The x-axis label, defaulted to ''
        :param y_label: The y-axis label, defaulted to ''
        :param title: The plot title, defaulted to ''
        :param x_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param y_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param label_pos: The position of the legend in the plot.  Defaulted to upper right
        :param label_font_size: The label font size, defaulted to 18
        :param tick_font_size: The tick font size, defaulted to 18
        :param marker_size: The size of the markers, defaulted to 35
        :param marker_edge_width: The width of the line surrounding each marker.
                                  Defaulted to 0.8
        :param grid: True if a grid is desired.  Defaulted to False
        :param row: The row within the plot grid where this plot will be
                    placed.  Defaulted to 1
        :param col: The column within the plot grid where this plot will
                    be placed.  Defaulted to 1

        .. code-block:: python

           > length = 20
           > x = np.linspace(0, length, num=length)
           > linear = x
           > squared = x ** 2.0
           > lin = np.repeat('linear', length)
           > sq = np.repeat('squared', length)
           > # Combine arrays into one
           > x = np.hstack((x, x))
           > y = np.hstack((linear, squared))
           > power = np.hstack((lin, sq))
           > # Create dataframe
           > dictionary = {'x': x, 'y': y, 'power': power}
           > df = pd.DataFrame(dictionary)
           > # Plot data
           > obj = MatPlotDataFrame(1, 1)
           > parsing_header = 'power'
           > column_values = ['linear', 'squared']
           obj.scatter_plot_filter_column(df, 'x', 'y', parsing_header,
                                          column_values,
                                          marker_colors=['red', 'green'],
                                          marker_style=['o', '^'],
                                          label_pos='upper left')
           obj.show_plot()

        .. image:: mat_scatter_test1.eps
           :align: center

        """
        df_list = [df[df[parsing_header] == col_val] for col_val in column_values]
        # Error checking
        if marker_colors[0] == 'None':
            marker_colors = self.colors
        if len(marker_colors) < len(column_values):
            msg1 = 'FATAL ERROR: The length of th emarker color list must be as '
            msg2 = 'large or larger than the size of the column values'
            sys.exit(msg1 + msg2)
        if marker_style[0] == 'None':
            marker_style = self.styles
        if len(marker_style) < len(column_values):
            msg1 = 'FATAL ERROR: The length of the marker stye list must be as '
            msg2 =  'large or larger than the size of the column values'
            sys.exit(msg1 + msg2)
        if y_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')
        if x_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')

        # begin plot
        plt.rcParams.update({'figure.autolayout': True})
        plt.style.use(style_name)
        #fig, ax = plt.subplots()
        rc('xtick', labelsize=tick_font_size)
        rc('ytick', labelsize=tick_font_size)
        if self.nrows > 1 or self.ncols > 1:
            self.ax[row, col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row, col].set_ylabel(y_label, fontsize=label_font_size)
        else:
            self.ax.set_xlabel(x_label, fontsize=label_font_size)
            self.ax.set_ylabel(y_label, fontsize=label_font_size)
        if title != 'NULL':
            if self.nrows > 1 or self.ncols > 1:
                self.ax[row, col].set_title(title, fontsize=title_font_size)
            else:
                self.ax.set_title(title, fontsize=title_font_size)
        if x_scale.upper() == 'LOG':
            if self.nrows > 1 or self.ncols > 1:
                self.ax[row, col].set_xscale('log')
            else:
                self.ax[row, col].set_xscale('log')
        if y_scale.upper() == 'LOG':
            if self.nrows > 1 or self.ncols > 1:
                self.ax[row, col].set_yscale('log')
            else:
                self.ax[row, col].set_yscale('log')
        if self.nrows > 1 or self.ncols > 1:
            for dfs in enumerate(df_list):
                self.ax[row, col].scatter(dfs[1][x_header], dfs[1][y_header],
                                  label=column_values[dfs[0]],
                                  marker=marker_style[dfs[0]],
                                  color=marker_colors[dfs[0]],
                                  alpha=fill_alpha, edgecolors=edge_color,
                                  s=marker_size, linewidth=marker_edge_width)
        else:
            for dfs in enumerate(df_list):
                self.ax.scatter(dfs[1][x_header], dfs[1][y_header],
                                label=column_values[dfs[0]],
                                marker=marker_style[dfs[0]],
                                color=marker_colors[dfs[0]],
                                alpha=fill_alpha, edgecolors=edge_color,
                                s=marker_size, linewidth=marker_edge_width)
        if self.nrows > 1 or self.ncols > 1:
            self.ax[row, col].legend(loc=label_pos)
        else:
            self.ax.legend(loc=label_pos)
        if grid:
            if self.nrows > 1 or self.ncols > 1:
                self.ax[row, col].grid(color=grid_color, linestyle=grid_style)
            else:
                self.ax.grid(color=grid_color, linestyle=grid_style)
# --------------------------------------------------------------------------------

    def show_plot(self):
        plt.show()
# ================================================================================
# ================================================================================
# eof

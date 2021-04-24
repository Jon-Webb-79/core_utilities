# Import necessary packages here
import sys
import warnings
from typing import List
from matplotlib import rc, pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
# ================================================================================
# ================================================================================
# Date:    April 22, 2021
# Purpose: This file contains functions and classes that can be used to plot
#          dataframes with MatPlotLib and Bokeh packages

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
                 gridspec_kw=None, height: int=6, width: int=7):
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
                                         gridspec_kw=gridspec_kw,
                                         figsize=(width, height))
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
                                  grid_color='grey', row: int=0, col: int=0,
                                  labels: bool=True) -> None:
        """

        :param df: A pandas dataframe containing data to be plotted
        :param x_header: The column header containing data to be plotted in the
                         x-axis
        :param y_header: The column header containing data to be plotted in the
                         y-axis
        :param parsing_header: The column containing key words that are used
                               to determine what data is plotted.  The keywords
                               will also be used as the plot labels is ``labels`` is
                               set to true
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
        :param labels: True is a legend is to be printed, False if not.  Defaulted
                       to True 

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
           obj.scatter_plot_parse_column(df, 'x', 'y', parsing_header, column_values,
                                         x_label='x-axis', y_label='y-axis', title='Test',
                                         style_name='default', marker_style=['o', '^'],
                                         label_pos='upper left', grid=True, labels=True)
           obj.show_plot()

        .. image:: scatter_one.png
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
        if labels not in (True, False):
            warnings.warn('labels not correctly set, default to False')
            labels = False

        # begin plot
        plt.rcParams.update({'figure.autolayout': True})
        plt.style.use(style_name)
        rc('xtick', labelsize=tick_font_size)
        rc('ytick', labelsize=tick_font_size)
        if self.nrows > 1 and self.ncols > 1:
            self.ax[row, col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row, col].set_ylabel(y_label, fontsize=label_font_size)
        elif self.nrows >1:
            self.ax[row].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row].set_ylabel(y_label, fontsize=label_font_size)
        elif self.ncols > 1:
            self.ax[col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[col].set_ylabel(y_label, fontsize=label_font_size)
        else:
            self.ax.set_xlabel(x_label, fontsize=label_font_size)
            self.ax.set_ylabel(y_label, fontsize=label_font_size)
        if title != 'NULL':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_title(title, fontsize=title_font_size)
            elif self.nrows > 1:
                self.ax[row].set_title(title, fontsize=title_font_size)
            elif self.ncols > 1:
                self.ax[col].set_title(title, fontsize=title_font_size)
            else:
                self.ax.set_title(title, fontsize=title_font_size)
        if x_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_xscale('log')
            elif self.nrows > 1:
                self.ax[row].set_xscale('log')
            elif self.ncols > 1:
                self.ax[col].set_xscale('log')
            else:
                self.ax.set_xscale('log')
        if y_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_yscale('log')
            elif self.nrows > 1:
                self.ax[row].set_yscale('log')
            elif self.ncols > 1:
                self.ax[col].set_yscale('log')
            else:
                self.ax.set_yscale('log')
        if self.nrows > 1 and self.ncols > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[row, col].scatter(dfs[1][x_header], dfs[1][y_header],
                                  label=column_values[dfs[0]],
                                  marker=marker_style[dfs[0]],
                                  color=marker_colors[dfs[0]],
                                  alpha=fill_alpha, edgecolors=edge_color,
                                  s=marker_size, linewidth=marker_edge_width)
        elif self.nrows > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[row].scatter(dfs[1][x_header], dfs[1][y_header],
                             label=column_values[dfs[0]],
                             marker=marker_style[dfs[0]],
                             color=marker_colors[dfs[0]],
                             alpha=fill_alpha, edgecolors=edge_color,
                             s=marker_size, linewidth=marker_edge_width)
        elif self.ncols > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[col].scatter(dfs[1][x_header], dfs[1][y_header],
                             label=column_values[dfs[0]],
                             marker=marker_style[dfs[0]],
                             color=marker_colors[dfs[0]],
                             alpha=fill_alpha, edgecolors=edge_color,
                             s=marker_size, linewidth=marker_edge_width)
        elif self.ncols == 1 and self.nrows == 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax.scatter(dfs[1][x_header], dfs[1][y_header],
                                label=column_values[dfs[0]],
                                marker=marker_style[dfs[0]],
                                color=marker_colors[dfs[0]],
                                alpha=fill_alpha, edgecolors=edge_color,
                                s=marker_size, linewidth=marker_edge_width)
        if self.nrows > 1 and self.ncols > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[row, col].scatter(dfs[1][x_header], dfs[1][y_header],
                                  marker=marker_style[dfs[0]],
                                  color=marker_colors[dfs[0]],
                                  alpha=fill_alpha, edgecolors=edge_color,
                                  s=marker_size, linewidth=marker_edge_width)
        elif self.nrows > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[row].scatter(dfs[1][x_header], dfs[1][y_header],
                             marker=marker_style[dfs[0]],
                             color=marker_colors[dfs[0]],
                             alpha=fill_alpha, edgecolors=edge_color,
                             s=marker_size, linewidth=marker_edge_width)
        elif self.ncols > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[col].scatter(dfs[1][x_header], dfs[1][y_header],
                             marker=marker_style[dfs[0]],
                             color=marker_colors[dfs[0]],
                             alpha=fill_alpha, edgecolors=edge_color,
                             s=marker_size, linewidth=marker_edge_width)
        else:
            for dfs in enumerate(df_list):
                self.ax.scatter(dfs[1][x_header], dfs[1][y_header],
                                marker=marker_style[dfs[0]],
                                color=marker_colors[dfs[0]],
                                alpha=fill_alpha, edgecolors=edge_color,
                                s=marker_size, linewidth=marker_edge_width)

        if labels is True:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].legend(loc=label_pos)
            elif self.nrows > 1:
                self.ax[row].legend(loc=label_pos)
            elif self.ncols > 1:
                self.ax[col].legend(loc=label_pos)
            else:
                self.ax.legend(loc=label_pos)
        if grid:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].grid(color=grid_color, linestyle=grid_style)
            elif self.nrows > 1:
                self.ax[row].grid(color=grid_color, linestyle=grid_style)
            elif self.ncols > 1:
                self.ax[col].grid(color=grid_color, linestyle=grid_style)
            else:
                self.ax.grid(color=grid_color, linestyle=grid_style)
# --------------------------------------------------------------------------------

    def scatter_plot_columns(self, df: pd.DataFrame, x_headers: List[str],
                             y_headers: List[str], labels: bool=True,
                             style_name: str='default',
                             marker_colors: List[str]=['None'],
                             marker_style: List[str]=['None'],
                             fill_alpha: np.float32=0.7, edge_color: str='black',
                             x_label: str='', y_label: str='', title: str='',
                             label_pos: str='upper right', x_scale: str='LIN',
                             y_scale: str='LIN', label_font_size: int=18,
                             tick_font_size: int=18, title_font_size=32,
                             marker_size: int=35, marker_edge_width: np.float32=0.8,
                             grid: bool=False, grid_style: str='-',
                             grid_color='grey', row: int=0, col: int=0) -> None:
        """

        :param df: A pandas dataframe containing the data to be plotted
        :param x_headers: The title of the dataframe columns containing the x-axis
                          data sets.
        :param y_headers: The title of the dataframe columns containing the y-axis
                          data sets. The y_headers values will also be used as the
                          labels for each individual plot if ``labels`` is set
                          to True
        :param labels: True if a legend is to be plotted, False if not.  Defaulted to
                       True
        :param style_name: The name of the matplotlib style that will be used to
                           format the plot.  Defaulted to 'default'.  Possible
                           styles can be found at :href
                           `styles<https://matplotlib.org/stable/api/style_api.html>`
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
        :param fill_apha: The density of the marker fill.  Defaulted to 0.7
        :param edge_color: The color of the line surrounding the marker
        :param x_label: The x axis label,defaulted to ' '
        :param y_label: The y axis label, defaulted to ' '
        :param title: The plot title, defaulted to ' '
        :param label_pos: The position of the legend in the plot.  Defaulted to 'upper right'
        :param x_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param y_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param label_font_size: The label font size, defaulted to 18
        :param tick_font_size: The tick font size, defaulted to 18
        :param title_font_size: The title font size, defaulted to 24
        :param marker_size: The size of the marker, defaulted to 35
        :param marker_edge_width: The thickness of the line outlining
                                  each marker.  Defaulted to 0.8
        :param grid: True if a grid overlaid on the plot is desired, False if not
        :param grid_color: Defaulted to 'grey'
        :grid_style: Defaulted to '-'

        This method will plot used defined dataframe columns for the x and
        y axis of a 2-d plot as a scatter plot.

        .. code-block:: python

           > length = 20
           > x = np.linspace(0, 20, num=20)
           > linear = x
           > squared = x ** 2.0
           > # create dataframe
           > dictionary = {'x': x, 'linear': linear, 'squared': squared}
           > df = pd.DataFrame(dictionary)
           > # plot data
           > obj = MatPlotDataFrame()
           > x_headers = ['x', 'x']
           > y_headers = ['linear', 'squared']
           > obj.scatter_plot_columns(df, x_headers, y_headers, y_headers,
                                      x_label='x-axis', y_label='y-axis', title='Test',
                                      style_name='default',marker_colors=['red', 'green'],
                                      fill_alpha=0.7, marker_style=['o', '^'],
                                      label_pos='upper left', grid=False, save=True,
                                      plot_name=plt_name)

        .. image:: scatter_two.png
           :align: center
        """
        # Error checking
        if marker_colors[0] == 'None':
            marker_colors = self.colors
        if len(x_headers) != len(y_headers):
            sys.exit('FATAL ERROR: x and y arrays must be the same size')
        if marker_style[0] == 'None':
            marker_style = self.styles
        if len(marker_style) < len(x_headers):
            msg1 = 'FATAL ERROR: The length of the marker stye list must be as '
            msg2 =  'large or larger than the size of the column values'
            sys.exit(msg1 + msg2)
        if y_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')
        if x_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')
        if labels not in (True, False):
            warnings.warn('labels not correctly set, default to False')
            labels = False

        # begin plot
        plt.rcParams.update({'figure.autolayout': True})
        plt.style.use(style_name)
        rc('xtick', labelsize=tick_font_size)
        rc('ytick', labelsize=tick_font_size)
        if self.nrows > 1 and self.ncols > 1:
            self.ax[row, col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row, col].set_ylabel(y_label, fontsize=label_font_size)
        elif self.nrows > 1:
            self.ax[row].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row].set_ylabel(y_label, fontsize=label_font_size)
        elif self.ncols > 1:
            self.ax[col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[col].set_ylabel(y_label, fontsize=label_font_size)
        else:
            self.ax.set_xlabel(x_label, fontsize=label_font_size)
            self.ax.set_ylabel(y_label, fontsize=label_font_size)

        if title != 'NULL':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_title(title, fontsize=title_font_size)
            elif self.nrows > 1:
                self.ax[row].set_title(title, fontsize=title_font_size)
            elif self.ncols > 1:
                self.ax[col].set_title(title, fontsize=title_font_size)
            else:
                self.ax.set_title(title, fontsize=title_font_size)
        if x_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_xscale('log')
            elif self.nrows > 1:
                self.ax[row].set_xscale('log')
            elif self.ncols > 1:
                self.ax[col].set_xscale('log')
            else:
                self.ax.set_xscale('log')
        if y_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_yscale('log')
            elif self.nrows > 1:
                self.ax[row].set_yscale('log')
            elif self.ncols > 1:
                self.ax[col].set_yscale('log')
            else:
                self.ax.set_yscale('log')

        if self.nrows > 1 and self.ncols > 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax[row, col].scatter(df[x_headers[i]], df[y_headers[i]],
                                          label=y_headers[i], marker=marker_style[i],
                                          color=marker_colors[i], alpha=fill_alpha,
                                          edgecolors=edge_color, s=marker_size,
                                          linewidth=marker_edge_width)
        elif self.nrows > 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax[row].scatter(df[x_headers[i]], df[y_headers[i]],
                                     label=y_headers[i], marker=marker_style[i],
                                     color=marker_colors[i], alpha=fill_alpha,
                                     edgecolors=edge_color, s=marker_size,
                                     linewidth=marker_edge_width)
        elif self.ncols > 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax[col].scatter(df[x_headers[i]], df[y_headers[i]],
                                     label=y_headers[i], marker=marker_style[i],
                                     color=marker_colors[i], alpha=fill_alpha,
                                     edgecolors=edge_color, s=marker_size,
                                     linewidth=marker_edge_width)
        elif self.ncols == 1 and self.nrows == 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax.scatter(df[x_headers[i]], df[y_headers[i]],
                                label=y_headers[i], marker=marker_style[i],
                                color=marker_colors[i], alpha=fill_alpha,
                                edgecolors=edge_color, s=marker_size,
                                linewidth=marker_edge_width)
        if self.nrows > 1 and self.ncols > 1 and labels is False:
            for i in range(len(x_headers)):
                self.ax[row, col].scatter(df[x_headers[i]], df[y_headers[i]],
                                          marker=marker_style[i],
                                          color=marker_colors[i], alpha=fill_alpha,
                                          edgecolors=edge_color, s=marker_size,
                                          linewidth=marker_edge_width)
        elif self.nrows > 1 and labels is False:
            for i in range(len(x_headers)):
                self.ax[row].scatter(df[x_headers[i]], df[y_headers[i]],
                                     marker=marker_style[i],
                                     color=marker_colors[i], alpha=fill_alpha,
                                     edgecolors=edge_color, s=marker_size,
                                     linewidth=marker_edge_width)
        elif self.ncols > 1 and labels is False:
            for i in range(len(x_headers)):
                self.ax[col].scatter(df[x_headers[i]], df[y_headers[i]],
                                     marker=marker_style[i],
                                     color=marker_colors[i], alpha=fill_alpha,
                                     edgecolors=edge_color, s=marker_size,
                                     linewidth=marker_edge_width)
        else:
            for i in range(len(x_headers)):
                self.ax.scatter(df[x_headers[i]], df[y_headers[i]],
                                marker=marker_style[i],
                                color=marker_colors[i], alpha=fill_alpha,
                                edgecolors=edge_color, s=marker_size,
                                linewidth=marker_edge_width)

        if labels is True:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].legend(loc=label_pos)
            elif self.nrows > 1:
                self.ax[row].legend(loc=label_pos)
            elif self.ncols > 1:
                self.ax[col].legend(loc=label_pos)
            else:
                self.ax.legend(loc=label_pos)

        if grid:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].grid(color=grid_color, linestyle=grid_style)
            elif self.nrows > 1:
                self.ax[row].grid(color=grid_color, linestyle=grid_style)
            elif self.ncols > 1:
                self.ax[col].grid(color=grid_color, linestyle=grid_style)
            else:
                self.ax.grid(color=grid_color, linestyle=grid_style)
# --------------------------------------------------------------------------------

    def line_plot_parse_column(self, df: pd.DataFrame, x_header: str,
                               y_header: str, parsing_header: str,
                               column_values: List[str],
                               style_name: str='default',
                               line_colors: List[str]=['None'],
                               line_weight: np.float32=2.0,
                               line_style: str='-', x_label: str='',
                               y_label: str='', title: str='',
                               label_pos: str='upper right',
                               x_scale: str='LIN', y_scale: str='LIN',
                               label_font_size: int=18,
                               tick_font_size: int=18, title_font_size: int=24,
                               grid: bool=False, grid_style='-',
                               grid_color='grey', row: int=0,
                               col: int=0, labels: bool=True) -> None:
        """

        :param df: A pandas dataframe containing data to be plotted
        :param x_header: The column header containing data to be plotted in the
                         x-axis
        :param y_header: The column header containing data to be plotted in the
                         y-axis
        :param parsing_header: The column containing key words that are used
                               to determine what data is plotted.  The keywords
                               will also be used as the plot labels is ``labels`` is
                               set to true
        :param column_values: The keywords that exist within the column defined by parsing
                              header.  The function will filter the dataframe to only
                              contain rows where this keyword is present
        :param style_name: The plot style, defaulted to 'default'.
                           See :href `styles<https://matplotlib.org/stable/api/style_api.html>`
        :param line_colors: A list of line colors, where each marker color
                            corresponds to each data set.  This parameter has a
                            default color lists that can accomodate 18 different
                            data sets.  The user can override the default colors
                            with a list of their own.  Potential colors can be
                            found at :href `colors<https://matplotlib.org/stable/gallery/color/named_colors.html>`
        :param line_weight: The weight of the line, defaulted to 2.0
        :param line_style: THe line style defaulted to '-'
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
        :param labels: True is a legend is to be printed, False if not.  Defaulted
                       to True

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
           obj.line_plot_parse_column(df, 'x', 'y', parsing_header,
                                      column_values,
                                      line_colors=['red', 'green'],
                                      label_pos='upper left')
           obj.show_plot()

        .. image:: line_one.png
           :align: center
        """

        df_list = [df[df[parsing_header] == col_val] for
                   col_val in column_values]

        # Error checking
        if line_colors[0] == 'None':
            line_colors = self.colors
        if len(line_colors) < len(column_values):
            msg1 = 'FATAL ERROR: The length of the marker color list must be as '
            msg2 =  'large or larger than the size of the column values'
            sys.exit(msg1 + msg2)

        if labels not in (True, False):
            warnings.warn('labels not correctly set, default to False')
            labels = False
        # begin plot
        plt.rcParams.update({'figure.autolayout': True})
        plt.style.use(style_name)
        rc('xtick', labelsize=tick_font_size)
        rc('ytick', labelsize=tick_font_size)

        if self.nrows > 1 and self.ncols > 1:
            self.ax[row, col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row, col].set_ylabel(y_label, fontsize=label_font_size)
        elif self.nrows >1:
            self.ax[row].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row].set_ylabel(y_label, fontsize=label_font_size)
        elif self.ncols > 1:
            self.ax[col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[col].set_ylabel(y_label, fontsize=label_font_size)
        else:
            self.ax.set_xlabel(x_label, fontsize=label_font_size)
            self.ax.set_ylabel(y_label, fontsize=label_font_size)
        if title != 'NULL':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_title(title, fontsize=title_font_size)
            elif self.nrows > 1:
                self.ax[row].set_title(title, fontsize=title_font_size)
            elif self.ncols > 1:
                self.ax[col].set_title(title, fontsize=title_font_size)
            else:
                self.ax.set_title(title, fontsize=title_font_size)
        if x_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_xscale('log')
            elif self.nrows > 1:
                self.ax[row].set_xscale('log')
            elif self.ncols > 1:
                self.ax[col].set_xscale('log')
            else:
                self.ax.set_xscale('log')
        if y_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_yscale('log')
            elif self.nrows > 1:
                self.ax[row].set_yscale('log')
            elif self.ncols > 1:
                self.ax[col].set_yscale('log')
            else:
                self.ax.set_yscale('log')

        if self.nrows > 1 and self.ncols > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[row, col].plot(dfs[1][x_header], dfs[1][y_header],
                                       label=column_values[dfs[0]],
                                       linestyle=line_style,
                                       color=line_colors[dfs[0]],
                                       linewidth=line_weight)
        elif self.nrows > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[row].plot(dfs[1][x_header], dfs[1][y_header],
                                         label=column_values[dfs[0]],
                                         linestyle=line_style,
                                         color=line_colors[dfs[0]],
                                         linewidth=line_weight)
        elif self.ncols > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[col].plot(dfs[1][x_header], dfs[1][y_header],
                                         label=column_values[dfs[0]],
                                         linestyle=line_style,
                                         color=line_colors[dfs[0]],
                                         linewidth=line_weight)
        elif self.ncols == 1 and self.nrows ==1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax.plot(dfs[1][x_header], dfs[1][y_header],
                                    label=column_values[dfs[0]],
                                    linestyle=line_style,
                                    color=line_colors[dfs[0]],
                                    linewidth=line_weight)
        if self.nrows > 1 and self.ncols > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[row, col].plot(dfs[1][x_header], dfs[1][y_header],
                                       linestyle=line_style,
                                       color=line_colors[dfs[0]],
                                       linewidth=line_weight)
        elif self.nrows > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[row].plot(dfs[1][x_header], dfs[1][y_header],
                                         linestyle=line_style,
                                         color=line_colors[dfs[0]],
                                         linewidth=line_weight)
        elif self.ncols > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[col].plot(dfs[1][x_header], dfs[1][y_header],
                                         linestyle=line_style,
                                         color=line_colors[dfs[0]],
                                         linewidth=line_weight)
        else:
            for dfs in enumerate(df_list):
                self.ax.plot(dfs[1][x_header], dfs[1][y_header],
                                    linestyle=line_style,
                                    color=line_colors[dfs[0]],
                                    linewidth=line_weight)

        if labels is True:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].legend(loc=label_pos)
            elif self.nrows > 1:
                self.ax[row].legend(loc=label_pos)
            elif self.ncols > 1:
                self.ax[col].legend(loc=label_pos)
            else:
                self.ax.legend(loc=label_pos)
        if grid:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].grid(color=grid_color, linestyle=grid_style)
            elif self.nrows > 1:
                self.ax[row].grid(color=grid_color, linestyle=grid_style)
            elif self.ncols > 1:
                self.ax[col].grid(color=grid_color, linestyle=grid_style)
            else:
                self.ax.grid(color=grid_color, linestyle=grid_style)
# --------------------------------------------------------------------------------

    def line_plot_columns(self, df: pd.DataFrame, x_headers: str, y_headers: str,
                          labels: List[str], style_name: str='default',
                          line_colors: List[str]=['None'],
                          line_weight: np.float32=2.0,
                          line_style: str='-', x_label: str='', y_label: str='',
                          title: str='', label_pos: str='upper right', x_scale: str='LIN',
                          y_scale: str='LIN', label_font_size: int=18,
                          tick_font_size: int=18, title_font_size: int=24,
                          grid: bool=False, grid_style='-', grid_color='grey',
                          row: int=0, col: int=0) -> None:
        """

        :param df: A pandas dataframe containing the data to be plotted
        :param x_headers: The title of the dataframe columns containing the x-axis
                          data sets
        :param y_headers: The title of the dataframe columns containing the y-axis
                          data sets
        :param labels: A list containing the name of each label
        :param style_name: The name of the matplotlib style that will be used to
                           format the plot.  Defaulted to 'default'.  Possible
                           styles can be found at :href
                           `styles<https://matplotlib.org/stable/api/style_api.html>`
        :param line_colors: A list of line colors, where each marker color
                            corresponds to each data set.  This parameter has a
                            default color lists that can accomodate 18 different
                            data sets.  The user can override the default colors
                            with a list of their own.  Potential colors can be
                            found at :href `colors<https://matplotlib.org/stable/gallery/color/named_colors.html>`
        :param line_weight: The weight corresponding to the line thickness, defaulted to 2.0
        :param x_label: The x axis label,defaulted to ' '
        :param y_label: The y axis label, defaulted to ' '
        :param title: The plot title, defaulted to ' '
        :param label_pos: The position of the legend in the plot.  Defaulted to 'upper right'
        :param x_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param y_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param label_font_size: The label font size, defaulted to 18
        :param tick_font_size: The tick font size, defaulted to 18
        :param title_font_size: The title font size, defaulted to 24
        :param grid: True if a grid overlaid on the plot is desired, False if not
        :param grid_color: Defaulted to 'grey'
        :param grid_style: Defaulted to '-'
        :param row: The row within the grid that the plot fill fill
        :param col: The column within the gird that the plot will fill

        This method will plot used defined dataframe columns for the x and
        y axis of a 2-d plot as a line plot.

        .. code-block:: python

           > length = 20
           > x = np.linspace(0, 20, num=20)
           > linear = x
           > squared = x ** 2.0
           > # create dataframe
           > dictionary = {'x': x, 'linear': linear, 'squared': squared}
           > df = pd.DataFrame(dictionary)
           > # plot data
           > obj = MatPlotDataFrame()
           > x_headers = ['x', 'x']
           > y_headers = ['linear', 'squared']
           obj.line_plot_columns(df, x_headers, y_headers, labels=False,
                                 x_label='x-axis', y_label='y-axis', title='Test',
                                 style_name='default',line_colors=['red', 'green'],
                                 label_pos='upper left', grid=False)

        .. image:: line_one.png
           :align: center
        """

        # Error checking
        if line_colors[0] == 'None':
            line_colors = self.colors
        if y_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')
        if x_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')

        # begin plot
        plt.rcParams.update({'figure.autolayout': True})
        plt.style.use(style_name)
        rc('xtick', labelsize=tick_font_size)
        rc('ytick', labelsize=tick_font_size)
        if self.nrows > 1 and self.ncols > 1:
            self.ax[row, col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row, col].set_ylabel(y_label, fontsize=label_font_size)
        elif self.nrows > 1:
            self.ax[row].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row].set_ylabel(y_label, fontsize=label_font_size)
        elif self.ncols > 1:
            self.ax[col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[col].set_ylabel(y_label, fontsize=label_font_size)
        else:
            self.ax.set_xlabel(x_label, fontsize=label_font_size)
            self.ax.set_ylabel(y_label, fontsize=label_font_size)

        if title != 'NULL':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_title(title, fontsize=title_font_size)
            elif self.nrows > 1:
                self.ax[row].set_title(title, fontsize=title_font_size)
            elif self.ncols > 1:
                self.ax[col].set_title(title, fontsize=title_font_size)
            else:
                self.ax.set_title(title, fontsize=title_font_size)
        if x_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_xscale('log')
            elif self.nrows > 1:
                self.ax[row].set_xscale('log')
            elif self.ncols > 1:
                self.ax[col].set_xscale('log')
            else:
                self.ax.set_xscale('log')
        if y_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_yscale('log')
            elif self.nrows > 1:
                self.ax[row].set_yscale('log')
            elif self.ncols > 1:
                self.ax[col].set_yscale('log')
            else:
                self.ax.set_yscale('log')

        if self.nrows > 1 and self.ncols > 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax[row, col].plot(df[x_headers[i]], df[y_headers[i]],
                                       label=y_headers[i], color=line_colors[i],
                                       linewidth=line_weight, linestyle=line_style)
        elif self.nrows > 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax[row].plot(df[x_headers[i]], df[y_headers[i]],
                                  label=y_headers[i], color=line_colors[i],
                                  linewidth=line_weight, linestyle=line_style)
        elif self.ncols > 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax[col].plot(df[x_headers[i]], df[y_headers[i]],
                                  label=y_headers[i], color=line_colors[i],
                                  linewidth=line_weight, linestyle=line_style)
        elif self.ncols == 1 and self.nrows == 1 and labels is True:
            for i in range(len(x_headers)):
                self.ax.plot(df[x_headers[i]], df[y_headers[i]],
                             label=y_headers[i], color=line_colors[i],
                             linewidth=line_weight, linestyle=line_style)
        if self.nrows > 1 and self.ncols > 1 and labels is False:
            for i in range(len(x_headers)):
                self.ax[row, col].plot(df[x_headers[i]], df[y_headers[i]],
                                       color=line_colors[i],
                                       linewidth=line_weight, linestyle=line_style)
        elif self.nrows > 1 and labels is False:
            for i in range(len(x_headers)):
                self.ax[row].plot(df[x_headers[i]], df[y_headers[i]],
                                  color=line_colors[i],
                                  linewidth=line_weight, linestyle=line_style)
        elif self.ncols > 1 and labels is False:
            for i in range(len(x_headers)):
                self.ax[col].plot(df[x_headers[i]], df[y_headers[i]],
                                  color=line_colors[i],
                                  linewidth=line_weight, linestyle=line_style)
        else:
            for i in range(len(x_headers)):
                self.ax.plot(df[x_headers[i]], df[y_headers[i]],
                             color=line_colors[i],
                             linewidth=line_weight, linestyle=line_style)

        if labels is True:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].legend(loc=label_pos)
            elif self.nrows > 1:
                self.ax[row].legend(loc=label_pos)
            elif self.ncols > 1:
                self.ax[col].legend(loc=label_pos)
            else:
                self.ax.legend(loc=label_pos)

        if grid:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].grid(color=grid_color, linestyle=grid_style)
            elif self.nrows > 1:
                self.ax[row].grid(color=grid_color, linestyle=grid_style)
            elif self.ncols > 1:
                self.ax[col].grid(color=grid_color, linestyle=grid_style)
            else:
                self.ax.grid(color=grid_color, linestyle=grid_style)
# --------------------------------------------------------------------------------

    def timedate_plot_parse_column(self, df: pd.DataFrame, x_header: str,
                                   y_header: str, parsing_header: str, column_values: List[str],
                                   style_name: str='default', line_colors: List[str]=['None'],
                                   line_weight: np.float32=2.0,
                                   line_style: str='-', x_label: str='', y_label: str='',
                                   title: str='', label_pos: str='upper right',
                                   x_scale: str='LIN', y_scale: str='LIN',
                                   label_font_size: int=18,
                                   tick_font_size: int=18, title_font_size: int=24,
                                   grid: bool=False, grid_style='-', grid_color='grey',
                                   row: int=0, col: int=0, labels: bool=True) -> None:
        """

        :param df: A pandas dataframe containing the data to be plotted
        :param x_header: The title of the dataframe column containing the x-axis
                         data sets.  It is assumes that the x axis is the datetime
                         axis for this plot.
        :param y_header: The title of the dataframe column containing the y-axis
                         data sets
        :param parsing_header: The title of the dataframe column containing the
                               values which will be used to parse the dataframe into
                               one or multiple data sets
        :param column_values: The values contained in the parsing_header column
                              that will be used to parse the data set into
                              multiple data sets
        :param style_name: The name of the matplotlib style that will be used to
                           format the plot.  Defaulted to 'default'.  Possible
                           styles can be found at :href
                           `styles<https://matplotlib.org/stable/api/style_api.html>`
        :param line_colors: A list of line colors, where each marker color
                            corresponds to each data set.  This parameter has a
                            default color lists that can accomodate 18 different
                            data sets.  The user can override the default colors
                            with a list of their own.  Potential colors can be
                            found at :href `colors<https://matplotlib.org/stable/gallery/color/named_colors.html>`
        :param line_weight: The weight corresponding to the line thickness, defaulted to 2.0
        :param fill_apha: The density of the marker fill.  Defaulted to 0.7
        :param x_label: The x axis label,defaulted to ' '
        :param y_label: The y axis label, defaulted to ' '
        :param title: The plot title, defaulted to ' '
        :param label_pos: The position of the legend in the plot.  Defaulted to 'upper right'
        :param x_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param y_scale: 'LOG' or 'LIN', defaulted to 'LIN'
        :param plot_name: The name of the file containing the plot if the plot is to
                          be saved.  Defaulted to 'NULL'
        :param save: True if the plot is to be saved, False if the plot is to be
                     shown and not saved.  Defaulted to False
        :param label_font_size: The label font size, defaulted to 18
        :param tick_font_size: The tick font size, defaulted to 18
        :param title_font_size: The title font size, defaulted to 24
        :param marker_size: The size of the marker, defaulted to 35
        :param marker_edge_width: The thickness of the line outlining
                                  each marker.  Defaulted to 0.8
        :param grid: True if a grid overlaid on the plot is desired, False if not
        :param grid_color: Defaulted to 'grey'
        :grid_style: Defaulted to '-'

        This method will parse a dataframe column based on a user specified
        value or list of values, and plot the data in a user specified
        x and y axis column based on filter data.  As an example, consider
        a dataframe with the following columnar data structure.

        .. code-block:: python

           > length = 6
           > dates = pd.date_range(start=pd.to_datetime('2016-09-24'),
                                   periods = length, freq='w')
           > x = np.linspace(0, length, num=length)
           > linear = x
           > squared = x ** 2.0
           > lin = np.repeat('linear', length)
           > sq = np.repeat('squared', length)

           > # Combine arrays into one
           > x = np.hstack((dates, dates))
           > y = np.hstack((linear, squared))
           > power = np.hstack((lin, sq))

           > # Create dataframe
           > dictionary = {'dates': x, 'y': y, 'power': power}
           > df = pd.DataFrame(dictionary)
           > # Plot data
           > obj = MatPlotDataFrame()

           > parsing_header = 'power'
           > column_values = ['linear', 'squared']
           > obj.timedate_plot_parse_column(df, 'dates', 'y', parsing_header, column_values,
                                            x_label='x-axis', y_label='y-axis', title='Test',
                                            style_name='default', line_colors=['red', 'green'],
                                            label_pos='upper left', grid=True)

        .. image:: time_plot.png
           :align: center
        """
        df_list = [df[df[parsing_header] == col_val] for
                   col_val in column_values]
        max_date = df[x_header].max()
        min_date = df[x_header].min()
        diff = (max_date - min_date) / np.timedelta64(1, 'D')
        df_list = [df[df[parsing_header] == col_val] for
                   col_val in column_values]
        df_list = [df.set_index(x_header) for df in df_list]

        # Error checking
        if line_colors[0] == 'None':
            line_colors = self.colors
        if len(line_colors) < len(column_values):
            msg1 = 'FATAL ERROR: The length of the marker color list must be as '
            msg2 =  'large or larger than the size of the column values'
            sys.exit(msg1 + msg2)
        if y_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')
        if x_scale not in ('LOG', 'LIN'):
            warnings.warn('y_scale must be set to LOG or LIN')

        # begin plot
        plt.rcParams.update({'figure.autolayout': True})
        plt.style.use(style_name)
        rc('xtick', labelsize=tick_font_size)
        rc('ytick', labelsize=tick_font_size)

        if self.nrows > 1 and self.ncols > 1:
            self.ax[row, col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row, col].set_ylabel(y_label, fontsize=label_font_size)
        elif self.nrows >1:
            self.ax[row].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[row].set_ylabel(y_label, fontsize=label_font_size)
        elif self.ncols > 1:
            self.ax[col].set_xlabel(x_label, fontsize=label_font_size)
            self.ax[col].set_ylabel(y_label, fontsize=label_font_size)
        else:
            self.ax.set_xlabel(x_label, fontsize=label_font_size)
            self.ax.set_ylabel(y_label, fontsize=label_font_size)
        if title != 'NULL':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_title(title, fontsize=title_font_size)
            elif self.nrows > 1:
                self.ax[row].set_title(title, fontsize=title_font_size)
            elif self.ncols > 1:
                self.ax[col].set_title(title, fontsize=title_font_size)
            else:
                self.ax.set_title(title, fontsize=title_font_size)
        if x_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_xscale('log')
            elif self.nrows > 1:
                self.ax[row].set_xscale('log')
            elif self.ncols > 1:
                self.ax[col].set_xscale('log')
            else:
                self.ax.set_xscale('log')
        if y_scale.upper() == 'LOG':
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].set_yscale('log')
            elif self.nrows > 1:
                self.ax[row].set_yscale('log')
            elif self.ncols > 1:
                self.ax[col].set_yscale('log')
            else:
                self.ax.set_yscale('log')

        if self.nrows > 1 and self.ncols > 1:
            if diff <= 2:
                myfmt = mdates.DateFormatter('%H')
                self.ax[row, col].xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 15:
                myfmt = mdates.DateFormatter('%b-%d')
                self.ax[row, col].xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 180:
                myfmt = mdates.DateFormatter('%b-%Y')
                self.ax[row, col].xaxis.set_major_locator(plt.MaxNLocator(5))
            elif diff <= 2191:
                myfmt = mdates.DateFormatter('%Y')
                self.ax[row, col].xaxis.set_major_locator(plt.MaxNLocator(5))
            else:
                myfmt = mdates.DateFormatter('%Y')
                self.ax[row, col].xaxis.set_major_locator(plt.MaxNLocator(5))
            self.ax[row, col].xaxis.set_major_formatter(myfmt)
        elif self.nrows > 1:
            if diff <= 2:
                myfmt = mdates.DateFormatter('%H')
                self.ax[row].xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 15:
                myfmt = mdates.DateFormatter('%b-%d')
                self.ax[row].xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 180:
                myfmt = mdates.DateFormatter('%b-%Y')
                self.ax[row].xaxis.set_major_locator(plt.MaxNLocator(5))
            elif diff <= 2191:
                myfmt = mdates.DateFormatter('%Y')
                self.ax[row].xaxis.set_major_locator(plt.MaxNLocator(5))
            else:
                myfmt = mdates.DateFormatter('%Y')
                self.ax[row].xaxis.set_major_locator(plt.MaxNLocator(5))
            self.ax[row].xaxis.set_major_formatter(myfmt)
        elif self.ncols > 1:
            if diff <= 2:
                myfmt = mdates.DateFormatter('%H')
                self.ax[col].xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 15:
                myfmt = mdates.DateFormatter('%b-%d')
                self.ax[col].xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 180:
                myfmt = mdates.DateFormatter('%b-%Y')
                self.ax[col].xaxis.set_major_locator(plt.MaxNLocator(5))
            elif diff <= 2191:
                myfmt = mdates.DateFormatter('%Y')
                self.ax[col].xaxis.set_major_locator(plt.MaxNLocator(5))
            else:
                myfmt = mdates.DateFormatter('%Y')
                self.ax[col].xaxis.set_major_locator(plt.MaxNLocator(5))
            self.ax[col].xaxis.set_major_formatter(myfmt)
        else:
            if diff <= 2:
                myfmt = mdates.DateFormatter('%H')
                self.ax.xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 60:
                myfmt = mdates.DateFormatter('%b-%d')
                self.ax.xaxis.set_major_locator(plt.MaxNLocator(6))
            elif diff <= 180:
                myfmt = mdates.DateFormatter('%b-%Y')
                self.ax.xaxis.set_major_locator(plt.MaxNLocator(5))
            elif diff <= 2191:
                myfmt = mdates.DateFormatter('%Y')
                self.ax.xaxis.set_major_locator(plt.MaxNLocator(5))
            else:
                myfmt = mdates.DateFormatter('%Y')
                self.ax.xaxis.set_major_locator(plt.MaxNLocator(5))
            self.ax.xaxis.set_major_formatter(myfmt)
        if self.nrows > 1 and self.ncols > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[row, col].plot(dfs[1][x_header], dfs[1][y_header],
                                       label=column_values[dfs[0]],
                                       linestyle=line_style,
                                       color=line_colors[dfs[0]],
                                       linewidth=line_weight)
        elif self.nrows > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[row].plot(dfs[1][x_header], dfs[1][y_header],
                                         label=column_values[dfs[0]],
                                         linestyle=line_style,
                                         color=line_colors[dfs[0]],
                                         linewidth=line_weight)
        elif self.ncols > 1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax[col].plot(dfs[1][x_header], dfs[1][y_header],
                                         label=column_values[dfs[0]],
                                         linestyle=line_style,
                                         color=line_colors[dfs[0]],
                                         linewidth=line_weight)
        elif self.ncols == 1 and self.nrows ==1 and labels is True:
            for dfs in enumerate(df_list):
                self.ax.plot(dfs[1].index, dfs[1][y_header],
                             label=column_values[dfs[0]],
                             linestyle=line_style,
                             color=line_colors[dfs[0]],
                             linewidth=line_weight)
        if self.nrows > 1 and self.ncols > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[row, col].plot(dfs[1].index, dfs[1][y_header],
                                       linestyle=line_style,
                                       color=line_colors[dfs[0]],
                                       linewidth=line_weight)
        elif self.nrows > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[row].plot(dfs[1].index, dfs[1][y_header],
                                  linestyle=line_style,
                                  color=line_colors[dfs[0]],
                                  linewidth=line_weight)
        elif self.ncols > 1 and labels is False:
            for dfs in enumerate(df_list):
                self.ax[col].plot(dfs[1].index, dfs[1][y_header],
                                  linestyle=line_style,
                                  color=line_colors[dfs[0]],
                                  linewidth=line_weight)
        else:
            for dfs in enumerate(df_list):
                self.ax.plot(dfs[1].index, dfs[1][y_header],
                             linestyle=line_style,
                             color=line_colors[dfs[0]],
                             linewidth=line_weight)

        if labels is True:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].legend(loc=label_pos)
            elif self.nrows > 1:
                self.ax[row].legend(loc=label_pos)
            elif self.ncols > 1:
                self.ax[col].legend(loc=label_pos)
            else:
                self.ax.legend(loc=label_pos)
        if grid:
            if self.nrows > 1 and self.ncols > 1:
                self.ax[row, col].grid(color=grid_color, linestyle=grid_style)
            elif self.nrows > 1:
                self.ax[row].grid(color=grid_color, linestyle=grid_style)
            elif self.ncols > 1:
                self.ax[col].grid(color=grid_color, linestyle=grid_style)
            else:
                self.ax.grid(color=grid_color, linestyle=grid_style)
# --------------------------------------------------------------------------------

    def show_plot(self):
        """

        This function will show a plot on the users screen without saving it
        """
        plt.show()
# --------------------------------------------------------------------------------

    def save_fig(self, file_name: str) -> None:
        """

        :param file_name: The name of the file to be saved to
                          include the path length

        This function will save a plot to a file and directory of the users
        choosing
        """
        plt.savefig(file_name)
# ================================================================================
# ================================================================================
# eof

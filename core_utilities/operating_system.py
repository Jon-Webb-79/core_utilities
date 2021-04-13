# Import necessary packages here

import os
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


class OSUtilities:
    """

    This set of functions were written as class methods in order
    to ensure that they can be passed in bulk via decorator patters
    or through inheritance.  This class provides file analysis
    capabilities and a user interface for file and directory management
    similar to Bash and DOS functionality, although with different
    syntax

    All code examples are predicated on the instantiation of this class
    with the following command

    .. code-block:: python

       > util = OSUtilities()
    """
    @classmethod
    def change_directory(cls, new_directory: str) -> None:
        """

        :param new_directory: The desired directory to include
                              path link
        :return None:

        This function will change the directory in the same manner as
        the `cd` DOS and Linux command.  For example, if you are
        in the `dir1` directory within the following chain;

        `home/dir1/dir2/`

        You can use the following python script to change to the `dir2`
        directory.

        .. code-block:: python

           > print(util.current_working_directory())
           '/home/dir1'
           > util.change_directory('dir2')
           > print(util.current_working_directory())
           '/home/dir1/dir2'

        You can change back to the `home` directory with the following
        command;

        .. code-block:: python

           > util.change_directory('../..')
           > print(util.current_working_directory())
           '/home'
        """
        if not os.path.isdir(new_directory):
            print('{}{}'.format(new_directory, ' does not exist'))
        else:
            os.chdir(new_directory)
# --------------------------------------------------------------------------------

# ================================================================================
# ================================================================================
# eof

# Import necessary packages here

import os
import shutil
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

    @classmethod
    def copy_directory(cls, source: str, destination: str) -> None:
        """

        :param source: The name and path-link of the directory to
                       be copied
        :param destination: The name and path-link for the directory
                            copy
        :return None:

        This function creates a copy of a directory and assigns
        it to the directory of the users choosing.  This function
        will copy populated and un-populated directories.  As
        an example lets assume the following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        The following command will make  copy of ``directory_2`` in
        the ``directory_3`` titled ``dir2_copy``, directory assuming
        we are in the ``directory_1`` directory

        .. code-block:: python

           > copy_directory('directory_2', 'directory_3/dir2_copy')
           > change_directory('directory_3')
           > print(list_contents())
           [''another_text_file.txt', 'dir2_copy']

        """
        if not os.path.isdir(source):
            print('{}{}'.format(source, ' does not exist'))
        elif os.path.isdir(destination):
            print('{}{}'.format(destination, ' already exists'))
        else:
            shutil.copytree(source, destination)
# ================================================================================
# ================================================================================
# eof

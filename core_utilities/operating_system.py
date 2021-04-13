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
# --------------------------------------------------------------------------------


    @classmethod
    def copy_file(cls, source: str, destination: str) -> None:
        """

        :param source: The name and path-link of the file to be
                       copied
        :param destination: The name and path-link for the file copy
        :return None:

        This function creates a copy of a file and assigns it to the
        name and directory of the users choosing.  As
        an example lets assume the following directory structure;

        .. code-block:: text

           directory_1
              |
              text_file.txt
              directory_2
              directory_3
                 |
                 another_text_file.txt

        The following command will make  copy of ``text_file.txt`` in
        the ``directory_3`` titled ``text_copy.txt``, directory assuming
        we are in the ``directory_1`` directory

        .. code-block:: python

           > copy_file('text_file.txt', 'directory_3/text_copy.txt')
           > change_directory('directory_3')
           > print(list_contents())
           [''another_text_file.txt', 'text_copy.txt']

        """
        if not os.path.isfile(source):
            print('{}{}'.format(source, ' does not exist'))
        elif os.path.isfile(destination):
            print('{}{}'.format(destination, ' already exists'))
        else:
            shutil.copy(source, destination)
# ----------------------------------------------------------------------------

    @classmethod
    def count_occurrence_of_word_in_file(cls, file_name: str, word: str) -> int:
        """

        :param file_name: The file name to include the path link
        :param word: the word for which the number of occurrences in
                     a file is desired.
        :return num: The number of times a specific word occurs in a
                     file.

        This function excludes the effects of punctuation.  For example
        if the user defined word is `book` and the file contains the
        word `book.` with a period following it indicating the end of a
        sentence, this function will count that word.  The same is true
        for commas.  As an example lets assume the file listed below,
        titled ``test.txt``;

        .. code-block:: text

           This is a text file, all
           of the information in this
           file is specifically for
           the purpose of testing file file

        The following code will count the occurrence of the word ``file``

        .. code-block:: python

           > num = util.count_occurrence_of_word_in_file('test.txt', 'file')
           > print(num)
           4
        """
        file = open(file_name, "rt")
        data = file.read().split()
        counter = 0
        for i in range(len(data)):
            if data[i] == word:
                counter += 1
            if data[i] == word + ',':
                counter += 1
            if data[i] == word + '.':
                counter += 1
        return counter
# ================================================================================
# ================================================================================
# eof

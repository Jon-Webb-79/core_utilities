****************
operating_system
****************

The ``operating_system`` module contains methods that allow a user to access common functions
from the Python console or from a Python script to enable file reading, plotting, and also
provides a Command Line Interface (CLI) for the Python interpreter. These functions are 
to simplify or augment many of the utilities offered in
`os <https://docs.python.org/3/library/os.html>`_ and `sys <https://docs.python.org/3/library/sys.html>`_ packages

The operating_system module contains the following functions

.. code-block:: python

   > from core_utilities import operating_system as util

.. autofunction:: operating_system.change_directory

.. autofunction:: operating_system.copy_directory

.. autofunction:: operating_system.copy_file

.. autofunction:: operating_system.count_occurrence_of_word_in_file

.. autofunction:: operating_system.create_directory

.. autofunction:: operating_system.create_file

.. autofunction:: operating_system.current_working_directory

.. autofunction:: operating_system.delete_directory

.. autofunction:: operating_system.delete_file

.. autofunction:: operating_system.delete_populated_directory

.. autofunction:: operating_system.determine_file_size

.. autofunction:: operating_system.file_line_count

.. autofunction:: operating_system.file_word_count

.. autofunction:: operating_system.move_directory

.. autofunction:: operating_system.move_file

.. autofunction:: operating_system.list_contents

.. autofunction:: operating_system.copy_files

.. autofunction:: operating_system.move_files

.. autofunction:: operating_system.verify_directory_existence

.. autofunction:: operating_system.verify_file_existence


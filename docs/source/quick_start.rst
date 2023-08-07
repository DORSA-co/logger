Quick Start
------------

Step 1: Import and Initialize The Logger
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First, you need to import the logger module in your Python script to use its functionalities.
Then, Create an instance of the logger by providing the necessary configurations. 
You need to specify the main folder path where log files will be stored:

.. code-block:: python

   import dorsa_logger

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
   )

After initializing a logger object, the specified `main_folderpath` is created.
Inside the main folder, a subfolder is generated with the name of the current date, and within that subfolder, 
a log file is created with the current date and time as its name.

Step 2: Define Log Message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Second, define custom log messages using the :py:class:`dorsa_logger.log_message` class. 
You must specify level and text of message. You can also specify a code for message. 
For more see section :doc:`logger_messages`:

.. code-block:: python

   log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, message="An error occurred", code="ERR000")

Step 3: Create New Log
^^^^^^^^^^^^^^^^^^^^^^^
Now, you can log messages using the :py:func:`dorsa_logger.logger.create_new_log` method.

.. code-block:: python

   logger_obj.create_new_log(message=log_msg)

After executing this function, the specified message is added to the end of the log file 
that corresponds to the current date and time. In addition, the message is printed on the console.

.. code-block:: console

   $ ERROR - 2023-08-06-10-38-00 - anonymous : (ERR000) An error occurred
   -----------------------------------------------------------------------------------
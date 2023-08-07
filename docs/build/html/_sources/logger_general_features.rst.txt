Logger General Features
------------------------

The **Logger** module offers various features and options to customize the logging behavior 
according to the needs of the developer. Below is an explanation of the general features 
and options available in this module:

.. _mainFolderPath-subsection:

Main Folder Path
^^^^^^^^^^^^^^^^^
The main_folderpath parameter allows you to specify the main folder 
where the log files will be stored. This folder will be created if it does not exist.
You need to specify main_folderpath parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
   )

You can change specified main_folderpath using :py:func:`dorsa_logger.logger.set_main_folderpath` method.

.. code-block:: python

   logger_obj.set_main_folderpath('./app_logs2')

.. _dateAndTime-subsection:

Date and Time
^^^^^^^^^^^^^^
The date_type, date_format, and time_format parameters enable you to define the type and format of the date and time 
used in the name and contents of the log file. This customization provides flexibility to match your preferred date 
and time representation.

Date Type
""""""""""
The available date types specified in the date_types class are as follows:

* SOLAR_DATE
* AD_DATE

The default value of date_type parameter is AD_DATE.
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        date_type=dorsa_logger.date_types.SOLAR_DATE,
   )

You can change date_type using :py:func:`dorsa_logger.date.set_date_type` method.

.. code-block:: python

   logger_obj.date.set_date_type(dorsa_logger.date_types.SOLAR_DATE)

Date Format
""""""""""""
The available date formats specified in the date_formats class are as follows:

* MMDDYY (month-day-year)
* DDMMYY (day-month-year)
* YYMMDD (year-month-day)

The default value of date_format parameter is YYMMDD.
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        date_format=dorsa_logger.date_formats.MMDDYY,
   )

You can change date_format using :py:func:`dorsa_logger.date.set_date_format` method.

.. code-block:: python

   logger_obj.date.set_date_format(dorsa_logger.date_formats.MMDDYY)

Time Format
""""""""""""
The available time formats specified in the time_formats class are as follows:

* HHMM (hour-minute)
* HHMMSS (hour-minute-second)
* HHMMSSMM (hour-minute-second-millisecond)

The default value of time_format parameter is HHMMSS.
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        time_format: str = time_formats.HHMMSSMM,
   )

You can change time_format using :py:func:`dorsa_logger.time.set_time_format` method.

.. code-block:: python

   logger_obj.time.set_time_format(dorsa_logger.time_formats.HHMMSSMM)

.. _logLevels-subsection:

Log Levels
^^^^^^^^^^^
The file_level and console_level parameters allow you to set the log levels for file logging and console logging, 
respectively. Logs with a lower level than the specified level will be ignored. 

The available log levels specified in the log_levels class are as follows:

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL
* EXCEPTION

File Level
"""""""""""
The default value of file_level parameter is DEBUG.
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        file_level=dorsa_logger.log_levels.CRITICAL,
   )

You can change file_level using :py:func:`dorsa_logger.logger.set_file_level` method.

.. code-block:: python

   logger_obj.set_file_level(dorsa_logger.log_levels.CRITICAL)

Console Level
""""""""""""""
The default value of console_level parameter is DEBUG.
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        console_level=dorsa_logger.log_levels.EXCEPTION,
   )

You can change console_level using :py:func:`dorsa_logger.logger.set_console_level` method.

.. code-block:: python

   logger_obj.set_console_level(dorsa_logger.log_levels.EXCEPTION)

Console Printing
^^^^^^^^^^^^^^^^^
The console_print parameter determines whether log messages should also be printed to the console. 
Setting it to True enables console logging, while setting it to False disables it.

The default value of console_print parameter is True.
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        console_print=False,
   )

You can change console_print using :py:func:`dorsa_logger.logger.set_console_print` method.

.. code-block:: python

   logger_obj.set_console_print(False)

Current Username
^^^^^^^^^^^^^^^^^
The current_username parameter is used to associate a username with log messages, 
which can be helpful when identifying the source of log entries.

The default value of current_username parameter is *anonymous*.
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        current_username="admin",
   )

You can change current_username using :py:func:`dorsa_logger.logger.set_current_user` method.

.. code-block:: python

   logger_obj.set_current_user('admin')

.. _lineSeperator-subsection:

Line Separator
^^^^^^^^^^^^^^^
The line_seperator parameter sets the character(s) used to separate lines in the log messages, 
making the log entries more readable.

The default value of line_seperator parameter is "-".
You can set this parameter when initializing the module:

.. code-block:: python

   logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
        line_seperator='-',
   )

You can change line_seperator using :py:func:`dorsa_logger.logger.set_line_seperator` method.

.. code-block:: python

   logger_obj.set_line_seperator('*')

Defined Log Messages
^^^^^^^^^^^^^^^^^^^^^
The logger class allows you to pre-define log messages. This feature is helpful when you have specific
log messages that you want to reuse throughout your code.

For more information about this feature see section :doc:`logger_messages`

Logging Decorators
^^^^^^^^^^^^^^^^^^^
The logger class provides three logging decorators. These decorators can be used to automatically log the 
start, exceptions, and end of functions with specified log messages.

For more information about this feature see section :doc:`logger_decorators`



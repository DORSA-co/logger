Logger Decorators
------------------
The logger class provides decorators to log the start, end, or exceptions of functions. 
You can use these decorators to automatically log function activities.

.. note::

   If you want to use more than one decorator for your function, 
   please follow the start, exception, and end order for proper functionality.

Function Start Decorator
^^^^^^^^^^^^^^^^^^^^^^^^^
The :py:func:`dorsa_logger.logger.function_start_decorator` decorator is used to log a message 
at the start of a function. It takes the log message (either a predefined message key or a custom log message) 
as an argument. If no message provided, it use a fixed defined message for logging.
The decorator creates a new log with the specified message at the beginning of the function execution.

You can use this decorator before defining your function with the *@* symbol:

.. code-block:: python

    @logger_obj.function_start_decorator()
    def func(a, b):
        # Function logic goes here

You can also pass your own log message to it:

.. code-block:: python

    @logger_obj.function_start_decorator(dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO, message="Function started.", code="ERR000"))
    def func(a, b):
        # Function logic goes here

Function Exception Decorators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :py:func:`dorsa_logger.logger.function_exception_decorator` is used to log a message 
when an exception occurs within a function. 
It takes the log message (either a predefined message key or a custom log message) 
as an argument. If no message provided, it use a fixed defined message for logging.
The decorator also provides an option to handle the exception and 
continue with the program execution or re-raise the exception to propagate it further.
When applied to a function, it creates a new log entry with the specified message 
if an exception occurs within the function.

You can use this decorator before defining your function with the *@* symbol:

.. code-block:: python

    @logger_obj.function_exception_decorator()
    def func(a, b):
        # Function logic goes here

You can also pass your own log message to it:

.. code-block:: python

    @logger_obj.function_exception_decorator(dorsa_logger.log_message(level=dorsa_logger.log_levels.EXCEPTION, message="An exception occurred.", code="ERR002"), with_handling=True)
    def func(a, b):
        # Function logic goes here

Function End Decorator
^^^^^^^^^^^^^^^^^^^^^^^
The :py:func:`dorsa_logger.logger.function_end_decorator` decorator is used to log a message 
at the end of a function. It takes the log message (either a predefined message key or a custom log message) 
as an argument. If no message provided, it use a fixed defined message for logging.
The decorator creates a new log entry with the specified message just after the function finishes executing.

You can use this decorator before defining your function with the *@* symbol:

.. code-block:: python

    @logger_obj.function_end_decorator()
    def func(a, b):
        # Function logic goes here

You can also pass your own log message to it:

.. code-block:: python

    @logger_obj.function_end_decorator(dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO, message="Function finished.", code="ERR001"))
    def func(a, b):
        # Function logic goes here

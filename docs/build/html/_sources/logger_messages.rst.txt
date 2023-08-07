Logger Messages
----------------
In the logger class, log messages are used to record information about the events that occur during the execution 
of a program. Log messages provide insights into the program's behavior, making it easier to monitor, 
debug, and analyze the application's performance. The class provides the ability to create custom log 
messages and use predefined log messages.

Log Messages
^^^^^^^^^^^^^
The :py:class:`dorsa_logger.log_message` class is a custom class utilized within the logger module 
to represent log text along with their corresponding log levels. 
Its primary purpose is to offer a structured approach for defining log messages with varying severity levels, 
catering to diverse logging requirements. 
Additionally, the class enables you to associate a unique code with each log message, 
enhancing message identification and management.

To create a log_message instance, you need to define log text and log level when initializing. You can also define
a code for your message:

.. code-block:: python

   log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR000")

You can change the level, text or code of the message as follows:

.. code-block:: python

   log_msg.set_level(dorsa_logger.log_levels.DEBUG)
   log_msg.set_text('This is a message for debug')
   log_msg.set_code('DEBUG000')

You can then pass this log message to the :py:func:`dorsa_logger.logger.create_new_log` method for logging.

Predefined Log Messages
^^^^^^^^^^^^^^^^^^^^^^^^
Predefined log messages in the logger module refer to a set of log messages that have been defined 
and stored in the logger object before their use. 
These messages are typically associated with unique keys for easy retrieval and logging 
throughout the application. 
The main purpose of predefined log messages is to standardize logging across different parts 
of the codebase and make it more convenient to log common events or errors without the need to 
write the entire message each time.

To predefine a log message, you should first create a log message as explained in previous part.

Second, you should use :py:func:`dorsa_logger.logger.defined_log_messages` method 
and pass the log message along with an optional string key. 
If no key is provided, the logger automatically generates a unique key for the message.
If the message is already defined, the method returns the corresponding key.

.. code-block:: python

    key = logger_obj.defined_log_messages.add_log_message(log_msg, key='my_message')

You can then pass this key to the :py:func:`dorsa_logger.logger.create_new_log` method for logging.

.. code-block:: python

   logger_obj.create_new_log(message=log_msg)

.. code-block:: console

   $ ERROR - 2023-08-07-16-53-39 - anonymous : (ERR000) An error occurred
    -----------------------------------------------------------------------------------

To find the key associated with a predefined message, you can use
:py:func:`dorsa_logger.defined_log_messages.get_defined_log_key` method.

.. code-block:: python

    key = logger_obj.defined_log_messages.get_defined_log_key(log_msg)

To find the message associated with a given key, you can use 
:py:func:`dorsa_logger.defined_log_messages.get_defined_log_message` method.

.. code-block:: python

    message = logger_obj.defined_log_messages.get_defined_log_message(key)

To delete a predefined message, you can use 
:py:func:`dorsa_logger.defined_log_messages.delete_defined_log` method.

.. code-block:: python

    logger_obj.defined_log_messages.delete_defined_log(key)
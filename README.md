
# Logger

Logger is a Python module that provides a logging functionality with various configuration options. It allows you to log messages to both a file and the console, with different log levels and formats.

## Installation

◌Instructions:  
 1-pip install dorsa_logger  
 2-clone repository

## Documentaion
Sphinx documents are available in docs folder.
To see that open index.html in docs/build/html folder.

## Quick Start

To use the Logger module, follow these steps:

1.  Import the module: 
``` python
import dorsa_logger
```

2.  Create a `logger` object:
``` python
logger_obj = dorsa_logger.logger(
	main_folderpath="./app_logs",
	date_type=dorsa_logger.date_types.AD_DATE,
	date_format=dorsa_logger.date_formats.YYMMDD,
	time_format=dorsa_logger.time_formats.HHMMSS,
	file_level=dorsa_logger.log_levels.DEBUG,
	console_level=dorsa_logger.log_levels.DEBUG,
	console_print=True,
	current_username="admin",
	line_seperator='-'
)
```

3. Define a log message:
```python
log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, message="An error occurred", code="ERR000")
```

4.  Start logging messages:
``` python
logger_obj.create_new_log(message=log_msg)
```

5  Customize the logger configuration by changing the parameters passed to the `logger` constructor or using setter functions of logger object. For example, you can set a different main folder path, log levels, date and time formats, and more. for more detailes see [Example1](Examples/example1.py)

## Predefined Log Messages

You can define and use predefined log messages. To define a log message, follow these steps:
1.  Define a log message:
```python
key = logger_obj.defined_logs.add_log_message(log_msg, key='MY_KEY')
```
If you don't define any key, key is assigned automatically. 

2. logging with defined messages:
```python
logger_obj.create_new_log(message=key)
```
This will log the predefined message with the specified log level. for more detailes see [Example2](Examples/example2.py)

## Decorators to log a function

You can use decorators to log start, end or exceptions of a function. To use decorators, define your function as follow:
```python
@logger_obj.function_start_decorator()
@logger_obj.function_exception_decorator()
@logger_obj.function_end_decorator()
def  test(a, b):
	res = a*b + 20 + a**b
	print('In the function')
	raise  Exception('This is a fake exception')
	return res
```
After calling function the start, exceptions and end will be logged with defined messages. you can also specify your own message. for more detailes see [Example3](Examples/example3.py)

## Log Levels

The following log levels are available:

-   DEBUG (level 10)
-   INFO (level 20)
-   WARNING (level 30)
-   ERROR (level 40)
-   CRITICAL (level 50)
-   EXCEPTION (level 60)

You can use these log levels when logging messages to specify the severity of the message.

## Date Types

The following date types are available:

-   SOLAR_DATE
- AD_DATE

## Date Formats

The following date formats are available:

- MMDDYY
- DDMMYY
- YYMMDD

## Time Formats

The following date formats are available:

- HHMM
- HHMMSS
- HHMMSSMM



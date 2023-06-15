from ast import keyword
from distutils.debug import DEBUG
from email import message
import logging
import os
from tkinter import EXCEPTION
from tkinter.messagebox import NO
from typing import overload
from persiantools.jdatetime import JalaliDate
import datetime
from multipledispatch import dispatch
from typing import overload


class ErrorAndWarnings:
    """Contains static methods that return error and warning messages for logging."""

    @staticmethod
    def undefined_date_type():
        """Returns an error message indicating that the given date type is undefined."""
        return "The given date type is undefined. select a type from date_types class."

    @staticmethod
    def undefined_date_format():
        """Returns an error message indicating that the given date format is undefined."""
        return "The given date format is undefined. select a format from date_formats class."

    @staticmethod
    def undefined_time_format():
        """Returns an error message indicating that the given time format is undefined."""
        return "The given time format is undefined. select a format from time_formats class."

    @staticmethod
    def undefined_log_level():
        """Returns an error message indicating that the given log level is undefined."""
        return "The given log level is undefined. select a level from log_levels class."

    @staticmethod
    def incorrect_message_datatype():
        """Returns an error message indicating that the given message must be an instance of the log_message class."""
        return "The given message must be an instance of the log_message class."

    @staticmethod
    def incorrect_key_datatype():
        """Returns an error message indicating that the given key must be a string."""
        return "The given key must be a string."

    @staticmethod
    def defined_key():
        """Returns a warning message indicating that the given key is already defined."""
        return "The given key is defined."

    @staticmethod
    def incorrect_input_datatype():
        """Returns an error message indicating that the given input must be a string or an instance of the log_message class."""
        return "The given input must be string or an instance of log_message class."

    @staticmethod
    def undefined_key():
        """Returns an error message indicating that the given key is undefined."""
        return "The given key is undefined."

class date_types:
    """Defines different types of date formats."""

    SOLAR_DATE = 'Solar'
    AD_DATE = 'AD'

class date_formats:
    """Defines different formats for representing dates."""

    MMDDYY = "MMDDYY"
    DDMMYY = "DDMMYY"
    YYMMDD = "YYMMDD"

class time_formats:
    """Defines different formats for representing time."""

    HHMM = "HHMM",
    HHMMSS = "HHMMSS",
    HHMMSSMM = "HHMMSSMM"

class log_levels:
    """Defines different log levels."""

    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    EXCEPTION = 60

class date:
    """Represents a date object with various date-related operations.

    Attributes:
        year (int): The year component of the date.
        month (int): The month component of the date.
        day (int): The day component of the date.
        date_type (str): The type of date being used (AD_DATE or SOLAR_DATE).
        date_format (str): The format of the date (YYMMDD, DDMMYY, or MMDDYY).
    """

    def __init__(self, date_type: str = date_types.AD_DATE, date_format: str = date_formats.YYMMDD) -> None:
        """Initialize the date object with the specified date type and format.

        Args:
            date_type (str): The type of date to be used (AD_DATE or SOLAR_DATE).
            date_format (str): The format of the date (YYMMDD, DDMMYY, or MMDDYY).
        """
        self.year = 0
        self.month = 0
        self.day = 0

        self.set_date_type(date_type)
        self.set_date_format(date_format)

    def set_date_type(self, type: str) -> None:
        """Set the date type for the date object.

        Args:
            type (str): The type of date (AD_DATE or SOLAR_DATE).
        
        Raises:
            AssertionError: If the given type is undefined.
        """
        types = [v for k, v in vars(date_types).items() if not(k.startswith('__'))]
        assert type in types, ErrorAndWarnings.undefined_date_type()
        self.date_type = type

    def set_date_format(self, format: str) -> None:
        """Set the date format for the date object.

        Args:
            format (str): The format of the date (YYMMDD, DDMMYY, or MMDDYY).
        
        Raises:
            AssertionError: If the given format is undefined.
        """
        formats = [v for k, v in vars(date_formats).items() if not(k.startswith('__'))]
        assert format in formats, ErrorAndWarnings.undefined_date_format()
        self.date_format = format

    def update_date(self) -> None:
        """Update the date attributes based on the selected date type.

        If the date type is SOLAR_DATE, the attributes will be updated with the current Jalali date.
        If the date type is AD_DATE, the attributes will be updated with the current Gregorian date.
        """
        if self.date_type == date_types.SOLAR_DATE:
            self.day = JalaliDate.today().day
            self.month = JalaliDate.today().month
            self.year = JalaliDate.today().year

        elif self.date_type == date_types.AD_DATE:
            self.day = datetime.datetime.today().date().day
            self.month = datetime.datetime.today().date().month
            self.year = datetime.datetime.today().date().year

    def get_date_string(self, sep: str = '-') -> str:
        """Get the date string representation based on the selected date format.

        Args:
            sep (str): The separator to be used between date components (default is '-').

        Returns:
            str: The date string representation.

        Raises:
            AssertionError: If the date type or format is undefined.
        """
        self.update_date()

        if self.day < 10:
            day = '0' + str(self.day)
        else:
            day = str(self.day)

        if self.month < 10:
            month = '0' + str(self.month)
        else:
            month = str(self.month)

class time:
    """
    A class representing time.

    Args:
        time_format (str): The format of the time (default: 'HHMMSS').

    Attributes:
        time: The current time.
        time_format (str): The format of the time.

    Methods:
        set_time_format(format): Set the format of the time.
        update_time(): Update the current time.
        get_time_string(sep='-'): Get the time string representation.

    Example:
        >>> t = Time()
        >>> t.get_time_string()
        '15-30-45'

    """

    def __init__(self, time_format='HHMMSS'):
        self.time = None
        self.set_time_format(time_format)

    def set_time_format(self, format):
        """
        Set the format of the time.

        Args:
            format (str): The format of the time.

        Raises:
            AssertionError: If the format is undefined.

        """
        formats = [v for k, v in vars(time_formats).items() if not(k.startswith('__'))]
        assert format in formats, ErrorAndWarnings.undefined_time_format()
        self.time_format = format

    def update_time(self):
        """
        Update the current time.

        """
        self.time = datetime.datetime.now()

    def get_time_string(self, sep='-'):
        """
        Get the time string representation.

        Args:
            sep (str): The separator for the time components (default: '-').

        Returns:
            str: The time string representation.

        """
        self.update_time()
        if self.time_format == time_formats.HHMM:
            time = str(self.time.strftime("%H{}%M".format(sep)))
        elif self.time_format == time_formats.HHMMSS:
            time = str(self.time.strftime("%H{}%M{}%S".format(sep, sep)))
        elif self.time_format == time_formats.HHMMSSMM:
            time = str(self.time.strftime("%H{}%M{}%S.%f".format(sep, sep)))

        return time

class log_message:
    def __init__(self, level: int, message: str, code: str = None) -> None:
        """
        Initializes a log message object with the specified level, message, and optional code.

        Args:
            level (int): The level of the log message.
            message (str): The log message.
            code (str, optional): The code associated with the log message. Defaults to None.
        """
        self.set_level(level)
        self.set_message(message)
        self.set_code(code)

    def set_level(self, level: int) -> None:
        """
        Sets the level of the log message.

        Args:
            level (int): The level of the log message.
        """
        self.level = level

    def set_message(self, message: str) -> None:
        """
        Sets the log message.

        Args:
            message (str): The log message.
        """
        self.message = message

    def set_code(self, code) -> None:
        """
        Sets the code associated with the log message.

        Args:
            code: The code associated with the log message.
        """
        self.code = code

    def get_message(self) -> str:
        """
        Returns the formatted log message.

        Returns:
            str: The formatted log message.
        """
        if self.code is not None:
            return '(%s) %s' % (self.code, self.message)
        else:
            return self.message

    def get_level(self) -> int:
        """
        Returns the level of the log message.

        Returns:
            int: The level of the log message.
        """
        return self.level

    def __eq__(self, __o: object) -> bool:
        """
        Compares the log message object with another object for equality.

        Args:
            __o (object): The object to compare with.

        Returns:
            bool: True if the log message objects are equal, False otherwise.
        """
        return self.level == __o.level and self.message == __o.message and self.code == __o.code

class logger:
    def __init__(
        self, 
        main_folderpath: str,
        date_type: str = date_types.AD_DATE,
        date_format: str = date_formats.YYMMDD,
        time_format: str = time_formats.HHMMSS,
        file_level: int = log_levels.DEBUG,
        console_level: int = log_levels.DEBUG,
        console_print: bool = True,
        current_username: str = "anonymous",
        line_seperator: str = '-',
    ) -> None:
        """
        Initializes a logger object with the specified configurations.

        Args:
            main_folderpath (str): The main folder path to store log files.
            date_type (str, optional): The type of date format. Defaults to date_types.AD_DATE.
            date_format (str, optional): The format of the date. Defaults to date_formats.YYMMDD.
            time_format (str, optional): The format of the time. Defaults to time_formats.HHMMSS.
            file_level (int, optional): The log level for file logging. Defaults to log_levels.DEBUG.
            console_level (int, optional): The log level for console logging. Defaults to log_levels.DEBUG.
            console_print (bool, optional): Whether to print log messages to the console. Defaults to True.
            current_username (str, optional): The current username for log messages. Defaults to "anonymous".
            line_seperator (str, optional): The separator character for log message lines. Defaults to '-'.
        """
        
        # Create logging object
        self.logger = logging.getLogger("Logger")
        self.logger.setLevel(log_levels.DEBUG)

        # Date
        self.date = date(date_type, date_format)

        # Time
        self.time = time(time_format)

        # set main folder path
        self.set_main_folderpath(main_folderpath)
        self.set_log_paths()
        self.__create_dailyfolder()

        # Create file handler
        self.file_handler = logging.FileHandler(filename=self.current_filepath, mode='w')
        self.set_file_level(file_level)
        self.file_format = logging.Formatter('%(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.file_format)
        self.logger.addHandler(self.file_handler)

        # Create console handler
        self.console_handler = logging.StreamHandler()
        self.set_console_level(console_level)
        self.console_format = logging.Formatter('%(levelname)s - %(message)s')
        self.console_handler.setFormatter(self.console_format)

        self.set_console_print(console_print)

        # set current username
        self.set_current_user(current_username)

        # set line seperator
        self.set_line_seperator(line_seperator)

        # private dict for store predefined log messages
        self.__defined_log_messages = {}
        self.__key = '0'

    def set_main_folderpath(self, main_folderpath) -> None:
        """
        Sets the main folder path for storing log files.

        Args:
            main_folderpath (str): The main folder path to store log files.

        Returns:
            None
        """

        self.main_folderpath = main_folderpath
        self.__create_mainfolder()

        if hasattr(self, 'file_handler'):
            self.__change_path()

    def set_log_paths(self) -> None:
        """
        Sets the log file paths based on the current date.

        Returns:
            None
        """
        self.daily_folderpath = self.date.get_date_string(sep='-')
        date_time = self.date.get_date_string(sep="-") + "-" + self.time.get_time_string(sep="-")
        self.current_filepath = os.path.join(self.main_folderpath, self.daily_folderpath, date_time+'.log')

    def set_console_print(self, console_print: bool) -> None:
        """
        Sets whether to print log messages to the console.

        Args:
            console_print (bool): Whether to print log messages to the console.

        Returns:
            None
        """
        self.console_print = console_print
        if self.console_print:
            self.logger.addHandler(self.console_handler)
        else:
            self.logger.removeHandler(self.console_handler)

    def set_file_level(self, level: int) -> None:
        """
        Sets the log level for file logging.

        Args:
            level (int): The log level for file logging.

        Returns:
            None
        """
        levels = [v for k, v in vars(log_levels).items() if not(k.startswith('__'))]
        assert level in levels, ErrorAndWarnings.undefined_log_level()
        self.file_level = level
        self.file_handler.setLevel(self.file_level)

    def set_console_level(self, level: int) -> None:
        """
        Sets the log level for console logging.

        Args:
            level (int): The log level for console logging.

        Returns:
            None
        """
        levels = [v for k, v in vars(log_levels).items() if not(k.startswith('__'))]
        assert level in levels, ErrorAndWarnings.undefined_log_level()
        self.console_level = level
        self.console_handler.setLevel(self.console_level)

    def set_current_user(self, current_username: str) -> None:
        """
        Sets the current username for log messages.

        Args:
            current_username (str): The current username for log messages.

        Returns:
            None
        """
        self.current_username = current_username

    def set_line_seperator(self, sep: str) -> None:
        """
        Sets the separator character for log message lines.

        Args:
            sep (str): The separator character for log message lines.

        Returns:
            None
        """
        self.line_seperator = sep

    def define_log(self, message: object, key: str = None) -> str:
        """
        Defines a log message with an optional key.

        Args:
            message (object): The log message to define.
            key (str, optional): The key to associate with the log message. Defaults to None.

        Returns:
            str: The key associated with the defined log message.
        """
        assert isinstance(message, log_message), ErrorAndWarnings.incorrect_message_datatype()
        if message in self.__defined_log_messages.values():
            key = [k for k, v in self.__defined_log_messages.items() if v == message]
            return key[0]

        if key is None:
            while self.__key in self.__defined_log_messages.keys(): self.__key = str(int(self.__key) + 1)
            key = self.__key
        else:
            assert isinstance(key, str), ErrorAndWarnings.incorrect_key_datatype()
            assert key not in self.__defined_log_messages.keys(), ErrorAndWarnings.defined_key()

        self.__defined_log_messages[key] = message
        return key

    def delete_defined_log(self, key: object) -> None:
        """
        Deletes a defined log message.

        Args:
            key (object): The key of the log message to delete.

        Returns:
            None
        """
        self.__defined_log_messages.pop(key)

    def function_start_decorator(self, keyword: object) -> None:
        """
        Decorator for logging the start of a function.

        Args:
            keyword (object): The keyword or log message to log at the start of the function.

        Returns:
            None
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                self.create_new_log(keyword=keyword)
                func(*args, **kwargs)
            return wrapper
        return decorator

    def function_exception_decorator(self, keyword: object, with_handling: bool) -> None:
        """
        Decorator for logging exceptions in a function.

        Args:
            keyword (object): The keyword or log message to log when an exception occurs.
            with_handling (bool): Whether to handle the exception or re-raise it.

        Returns:
            None
        """
        def decorator(fun):
            def wrapper(*args, **kwargs):
                try:
                    fun(*args, **kwargs)
                except Exception as e:
                   self.create_new_log(keyword=keyword)
                   if not with_handling:
                        raise e
            return wrapper
        return decorator

    def function_end_decorator(self, keyword: object) -> None:
        """
        Decorator for logging the end of a function.

        Args:
            keyword (object): The keyword or log message to log at the end of the function.

        Returns:
            None
        """
        def decorator(fun):
            def wrapper(*args, **kwargs):
                fun(*args, **kwargs)
                self.create_new_log(keyword=keyword)
            return wrapper
        return decorator

    def create_new_log(self, keyword: object) -> None:
        """
        Creates a new log message with the specified keyword.

        Args:
            keyword (object): The keyword or log message to log.

        Returns:
            None
        """
        assert isinstance(keyword, str) ^ isinstance(keyword, log_message), ErrorAndWarnings.incorrect_input_datatype()
        if isinstance(keyword, str):
            assert keyword in self.__defined_log_messages.keys(), ErrorAndWarnings.undefined_key()
            message = self.__defined_log_messages[keyword]
        else:
            message = keyword
        self.__create_new_log(message)

    def __create_new_log(self, message: object) -> None:
        """
        Creates a new log message with the specified log message object.

        Args:
            message (object): The log message object to log.

        Returns:
            None
        """
        # get date and time
        date_time = self.date.get_date_string(sep="-") + "-" + self.time.get_time_string(sep="-")

        # change log path on date change
        if self.daily_folderpath != self.date.get_date_string(sep='-'):
            self.__change_path()

        line_seperator = self.line_seperator * 120

        level = message.get_level()
        msg = message.get_message()

        # do log by levels
        # debug
        if level == log_levels.DEBUG:
            self.logger.debug(msg='%s - %s : %s\n%s' % (date_time, self.current_username, msg, line_seperator))
        #
        # info
        elif level == log_levels.INFO:
            self.logger.info(msg='%s - %s : %s\n%s' % (date_time, self.current_username, msg, line_seperator))
        #
        # warning
        elif level == log_levels.WARNING:
            self.logger.warning(msg='%s - %s : %s\n%s' % (date_time, self.current_username, msg, line_seperator))
        #
        # error
        elif level == log_levels.ERROR:
            self.logger.error(msg='%s - %s : %s\n%s' % (date_time, self.current_username, msg, line_seperator))
        #
        # critical error
        elif level == log_levels.CRITICAL:
            self.logger.critical(msg='%s - %s : %s\n%s' % (date_time, self.current_username, msg, line_seperator))
        #
        # exception error (with logging exception message)
        elif level == log_levels.EXCEPTION:
            self.logger.exception(msg='%s - %s : %s\n%s' % (date_time, self.current_username, msg, line_seperator))

    def __change_path(self) -> None:
        """
        Changes the log file path when the date changes.

        Returns:
            None
        """

        self.set_log_paths()
        self.__create_dailyfolder()

        self.logger.removeHandler(self.file_handler)

        self.file_handler = logging.FileHandler(filename=self.current_filepath, mode='w')
        self.set_file_level(self.file_level)
        self.file_format = logging.Formatter('%(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.file_format)
        self.logger.addHandler(self.file_handler)

    def __create_mainfolder(self) -> None:
        """
        Creates the main folder for storing log files.

        Returns:
            None
        """

        # create if not exist
        if not os.path.exists(self.main_folderpath):
            os.mkdir(self.main_folderpath)

    def __create_dailyfolder(self) -> None:
        """
        Creates the daily folder for storing log files.

        Returns:
            None
        """

        # create if not exist
        if not os.path.exists(os.path.join(self.main_folderpath, self.daily_folderpath)):
            os.mkdir(os.path.join(self.main_folderpath, self.daily_folderpath))


if __name__ == "__main__":
    # d = date(date_type=date_types.AD_DATE, date_format=date_formats.YYMMDD)
    # print(d.get_date_string())

    # d.set_date_type(date_types.SOLAR_DATE)
    # print(d.get_date_string())

    # d.set_date_format(date_formats.DDMMYY)
    # print(d.get_date_string())

    # d.set_date_format(date_formats.MMDDYY)
    # print(d.get_date_string())

    # d.set_date_type(date_types.AD_DATE)
    # print(d.get_date_string(sep='/'))

    # t = time(time_format=time_formats.HHMM)
    # print(t.get_time_string())

    # t.set_time_format(format=time_formats.HHMMSS)
    # print(t.get_time_string())

    # t.set_time_format(format=time_formats.HHMMSSMM)
    # print(t.get_time_string(sep=':'))

    l = logger(main_folderpath='./app_logs', 
            date_type=date_types.SOLAR_DATE,
            time_format=time_formats.HHMMSSMM,
            )

    # l.create_new_log(log_message(message='Test1', level=log_levels.DEBUG))
    # l.set_console_print(False)
    # l.set_file_level(log_levels.ERROR)
    # l.create_new_log(log_message(message='Test2', code='002', level=log_levels.DEBUG))
    # l.set_console_print(True)
    # l.set_console_level(log_levels.INFO)
    # l.create_new_log(log_message(message='Test3', level=log_levels.DEBUG))

    # try:
    #     a = 2/0
    # except:
    #    l.create_new_log(log_message(message='Test4', level=log_levels.EXCEPTION)) 

    # l.set_main_folderpath('./LOGS')
    # l.create_new_log('Test2', level=log_levels.DEBUG)


    # k = l.define_log(log_message(message='Test2', level=log_levels.DEBUG), key='2')
    # print(k)
    # k = l.define_log(log_message(message='Test3', level=log_levels.DEBUG), key="reyhane123")
    # print(k)
    # k = l.define_log(log_message(message='Test4', level=log_levels.DEBUG))
    # print(k)

    # l.create_new_log(log_message(message='Test1', level=log_levels.DEBUG))
    # l.create_new_log(keyword=log_message(message='Test1', level=log_levels.DEBUG))
    # l.create_new_log("reyhane123")
    # l.delete_defined_log('2')
    # l.create_new_log(keyword='2')

    @l.function_start_decorator(log_message(message='START', level=log_levels.DEBUG))
    @l.function_end_decorator(log_message(message='END', level=log_levels.DEBUG))
    @l.function_exception_decorator(log_message(message='EXCEPTION', level=log_levels.EXCEPTION), with_handling=True)
    def test(a, b):
        res = a*b + 20 + a**b
        print('In the function')
        raise Exception('this is a fake exception')
        return res

    test(5, 1)




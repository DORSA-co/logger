from distutils.debug import DEBUG
from email import message
import logging
import os
from tkinter import EXCEPTION
from persiantools.jdatetime import JalaliDate
import datetime
import time as ttt


class date_types:
    SOLAR_DATE = 'Solar'
    AD_DATE = 'AD'

class date_formats:
    MMDDYY = "MMDDYY"
    DDMMYY = "DDMMYY"
    YYMMDD = "YYMMDD"

class time_formats:
    HHMM = "HHMM",
    HHMMSS = "HHMMSS",
    HHMMSSMM = "HHMMSSMM"

class log_levels:
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    EXCEPTION = 60

class date:
    def __init__(self, date_type: str = date_types.AD_DATE, date_format: str = date_formats.YYMMDD) -> None:
        self.year = 0
        self.month = 0
        self.day = 0

        self.set_date_type(date_type)
        self.set_date_format(date_format)

    def set_date_type(self, type: str) -> None:
        types = [v for k, v in vars(date_types).items() if not(k.startswith('__'))]
        assert type in types, "Given date type is undefined."
        self.date_type = type

    def set_date_format(self, format: str) -> None:
        formats = [v for k, v in vars(date_formats).items() if not(k.startswith('__'))]
        assert format in formats, "Given date format is undefined."
        self.date_format = format

    def update_date(self) -> None:
        if self.date_type == date_types.SOLAR_DATE:
            self.day = JalaliDate.today().day
            self.month = JalaliDate.today().month
            self.year = JalaliDate.today().year

        elif self.date_type == date_types.AD_DATE:
            self.day = datetime.datetime.today().date().day
            self.month = datetime.datetime.today().date().month
            self.year = datetime.datetime.today().date().year

    def get_date_string(self, sep='-') -> str:
        self.update_date()

        if self.day < 10:
            day = '0' + str(self.day)
        else:
            day = str(self.day)

        if self.month < 10:
            month = '0' + str(self.month)
        else:
            month = str(self.month)

        year = str(self.year)

        if self.date_format == date_formats.YYMMDD:
            date = '%s%s%s%s%s' % (year, sep, month, sep, day)
        elif self.date_format == date_formats.DDMMYY:
            date = '%s%s%s%s%s' % (day, sep, month, sep, year)
        elif self.date_format == date_formats.MMDDYY:
            date = '%s%s%s%s%s' % (month, sep, day, sep, year)

        return date

class time:
    def __init__(self, time_format: str = time_formats.HHMMSS) -> None:
        self.time = None
        self.set_time_format(time_format)

    def set_time_format(self, format: str) -> None:
        formats = [v for k, v in vars(time_formats).items() if not(k.startswith('__'))]
        assert format in formats, "Given time format is undefined."
        self.time_format = format

    def update_time(self) -> None:
        self.time = datetime.datetime.now()

    def get_time_string(self, sep='-') -> str:
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
        self.set_level(level)
        self.set_message(message)
        if code:
            self.set_code(code)

    def set_level(self, level: int) -> None:
        self.level = level

    def set_message(self, message: str) -> None:
        self.message = message

    def set_code(self, code) -> None:
        self.code = code

    def get_message(self) -> str:
        if hasattr(self, 'code'):
            return '(%s) %s' % (self.code, self.message)
        else:
            return self.message

    def get_level(self) -> int:
        return self.level

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

        self.__defined_log_messages = {}

    def set_main_folderpath(self, main_folderpath):
        self.main_folderpath = main_folderpath
        self.__create_mainfolder()

        if hasattr(self, 'file_handler'):
            self.__change_path()

    def set_log_paths(self) -> None:
        self.daily_folderpath = self.date.get_date_string(sep='-')
        date_time = self.date.get_date_string(sep="-") + "-" + self.time.get_time_string(sep="-")
        self.current_filepath = os.path.join(self.main_folderpath, self.daily_folderpath, date_time+'.log')

    def set_console_print(self, console_print: bool) -> None:
        self.console_print = console_print
        if self.console_print:
            self.logger.addHandler(self.console_handler)
        else:
            self.logger.removeHandler(self.console_handler)

    def set_file_level(self, level: int):
        levels = [v for k, v in vars(log_levels).items() if not(k.startswith('__'))]
        assert level in levels, "Given log level is undefined."
        self.file_level = level
        self.file_handler.setLevel(self.file_level)

    def set_console_level(self, level: int):
        levels = [v for k, v in vars(log_levels).items() if not(k.startswith('__'))]
        assert level in levels, "Given log level is undefined."
        self.console_level = level
        self.console_handler.setLevel(self.console_level)

    def set_current_user(self, current_username: str) -> None:
        """This function sets the input username as the current user.

        :param current_username: Current username that logged in the app
        :type current_username: str
        """
    
        self.current_username = current_username

    def set_line_seperator(self, sep: str) -> None:
        self.line_seperator = sep

    def create_new_log(self, log_message: object):
        """This function creates a log with input message and log level.

        :param message: The log message, defaults to 'nothing'
        :type message: str, optional
        :param level: The log level (in int), an int value between [0, 5] specifying the log level.
        :type level: int, optional
        """
        
        # get date and tme
        date_time = self.date.get_date_string(sep="-") + "-" + self.time.get_time_string(sep="-")

        # change log path on date change
        if self.daily_folderpath != self.date.get_date_string(sep='-'):
            self.__change_path()

        line_seperator = self.line_seperator * 120

        level = log_message.get_level()
        message = log_message.get_message()

        # do log by levels
        # debug
        if level == log_levels.DEBUG:
            self.logger.debug(msg='%s - %s : %s\n%s' % (date_time, self.current_username, message, line_seperator))
        #
        # info
        elif level == log_levels.INFO:
            self.logger.info(msg='%s - %s : %s\n%s' % (date_time, self.current_username, message, line_seperator))
        #
        # warning
        elif level == log_levels.WARNING:
            self.logger.warning(msg='%s - %s : %s\n%s' % (date_time, self.current_username, message, line_seperator))
        #
        # error
        elif level == log_levels.ERROR:
            self.logger.error(msg='%s - %s : %s\n%s' % (date_time, self.current_username, message, line_seperator))
        #
        # critical error
        elif level == log_levels.CRITICAL:
            self.logger.critical(msg='%s - %s : %s\n%s' % (date_time, self.current_username, message, line_seperator))
        #
        # exception error (with logging exception message)
        elif level == log_levels.EXCEPTION:
            self.logger.exception(msg='%s - %s : %s\n%s' % (date_time, self.current_username, message, line_seperator))

    def define_log(self, key: object, log_message: object):
        assert key not in self.__defined_log_messages.keys(), 'Given key is defined.'

        self.__defined_log_messages[key] = log_message

    def delete_defined_log(self, key: object):
        self.__defined_log_messages.pop(key)

    def get_decorator(self):
        pass

    def __change_path(self):
        """This function is used to change log file path on date change (end of the day).
        """

        self.set_log_paths()
        self.__create_dailyfolder()

        self.logger.removeHandler(self.file_handler)

        self.file_handler = logging.FileHandler(filename=self.current_filepath, mode='w')
        self.set_file_level(self.file_level)
        self.file_format = logging.Formatter('%(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.file_format)
        self.logger.addHandler(self.file_handler)

    def __create_mainfolder(self):
        """This function creates the main folder to store log files.
        """

        # create if not exist
        if not os.path.exists(self.main_folderpath):
            os.mkdir(self.main_folderpath)

    def __create_dailyfolder(self):
        """This function creates day by day folders in the main folder, to storing the log files of each day.
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

    l.__defined_log_messages = {}#(log_message(message='Test1', level=log_levels.DEBUG))



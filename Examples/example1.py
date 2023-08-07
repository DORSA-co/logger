import sys
sys.path.append('./')
sys.path.append('../')
import dorsa_logger

if __name__ == "__main__":
    # Quick Start
    logger_obj = dorsa_logger.logger(
        main_folderpath="./app_logs",
        date_type=dorsa_logger.date_types.AD_DATE,
        date_format=dorsa_logger.date_formats.YYMMDD,
        time_format=dorsa_logger.time_formats.HHMMSS,
        file_level=dorsa_logger.log_levels.DEBUG,
        console_level=dorsa_logger.log_levels.DEBUG,
        console_print=True,
        # current_username="admin",
        line_seperator='-'
    )

    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR000")
    logger_obj.create_new_log(message=log_msg)

    # change main folder
    logger_obj.set_main_folderpath('./app_logs2')
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR001")
    logger_obj.create_new_log(message=log_msg)

    # change date type
    logger_obj.date.set_date_type(dorsa_logger.date_types.SOLAR_DATE)
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR002")
    logger_obj.create_new_log(message=log_msg)

    # change date format
    logger_obj.date.set_date_format(dorsa_logger.date_formats.MMDDYY)
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR003")
    logger_obj.create_new_log(message=log_msg)

    # change time format
    logger_obj.time.set_time_format(dorsa_logger.time_formats.HHMMSSMM)
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR004")
    logger_obj.create_new_log(message=log_msg)

    # change file level
    logger_obj.set_file_level(dorsa_logger.log_levels.CRITICAL)
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR005")
    logger_obj.create_new_log(message=log_msg)

    # change console level
    logger_obj.set_console_level(dorsa_logger.log_levels.EXCEPTION)
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR006")
    logger_obj.create_new_log(message=log_msg)

    # unset console print
    logger_obj.set_file_level(dorsa_logger.log_levels.DEBUG)
    logger_obj.set_console_level(dorsa_logger.log_levels.DEBUG)
    logger_obj.set_console_print(False)
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR007")
    logger_obj.create_new_log(message=log_msg)

    # set current user
    logger_obj.set_current_user('admin2')
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR008")
    logger_obj.create_new_log(message=log_msg)

    # set line seperator
    logger_obj.set_line_seperator('*')
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, text="An error occurred", code="ERR009")
    logger_obj.create_new_log(message=log_msg)
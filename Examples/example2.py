import sys
sys.path.append('./')
sys.path.append('../')
import dorsa_logger

if __name__ == "__main__":
    # Define Logs
    logger_obj = dorsa_logger(
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

    # Define log message with given key
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, message="An error occurred", code="ERR001")
    key1 = logger_obj.define_log(log_msg, key='MY_KEY')
    logger_obj.create_new_log(message=key1)
    
    # Define log message with automatic key
    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR, message="An error occurred", code="ERR000")
    key2 = logger_obj.define_log(log_msg)
    logger_obj.create_new_log(message=key2)
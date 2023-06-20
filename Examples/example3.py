import sys
sys.path.append('./')
sys.path.append('../')
import dorsa_logger

if __name__ == "__main__":
    # Use Decorators
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
    
    @logger_obj.function_start_decorator()#dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO, message="Function started.", code="ERR000"))
    @logger_obj.function_exception_decorator()#dorsa_logger.log_message(level=dorsa_logger.log_levels.EXCEPTION, message="An exception occurred.", code="ERR002"), with_handling=True)
    @logger_obj.function_end_decorator()#dorsa_logger.log_message(level=dorsa_logger.log_levels.INFO, message="Function finished.", code="ERR001"))
    def test(a, b):
        res = a*b + 20 + a**b
        print('In the function')
        raise Exception('This is a fake exception')
        return res

    res = test(5, 1)
    print(res)

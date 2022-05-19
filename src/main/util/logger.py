import logging


def get_logger(name_logger: str, file: str) -> logging.Logger:
    format_log_output = (
        "%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d"
    )

    log = logging.getLogger(name=name_logger)
    log.setLevel(logging.INFO)
    if not log.handlers:
        log.addHandler(logger_stream_handler(file, format_log_output))
    log.propagate = False

    return log


def logger_stream_handler(file: str, format_log_output: str) -> logging.Handler:
    fh = logging.FileHandler(file, encoding='utf-8')
    fh.setFormatter(logging.Formatter(format_log_output))

    return fh


logger_error = get_logger('Error', r'logs_error')
logger_info = get_logger('Info', r'logs_info')

import logging


def function_to_log():
    logging.basicConfig(
        filename="logging.log", filemode="w", format="%(asctime)s %(message)s"
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("INFO")
    logger.error("ERROR")
    logger.warning("WARNING")
    logger.critical("CRITICAL")
    logger.debug("DEBUG")


if __name__ == "__main__":
    function_to_log()

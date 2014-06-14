"""This is my Doc String this is a library of shared code."""

import logging 

def get_logger():

    """Function to build a logger object.

    :returns: Logger Object.

    """
    logger = logging.getLogger(__name__)

    # Build Steam output formater
    stream_formatter = logging.Formatter("%(filename)s | %(funcName)s |"
                                        "%(lineno)d   |  %(levelname)s |"
                                        "%(message)s")

    # Build Stream Handler (for output to stdout)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel("DEBUG")
    stream_handler.setFormatter(stream_formatter)

    #Add Handler to logger
    
    logger.addHandler(stream_handler)
    return logger




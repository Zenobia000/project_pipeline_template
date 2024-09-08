# logging_config.py
import logging
import os


def setup_logger(name, filename='test.log', output_dir='..\\data\\logs'):
    logger = logging.getLogger(name)
    # print(f"Logger has handlers: {logger.hasHandlers()}")  # This will show whether handlers are attached

    # Check if the logger already has handlers
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        # Define output format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Set up console output
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        # Set up file output
        output_path = os.path.join(output_dir, filename)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        fh = logging.FileHandler(output_path)
        fh.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger

# 在需要使用 logger 的地方使用 setup_logger 函數



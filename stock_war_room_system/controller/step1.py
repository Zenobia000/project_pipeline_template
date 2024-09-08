import logging
from configparser import ConfigParser
from stock_war_room_system.controller.step_template import Step

# from pipeline_step import PipelineStep
from stock_war_room_system.utils.logger import setup_logger

# Configuration Management
config = ConfigParser()
config.read("config.ini")

# Environment Variables
from dotenv import load_dotenv

load_dotenv(".env")


# Example Pipeline Steps
class Step1(Step):
    def __init__(self, name, logger, log_level=logging.INFO):
        super().__init__(name)
        logger.setLevel(log_level)
        self.logger = logger

    def execute(self, data):
        self.logger.info(f"Executing {self.name}")
        # Process data
        print(data + " -> Step1")
        return data + " -> Step1"

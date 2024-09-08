from dotenv import load_dotenv
import logging
from stock_war_room_system.controller.step_template import Step
from stock_war_room_system.utils.extract_path import PathSetting

# Load environment variables from .env file
load_dotenv()

# Example Pipeline Steps
class CreateFolder(Step):
    def __init__(self, name, logger, log_level=logging.INFO):
        super().__init__(name)
        logger.setLevel(log_level)
        self.name = name
        self.logger = logger

    def execute(self, data=None):
        self.logger.info(f"Executing {self.name}")
        # Process data
        self._create_folder()

        return None

    def _create_folder(self):
        PathSetting().initialize_path()


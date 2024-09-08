import os
import logging
from configparser import ConfigParser
from concurrent.futures import ThreadPoolExecutor, as_completed

from stock_war_room_system.controller.pipeline_template import Pipeline
from stock_war_room_system.controller.step1 import Step1
from stock_war_room_system.controller.step2 import Step2
from stock_war_room_system.utils.logger import setup_logger
from stock_war_room_system.controller.pipeline import Pipeline

filename = "test.log"
output_dir = "..\\data\\logs"

# Set up different loggers
main_logger = setup_logger("main_logger", filename=filename, output_dir=output_dir)
main_logger.setLevel(logging.INFO)

steps_logger = setup_logger("steps_logger", filename=filename, output_dir=output_dir)
pipeline_logger = setup_logger(
    "pipeline_logger", filename=filename, output_dir=output_dir
)


# Dynamic Pipeline Execution with Parallelism
def run_pipeline(pipeline, data):
    with ThreadPoolExecutor() as executor:
        future = executor.submit(pipeline.run, data)
        return future.result()


# Main Program

if __name__ == "__main__":
    main_logger.info("Program started")

    # Instantiate pipeline steps
    Step1 = Step1("step1_demo", steps_logger, log_level=logging.INFO)

    # Additional steps can be added here
    Step2 = Step2("step2_demo", steps_logger, log_level=logging.INFO)

    # Define pipeline
    pipeline = Pipeline([Step1, Step2], pipeline_logger, log_level=logging.INFO)
    # Multiple pipelines can be defined similarly

    # Run pipeline
    input_data = "go go start"
    result = run_pipeline(pipeline, input_data)

    main_logger.info(f"Pipeline result: {result}")

    main_logger.info("Program finished")

    # Additional code for managing multiple pipelines, handling errors, etc.

import logging

# Pipeline Class
class Pipeline:
    def __init__(self, steps, logger, log_level=logging.INFO):
        logger.setLevel(log_level)
        self.steps = steps
        self.logger = logger

    def run(self, data):
        self.logger.info("Pipeline execution started")
        for step in self.steps:
            data = step.execute(data)
        self.logger.info("Pipeline execution finished")
        return data


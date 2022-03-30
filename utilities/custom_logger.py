import logging
from utilities import config


class LogGen():
	@staticmethod
	def loggen():
		conf = config.loadConfig()

		logging.basicConfig(
			filename="log/automation.log",
			format='%(asctime)s: %(levelname)s: %(message)s',
			datefmt=conf.get("dateFormat")
		)
		logger = logging.getLogger()
		logger.setLevel(logging.INFO)

		return logger

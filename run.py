from argparse import ArgumentParser
from datetime import datetime
from os import (
	getcwd as getCwd,
	environ,
	pathsep
)
from os.path import join as pathJoin
from platform import system as systemPlatform
from sys import exit
from utilities import config


# We add drivers to path so Selenium can see them
operatingSystem = systemPlatform().lower()
operatingSystem = "mac" if operatingSystem == "darwin" else operatingSystem
environ["PATH"] += pathsep + pathJoin(getCwd(), "drivers", operatingSystem)


def getBrowsersForTest(conf, userPassedBrowsers):
	possibleBroswers = conf.get("broswerMapping")
	userPassedBrowsers = userPassedBrowsers.split(",") if userPassedBrowsers else None

	if not userPassedBrowsers:
		return possibleBroswers

	browsers = {}
	for browser, options in possibleBroswers.items():
		if browser in userPassedBrowsers:
			browsers[browser] = options

	if not browsers:
		quitWithUsage("Invalid broswer passed.")
	else:
		return browsers


def quitWithUsage(msg):
	exit(
		"{}\n"
		"usage: python run.py -p [file|path] -b [browser1, browser2, etc..]\n".format(msg)
	)


if __name__ == "__main__":
	conf = config.loadConfig()

	parser = ArgumentParser(description="QA Automation Test Suite")
	parser.add_argument("-p", "--path", required=False, help="Path to test file")
	parser.add_argument("-b", "--browsers", required=False, help="Browsers to use")
	args = parser.parse_args()

	if args.path:
		files = pathJoin(conf.get("rootTestCaseDir"), args.path)
	else:
		files = conf.get("rootTestCaseDir")

	now = datetime.now().strftime(conf.get("dateFormat"))
	browsers = getBrowsersForTest(conf, args.browsers)
	# reportFile = pathJoin(conf.get("rootHtmlDir"), str(browsers) + " - test-{}.html".format(now)).replace(" ", "_")
	#reportFile = pathJoin(conf.get("rootHtmlDir"), "test-{}.html".format(now)).replace(" ", "_")

	for browser, options in browsers.items():
		if options.get("driver") == "chromedriver-87":
			browser_name = "Chrome-87"
		elif options.get("driver") == "chromedriver-79":
			browser_name = "Chrome-79"
		elif options.get("driver") == "geckodriver":
			browser_name = "Firefox"
		elif options.get("driver") == "safaridriver":
			browser_name = "Safari"

		reportFile = pathJoin(conf.get("rootHtmlDir"), browser_name + "-TestReport-{}.html".format(now))

		from pytest import main as runPytest
		runPytest([
			"-s", "-v",
			"--browser", options.get("browser"),
			"--driver", options.get("driver"),
			"--binary", pathJoin(getCwd(), "binaries", operatingSystem, options.get("binary") or ""),
			"--html", reportFile,
			files
		])

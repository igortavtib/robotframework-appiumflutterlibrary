# -*- coding: utf-8 -*-

from AppiumFlutterLibrary.keywords import *
from AppiumFlutterLibrary.version import VERSION

__version__ = VERSION

class AppiumFlutterLibrary(
	_ApplicationManagementKeyWords,
	_ElementKeywords,
	_LoggingKeywords,
	_ScreenKeywords,
	_RunOnFailureKeyWords,
	_WaintingKeywords,
):
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	ROBOT_LIBRARY_VERSION = VERSION

	def __init__(self, timeout=5, run_on_failure='Capture Page Screenshot'):
		for base in AppiumFlutterLibrary.__bases__:
			base.__init__(self)
		self.set_appium_timeout(timeout)
		self.register_keyword_to_run_on_failure(run_on_failure)
# -*- coding: utf-8 -*-

from AppiumFlutterLibrary.keywords import *
from AppiumFlutterLibrary.version import VERSION

__version__ = VERSION

class AppiumFlutterLibrary(
	_ApplicationManagementKeyWords,
	_ElementKeywords,
	_KeyeventsKeywords,
	_LoggingKeywords,
	_ScreenKeywords,
	_RunOnFailureKeyWords,
	_TouchKeywords,
	_WaintingKeywords,
):
	""" AppiumFlutterLibrary is a flutter testing library for Robot Framework
	that uses FlutterDriver class and appium to test flutter mobile apps.

	 The lib was inspired by AppiumLibrary.

	== Flutter Finder ==

	 All keywords that needs to interact with and element needs to find this element
	first. For this prupose we have the locators that comunicate with FlutterDriver
	findBy functions.

	== Locators ==

	 By default when passing a locator without a specifier the library will get this
	locator as a FlutterDriver key. If you want to use a different locator you need to
	set the specifier.

	Example:

	| Click Element		input-button
	| Click Element 	text=Input

	 Avalible locators:

	| *Locator*    | *Description*              |
	| key(default) | FlutterDriver element key. |
	| text         | Element text.              |
	| semantics    | Element semantics label    |
    | tooltip      | Element tooltip message    |
	| type         | Element type               |
	"""
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	ROBOT_LIBRARY_VERSION = VERSION

	def __init__(self, timeout=5, run_on_failure='Capture Page Screenshot'):
		"""AppiumFlutterLibrary can be imported with optional arguments.
        ``timeout`` is the default timeout used to wait for all waiting actions.
        It can be later set with `Set Appium Timeout`.

        ``run_on_failure`` specifies the name of a keyword (from any available
        libraries) to execute when a AppiumFlutterLibrary keyword fails.
        By default `Capture Page Screenshot` will be used to take a screenshot of the current page.
        Using the value `No Operation` will disable this feature altogether. See
        `Register Keyword To Run On Failure` keyword for more information about this
        functionality.
		
        Examples:
        | Library | AppiumFlutterLibrary | 10 | # Sets default timeout to 10 seconds                                                                             |
        | Library | AppiumFlutterLibrary | timeout=10 | run_on_failure=No Operation | # Sets default timeout to 10 seconds and does nothing on failure           |
        """
		for base in AppiumFlutterLibrary.__bases__:
			base.__init__(self)
		self.set_appium_timeout(timeout)
		self.register_keyword_to_run_on_failure(run_on_failure)
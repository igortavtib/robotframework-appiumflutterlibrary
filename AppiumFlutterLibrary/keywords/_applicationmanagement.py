# -*- coding: utf-8 -*-

import robot
from appium import webdriver
from AppiumFlutterLibrary.utils import ApplicationCache
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup
from appium.webdriver import Remote
from appium_flutter_finder import FlutterElement, FlutterFinder

class _ApplicationManagementKeyWords(KeywordGroup):
    def __init__(self):
        self._cache = ApplicationCache()
        self._timeout_in_secs = float(5)

    def close_application(self):
        self._cache.close()

    def open_application(self, remote_url, alias =None, **kwargs):
        desired_caps = kwargs
        application = Remote(str(remote_url), desired_caps)

        return self._cache.register(application, alias)

    def set_appium_timeout(self, seconds):
        old_timeout = self.get_appium_timeout()
        self._timeout_in_secs = robot.utils.timestr_to_secs(seconds)
        return old_timeout
    
    def get_appium_timeout(self):
        """Gets the timeout in seconds that is used by various keywords.

        See `Set Appium Timeout` for an explanation."""
        return robot.utils.secs_to_timestr(self._timeout_in_secs)

    # Private

    def _current_application(self):
        if not self._cache.current:
            raise RuntimeError('No application is open')
        return self._cache.current
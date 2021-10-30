# -*- coding: utf-8 -*-

import robot

from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup

class _ApplicationManagementKeyWords(KeywordGroup):
    def __init_(self):
        self._timeout_in_secs = float(5)

    def set_appium_timeout(self, seconds):
        old_timeout = self.get_appium_timeout()
        self._timeout_in_secs = robot.utils.timestr_to_secs(seconds)
        return old_timeout
    
    def get_appium_timeout(self):
        """Gets the timeout in seconds that is used by various keywords.

        See `Set Appium Timeout` for an explanation."""
        return robot.utils.secs_to_timestr(self._timeout_in_secs)
# -*- coding: utf-8 -*-

import robot
from appium import webdriver
from AppiumFlutterLibrary.utils import ApplicationCache
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup
from appium.webdriver import Remote
from appium_flutter_finder import FlutterElement, FlutterFinder

class _ApplicationManagementKeyWords(KeywordGroup):
    def __init__(self):
        self._cache = ApplicationCache
        self._timeout_in_secs = float(5)

    def open_application(self, remote_url, alias=None, **kwargs):
        desired_caps = kwargs
        application = Remote(str(remote_url), dict(desired_caps))

        return self._cache.register(application, alias)

    def login_to_application(self, remote_url, alias=None, **kwargs):
        driver = Remote('http://localhost:4723/wd/hub', dict(
            platformName='android',
            automationName='flutter',
            udid='emulator-5554',
            app='/home/igortavtib/Projects/robotframework-appiumflutterlibrary/app-prod-debug.apk'
        ))

        finder = FlutterFinder()

        key_finder = finder.by_value_key('input-user')
        input_element = FlutterElement(driver, key_finder)
        key_finder = finder.by_value_key('input-password')
        password_element = FlutterElement(driver, key_finder)
        driver.execute_script('flutter:waitFor', input_element)
        input_element.send_keys('igoraugsto@gmail.com')
        password_element.send_keys('senha123')

    def set_appium_timeout(self, seconds):
        old_timeout = self.get_appium_timeout()
        self._timeout_in_secs = robot.utils.timestr_to_secs(seconds)
        return old_timeout
    
    def get_appium_timeout(self):
        """Gets the timeout in seconds that is used by various keywords.

        See `Set Appium Timeout` for an explanation."""
        return robot.utils.secs_to_timestr(self._timeout_in_secs)
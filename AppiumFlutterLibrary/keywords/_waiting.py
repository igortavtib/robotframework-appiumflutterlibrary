import robot
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup
from AppiumFlutterLibrary.finder import ElementFinder


class _WaintingKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()

    def wait_for_element(self, locator, timeout=20):
        """ Uses FlutterDriver.waitFor() to wait for an element by the
        specified timeout duration.

        By default the timeout is 20 seconds.
        """
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        if timeout == 0:
            timeout=None
        try:
            if timeout is None:
                application.execute_script('flutter:waitFor', element)
            else:
                application.execute_script('flutter:waitFor', element, timeout)
        except Exception:
            raise AssertionError("Could not find element '%s' in %s seconds" % (locator, timeout))
    
    def wait_for_element_absent(self, locator, timeout=20):
        """Wait until element is absent. Uses FlutterDriver.waitForAbsent() to wait
        for an element be absent for the specified timeout duration.

        By default the timeout is 20 seconds.
        """
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        if timeout == 0:
            timeout=None
        try:
            if timeout is None:
                application.execute_script('flutter:waitForAbsent', element)
            else:
                application.execute_script('flutter:waitForAbsent', element, timeout)
        except Exception:
            raise AssertionError("Element '%s' still not absent in %s seconds" % (locator, timeout))
    



    def _format_timeout(self, timeout):
        timeout = robot.utils.timestr_to_secs(timeout) if timeout is not None else self._timeout_in_secs
        return robot.utils.secs_to_timestr(timeout)

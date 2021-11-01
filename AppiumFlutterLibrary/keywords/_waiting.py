import robot
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup
from appium_flutter_finder import FlutterElement, FlutterFinder


class _WaintingKeywords(KeywordGroup):
    def wait_for_element(self, locator, timeout=None, error=None):
        application = self._current_application()
        finder = FlutterFinder()
        key_finder = finder.by_value_key(locator)
        element = FlutterElement(application, key_finder)
        application.execute_script('flutter:waitFor', element)

    def _format_timeout(self, timeout):
        timeout = robot.utils.timestr_to_secs(timeout) if timeout is not None else self._timeout_in_secs
        return robot.utils.secs_to_timestr(timeout)

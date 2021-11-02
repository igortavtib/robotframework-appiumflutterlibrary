import robot
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup
from AppiumFlutterLibrary.finder import ElementFinder


class _WaintingKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()

    def wait_for_element(self, locator, timeout=None, error=None):
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        application.execute_script('flutter:waitFor', element)

    def _format_timeout(self, timeout):
        timeout = robot.utils.timestr_to_secs(timeout) if timeout is not None else self._timeout_in_secs
        return robot.utils.secs_to_timestr(timeout)

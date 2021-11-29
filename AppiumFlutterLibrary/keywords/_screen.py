from AppiumFlutterLibrary.finder import ElementFinder
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup

class _ScreenKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()

    def scroll_to_element(self, locator):
        """ Uses FlutterDriver.scrollIntoView() to scroll until element is visible.
        """
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        self._info(element)
        application.execute_script('flutter:scrollIntoView', element, 0)
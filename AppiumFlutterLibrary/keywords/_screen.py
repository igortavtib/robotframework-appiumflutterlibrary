from _typeshed import ReadableBuffer
from AppiumFlutterLibrary.finder import ElementFinder
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup

class _ScreenKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()

    def scroll_to_element(self, locator):
        application = self._current_application()
        element = self._element_finder.find_by_key(application, locator)
        application.execute_script('flutter:scrollIntoView', element)
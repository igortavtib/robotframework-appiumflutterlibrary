import time
from .keywordgroup import KeywordGroup
from AppiumFlutterLibrary.finder import ElementFinder

def isstr(s):
    return isinstance(s, str)

class _ElementKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()

    def input_text(self, locator, text):
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        self._info("Typing text '%s' into component '%s'" % (text, locator))
        element.send_keys(text)

    def click_element(self, locator):
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        element.click()

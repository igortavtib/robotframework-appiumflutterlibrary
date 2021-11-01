import time
from robot.libraries.BuiltIn import BuiltIn
from .keywordgroup import KeywordGroup
from appium_flutter_finder import FlutterElement, FlutterFinder

try:
    basestring  # attempt to evaluate basestring

    def isstr(s):
        return isinstance(s, basestring)
except NameError:
    def isstr(s):
        return isinstance(s, str)

class _ElementKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = FlutterFinder()
        self._bi = BuiltIn()

    def input_text(self, locator, text):
        application = self._current_application()
        finder = FlutterFinder()
        key_finder = finder.by_value_key(locator)
        element = FlutterElement(application, key_finder)
        element.send_keys(text)


    def _element_find(self, locator):
        application = self._current_application()
        element = None
        if isstr(locator):
            _locator = locator
            _key_finder = self._element_finder.by_value_key(_locator)
            element = FlutterElement(application, _key_finder)

        return element

    def _is_visible(self, locator):
        element = self._element_find(locator)
        if element is not None:
            return element.is_displayed()
        return None
from appium.webdriver.webelement import WebElement
from .keywordgroup import KeywordGroup
from AppiumFlutterLibrary.finder import ElementFinder

def isstr(s):
    return isinstance(s, str)

class _ElementKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()

    def input_text(self, locator, text):
        element = self._find_element(locator)
        self._info("Typing text '%s' into component '%s'" % (text, locator))
        element.send_keys(text)

    def click_element(self, locator):
        element = self._find_element(locator)
        self._info("Clicking on element %s" % locator)
        element.click()

    def element_should_be_visible(self, locator):
        element = self._find_element(locator)
        if not self._is_visible(element):
            raise AssertionError("Element '%s' should be visible but not" % locator)

    def element_text_should_be(self, locator, text):
        element = self._find_element(locator)
        if element.text != text:
            raise AssertionError("Element '%s' text should be '%s' but is '%s'." %
                                    (locator, text, element.text))

    def _is_visible(self, element):
        application = self._current_application()
        application.execute_script('flutter:waitFor', element, 1)
        return 1

    def _find_element(self, locator):
        application = self._current_application()
        return self._element_finder.find(application, locator)

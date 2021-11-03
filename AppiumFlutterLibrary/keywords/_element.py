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
        if not self._find_element(locator).is_displayed():
            raise AssertionError("Element '%s' should be visible but not" % locator)
    
    def element_should_be_enabled(self, locator):
        if not self._find_element(locator).is_enabled():
            raise AssertionError("Element '%s' should be enabled but is not" % (locator))
        self._info("Element '%s' is enabled" % (locator))

    def element_should_be_disabled(self, locator):
        if self._find_element(locator).is_enabled():
            raise AssertionError("Element '%s' should be disabled but is not" % (locator))
        self._info("Element '%s' is disabled" % (locator))
        
    def element_value_should_be(self, locator, value):
        element = self._find_element(locator)
        if str(value) != str(element.get_attribute('value')):
            raise AssertionError("Element '%s' value should be '%s' but is '%s'." %
                                    (locator, value, element.get_attribute('value')))

    def element_text_should_be(self, locator, text):
        element = self._find_element(locator)
        if element.text != text:
            raise AssertionError("Element '%s' text should be '%s' but is '%s'." %
                                    (locator, text, element.text))

    def _find_element(self, locator):
        application = self._current_application()
        return self._element_finder.find(application, locator)

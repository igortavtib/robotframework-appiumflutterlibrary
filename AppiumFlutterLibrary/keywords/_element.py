from appium.webdriver.webelement import WebElement
from .keywordgroup import KeywordGroup
from AppiumFlutterLibrary.finder import ElementFinder

def isstr(s):
    return isinstance(s, str)

class _ElementKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()

    def input_text(self, locator, text):
        """Input text into the specified element.

        If the element does not support text input an error
        will be raised.
        """
        element = self._find_element(locator)
        self._info("Typing text '%s' into component '%s'" % (text, locator))
        try:
            element.send_keys(text)
        except Exception as err:
            raise err

    def clear_text(self, locator):
        """Clear the text from specified element.

        If the element does not support text clearing an error
        will be raised.
        """
        element = self._find_element(locator)
        self._info("Clearing text from element '%s'" % (locator))
        try:
            element.clear()
        except Exception as err:
            raise err

    def click_element(self, locator):
        """Tap the specified element.

        If the element does not support tapping an error
        will be raised.
        """
        element = self._find_element(locator)
        self._info("Clicking on element %s" % locator)
        try:
            element.click()
        except Exception as err:
            raise err

    def element_should_be_visible(self, locator):
        """Verify if the element is visible using FlutterDriver.waitFor().

        If the element isn't visible raise an Assertion Error.
        """
        element = self._find_element(locator)
        if not self._is_visible(element):
            raise AssertionError("Element '%s' should be visible but not" % locator)

    def element_text_should_be(self, locator, text):
        """Verify if the element text is equal to provided text.

        If the text isn't equal raise an Assertion Error.

        If the element does not support getText() raise an error.
        """
        element = self._find_element(locator)
        if element.text != text:
            raise AssertionError("Element '%s' text should be '%s' but is '%s'." %
                                    (locator, text, element.text))

    def element_text_should_not_be(self, locator, text):
        """Verify if the element text is not equal to provided text.

        If the text isn't equal raise an Assertion Error.

        If the element does not support getText() raise an error.
        """
        element = self._find_element(locator)
        if element.text == text:
            raise AssertionError("Element '%s' text should not be '%s' but is." %
                                    (locator, text))

    def get_element(self, locator):
        """Returns the element object.
        """
        return self._find_element(locator)

    def get_element_text(self, locator):
        """Returns element text

        If the element does not support getText() raise an error.
        """
        element = self._find_element(locator)
        return self._get_element_text(element)

    def _is_visible(self, element):
        application = self._current_application()
        application.execute_script('flutter:waitFor', element, 1)
        return 1

    def _find_element(self, locator):
        application = self._current_application()
        return self._element_finder.find(application, locator)

    def _get_element_text(self, element):
        application = self._current_application()
        return application.execute_script('flutter:getText', element)
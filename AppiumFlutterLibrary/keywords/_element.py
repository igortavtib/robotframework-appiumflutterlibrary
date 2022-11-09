from appium.webdriver.webelement import WebElement
from .keywordgroup import KeywordGroup
from AppiumFlutterLibrary.finder import ElementFinder
from appium_flutter_finder import FlutterElement
from typing import Optional

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

    def click_element(self, locator: str | FlutterElement) -> None:
        """Tap the specified element.

        If the element does not support tapping an error
        will be raised.
        """
        if isinstance(locator, FlutterElement):
            element = locator
        else:
            element = self._find_element(locator)

        self._info("Clicking on element %s" % locator)
        try:
            element.click()
        except Exception as err:
            raise err

    def element_should_be_visible(self, locator: str | FlutterElement):
        """Verify if the element is visible using FlutterDriver.waitFor().

        If the element isn't visible raise an Assertion Error.
        """
        if isinstance(locator, FlutterElement):
            element = locator
        else:
            element = self._find_element(locator)
        
        if not self._is_visible(element):
            raise AssertionError("Element '%s' should be visible but not" % locator)

    def element_text_should_be(self, locator: str | FlutterElement, text):
        """Verify if the element text is equal to provided text.

        If the text isn't equal raise an Assertion Error.

        If the element does not support getText() raise an error.
        """
        if isinstance(locator, FlutterElement):
            element = locator
        else:
            element = self._find_element(locator)

        if element.text != text:
            raise AssertionError("Element '%s' text should be '%s' but is '%s'." %
                                    (locator, text, element.text))

    def element_text_should_not_be(self, locator: str | FlutterElement, text):
        """Verify if the element text is not equal to provided text.

        If the text isn't equal raise an Assertion Error.

        If the element does not support getText() raise an error.
        """
        if isinstance(locator, FlutterElement):
            element = locator
        else:
            element = self._find_element(locator)

        if element.text == text:
            raise AssertionError("Element '%s' text should not be '%s' but is." %
                                    (locator, text))

    def get_element(self, locator):
        """Returns the element object.
        """
        return self._find_element(locator)

    def get_element_text(self, locator: str | FlutterElement):
        """Returns element text

        If the element does not support getText() raise an error.
        """
        text = self._get_text(locator)
        self._info("Element '%s' text is '%s' " % (locator, text))
        return text

    def get_element_descendant(
        self, 
        of: str, 
        matching: str,
        match_root: bool = False,
        first_match_only: bool = False,
        ) -> FlutterElement:
        """Returns the element's descendant
        
        Params:
            of: locator for the parent element
            matching: locator for the child element
        """
        application = self._current_application()
        return self._element_finder._get_descendant(
            application, of, matching, match_root, first_match_only
            )

    def get_element_ancestor(
        self, 
        of: str, 
        matching: str,
        match_root: bool = False,
        first_match_only: bool = False,
        ) -> FlutterElement:
        """Returns the element's ancestor
        
        Params:
            of: locator for the parent element
            matching: locator for the child element
        """
        application = self.current_application()
        return self._element_finder._get_ancestor(
            application, of, matching, match_root, first_match_only
            )

    def _is_visible(self, element):
        application = self._current_application()
        application.execute_script('flutter:waitFor', element.id, 1)
        return 1

    def _find_element(self, locator):
        application = self._current_application()
        return self._element_finder.find(application, locator)

    def _get_text(self, locator: str | FlutterElement) -> Optional[str]:
        if isinstance(locator, FlutterElement):
            element = locator
        else:
            element = self._find_element(locator)

        if element is not None:
            return element.text
        return None
    
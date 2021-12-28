from .keywordgroup import  KeywordGroup
from AppiumFlutterLibrary.finder import ElementFinder

class _TouchKeywords(KeywordGroup):
    def init(self):
        self._element_finder = ElementFinder()

    def scroll(self, start_locator, end_locator):
        """
        Scrolls from one element to another
        Key attributes for arbitrary elements are `id` and `name`. See
        `introduction` for details about locating elements.
        """
        el1 = self._find_element(self, start_locator)
        el2 = self._find_element(self, end_locator)
        driver = self._current_application()
        driver.scroll(el1, el2)

    def scroll_down(self, locator):
        """Scrolls down to element"""
        driver = self._current_application()
        element = self._find_element(self, locator)
        driver.execute_script("mobile: scroll", {"direction": 'down', 'elementid': element.id})

    def scroll_up(self, locator):
        """Scrolls up to element"""
        driver = self._current_application()
        element = self._element_find(locator, True, True)
        driver.execute_script("mobile: scroll", {"direction": 'up', 'elementid': element.id})
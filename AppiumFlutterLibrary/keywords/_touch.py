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

    def flutter_scroll(self, locator, dx, dy, durationmilliseconds=200, frequency=60):
        """ Tell the driver to perform a scrolling action.
        A scrolling action begins with a "pointer down" event, which commonly maps to finger press on the touch screen
        or mouse button press. A series of "pointer move" events follow.
        The action is completed by a "pointer up" event.

        dx and dy specify the total offset for the entire scrolling action.

        durationmilliseconds specifies the length of the action in milliseconds.

        The move events are generated at a given frequency in Hz (or events per second). It defaults to 60Hz.
        """
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        try:
            application.execute_script('flutter:scroll',
                                       element.id,
                                       {'durationMilliseconds': int(durationmilliseconds), 'dx': int(dx), 'dy': int(dy),
                                        'frequency': int(frequency)})
        except Exception:
            raise AssertionError("Unable to perform scroll")

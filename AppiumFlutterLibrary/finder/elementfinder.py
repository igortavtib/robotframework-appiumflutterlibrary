from appium_flutter_finder import FlutterElement, FlutterFinder
from typing import Literal, overload

class ElementFinder():
    def __init__(self):
        self._element_finder = FlutterFinder()
        self._strategies = {
            'xpath': self._find_by_xpath,
            'key': self._find_by_key,
            'text': self._find_by_text,
            'semantics': self._find_by_semantics_label,
            'tooltip': self._find_by_tooltip_message,
            'type': self._find_by_type,
            'default': self._find_by_key,
        }

    @overload
    def find(self, application, locator, serialized: Literal[False] = False) -> FlutterElement:
        ...

    @overload
    def find(self, application, locator, serialized: Literal[True]) -> str:
        ...

    @overload
    def find(self, application, locator, serialized: bool) -> FlutterElement | str:
        ...

    def find(self, application, locator, serialized: bool = False) -> FlutterElement | str:
        """Finds the element
        
        Params:
            serialized: Returns the serialized str of the element
        """
        assert application is not None
        assert application is not None and len(locator) > 0

        (prefix , criteria) = self._parse_locator(locator)

        prefix= 'default' if prefix is None else prefix
        strategy = self._strategies.get(prefix)
        if strategy is None:
            raise ValueError("Element locator with prefix '" + prefix + "' is not supported")
        return strategy(application, criteria, serialized=serialized)

    def _find_by_key(self, application, element_key, serialized=False):
        finder_key = self._element_finder.by_value_key(element_key)
        
        if serialized:
            return finder_key

        element = FlutterElement(application, finder_key)

        return element
        
    def _find_by_xpath(self, application, xpath, **kwargs):
        return

    def _find_by_text(self, application, element_text, **kwargs):
        finder_text = self._element_finder.by_text(element_text)
        element = FlutterElement(application, finder_text)

        return element

    def _find_by_semantics_label(self, application, semantics, **kwargs):
        finder_semantics_label = self._element_finder.by_semantics_label(semantics)
        element = FlutterElement(application, finder_semantics_label)

        return element

    def _find_by_tooltip_message(self, application, tooltip, **kwargs):
        finder_tooltip_message = self._element_finder.by_tooltip(tooltip)
        element = FlutterElement(application, finder_tooltip_message)

        return element

    def _find_by_type(self, application, type, **kwargs):
        finder_type = self._element_finder.by_type(type)
        element = FlutterElement(application, finder_type)

        return element

    def _get_descendant(self, application, of, matching) -> FlutterElement:
        finder_descendant = self._element_finder.by_descendant(
            self.find(application, of, serialized=True), 
            self.find(application, matching, serialized=True)
            )

        element = FlutterElement(application, finder_descendant)

        return element

    def _get_ancestor(self, application, of, matching) -> FlutterElement:
        finder_descendant = self._element_finder.by_ancestor(
            self.find(application, of, serialized=True), 
            self.find(application, matching, serialized=True)
            )

        element = FlutterElement(application, finder_descendant)

        return element

    def _parse_locator(self, locator):
        prefix = None
        criteria = locator

        if not locator.startswith('//'):
            locator_parts = locator.partition('=')
            if len(locator_parts[1]) > 0:
                prefix = locator_parts[0].strip().lower()
                criteria = locator_parts[2].strip()
        return (prefix, criteria)

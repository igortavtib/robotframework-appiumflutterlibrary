from appium_flutter_finder import FlutterElement, FlutterFinder

class ElementFinder():
    def __init__(self):
        self._element_finder = FlutterFinder()

    def find_by_key(self, application, element_key):
        finder_key = self._element_finder.by_value_key(element_key)
        element = FlutterElement(application, finder_key)

        return element
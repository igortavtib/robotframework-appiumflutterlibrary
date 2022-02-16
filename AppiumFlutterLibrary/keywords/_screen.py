from AppiumFlutterLibrary.finder import ElementFinder
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup
import os
import robot

class _ScreenKeywords(KeywordGroup):
    def __init__(self):
        self._element_finder = ElementFinder()
        self._screenshot_index = 0

    def scroll_to_element(self, locator):
        """ Uses FlutterDriver.scrollIntoView() to scroll until element is visible.
        """
        application = self._current_application()
        element = self._element_finder.find(application, locator)
        self._info(element)
        application.execute_script('flutter:scrollIntoView', element.id, 0)

    def capture_page_screenshot(self, filename=None):
        """Takes a screenshot of the current page and embeds it into the log.

        `filename` argument specifies the name of the file to write the
        screenshot into. If no `filename` is given, the screenshot is saved into file
        `appiumflutter-screenshot-<counter>.png` under the directory where
        the Robot Framework log file is written into. The `filename` is
        also considered relative to the same directory, if it is not
        given in absolute format.

        `css` can be used to modify how the screenshot is taken. By default
        the background color is changed to avoid possible problems with
        background leaking when the page layout is somehow broken.
        """
        path, link = self._get_screenshot_paths(filename)

        if hasattr(self._current_application(), 'get_screenshot_as_file'):
            self._current_application().get_screenshot_as_file(path)
        else:
            self._current_application().save_screenshot(path)

        # Image is shown on its own row and thus prev row is closed on purpose
        self._html('</td></tr><tr><td colspan="3"><a href="%s">'
                   '<img src="%s" width="800px"></a>' % (link, link))
        return path

    # Private

    def _get_screenshot_paths(self, filename):
        if not filename:
            self._screenshot_index += 1
            filename = 'appiumflutter-screenshot-%d.png' % self._screenshot_index
        else:
            filename = filename.replace('/', os.sep)
        logdir = self._get_log_dir()
        path = os.path.join(logdir, filename)
        link = robot.utils.get_link_path(path, logdir)
        return path, link

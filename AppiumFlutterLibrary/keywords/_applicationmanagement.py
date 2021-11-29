# -*- coding: utf-8 -*-

import robot
from AppiumFlutterLibrary.utils import ApplicationCache
from AppiumFlutterLibrary.keywords.keywordgroup import KeywordGroup
from appium.webdriver import Remote

class _ApplicationManagementKeyWords(KeywordGroup):
    def __init__(self):
        self._cache = ApplicationCache()
        self._timeout_in_secs = float(5)

    def open_application(self, remote_url, alias =None, **kwargs):
        """Opens a new application to given Appium server.

        *Note*: You must specify automationName capability as 'flutter', so the
        FlutterDriver is enabled.

        Capabilities of appium server, Android and iOS,
        Please check https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/server-args.md
        | *Option*            | *Man.* | *Description*     |
        | remote_url          | Yes    | Appium server url |
        | alias               | no     | alias             |

        Examples:
        | Open Application | http://localhost:4723/wd/hub | alias=Myapp1         | automationName=flutter | platformName=iOS       | platformVersion=7.0            | deviceName='iPhone Simulator'           | app=your.app                         |
        | Open Application | http://localhost:4723/wd/hub | platformName=Android | automationName=flutter | platformVersion=4.2.2  | deviceName=192.168.56.101:5555 | app=${CURDIR}/demoapp/OrangeDemoApp.apk | appPackage=com.netease.qa.orangedemo | appActivity=MainActivity |
        """
        desired_caps = kwargs
        if desired_caps['automationName'] != 'flutter':
            raise ValueError("Appium Flutter Library only suports flutter automation. Try changing automationName capability to 'flutter'")
        self._debug("Opening application")
        application = Remote(str(remote_url), desired_caps)
        return self._cache.register(application, alias)

    def reset_application(self):
        self._debug("Reseting application")
        self._current_application().reset()

    def close_all_applications(self):
        """Closes all open applications.

        This keyword is meant to be used in test or suite teardown to
        make sure all the applications are closed before the test execution
        finishes.

        After this keyword, the application indices returned by `Open Application`
        are reset and start from `1`.
        """
        self._debug("Closing all applications")
        self._cache.close_all()

    def close_application(self):
        """Closes the current application and also close webdriver session."""
        self._debug("Closing current apllication")
        self._cache.close()

    def background_app(self, seconds=5):
        """
        Puts the application in the background on the device for a certain
        duration in seconds.
        """
        self._current_application().background_app(seconds)

    def lock(self, seconds=5):
        """
        Lock the device for a certain period of time. iOS only.
        """
        self._current_application().lock(robot.utils.timestr_to_secs(seconds))

    def portrait(self):
        """
        Set the device orientation to PORTRAIT
        """
        self._rotate("PORTRAIT")

    def landscape(self):
        """
        Set the device orientation to LANDSCAPE
        """
        self._rotate('LANDSCAPE')

    def touch_id(self, match = True):
        """
        Simulate Touch ID on iOS Simulator
        `match` (boolean) whether the simulated fingerprint is valid (default true)

        New in AppiumLibrary 1.5
        """
        self._current_application().touch_id(match)

    def set_appium_timeout(self, seconds):
        """Sets the timeout in seconds used by various keywords.

        There are several `Wait ...` keywords that take timeout as an
        argument. All of these timeout arguments are optional. The timeout
        used by all of them can be set globally using this keyword.

        The previous timeout value is returned by this keyword and can
        be used to set the old value back later. The default timeout
        is 5 seconds, but it can be altered in `importing`.
        
        Example:
        | ${orig timeout} = | Set Appium Timeout | 15 seconds |
        | Open page that loads slowly |
        | Set Appium Timeout | ${orig timeout} |
        """
        old_timeout = self.get_appium_timeout()
        self._timeout_in_secs = robot.utils.timestr_to_secs(seconds)
        return old_timeout
    
    def get_appium_timeout(self):
        """Gets the timeout in seconds that is used by various keywords.

        See `Set Appium Timeout` for an explanation."""
        return robot.utils.secs_to_timestr(self._timeout_in_secs)

    # Private

    def _current_application(self):
        if not self._cache.current:
            raise RuntimeError('No application is open')
        return self._cache.current

    def _rotate(self, orientation):
        driver = self._current_application()
        driver.orientation = orientation
import os
from appium.webdriver import Remote
from appium_flutter_finder import FlutterElement, FlutterFinder

driver = Remote('http://localhost:4723/wd/hub', dict(
    platformName='android',
    automationName='flutter',
    udid='emulator-5554',
    app='/home/igortavtib/Projects/platform-mobile/app-prod-debug.apk'
))

finder = FlutterFinder()

key_finder = finder.by_value_key('input-user')
input_element = FlutterElement(driver, key_finder)
driver.execute_script('flutter:waitFor', input_element)
input_element.send_keys('Teste 123')


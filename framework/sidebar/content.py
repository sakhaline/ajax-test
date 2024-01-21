from appium.webdriver.common.appiumby import AppiumBy
from utils.android_utils import android_get_desired_capabilities
from appium import webdriver


SETTINGS_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")
HELP_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/help")
REPORT_PROBLEM_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/logs")
CCTV_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/camera")
ADD_HUB_BUTTON = (AppiumBy.XPATH, "//android.widget.Button")
DOC_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/documentation_text")

driver = webdriver.Remote('http://localhost:4723/wd/hub',
                          android_get_desired_capabilities())

WINDOW_WIDTH = driver.get_window_size()["width"]
WINDOW_HEIGHT = driver.get_window_size()["height"]

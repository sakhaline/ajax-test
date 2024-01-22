from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from utils.android_utils import android_get_desired_capabilities

SIDEBAR_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")
SETTINGS_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/settings")
HELP_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/help")
REPORT_PROBLEM_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/logs")
CCTV_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/camera")
ADD_HUB_BUTTON = (AppiumBy.XPATH,
                  "(//android.widget.TextView"
                  "[@resource-id='com.ajaxsystems:id/text'])[2]")
DOC_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/documentation_text")

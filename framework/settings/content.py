from appium.webdriver.common.appiumby import AppiumBy

SETTINGS_BUTTON = (AppiumBy.ID, 'com.ajaxsystems:id/settings')
LOGOUT_BUTTON = (AppiumBy.XPATH, '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/android.view.View/android.view.View[1]')
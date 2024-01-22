from appium.webdriver.common.appiumby import AppiumBy


LOGIN_BUTTON = (AppiumBy.XPATH,
                      '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[1]/android.view.View/android.view.View/android.widget.Button')
USERNAME_FIELD = (AppiumBy.XPATH,
                  '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]')
PASSWORD_FIELD = (AppiumBy.XPATH,
                  '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]')
CONFIRM_BUTTON = (AppiumBy.XPATH,
                '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View/android.widget.Button')

from appium.webdriver.common.appiumby import AppiumBy


USERNAME_FIELD = (AppiumBy.ID, 'com.ajaxsystems.app:id/username')
PASSWORD_FIELD = (AppiumBy.ID, 'com.ajaxsystems.app:id/password')
LOGIN_BUTTON = (AppiumBy.XPATH,
                '((//androidx.compose.ui.platform.ComposeView'
                '[@resource-id="com.ajaxsystems:id/compose_view"])[1]'
                '/android.view.View/android.view.View/android.widget.Button')

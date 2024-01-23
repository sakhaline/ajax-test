import subprocess


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '13',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_device_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }


def get_device_udid():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
        output_lines = result.stdout.splitlines()
        if len(output_lines) > 1:
            udid = output_lines[1].split('\t')[0].strip()
            return udid
        else:
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error running adb devices: {e}")
        return None

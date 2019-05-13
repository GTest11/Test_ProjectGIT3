from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['appiumVersion'] = '8.0.0'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'Galaxy_J7_6.0.1'
desired_caps['browserName'] = ''
desired_caps['name'] = 'Sample Test'
desired_caps['app'] = 'com.google.android.youtube'

driver = webdriver.Remote('http://10.47.166.48:8288/wd/hub', desired_caps)

# Test Actions here...

driver.quit()
from selenium.webdriver.support.ui import WebDriverWait
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Установка переменной среды PATH для ChromeDriver
chromedriver_path = 'C:/chromedriver/'
os.environ['PATH'] = chromedriver_path + os.pathsep + os.environ['PATH']

class Browser:
    """
    This class is a wrapper around Selenium driver
    """
    def __init__(self, url, browser_name="chrome", time_wait=10):
        # Decide which browser to open based on browser_name parameter
        if browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=360")
            options.add_argument("--height=800")
            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference("browser.urlbar.showPopup", True)
            self.driver = webdriver.Firefox(options=options)
            self.driver.maximize_window()
        elif browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--window-size=360,800")
            options.add_argument("--incognito")
            options.add_argument("--disable-popup-blocking")
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            self.driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == 'remote':
            desired_capabilities = {
                'browserName': 'chrome'}
            self.driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor="http://localhost:4444/wd/hub")

            # options = FirefoxOptions()
            # options.browser_version = '92'
            # options.platform_name = 'Windows 10'
            # cloud_options = {}
            # cloud_options['build'] = "first bild"
            # cloud_options['name'] = "first test"
            # options.set_capability('cloud:options', cloud_options)
            # driver = webdriver.Remote('https://iuliia_SmZ2tQ:CvFJVNpvrHde4BdncjDT@hub-cloud.browserstack.com/wd/hub', options=options)

            # options = FirefoxOptions()
            # options.browser_version = '92'
            # options.platform_name = 'Windows 10'

            # # Настройки Cloud
            # cloud_options = {
            #     'build': 'my_test_build',
            #     'name': 'my_test_name'
            # }
            #
            # # Установите опции Cloud
            # options.set_capability('cloud:options', cloud_options)
            #
            # # Создайте драйвер для удаленного управления
            # driver = webdriver.Remote(
            #     command_executor='https://iuliia_SmZ2tQ:CvFJVNpvrHde4BdncjDT@hub-cloud.browserstack.com/wd/hub',
            #     options=options
            # )

            # BROWSERSTACK_URL = 'https://iuliia_SmZ2tQ:CvFJVNpvrHde4BdncjDT@hub-cloud.browserstack.com/wd/hub'
            # desired_cap = {
            #     'os': 'Windows',
            #     'os_version': '10',
            #     'browser': "Chrome",
            #     'browserVersion': '80.0',
            #     'name': 'iuliia First Test'
            # }
            # self.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

        # elif browser_name.lower() == 'remote':
        #     BROWSERSTACK_URL = 'https://iuliia_SmZ2tQ:CvFJVNpvrHde4BdncjDT@hub-cloud.browserstack.com/wd/hub'
        #     desired_cap = {
        #         'os': 'Windows',
        #         'os_version': '10',
        #         'browser': "Chrome",
        #         'browserVersion': '80.0',
        #         'name': 'iuliia First Test'
        #     }
        #
        #     self.driver = webdriver.Remote(
        #         command_executor=BROWSERSTACK_URL,
        #         desired_capabilities=desired_cap
        #     )


        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(time_wait)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
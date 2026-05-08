from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import Config
import os


class DriverManager:
    @staticmethod
    def get_driver():
        if Config.BROWSER == 'chrome':
            options = webdriver.ChromeOptions()

            # 模拟手机浏览器，绕过验证
            options.add_argument(f'--user-agent={Config.MOBILE_USER_AGENT}')

            if Config.HEADLESS:
                options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            driver_path = Config.CHROME_DRIVER_PATH
            if not os.path.isabs(driver_path):
                driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), driver_path)

            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"不支持的浏览器: {Config.BROWSER}")

        driver.implicitly_wait(Config.IMPLICITLY_WAIT)
        driver.maximize_window()
        return driver

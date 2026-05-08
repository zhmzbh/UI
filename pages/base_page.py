import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, NoSuchElementException
from config import Config
from utils.logger import get_logger

logger = get_logger()


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICITLY_WAIT)

    def find_element(self, locator, timeout=None):
        """查找单个元素"""
        wait = WebDriverWait(self.driver, timeout or Config.EXPLICITLY_WAIT)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            logger.debug(f"找到元素: {locator}")
            return element
        except TimeoutException:
            logger.error(f"元素未找到: {locator}")
            raise

    def find_elements(self, locator):
        """查找多个元素"""
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        logger.debug(f"找到 {len(elements)} 个元素: {locator}")
        return elements

    def click(self, locator, timeout=None):
        """点击元素"""
        try:
            wait = WebDriverWait(self.driver, timeout or Config.EXPLICITLY_WAIT)
            element = wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.3)
            element.click()
            logger.info(f"点击元素: {locator}")
        except Exception as e:
            logger.error(f"点击失败: {locator}, 错误: {e}")
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text, clear_first=True):
        """输入文本"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)

        if clear_first:
            try:
                element.clear()
            except:
                self.driver.execute_script("arguments[0].value = '';", element)

        time.sleep(0.2)
        element.send_keys(text)
        logger.info(f"输入文本: {text[:30]}...")

    def get_text(self, locator):
        """获取元素文本"""
        text = self.find_element(locator).text
        logger.debug(f"获取文本: {text[:50]}...")
        return text

    def get_title(self):
        """获取页面标题"""
        title = self.driver.title
        logger.info(f"当前页面标题: {title}")
        return title

    def take_screenshot(self, name):
        """截图"""
        import os
        if not os.path.exists(Config.SCREENSHOT_DIR):
            os.makedirs(Config.SCREENSHOT_DIR)
        path = f"{Config.SCREENSHOT_DIR}/{name}.png"
        self.driver.save_screenshot(path)
        logger.info(f"截图已保存: {path}")
        return path

    def wait_for_element_visible(self, locator, timeout=None):
        """等待元素可见"""
        wait = WebDriverWait(self.driver, timeout or Config.EXPLICITLY_WAIT)
        return wait.until(EC.visibility_of_element_located(locator))

    def is_element_present(self, locator):
        """检查元素是否存在"""
        try:
            self.find_element(locator, timeout=3)
            return True
        except:
            return False

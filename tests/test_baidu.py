import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import Config
from utils.logger import get_logger
from utils.test_data import TestData

logger = get_logger()


class BaiduPage(BasePage):
    """百度页面对象（手机版）"""
    SEARCH_INPUT = (By.ID, "index-kw")
    SEARCH_BUTTON = (By.ID, "index-bn")

    def search(self, keyword):
        """执行搜索"""
        logger.info(f"开始搜索: {keyword}")
        self.input_text(self.SEARCH_INPUT, keyword)
        time.sleep(0.5)
        self.click(self.SEARCH_BUTTON)
        logger.info("搜索完成")

    def get_search_result_title(self):
        """获取搜索结果页标题"""
        return self.get_title()


class TestBaidu:
    """百度搜索测试类"""

    @pytest.mark.smoke
    @pytest.mark.parametrize("keyword", TestData.SEARCH_KEYWORDS[:2])
    def test_search_valid_keyword(self, driver, keyword):
        """测试有效关键词搜索（参数化）"""
        logger.info(f"========== 开始测试: {keyword} ==========")

        driver.get(Config.BASE_URL)
        time.sleep(2)

        baidu_page = BaiduPage(driver)
        baidu_page.search(keyword)

        time.sleep(2)
        title = baidu_page.get_title()

        # 验证搜索结果
        assert "百度" in title
        logger.info(f"✅ 测试通过: {keyword}")

        # 截图
        baidu_page.take_screenshot(f"search_{keyword[:10]}")

    @pytest.mark.regression
    def test_search_long_keyword(self, driver):
        """测试超长关键词搜索"""
        keyword = "Selenium" * 50
        logger.info(f"测试超长关键词（长度: {len(keyword)}）")

        driver.get(Config.BASE_URL)
        time.sleep(2)

        baidu_page = BaiduPage(driver)
        baidu_page.search(keyword)

        time.sleep(2)
        title = baidu_page.get_title()

        assert "百度" in title
        logger.info("✅ 超长关键词测试通过")

    @pytest.mark.regression
    @pytest.mark.parametrize("keyword", TestData.INVALID_DATA[:2])
    def test_search_empty_keyword(self, driver, keyword):
        """测试空搜索/无效搜索"""
        logger.info(f"测试无效关键词: '{keyword}'")

        driver.get(Config.BASE_URL)
        time.sleep(2)

        baidu_page = BaiduPage(driver)

        if keyword:
            baidu_page.input_text(baidu_page.SEARCH_INPUT, keyword)
            time.sleep(0.5)

        baidu_page.click(baidu_page.SEARCH_BUTTON)
        time.sleep(2)

        title = baidu_page.get_title()
        assert "百度" in title
        logger.info("✅ 无效搜索测试通过")

    def test_multiple_searches(self, driver):
        """测试连续搜索"""
        keywords = ["Selenium", "Python", "Pytest"]

        for keyword in keywords:
            logger.info(f"连续搜索: {keyword}")
            driver.get(Config.BASE_URL)
            time.sleep(1)

            baidu_page = BaiduPage(driver)
            baidu_page.search(keyword)
            time.sleep(1)

            title = baidu_page.get_title()
            assert "百度" in title
            baidu_page.take_screenshot(f"multi_{keyword}")

        logger.info("✅ 连续搜索测试通过")


# 直接运行入口
if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    print("=" * 60)
    print("百度搜索完整测试套件")
    print("=" * 60)

    service = Service(Config.CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-agent={Config.MOBILE_USER_AGENT}')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    test = TestBaidu()

    try:
        # 运行测试
        test.test_search_valid_keyword(driver, "Pytest自动化测试")
        test.test_multiple_searches(driver)

        print("\n" + "=" * 60)
        print("🎉 所有测试通过！")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")

    finally:
        time.sleep(2)
        driver.quit()
        print("✅ 浏览器已关闭")
        
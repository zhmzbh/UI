import os


class Config:
    # 浏览器配置
    BROWSER = 'chrome'
    HEADLESS = False

    # 测试环境（手机版百度绕过验证）
    BASE_URL = 'https://m.baidu.com'

    # 超时时间（秒）
    IMPLICITLY_WAIT = 10
    EXPLICITLY_WAIT = 20

    # ChromeDriver路径（项目根目录下）
    CHROME_DRIVER_PATH = './chromedriver.exe'

    # 报告和截图路径
    REPORT_DIR = "reports"
    SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")
    LOG_DIR = "logs"

    # 手机版User-Agent（绕过反爬）
    MOBILE_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, ' \
                        'like Gecko) Version/14.0 Mobile/15E148 Safari/604.1 '

    @classmethod
    def create_dirs(cls):
        """创建必要的文件夹"""
        for dir_path in [cls.REPORT_DIR, cls.SCREENSHOT_DIR, cls.LOG_DIR]:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

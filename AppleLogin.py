from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class AppleLogin:
    def __init__(self, username, password, url):
        print(f"Username: {username}, Password: {password}, URL: {url}")

        options = Options()
        options.add_experimental_option("detach", True)  # Keep the browser open after script finishes

        # Initialize the ChromeDriver
        self.driver = webdriver.Chrome(options=options)

        self.username = username
        self.password = password

        # Get to the login window
        self.driver.get(url)
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CLASS_NAME, "signin svelte-jf121i")

        

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Set the path to the ChromeDriver
chrome_driver_path = 'path/to/your/chromedriver'  # Change this to your actual path

# Set up the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Go to Google.com
    driver.get("https://www.google.com")
    
    # Wait for a few seconds to ensure the site loads completely
    time.sleep(3)
    
    # Check if the title contains "Google"
    if "Google" in driver.title:
        print("Successfully went to the site.")
    else:
        print("Failed to reach the expected site.")

finally:
    # Close the browser
    driver.quit()



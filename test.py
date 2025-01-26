from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
chromedriver_path = "/use/local/bin/chromedriver"

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the Chrome driver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open Google
    driver.get("https://www.google.com")

    # Optional: Wait for a few seconds to ensure the page loads
    time.sleep(3)
    
    # Check if the title of the page is correct
    if "Google" in driver.title:
        print("Successfully opened the site: Google")
    else:
        print("Failed to open the site: Google")
finally:
    # Clean up and close the driver
    driver.quit()



# Facebook Login Automation with Selenium

This project demonstrates how to automate the process of logging into Facebook using Selenium WebDriver in Python. It includes steps to enter login credentials, handle cookies consent, and log into the Facebook account.

## Prerequisites

1. Python 3.x
2. Google Chrome Browser
3. ChromeDriver (ensure it's compatible with your Chrome version)
4. Selenium library

## Installation

1. **Install Selenium**

    ```bash
    pip install selenium
    ```

2. **ChromeDriver Setup**

    Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)(https://googlechromelabs.github.io/chrome-for-testing/) and ensure it's in your system's PATH or specify its location when initializing the WebDriver.

3. **Credentials Module**

    Create a file named `creds.py` in the same directory with the following content:

    ```python
    def creds():
        return ["your_email@example.com", "your_password"]
    ```

## Usage

1. **Clone the repository**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Run the Script**

    ```bash
    python app.py
    ```

## Script Explanation

Here's a step-by-step explanation of the script:

1. **Import necessary libraries**

    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import creds
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    ```

2. **Set Chrome options**

    ```python
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    ```

3. **Initialize WebDriver**

    ```python
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com/")
    ```

4. **Verify Page Title**

    ```python
    title = driver.title
    assert title == "Facebook – zaloguj się lub zarejestruj"
    ```

5. **Enter Login Credentials**

    ```python
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(creds.creds()[0])
    time.sleep(10)  # wait for 10 seconds before entering password
    driver.find_element(By.NAME, "pass").clear()
    driver.find_element(By.NAME, "pass").send_keys(creds.creds()[1])
    time.sleep(1)
    ```

6. **Handle Cookies Consent**

    ```python
    try:
        wait = WebDriverWait(driver, 10)
        accept_cookies_button = driver.find_element(By.XPATH, '//div[@aria-label="Zezwól na wszystkie pliki cookie" and @role="button"]')
        driver.execute_script("arguments[0].removeAttribute('aria-disabled'); arguments[0].click();", accept_cookies_button)
        print("Accepted cookies")
    except Exception as e:
        print("Cookies button not found:", e)
    ```

7. **Click Login Button**

    ```python
    driver.find_element(By.NAME, "login").click()
    ```

## Notes

- **Delays (`time.sleep`)**: Adjust the sleep times based on your internet speed and system performance. These delays are added to ensure that the page elements are loaded before interacting with them.
- **Cookies Handling**: The script attempts to find and click the cookies consent button. Ensure the XPATH used in the script matches the current HTML structure of Facebook's login page.

## Troubleshooting

- **Element Not Found**: If any element is not found, it might be due to changes in the HTML structure of the Facebook login page. Use browser developer tools to inspect the element and update the script accordingly.
- **ChromeDriver Version**: Ensure the ChromeDriver version matches your installed Chrome browser version.

## Disclaimer

This script is for educational purposes only. Use it responsibly and ensure compliance with Facebook's terms of service.

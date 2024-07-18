# IRCTC Automation Script

This project contains a Selenium script to automate the process of booking train tickets on the IRCTC website. The script navigates through the train search, selects train classes, modifies the search, and proceeds to the booking process.

## Prerequisites

- Python 3.x
- Selenium library
- Chrome browser
- ChromeDriver executable

## Installation

1. **Install Selenium:**

    ```sh
    pip install selenium
    ```

2. **Download ChromeDriver:**

    - Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the ChromeDriver executable in a directory and update the `Path` variable in the script accordingly.

## Script Explanation

The script is divided into several key steps, explained below:

### 1. Importing Required Libraries

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
```

### 2. Setting Up WebDriver

```python
Path = r"C:\Users\Rajdeep Shaw\Downloads\Selenium_python\irctc_automation\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
service = Service(Path)
driver = webdriver.Chrome(service=service, options=chrome_options)
```

### 3. Navigating to the IRCTC Website

```python
driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
```

### 4. Handling Initial Popup

```python
try:
    ok_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button'))
    )
    ok_field.click()
except Exception as e:
    print(f"Error: {e}")
    driver.quit()
```

### 5. Filling in Train Search Details

```python
from_field = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
from_field.send_keys("KOLKATA - KOAA")
from_field.send_keys(Keys.TAB)

to_field = driver.find_element(By.XPATH, '//*[@id="destination"]/span/input')
to_field.send_keys("NEW JALPAIGURI - NJP")
to_field.send_keys(Keys.TAB)

date_field = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input')
date_field.click()

date_field1 = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/div/table/tbody/tr[5]/td[5]/a')
date_field1.click()

class_field = driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div/div[3]')
class_field.click()

class1_field = driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div/div[4]/div/ul/li[3]/span')
class1_field.click()

find_field = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button')
find_field.click()
sleep(5)
```

### 6. Modifying Search and Selecting Number of Passengers

```python
passenger_field = driver.find_element(By.XPATH, '//*[@id="numberOfPassengers"]/div/label')
passenger_field.click()

select_three = driver.find_element(By.XPATH, '//*[@id="numberOfPassengers"]/div/div[4]/div/ul/li[4]')
select_three.click()

class_field1 = driver.find_element(By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/label')
class_field1.click()

class1_field1 = driver.find_element(By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/div[4]/div/ul/li[5]/span')
class1_field1.click()

modify_search = driver.find_element(By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[6]/button')
modify_search.click()
sleep(5)
```

### 7. Checking Availability and Booking

```python
check_avail = driver.find_element(By.XPATH, '//*[@id="check-availability"]')
for x in range(6):
    check_avail.send_keys(Keys.DOWN)
check_avail.click()
sleep(10)

book_now = driver.find_element(By.XPATH, '//*[@id="ui-panel-0-content"]/div/div/div/table/tbody/tr/td[2]/div/div[3]/button')
book_now.click()

agree = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[1]/div/div[3]/p-footer/div/button[2]/span[2]')
agree.click()

ok1_field = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[2]/div/div[3]/p-footer/div/button[2]/span[2]')
ok1_field.click()
```

### 8. Logging In and Completing Booking

```python
username_field = driver.find_element(By.XPATH, '//*[@id="userId"]')
username_field.send_keys('shawrajdeep00')

password_field = driver.find_element(By.XPATH, '//*[@id="pwd"]')
password_field.send_keys('abcd1234@123')

captcha = driver.find_element(By.XPATH, '//*[@id="nlpAnswer"]')
sleep(15)

sign_in = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/button')
sign_in.click()
```

### 9. Closing the Browser

```python
driver.quit()
```

## Note

Screenshots couldn't be added as login credentials are confidential.

## Conclusion

This script automates the process of booking train tickets on the IRCTC website using Selenium WebDriver. It navigates through various steps such as selecting stations, dates, classes, modifying the search, checking availability, and finally logging in to complete the booking process.

Feel free to customize the script according to your requirements, especially the login credentials and other personal details.

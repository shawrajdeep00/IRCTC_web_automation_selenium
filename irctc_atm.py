from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Path to the ChromeDriver executable
Path = r"C:\Users\Rajdeep Shaw\Downloads\Selenium_python\irctc_automation\chromedriver.exe"

# Initialize Chrome options
chrome_options = webdriver.ChromeOptions()

# Initialize a new Chrome browser session using Service
service = Service(Path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the IRCTC train search page
driver.get('https://www.irctc.co.in/nget/train-search')
# Maximize the browser window
driver.maximize_window()

# Wait for the OK button to be present and click it
#try:
#    ok_field = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button'))
 #   )
 #   ok_field.click()
#except Exception as e:
#    print(f"Error: {e}")
 #   driver.quit()

#sleep(5)

# Find and fill the 'From' field with the station name
from_field = driver.find_element(By.XPATH, '//*[@id="origin"]/span/input')
from_field.send_keys("KOLKATA - KOAA")
from_field.send_keys(Keys.TAB)

# Find and fill the 'To' field with the station name
to_field = driver.find_element(By.XPATH, '//*[@id="destination"]/span/input')
to_field.send_keys("NEW JALPAIGURI - NJP")
to_field.send_keys(Keys.TAB)

# Find and click the date field to open the date picker
date_field = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input')
date_field.click()

# Select a date from the date picker
date_field1 = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/div/table/tbody/tr[5]/td[5]/a')
date_field1.click()

# Open the class dropdown menu
class_field = driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div/div[3]')
class_field.click()

# Select the desired class from the dropdown
class1_field = driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div/div[4]/div/ul/li[3]/span')
class1_field.click()

# Click the 'Find Trains' button to search for trains
find_field = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button')
find_field.click()
sleep(5)

# Open the number of passengers dropdown menu
passenger_field = driver.find_element(By.XPATH, '//*[@id="numberOfPassengers"]/div/label')
passenger_field.click()

# Select the number of passengers
select_three = driver.find_element(By.XPATH, '//*[@id="numberOfPassengers"]/div/div[4]/div/ul/li[4]')
select_three.click()

# Open the class dropdown menu for modification
class_field1 = driver.find_element(By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/label')
class_field1.click()

# Select the desired class from the dropdown for modification
class1_field1 = driver.find_element(By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[3]/p-dropdown/div/div[4]/div/ul/li[5]/span')
class1_field1.click()

# Click the 'Modify Search' button
modify_search = driver.find_element(By.XPATH, '//*[@id="ui-accordiontab-0-content"]/div/div/form/div[1]/div[6]/button')
modify_search.click()
sleep(5)

# Find and click the 'Check Availability' button
check_avail = driver.find_element(By.XPATH, '//*[@id="check-availability"]')
for x in range(6):
    check_avail.send_keys(Keys.DOWN)
check_avail.click()
sleep(10)

# Find and click the 'Book Now' button
book_now = driver.find_element(By.XPATH, '//*[@id="ui-panel-0-content"]/div/div/div/table/tbody/tr/td[2]/div/div[3]/button')
book_now.click()

# Find and click the 'I Agree' button on the confirmation dialog
agree = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[1]/div/div[3]/p-footer/div/button[2]/span[2]')
agree.click()

# Find and click the OK button on the next confirmation dialog
ok1_field = driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-train-list/div/p-confirmdialog[2]/div/div[3]/p-footer/div/button[2]/span[2]')
ok1_field.click()

# Find the username field and enter your username
username_field = driver.find_element(By.XPATH, '//*[@id="userId"]')
# Enter your username between ''
username_field.send_keys('shawrajdeep00')

# Find the password field and enter your password
password_field = driver.find_element(By.XPATH, '//*[@id="pwd"]')
# Enter your password between ''
password_field.send_keys('abcd1234@123')

# Find the captcha field
captcha = driver.find_element(By.XPATH, '//*[@id="nlpAnswer"]')
# Enter the given captcha manually
sleep(15)

# Click the 'Sign In' button
sign_in = driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/button')
sign_in.click()

# Close the browser window
driver.quit()







from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(15)
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
assert  expected_url == driver.current_url, f"Invalid Credentials!"
driver.find_element(By.CLASS_NAME,"oxd-main-menu-item").click()
driver.implicitly_wait(10)
add = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]")
add.click()

select_elements = driver.find_elements(By.XPATH,"//i[contains(@class,'oxd-select-text--arrow')]")

select_elements[0].click()

wait = WebDriverWait(driver, 10)
admin_option = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@role='listbox']//span[text()='Admin']")))
admin_option.click()

select_elements[1].click()
admin_option = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@role='listbox']//span[text()='Disabled']")))
admin_option.click()


Emp_name = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]")
Emp_name.send_keys("Peter Anderson")
username = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/input[1]")
username.send_keys("Hamza")
password = driver.find_elements(By.XPATH,"//input[contains(@type,'password')]")
password[0].send_keys("Admin123.")
password[1].send_keys("Admin123.")


driver.implicitly_wait()
btn = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]")
btn.click()
user_roll_dropdown.select_by_visible_text("Admin")
driver.implicitly_wait(10)

elements= driver.find_elements(By.CLASS_NAME,"oxd-table-card")
if len(elements)>1:
    print(len(elements))
    for element in elements:
        checkbox = element.find_element(By.CLASS_NAME,"oxd-checkbox-wrapper")
        checkbox.click()
    driver.implicitly_wait(10)
    button = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]")
    driver.execute_script("arguments[0].scrollIntoView();", button)
    driver.execute_script("arguments[0].click();", button)
    delete = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]")
    driver.execute_script("arguments[0].scrollIntoView();", delete)
    driver.execute_script("arguments[0].click();", delete)
    print("Deleted")
else:
    print("lenght is 0!!")







# /html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]

# /html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]


 


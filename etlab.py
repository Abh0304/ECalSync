from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

service = Service('/Users/abhinava/Desktop/palm-chatbot-angular/Automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("https://tkmce.etlab.in/user/login")

input_element_user = driver.find_element(By.ID, "LoginForm_username")
input_element_user.clear()
input_element_user.send_keys("") #Enter your username

input_element_pass = driver.find_element(By.ID,"LoginForm_password")
input_element_pass.clear()
input_element_pass.send_keys("") #Enter your password

login = driver.find_element(By.NAME,"yt0")
login.click()

driver.get("https://tkmce.etlab.in/student/assignments")

element = driver.find_element(By.XPATH, "//a[@href='/student/assignments']")
element.click()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sem_position")))
select = Select(driver.find_element(By.ID, "sem_position"))
select.select_by_value("3") #Manual entry for semester

select = Select(driver.find_element(By.ID, "sem_position"))
print(f"✔️ Selected Semester: {select.first_selected_option.text}")

assignments = []
WebDriverWait(driver,10).until(
   EC.presence_of_element_located((By.ID,"assignments"))
)

rows = driver.find_elements(By.CSS_SELECTOR, "#assignments table.items tbody tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 6 and "NOT SUBMITTED" in cols[5].text.upper():
        assignments.append({
            "subject": cols[0].text.strip(),
            "semester": cols[1].text.strip(),
            "start_time": cols[3].text.strip(),
            "due_time": cols[4].text.strip(),
            "status": cols[5].text.strip()
        })

print(assignments)

from google_calendar import authenticate_google, add_assignment_event

service = authenticate_google()

for assignment in assignments:
    add_assignment_event(service, assignment)

input("Press Enter to exit the browser")
driver.quit()
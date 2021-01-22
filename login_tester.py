from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import smtplib

# mail credentials
gmail_user = 'mail'
gmail_password = 'password'

# mobile device login credentials
username = "user"
password = "password"

# mail message setup
subject = "problem with mobile device"
body = "problem with mobile device, it might be down"
message = "Subject: {}\n\n".format(subject) + body

# login to gmail
try:
    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail.ehlo()
    mail.login(gmail_user, gmail_password)
except:
    print("Something with the gmail login went wrong...")


# initialize the Chrome driver
driver = webdriver.Chrome(
    "/pathToChromedriver")

# head to mobile device login page
try:
    driver.get("http://mobileDevicePage")
    # find username/email field and send the username itself to the input field
    driver.find_element_by_id("UserId").send_keys(username)
    # find password input field and insert password as well
    driver.find_element_by_id("Password").send_keys(password)
    # click login button
    driver.find_element_by_name("WHSButton").click()
except:
    mail.sendmail("from_mail", "to_mail", message)
    # catch if its a connection failure

# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

# search string to determine succesfull login
# catch if connection can be established, but the main menu can't be called
text = "Main Menu"
if (text in driver.page_source):
    print("Login Successful")
else:
    print("Login Failed")
    mail.sendmail("from_mail", "to_mail", message)
driver.close()

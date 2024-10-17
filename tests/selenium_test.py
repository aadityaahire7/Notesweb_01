# Selenium Testing Done !!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.service import Service

# List of user credentials
user_credentials = [
    {"email": "bob@exampleas.com", "password": "bob12h3", "first_name": "Bob"},
    {"email": "charlie@examasdple.com", "password": "charlie123", "first_name": "Charlie"},
    {"email": "dave@exampleasd.com", "password": "dave123", "first_name": "Dave"},
    {"email": "eve@exasdample.com", "password": "eve12j3", "first_name": "Eve"},
    {"email": "frank@examasdple.com", "password": "frank123", "first_name": "Frank"},
    {"email": "grace@easdxample.com", "password": "grace123", "first_name": "Grace"},
    {"email": "hannahasd@example.com", "password": "hannah123", "first_name": "Hannah"},
    {"email": "ian@exasample.com", "password": "ian12j3", "first_name": "Ian"},
    {"email": "james@example.com", "password": "james123", "first_name": "James"},
    {"email": "karen@example.com", "password": "karen123", "first_name": "Karen"},
    {"email": "lily@example.com", "password": "lily123", "first_name": "Lily"},
    {"email": "mike@example.com", "password": "mike123", "first_name": "Mike"},
    {"email": "nina@example.com", "password": "nina123", "first_name": "Nina"},
    {"email": "oliver@example.com", "password": "oliver123", "first_name": "Oliver"},
    {"email": "paul@example.com", "password": "paul123", "first_name": "Paul"},
    {"email": "quinn@example.com", "password": "quinn123", "first_name": "Quinn"},
    {"email": "rachel@example.com", "password": "rachel123", "first_name": "Rachel"},
    {"email": "sam@example.com", "password": "sam123", "first_name": "Sam"},
    {"email": "tina@example.com", "password": "tina123", "first_name": "Tina"},
    {"email": "uma@example.com", "password": "uma123", "first_name": "Uma"},
    {"email": "victor@example.com", "password": "victor123", "first_name": "Victor"},
    {"email": "will@example.com", "password": "will123", "first_name": "Will"},
    {"email": "xena@example.com", "password": "xena123", "first_name": "Xena"},
    {"email": "yara@example.com", "password": "yara123", "first_name": "Yara"},
    {"email": "zara@example.com", "password": "zara123", "first_name": "Zara"},
    {"email": "user2@example.com", "password": "password2", "first_name": "User Two"},
    {"email": "user3@example.com", "password": "password3", "first_name": "User Three"},
    {"email": "alice@example.com", "password": "alice123", "first_name": "Alice"},
]


# URLs for the app
base_url = "http://127.0.0.1:5000"
login_url = f"{base_url}/login"
signup_url = f"{base_url}/sign-up"

# Initialize the Safari WebDriver
service = Service()  # No need for a path, SafariDriver is built into macOS
driver = webdriver.Safari(service=service)

for user in user_credentials:
    test_email = user["email"]
    test_password = user["password"]
    test_first_name = user["first_name"]

    try:
        # Test the Sign Up Functionality
        driver.get(signup_url)


        # Fill in the sign-up form
        driver.find_element(By.NAME, "email").send_keys(test_email)
        driver.find_element(By.NAME, "firstName").send_keys(test_first_name)
        driver.find_element(By.NAME, "password1").send_keys(test_password)
        driver.find_element(By.NAME, "password2").send_keys(test_password)

        # Submit the sign-up form
        driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

        # Wait for the sign-up to complete and check for success message
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account created!')]")))
        print(f"Sign Up Test Passed for {test_email}")

        # Test the Login Functionality
        driver.get(login_url)

        # Fill in the login form
        driver.find_element(By.NAME, "email").send_keys(test_email)
        driver.find_element(By.NAME, "password").send_keys(test_password)

        # Wait for the login button to be clickable and then click
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))).click()

        # Wait for the login to complete and check for successful navigation
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Note added!')] | //*[contains(text(), 'Your Notes')]")))
        print(f"Login Test Passed for {test_email}")

    except Exception as e:
        print(f"Test failed for {test_email}: {e}")
        print(f"Current URL: {driver.current_url}")
        print(f"Page Title: {driver.title}")
    finally:
        # Optional: Navigate back to the sign-up page before the next iteration
        driver.get(signup_url)

# Close the browser once all tests are done
driver.quit()



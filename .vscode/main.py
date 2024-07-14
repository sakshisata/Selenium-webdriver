from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def submit_form_and_capture_screenshot():
    chrome_driver_path = '/Users/apple/Downloads/selenium/chromedriver'

    # Configure ChromeOptions
    options = Options()
    options.headless = True  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use ChromeService and ChromeDriver with Options
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    form_url = "https://forms.gle/WT68aV5UnPajeoSc8"
    driver.get(form_url)

    try:
        # Wait for form elements to load (increase timeout to 300 seconds)
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

        # Fill out the form fields
        name_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        name_field.send_keys('Sakshi bhavesh sata')

        contact_number_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        contact_number_field.send_keys('8261002972')

        email_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        email_field.send_keys('satasakshi10@gmail.com')

        address_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        address_field.send_keys('gulmohar plaza above reliance fresh virar west')

        pin_code_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        pin_code_field.send_keys('401303')

        dob_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        dob_field.send_keys('10/02/2005')

        gender_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        gender_field.send_keys('Female')

        captcha_field = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        captcha_field.send_keys('GNFPYC')

        # Submit the form
        submit_button = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div')))
        submit_button.click()


        # Capture screenshot of confirmation page
        screenshot_path = 'confirmation.png'
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    finally:
        driver.quit()

    return screenshot_path

# Example usage:
if __name__ == "__main__":
    submit_form_and_capture_screenshot()








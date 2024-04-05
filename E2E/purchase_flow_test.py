from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.saucedemo.com/")

# Login with standard_user credentials
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

time.sleep(2) # Adding delay to ensure elements are ready

login_button.click()

# Wait for inventory container to be visible
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "inventory_container"))
)

# Find all elements containing the text "Add to cart"
add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")

# Click on the first two "Add to cart" buttons
for button in add_to_cart_buttons[:2]:
    button.click()

# Verify that at least two items have been added to the cart
assert len(add_to_cart_buttons) >= 2, "Failed to add products to cart"

time.sleep(2) # Adding delay to ensure elements are ready

# Visualize the cart
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()
# Adding a delay to ensure the page loads
driver.implicitly_wait(2)

time.sleep(2) # Adding delay to ensure elements are ready

# Proceed to checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
# Adding a delay to ensure the page loads
driver.implicitly_wait(2)

time.sleep(2) # Adding delay to ensure elements are ready

# Fill out checkout information
time.sleep(2)  # Adding delay to ensure elements are ready
first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")

first_name.send_keys("Daniel")
last_name.send_keys("Mora")
postal_code.send_keys("000")

# Assert that the correct first name, last name, and postal code are entered
assert first_name.get_attribute("value") == "Daniel", "First name entry failed"
assert last_name.get_attribute("value") == "Mora", "Last name entry failed"
assert postal_code.get_attribute("value") == "000", "Postal code entry failed"

time.sleep(2) # Adding delay to ensure elements are ready

# Proceed to complete the purchase
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
# Adding a delay to ensure the page loads
driver.implicitly_wait(2)

time.sleep(2) # Adding delay to ensure elements are ready

finish_button = driver.find_element(By.ID, "finish")
finish_button.click()
# Adding a delay to ensure the page loads
driver.implicitly_wait(2)

time.sleep(2) # Adding delay to ensure elements are ready

# Locate the checkout completion container div
completion_container = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "checkout_complete_container"))
)

time.sleep(2) # Adding delay to ensure elements are ready

# Locate the completion message within the container
completion_message = completion_container.find_element(By.CSS_SELECTOR, "h2.complete-header")

# Verify the completion message text
assert completion_message.text == "Thank you for your order!", "Failed to complete the order"

# Print completion message
print(completion_message.text)

# Close the browser
driver.quit()

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_valid(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(1)
def test_login_invalid(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    time.sleep(1)
    message = driver.find_element(By.ID, "alert").text
    assert "Warning: No match for E-Mail Address and/or Password." in message

def test_logout(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/logout']").click()
    time.sleep(1)

def test_form_submission(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    message = driver.find_element(By.ID, "alert").text
    assert "Warning: No match for E-Mail Address and/or Password." in message
def test_navigation(driver):
    driver.get("https://demo.opencart.com/home")
    driver.find_element(By.LINK_TEXT, "About Us").click()
    assert "About Us" in driver.title
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    assert "Contact Us" in driver.title
    time.sleep(1)

def test_data_validation(driver):
    driver.get("https://demo.opencart.com/home")
    time.sleep(1)
    macbook_element = driver.find_element(By.XPATH, "//a[text()='MacBook']")
    assert macbook_element.text == "MacBook", "Tên sản phẩm không khớp!"
    macbook_price_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")
    macbook_price = macbook_price_element.text.split("\n")[0]  # Lấy giá đầu tiên (không bao gồm thuế)
    assert macbook_price == "$602.00", "Giá của MacBook không khớp!"
    macbook_description_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/p")
    macbook_description = macbook_description_element.text
    expected_description = "Intel Core 2 Duo processor"
    assert expected_description in macbook_description, "Mô tả chứa thông tin mong đợi!"
    print("Tất cả dữ liệu sản phẩm MacBook đã được xác thực thành công!")
def test_add_to_cart_and_checkout(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]").click()
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle").click()
    driver.find_element(By.XPATH, "//*[@id='header-cart']/div/ul/li/div/p/a[2]").click()
    assert "Checkout" in driver.title
    time.sleep(1)
def test_search_functionality(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(1)
    driver.find_element(By.NAME, "search").send_keys("Iphone")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    time.sleep(1)
    # Kiểm tra kết quả tìm kiếm
    assert "Search - Iphone" in driver.title

@pytest.mark.parametrize("size", [(800, 600), (1024, 768), (1920, 1080)])
def test_responsive_design(driver, size):
    driver.set_window_size(*size)
    driver.get("https://demo.opencart.com/")
    time.sleep(1)
    element = driver.find_element(By.ID, "logo")
    assert element.is_displayed()
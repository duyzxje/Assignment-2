import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Khởi tạo trình duyệt Edge
@pytest.fixture
def driver():
    driver = webdriver.Edge()  # Khởi tạo trình duyệt Edge
    driver.maximize_window()  # Tối đa hóa cửa sổ trình duyệt
    yield driver  # Trả về đối tượng driver cho các bài kiểm tra
    driver.quit()  # Đóng trình duyệt sau khi kiểm tra xong

# Kiểm tra đăng nhập hợp lệ
def test_login_valid(driver):
    driver.get("https://demo.opencart.com/")  # Mở trang chính
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()  # Nhấp vào tài khoản
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()  # Nhấp vào đăng nhập
    driver.find_element(By.NAME, "email").send_keys("anhduy123456@gmail.com")  # Nhập email
    driver.find_element(By.NAME, "password").send_keys("123456")  # Nhập mật khẩu
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")  # Tìm nút đăng nhập
    submit_button.click()  # Nhấp vào nút đăng nhập

# Kiểm tra đăng nhập không hợp lệ
def test_login_invalid(driver):
    driver.get("https://demo.opencart.com/")  # Mở trang chính
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()  # Nhấp vào tài khoản
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()  # Nhấp vào đăng nhập
    driver.find_element(By.NAME, "email").send_keys("anhduy123456@gmail.com")  # Nhập email
    driver.find_element(By.NAME, "password").send_keys("123")  # Nhập mật khẩu sai
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")  # Tìm nút đăng nhập
    submit_button.click()  # Nhấp vào nút đăng nhập
    time.sleep(1)  # Chờ 1 giây
    message = driver.find_element(By.ID, "alert").text  # Lấy thông báo lỗi
    assert "Warning: No match for E-Mail Address and/or Password." in message  # Kiểm tra thông báo lỗi

# Kiểm tra đăng xuất
def test_logout(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")  # Mở trang đăng nhập
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.NAME, "email").send_keys("anhduy123456@gmail.com")  # Nhập email
    driver.find_element(By.NAME, "password").send_keys("123456")  # Nhập mật khẩu
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")  # Tìm nút đăng nhập
    submit_button.click()  # Nhấp vào nút đăng nhập
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()  # Nhấp vào tài khoản
    time.sleep(2) 
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/logout']").click()  # Nhấp vào đăng xuất
    time.sleep(1)  # Chờ 1 giây

# Kiểm tra gửi biểu mẫu
def test_form_submission(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/login")  # Mở trang đăng nhập
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")  # Nhập email
    driver.find_element(By.NAME, "password").send_keys("123")  # Nhập mật khẩu sai
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()  # Nhấp vào nút đăng nhập
    message = driver.find_element(By.ID, "alert").text  # Lấy thông báo lỗi
    assert "Warning: No match for E-Mail Address and/or Password." in message  # Kiểm tra thông báo lỗi

# Kiểm tra điều hướng
def test_navigation(driver):
    driver.get("https://demo.opencart.com/home")  # Mở trang chính
    driver.find_element(By.LINK_TEXT, "About Us").click()  # Nhấp vào "Giới thiệu"
    assert "About Us" in driver.title  # Kiểm tra tiêu đề trang
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.LINK_TEXT, "Contact Us").click()  # Nhấp vào "Liên hệ"
    assert "Contact Us" in driver.title  # Kiểm tra tiêu đề trang
    time.sleep(1)  # Chờ 1 giây

# Kiểm tra xác thực dữ liệu
def test_data_validation(driver):
    driver.get("https://demo.opencart.com/home")  # Mở trang chính
    time.sleep(1)  # Chờ 1 giây
    macbook_element = driver.find_element(By.XPATH, "//a[text()='MacBook']")  # Tìm phần tử MacBook
    assert macbook_element.text == "MacBook", "Tên sản phẩm không khớp!"  # Kiểm tra tên sản phẩm
    macbook_price_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")  # Tìm giá MacBook
    macbook_price = macbook_price_element.text.split("\n")[0]  # Lấy giá đầu tiên (không bao gồm thuế)
    assert macbook_price == "$602.00", "Giá của MacBook không khớp!"  # Kiểm tra giá
    macbook_description_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/p")  # Tìm mô tả MacBook
    macbook_description = macbook_description_element.text  # Lấy mô tả
    expected_description = "Intel Core 2 Duo processor"  # Mô tả mong đợi
    assert expected_description in macbook_description, "Mô tả chứa thông tin mong đợi!"  # Kiểm tra mô tả
    print("Tất cả dữ liệu sản phẩm MacBook đã được xác thực thành công!")  # In thông báo xác thực thành công

# Kiểm tra thêm vào giỏ hàng và thanh toán
def add_to_cart(driver):
    # Mở trang đăng nhập
    driver.get("https://demo.opencart.com/index.php?route=account/login")

    # Khởi tạo WebDriverWait với thời gian chờ tối đa
    wait = WebDriverWait(driver, 3)  # Thay đổi 10 thành thời gian chờ tối đa bạn mong muốn

    # Chờ cho trường email có thể nhìn thấy và nhập email
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    email_field.send_keys("anhduy123456@gmail.com")

    # Chờ cho trường mật khẩu có thể nhìn thấy và nhập mật khẩu
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    password_field.send_keys("123456")

    time.sleep(3)  # Chờ trang tải xong

    # Chờ cho nút đăng nhập có thể nhấp được và nhấn
    login_button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button")
    login_button.click()

    # Chờ cho việc đăng nhập hoàn tất (kiểm tra tiêu đề trang hoặc một phần tử nào đó)
    wait.until(EC.title_contains("My Account"))  # Kiểm tra tiêu đề trang nếu đăng nhập thành công
    driver.get(
        "https://demo.opencart.com/index.php?route=product/product&product_id=44")  # Cập nhật với ID sản phẩm hợp lệ
    wait = WebDriverWait(driver, 10)

    time.sleep(10)  # Chờ trang tải xong
    # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_to_cart_button.click()
    time.sleep(10)  # Chờ trang tải xong

    # Đi đến giỏ hàng
    driver.get("https://demo.opencart.com/index.php?route=checkout/cart")

    time.sleep(10)  # Chờ giỏ hàng cập nhật

    # Chọn nút thanh toán
    checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkout")))
    checkout_button.click()

    time.sleep(10)
def test_add_to_cart_and_checkout(driver):
    add_to_cart(driver)
    select_element = driver.find_element(By.NAME, "address_id")
    # Tạo đối tượng Select
    select = Select(select_element)

    # Chọn theo giá trị (value)
    select.select_by_value("1156")
    time.sleep(5)


    button_choose_payment = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button")
    button_choose_payment.click()
    time.sleep(5)
    button_option = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[1]/label")
    button_option.click()
    time.sleep(5)
    button_submit = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/button")
    button_submit.click()
    time.sleep(5)

    button_choose_shipment = driver.find_element(By.XPATH,
                                                "/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button")
    button_choose_shipment.click()
    time.sleep(5)
    button_option = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/label")
    button_option.click()
    time.sleep(5)
    button_submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/button")
    button_submit.click()
    time.sleep(5)

    button_confirm = driver.find_element(By.XPATH,
                                                "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
    button_confirm.click()

    # Kiểm tra thông báo thành công
    try:
        success_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div/h1, 'Your order has been placed!')]"))
        )
        assert success_message.is_displayed(), "Success message not displayed."
        print("Đơn hàng đã được đặt thành công.")
    except Exception as e:
        print("Đặt hàng không thành công.")
        print(e)

# Kiểm tra chức năng tìm kiếm
def test_search_functionality(driver):
    driver.get("https://demo.opencart.com/")  # Mở trang chính
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.NAME, "search").send_keys("Iphone")  # Nhập từ khóa tìm kiếm
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()  # Nhấp vào nút tìm kiếm
    time.sleep(1)  # Chờ 1 giây
    assert "Search - Iphone" in driver.title  # Kiểm tra tiêu đề trang tìm kiếm

# Kiểm tra thiết kế đáp ứng
@pytest.mark.parametrize("size", [(800, 600), (1024, 768), (1920, 1080)])  # Thử nghiệm với các kích thước khác nhau
def test_responsive_design(driver, size):
    driver.set_window_size(*size)  # Đặt kích thước cửa sổ
    driver.get("https://demo.opencart.com/")  # Mở trang chính
    time.sleep(1)  # Chờ 1 giây
    element = driver.find_element(By.ID, "logo")  # Tìm phần tử logo
    assert element.is_displayed()  # Kiểm tra xem logo có hiển thị không
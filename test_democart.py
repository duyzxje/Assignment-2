import pytest  # Thư viện pytest để viết và chạy các bài kiểm tra
import time  # Thư viện time để sử dụng hàm sleep
from selenium import webdriver  # Thư viện selenium để tự động hóa trình duyệt
from selenium.webdriver.common.by import By  # Để sử dụng các phương thức tìm kiếm phần tử

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
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")  # Nhập email
    driver.find_element(By.NAME, "password").send_keys("123456")  # Nhập mật khẩu
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")  # Tìm nút đăng nhập
    submit_button.click()  # Nhấp vào nút đăng nhập

# Kiểm tra đăng nhập không hợp lệ
def test_login_invalid(driver):
    driver.get("https://demo.opencart.com/")  # Mở trang chính
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()  # Nhấp vào tài khoản
    driver.find_element(By.CSS_SELECTOR, "a.dropdown-item[href*='route=account/login']").click()  # Nhấp vào đăng nhập
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")  # Nhập email
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
    driver.find_element(By.NAME, "email").send_keys("duy@gmail.com")  # Nhập email
    driver.find_element(By.NAME, "password").send_keys("123456")  # Nhập mật khẩu
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")  # Tìm nút đăng nhập
    submit_button.click()  # Nhấp vào nút đăng nhập
    driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/a").click()  # Nhấp vào tài khoản
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
def test_add_to_cart_and_checkout(driver):
    driver.get("https://demo.opencart.com/")  # Mở trang chính
    time.sleep(1)  # Chờ 1 giây
    driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]").click()  # Nhấp vào nút thêm vào giỏ hàng
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-inverse.btn-block.dropdown-toggle").click()  # Nhấp vào giỏ hàng
    driver.find_element(By.XPATH, "//*[@id='header-cart']/div/ul/li/div/p/a[2]").click()  # Nhấp vào thanh toán
    assert "Checkout" in driver.title  # Kiểm tra tiêu đề trang thanh toán
    time.sleep(1)  # Chờ 1 giây

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
# Demo Cart Automation Tests

## Mô tả
Dự án này chứa các bài kiểm tra tự động cho trang web Demo OpenCart bằng cách sử dụng Python, Pytest và Selenium. Các bài kiểm tra bao gồm đăng nhập, đăng xuất, xác thực dữ liệu, và kiểm tra chức năng tìm kiếm.

## Yêu cầu
- Python 3.x
- Pytest
- Selenium
- Trình điều khiển Web (ví dụ: Edge WebDriver)

## Cài đặt
1. Cài đặt Python từ [python.org](https://www.python.org/downloads/).
2. Cài đặt các thư viện cần thiết:
   ```bash
   pip install pytest selenium
   ```
3. Tải xuống và cài đặt trình điều khiển Web tương ứng với trình duyệt bạn đang sử dụng (ví dụ: [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)).

## Cách sử dụng
1. Chạy các bài kiểm tra bằng lệnh sau:
   ```bash
   pytest test_democart.py
   ```

## Các bài kiểm tra
- `test_login_valid`: Kiểm tra đăng nhập hợp lệ.
- `test_login_invalid`: Kiểm tra đăng nhập không hợp lệ.
- `test_logout`: Kiểm tra chức năng đăng xuất.
- `test_form_submission`: Kiểm tra việc gửi biểu mẫu với thông tin không hợp lệ.
- `test_navigation`: Kiểm tra điều hướng đến các trang khác nhau.
- `test_data_validation`: Xác thực dữ liệu sản phẩm MacBook.
- `test_add_to_cart_and_checkout`: Kiểm tra chức năng thêm vào giỏ hàng và thanh toán.
- `test_search_functionality`: Kiểm tra chức năng tìm kiếm.
- `test_responsive_design`: Kiểm tra thiết kế đáp ứng với các kích thước màn hình khác nhau.

## Ghi chú
- Đảm bảo rằng trình duyệt và trình điều khiển Web tương ứng đã được cài đặt và cấu hình đúng cách.
- Các bài kiểm tra có thể yêu cầu thời gian chờ để đảm bảo rằng các phần tử trên trang đã được tải hoàn toàn.

## Liên hệ
Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ với tôi qua email: [duyzxje2110@gmail.com](mailto:duyzxje2110@gmail.com).
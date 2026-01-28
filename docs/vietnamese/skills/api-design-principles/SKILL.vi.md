---
name: api-design-principles
description: Làm chủ các nguyên tắc thiết kế REST và GraphQL API để xây dựng các API trực quan, có khả năng mở rộng và dễ bảo trì, làm hài lòng các nhà phát triển. Sử dụng khi thiết kế API mới, xem xét đặc tả API, hoặc thiết lập các tiêu chuẩn thiết kế API.
---

# Nguyên tắc Thiết kế API (API Design Principles)

Làm chủ các nguyên tắc thiết kế REST và GraphQL API để xây dựng các API trực quan, có khả năng mở rộng và dễ bảo trì, làm hài lòng các nhà phát triển và bền vững theo thời gian.

## Sử dụng kỹ năng này khi

- Thiết kế REST hoặc GraphQL APIs mới
- Refactoring các API hiện có để cải thiện tính khả dụng
- Thiết lập tiêu chuẩn thiết kế API cho team của bạn
- Review đặc tả API (API specifications) trước khi cài đặt
- Chuyển đổi giữa các mô hình API (REST sang GraphQL, v.v.)
- Tạo tài liệu API thân thiện với developer
- Tối ưu hóa API cho các use case cụ thể (mobile, tích hợp bên thứ ba)

## Không sử dụng kỹ năng này khi

- Bạn chỉ cần hướng dẫn cài đặt cho một framework cụ thể
- Bạn đang làm việc thuần túy về hạ tầng mà không có hợp đồng API (API contracts)
- Bạn không thể thay đổi hoặc đánh phiên bản các giao diện public

## Hướng dẫn

1. Xác định người tiêu dùng, use cases, và các ràng buộc.
2. Chọn phong cách API (REST/GraphQL) và mô hình hóa tài nguyên hoặc types.
3. Chỉ định lỗi, đánh phiên bản (versioning), phân trang (pagination), và chiến lược xác thực (auth strategy).
4. Xác nhận bằng các ví dụ và review tính nhất quán.

Tham khảo `resources/implementation-playbook.md` để biết các mẫu chi tiết, danh sách kiểm tra và templates.

## Tài nguyên

- `resources/implementation-playbook.md` cho các mẫu chi tiết, danh sách kiểm tra và templates.

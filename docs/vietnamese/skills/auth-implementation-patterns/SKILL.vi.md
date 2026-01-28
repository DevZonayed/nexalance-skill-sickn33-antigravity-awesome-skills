---
name: auth-implementation-patterns
description: Làm chủ các mẫu xác thực (authentication) và phân quyền (authorization) bao gồm JWT, OAuth2, quản lý phiên (session management), và RBAC để xây dựng các hệ thống kiểm soát truy cập an toàn, có khả năng mở rộng. Sử dụng khi triển khai hệ thống auth, bảo mật API, hoặc gỡ lỗi các vấn đề bảo mật.
---

# Các Mẫu Triển khai Xác thực & Phân quyền

Xây dựng hệ thống xác thực và phân quyền an toàn, có khả năng mở rộng bằng cách sử dụng các tiêu chuẩn công nghiệp và thực hành tốt nhất hiện đại.

## Sử dụng kỹ năng này khi

- Triển khai hệ thống xác thực người dùng
- Bảo mật REST hoặc GraphQL APIs
- Thêm OAuth2/social login hoặc SSO
- Thiết kế quản lý phiên hoặc RBAC
- Gỡ lỗi các vấn đề xác thực hoặc phân quyền

## Không sử dụng kỹ năng này khi

- Bạn chỉ cần nội dung giao diện người dùng (UI copy) hoặc styling trang đăng nhập
- Nhiệm vụ thuần túy về hạ tầng không liên quan đến định danh (identity)
- Bạn không thể thay đổi chính sách auth hoặc lưu trữ thông tin đăng nhập

## Hướng dẫn

- Xác định người dùng, người thuê (tenants), các luồng (flows), và các ràng buộc mô hình mối đe dọa (threat model).
- Chọn chiến lược auth (session, JWT, OIDC) và vòng đời token.
- Thiết kế mô hình phân quyền và các điểm thực thi chính sách (policy enforcement points).
- Lập kế hoạch lưu trữ bí mật (secrets), xoay vòng (rotation), ghi log, và các yêu cầu kiểm toán (audit).
- Nếu cần các ví dụ chi tiết, hãy mở `resources/implementation-playbook.md`.

## An toàn

- Không bao giờ ghi log bí mật, tokens, hoặc thông tin đăng nhập.
- Thực thi nguyên tắc đặc quyền tối thiểu (least privilege) và lưu trữ an toàn cho các khóa (keys).

## Tài nguyên

- `resources/implementation-playbook.md` cho các mẫu và ví dụ chi tiết.

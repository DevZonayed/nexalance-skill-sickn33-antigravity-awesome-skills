---
name: api-security-best-practices
description: "Triển khai các mẫu thiết kế API an toàn bao gồm xác thực (authentication), phân quyền (authorization), xác thực đầu vào (input validation), giới hạn tốc độ (rate limiting), và bảo vệ chống lại các lổ hổng API phổ biến."
---

# Thực hành Tốt nhất về Bảo mật API (API Security Best Practices)

## Tổng quan

Hướng dẫn các lập trình viên xây dựng API an toàn bằng cách triển khai xác thực, phân quyền, xác thực đầu vào, giới hạn tốc độ và bảo vệ chống lại các lổ hổng phổ biến. Kỹ năng này bao gồm các mẫu bảo mật cho REST, GraphQL và WebSocket APIs.

## Khi nào Sử dụng Kỹ năng này

- Sử dụng khi thiết kế các API endpoints mới
- Sử dụng khi bảo mật các API hiện có
- Sử dụng khi triển khai xác thực và phân quyền
- Sử dụng khi bảo vệ chống lại các cuộc tấn công API (injection, DDoS, v.v.)
- Sử dụng khi thực hiện đánh giá bảo mật API
- Sử dụng khi chuẩn bị cho kiểm toán bảo mật (security audits)
- Sử dụng khi triển khai giới hạn tốc độ và điều tiết (throttling)
- Sử dụng khi xử lý dữ liệu nhạy cảm trong APIs

## Cách Thức Hoạt động

### Bước 1: Xác thực & Phân quyền
Tôi sẽ giúp bạn triển khai xác thực an toàn:
- Chọn phương thức xác thực (JWT, OAuth 2.0, API keys)
- Triển khai xác thực dựa trên token
- Thiết lập kiểm soát truy cập dựa trên vai trò (RBAC)
- Quản lý phiên an toàn
- Triển khai xác thực đa yếu tố (MFA)

### Bước 2: Xác thực & Làm sạch Đầu vào
Bảo vệ chống lại các cuộc tấn công injection:
- Validate tất cả dữ liệu đầu vào
- Làm sạch (Sanitize) đầu vào của người dùng
- Sử dụng parameterized queries
- Triển khai validation request schema
- Ngăn chặn SQL injection, XSS, và command injection

### Bước 3: Giới hạn Tốc độ & Điều tiết
Ngăn chặn lạm dụng và tấn công DDoS:
- Triển khai rate limiting theo user/IP
- Thiết lập API throttling
- Cấu hình hạn ngạch yêu cầu (request quotas)
- Xử lý lỗi rate limit một cách nhẹ nhàng
- Giám sát các hoạt động đáng ngờ

### Bước 4: Bảo vệ Dữ liệu
Bảo mật dữ liệu nhạy cảm:
- Mã hóa dữ liệu khi truyền tải (HTTPS/TLS)
- Mã hóa dữ liệu nhạy cảm khi lưu trữ (at rest)
- Triển khai xử lý lỗi đúng cách (không rò rỉ dữ liệu)
- Làm sạch thông báo lỗi
- Sử dụng các header bảo mật

### Bước 5: Kiểm thử Bảo mật API
Xác minh việc triển khai bảo mật:
- Test xác thực và phân quyền
- Thực hiện kiểm thử thâm nhập (penetration testing)
- Kiểm tra các lổ hổng phổ biến (OWASP API Top 10)
- Validate việc xử lý đầu vào
- Test rate limiting

## Ví dụ

### Ví dụ 1: Triển khai Xác thực JWT
*(Giữ nguyên code examples vì là code kỹ thuật)*

### Các thực hành Tốt nhất về Bảo mật (Security Best Practices)
- ✅ Sử dụng bí mật JWT mạnh (tối thiểu 256-bit)
- ✅ Đặt thời gian hết hạn ngắn (1 giờ cho access tokens)
- ✅ Triển khai refresh tokens cho các phiên dài hạn
- ✅ Lưu trữ refresh tokens trong database (có thể thu hồi)
- ✅ Chỉ sử dụng HTTPS
- ✅ Không lưu trữ dữ liệu nhạy cảm trong JWT payload
- ✅ Validate token issuer và audience
- ✅ Triển khai danh sách đen token (token blacklisting) cho đăng xuất

### Ví dụ 2: Ngăn chặn SQL Injection và Xác thực Đầu vào
*(Giữ nguyên code examples)*

### Danh sách kiểm tra Validation
- [ ] Validate tất cả đầu vào của người dùng
- [ ] Sử dụng parameterized queries hoặc ORM
- [ ] Validate kiểu dữ liệu (string, number, email, v.v.)
- [ ] Validate phạm vi dữ liệu (độ dài min/max, khoảng giá trị)
- [ ] Làm sạch nội dung HTML
- [ ] Escape các ký tự đặc biệt
- [ ] Validate file uploads (loại, kích thước, nội dung)
- [ ] Sử dụng danh sách cho phép (allowlists), không dùng danh sách chặn (blocklists)

### Ví dụ 3: Rate Limiting và Bảo vệ DDoS
*(Giữ nguyên code examples)*

## Thực hành Tốt nhất (Best Practices)

### ✅ Nên làm
- **Sử dụng HTTPS mọi nơi** - Không bao giờ gửi dữ liệu nhạy cảm qua HTTP
- **Triển khai Xác thực** - Yêu cầu xác thực cho các protected endpoints
- **Validate Tất cả Đầu vào** - Không bao giờ tin tưởng đầu vào của người dùng
- **Sử dụng Parameterized Queries** - Ngăn chặn SQL injection
- **Triển khai Rate Limiting** - Bảo vệ chống brute force và DDoS
- **Hash Mật khẩu** - Sử dụng bcrypt với salt rounds >= 10
- **Sử dụng Token Ngắn hạn** - JWT access tokens nên hết hạn nhanh chóng
- **Triển khai CORS Đúng cách** - Chỉ cho phép các nguồn tin cậy (trusted origins)
- **Ghi log Sự kiện Bảo mật** - Giám sát hoạt động đáng ngờ
- **Luôn Cập nhật Dependencies** - Cập nhật các gói thường xuyên
- **Sử dụng Security Headers** - Triển khai Helmet.js
- **Làm sạch Thông báo Lỗi** - Không rò rỉ thông tin nhạy cảm

### ❌ Không nên làm
- **Đừng Lưu Password dạng Plain Text** - Luôn hash mật khẩu
- **Đừng Dùng Bí mật Yếu** - Sử dụng JWT secrets mạnh, ngẫu nhiên
- **Đừng Tin tưởng Đầu vào Người dùng** - Luôn validate và sanitize
- **Đừng Để lộ Stack Traces** - Ẩn chi tiết lỗi trong production
- **Đừng Dùng Cộng chuỗi cho SQL** - Sử dụng parameterized queries
- **Đừng Lưu Dữ liệu Nhạy cảm trong JWT** - JWT không được mã hóa
- **Đừng Phớt lờ Cập nhật Bảo mật** - Cập nhật dependencies thường xuyên
- **Đừng Dùng Thông tin đăng nhập Mặc định** - Thay đổi tất cả mật khẩu mặc định
- **Đừng Tắt CORS Hoàn toàn** - Cấu hình nó đúng cách thay vì tắt
- **Đừng Ghi log Dữ liệu Nhạy cảm** - Sanitize logs

## Các Bẫy Phổ biến (Common Pitfalls)

### Vấn đề: Lộ JWT Secret trong Code
**Triệu chứng:** JWT secret bị hardcode hoặc commit lên Git
**Giải pháp:** Dùng biến môi trường (`process.env.JWT_SECRET`)

### Vấn đề: Yêu cầu Mật khẩu Yếu
**Triệu chứng:** Người dùng có thể đặt mật khẩu yếu như "password123"
**Giải pháp:** Sử dụng thư viện validate như zxcvbn hoặc regex mạnh.

### Vấn đề: Thiếu Kiểm tra Phân quyền
**Triệu chứng:** Người dùng có thể truy cập tài nguyên họ không nên thấy
**Giải pháp:** Kiểm tra quyền sở hữu hoặc vai trò admin trước khi thực hiện hành động.

### Vấn đề: Thông báo Lỗi Quá Chi tiết
**Triệu chứng:** Thông báo lỗi tiết lộ chi tiết hệ thống (VD: tên bảng db)
**Giải pháp:** Trả về thông báo lỗi chung chung cho client, log chi tiết lỗi ở server.

## Danh sách Kiểm tra Bảo mật (Security Checklist)

### Xác thực & Phân quyền
- [ ] Triển khai xác thực mạnh (JWT, OAuth 2.0)
- [ ] Sử dụng HTTPS cho tất cả endpoints
- [ ] Hash mật khẩu với bcrypt (salt rounds >= 10)
- [ ] Triển khai hết hạn token
- [ ] Thêm cơ chế refresh token
- [ ] Xác minh phân quyền người dùng cho mỗi yêu cầu
- [ ] Triển khai kiểm soát truy cập dựa trên vai trò (RBAC)

### Xác thực Đầu vào
- [ ] Validate tất cả đầu vào người dùng
- [ ] Sử dụng parameterized queries hoặc ORM
- [ ] Làm sạch nội dung HTML
- [ ] Validate file uploads
- [ ] Triển khai request schema validation
- [ ] Sử dụng allowlists, không dùng blocklists

### Rate Limiting & Bảo vệ DDoS
- [ ] Triển khai rate limiting theo user/IP
- [ ] Thêm giới hạn nghiêm ngặt hơn cho auth endpoints
- [ ] Sử dụng Redis cho rate limiting phân tán
- [ ] Trả về header rate limit đúng chuẩn
- [ ] Triển khai request throttling

### Bảo vệ Dữ liệu
- [ ] Sử dụng HTTPS/TLS cho tất cả lưu lượng
- [ ] Mã hóa dữ liệu nhạy cảm khi lưu trữ
- [ ] Không lưu dữ liệu nhạy cảm trong JWT
- [ ] Làm sạch thông báo lỗi
- [ ] Triển khai cấu hình CORS đúng cách
- [ ] Sử dụng security headers (Helmet.js)

### Giám sát & Logging
- [ ] Ghi log các sự kiện bảo mật
- [ ] Giám sát hoạt động đáng ngờ
- [ ] Thiết lập cảnh báo cho các lần thử auth thất bại
- [ ] Theo dõi các mẫu sử dụng API
- [ ] Không ghi log dữ liệu nhạy cảm

## OWASP API Security Top 10

1. **Broken Object Level Authorization** - Luôn xác minh người dùng có thể truy cập tài nguyên
2. **Broken Authentication** - Triển khai cơ chế xác thực mạnh
3. **Broken Object Property Level Authorization** - Validate thuộc tính nào người dùng có thể truy cập
4. **Unrestricted Resource Consumption** - Triển khai rate limiting và quotas
5. **Broken Function Level Authorization** - Xác minh vai trò người dùng cho mỗi chức năng
6. **Unrestricted Access to Sensitive Business Flows** - Bảo vệ các luồng công việc quan trọng
7. **Server Side Request Forgery (SSRF)** - Validate và sanitize URLs
8. **Security Misconfiguration** - Sử dụng thực hành tốt nhất về bảo mật và headers
9. **Improper Inventory Management** - Tài liệu hóa và bảo mật tất cả API endpoints
10. **Unsafe Consumption of APIs** - Validate dữ liệu từ APIs bên thứ ba

## Tài nguyên Bổ sung

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [JWT Best Practices](https://tools.ietf.org/html/rfc8725)
- [Express Security Best Practices](https://expressjs.com/en/advanced/best-practice-security.html)
- [Node.js Security Checklist](https://blog.risingstack.com/node-js-security-checklist/)
- [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist)

---

**Mẹo chuyên nghiệp:** Bảo mật không phải là nhiệm vụ một lần - hãy thường xuyên kiểm toán API của bạn, cập nhật dependencies, và cập nhật thông tin về các lổ hổng mới!

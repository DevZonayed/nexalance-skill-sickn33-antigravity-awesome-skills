---
name: azure-functions
description: "Các mẫu chuyên gia cho phát triển Azure Functions bao gồm mô hình isolated worker, điều phối Durable Functions, tối ưu hóa cold start, và các mẫu production. Bao gồm các mô hình lập trình .NET, Python, và Node.js. Sử dụng khi: azure function, azure functions, durable functions, azure serverless, function app."
source: vibeship-spawner-skills (Apache 2.0)
---

# Azure Functions

## Các Mẫu (Patterns)

### Mô hình Isolated Worker (.NET)

Mô hình thực thi .NET hiện đại với sự cách ly tiến trình (process isolation).

### Mô hình Lập trình Node.js v4

Cách tiếp cận tập trung vào code (code-centric) hiện đại cho TypeScript/JavaScript.

### Mô hình Lập trình Python v2

Cách tiếp cận dựa trên Decorator cho Python functions.

## Anti-Patterns (Nên tránh)

### ❌ Các Cuộc gọi Async Bị Chặn (Blocking Async Calls)

### ❌ Tạo HttpClient Mới cho Mỗi Yêu cầu (New HttpClient Per Request)

### ❌ Mô hình In-Process cho Dự Án Mới

## ⚠️ Các Cạnh Sắc (Rủi ro)

| Vấn đề | Mức độ nghiêm trọng | Giải pháp |
|-------|----------|----------|
| Vấn đề time-out | cao | ## Sử dụng mẫu async với Durable Functions |
| Cạn kiệt socket | cao | ## Sử dụng IHttpClientFactory (Khuyên dùng) |
| Deadlock | cao | ## Luôn sử dụng async/await |
| Timeout mặc định ngắn | trung bình | ## Cấu hình thời gian chờ tối đa (Consumption plan) |
| Phiên bản .NET xung đột | cao | ## Sử dụng isolated worker cho dự án mới |
| Thiếu log | trung bình | ## Cấu hình Application Insights đúng cách |
| Lỗi binding | trung bình | ## Kiểm tra extension bundle (phổ biến nhất) |
| Cold Start | trung bình | ## Thêm warmup trigger để khởi tạo code của bạn |

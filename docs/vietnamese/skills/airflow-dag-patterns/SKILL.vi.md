---
name: airflow-dag-patterns
description: Xây dựng các Apache Airflow DAGs cấp production với các thực hành tốt nhất cho operators, sensors, kiểm thử và triển khai. Sử dụng khi tạo đường ống dữ liệu (data pipelines), điều phối luồng công việc (orchestrating workflows), hoặc lập lịch các tác vụ batch (batch jobs).
---

# Các Mẫu Apache Airflow DAG

Các mẫu sẵn sàng cho production cho Apache Airflow bao gồm thiết kế DAG, operators, sensors, chiến lược kiểm thử và triển khai.

## Sử dụng kỹ năng này khi

- Tạo điều phối đường ống dữ liệu với Airflow
- Thiết kế cấu trúc DAG và các phụ thuộc
- Triển khai custom operators và sensors
- Kiểm thử Airflow DAGs cục bộ
- Thiết lập Airflow trong production
- Gỡ lỗi các lần chạy DAG bị thất bại

## Không sử dụng kỹ năng này khi

- Bạn chỉ cần một cron job đơn giản hoặc shell script
- Airflow không phải là một phần của bộ công cụ
- Nhiệm vụ không liên quan đến điều phối luồng công việc

## Hướng dẫn

1. Xác định nguồn dữ liệu, lịch trình và các phụ thuộc.
2. Thiết kế các tác vụ idempotent (có thể chạy lại nhiều lần mà kết quả không đổi) với quyền sở hữu rõ ràng và cơ chế thử lại (retries).
3. Triển khai DAGs với khả năng quan sát (observability) và hooks cảnh báo.
4. Xác nhận trong môi trường staging và tài liệu hóa sổ tay vận hành (operational runbooks).

Tham khảo `resources/implementation-playbook.md` để biết các mẫu chi tiết, danh sách kiểm tra và templates.

## An toàn

- Tránh thay đổi lịch trình DAG production mà không được phê duyệt.
- Kiểm thử backfills và retries cẩn thận để ngăn chặn trùng lặp dữ liệu.

## Tài nguyên

- `resources/implementation-playbook.md` cho các mẫu chi tiết, danh sách kiểm tra và templates.

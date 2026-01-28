---
name: aws-serverless
description: "Kỹ năng chuyên biệt để xây dựng các ứng dụng serverless sẵn sàng cho production trên AWS. Bao gồm Lambda functions, API Gateway, DynamoDB, các mẫu hướng sự kiện SQS/SNS, triển khai SAM/CDK, và tối ưu hóa cold start."
source: vibeship-spawner-skills (Apache 2.0)
---

# AWS Serverless

## Các Mẫu (Patterns)

### Mẫu Lambda Handler

Cấu trúc Lambda function đúng chuẩn với xử lý lỗi.

**Khi nào dùng**: ['Bất kỳ triển khai Lambda function nào', 'API handlers, bộ xử lý sự kiện, tác vụ định kỳ']

```javascript
// Node.js Lambda Handler
// handler.js

// Khởi tạo bên ngoài handler (tái sử dụng qua các lần gọi)
const { DynamoDBClient } = require('@aws-sdk/client-dynamodb');
const { DynamoDBDocumentClient, GetCommand } = require('@aws-sdk/lib-dynamodb');

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

// Hàm Handler
exports.handler = async (event, context) => {
  // Tùy chọn: Không đợi event loop trống (Node.js) có thể giúp function kết thúc sớm hơn
  context.callbackWaitsForEmptyEventLoop = false;

  try {
    // Parse input dựa trên nguồn sự kiện
    const body = typeof event.body === 'string'
      ? JSON.parse(event.body)
      : event.body;

    // Logic nghiệp vụ
    const result = await processRequest(body);

    // Trả về phản hồi tương thích API Gateway
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(result)
    };
  } catch (error) {
    console.error('Error:', JSON.stringify({
      error: error.message,
      stack: error.stack,
      requestId: context.awsRequestId
    }));

    return {
      statusCode: error.statusCode || 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        error: error.message || 'Internal server error'
      })
    };
  }
};

async function processRequest(data) {
  // Logic nghiệp vụ của bạn ở đây
  const result = await docClient.send(new GetCommand({
    TableName: process.env.TABLE_NAME,
    Key: { id: data.id }
  }));
  return result.Item;
}
```

### Mẫu Tích hợp API Gateway

Tích hợp REST API và HTTP API với Lambda.

**Khi nào dùng**: ['Xây dựng REST APIs bằng Lambda', 'Cần các HTTP endpoints cho functions']

```yaml
# template.yaml (SAM)
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Globals:
  Function:
    Runtime: nodejs20.x
    Timeout: 30
    MemorySize: 256
    Environment:
      Variables:
        TABLE_NAME: !Ref ItemsTable

Resources:
  # HTTP API (khuyên dùng cho các trường hợp đơn giản, hiệu năng cao, rẻ hơn)
  HttpApi:
    Type: AWS::Serverless::HttpApi
    Properties:
      StageName: prod
      CorsConfiguration:
        AllowOrigins:
          - "*"
        AllowMethods:
          - GET
          - POST
          - DELETE
        AllowHeaders:
          - "*"

  # Lambda Functions
  GetItemFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/get.handler
      Events:
        GetItem:
          Type: HttpApi
          Properties:
            ApiId: !Ref HttpApi
            Path: /items/{id}
            Method: GET
      Policies:
        - DynamoDBReadPolicy:
            TableName: !Ref ItemsTable

  CreateItemFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/create.handler
      Events:
        CreateItem:
          Type: HttpApi
          Properties:
            ApiId: !Ref HttpApi
            Path: /items
            Method: POST
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref ItemsTable

  # DynamoDB Table
  ItemsTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST

Outputs:
  ApiUrl:
    Value: !Sub "https://${HttpApi}.execute-api.${AWS::Region}.amazonaws.com/prod"
```

### Mẫu SQS Hướng Sự Kiện (Event-Driven SQS Pattern)

Lambda được kích hoạt bởi SQS để xử lý không đồng bộ tin cậy.

**Khi nào dùng**: ['Xử lý không đồng bộ, tách biệt (decoupled)', 'Cần logic thử lại và Dead Letter Queue (DLQ)', 'Xử lý tin nhắn theo lô (batches)']

```yaml
# template.yaml
Resources:
  ProcessorFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: src/handlers/processor.handler
      Events:
        SQSEvent:
          Type: SQS
          Properties:
            Queue: !GetAtt ProcessingQueue.Arn
            BatchSize: 10
            FunctionResponseTypes:
              - ReportBatchItemFailures  # Xử lý thất bại từng phần trong lô
```

```javascript
// src/handlers/processor.js
exports.handler = async (event) => {
  const batchItemFailures = [];

  for (const record of event.Records) {
    try {
      const body = JSON.parse(record.body);
      await processMessage(body);
    } catch (error) {
      console.error(`Failed to process message ${record.messageId}:`, error);
      // Báo cáo item này bị lỗi (để SQS thử lại chỉ item này)
      batchItemFailures.push({
        itemIdentifier: record.messageId
      });
    }
  }

  // Trả về các item thất bại để thử lại
  return { batchItemFailures };
};
```

## Anti-Patterns (Nên tránh)

### ❌ Monolithic Lambda

**Tại sao tệ**: Gói triển khai lớn gây cold start chậm.
Khó mở rộng các hoạt động riêng lẻ.
Cập nhật ảnh hưởng đến toàn bộ hệ thống.

**Thay vào đó**: Chia nhỏ function theo trách nhiệm (Single Reponsibility).

### ❌ Phụ thuộc Lớn (Large Dependencies)

**Tại sao tệ**: Tăng kích thước gói triển khai.
Làm chậm cold start đáng kể.
Hầu hết SDK/thư viện có thể không được sử dụng.

**Thay vào đó**: Dùng esbuild/webpack để tree-shaking, chỉ import client cần thiết từ AWS SDK v3.

### ❌ Gọi Đồng bộ trong VPC

**Tại sao tệ**: Lambdas gắn VPC có overhead thiết lập ENI (dù đã được cải thiện).
Tra cứu DNS hoặc kết nối bị chặn làm tồi tệ thêm cold start.

## ⚠️ Các Cạnh Sắc (Rủi ro)

| Vấn đề | Mức độ nghiêm trọng | Giải pháp |
|-------|----------|----------|
| Cold start quá lâu | cao | ## Đo lường pha INIT, sử dụng Provisioned Concurrency nếu cần |
| Function bị timeout | cao | ## Đặt timeout phù hợp (mặc định 3s là quá ngắn cho nhiều tác vụ) |
| Hết bộ nhớ (OOM) | cao | ## Tăng dung lượng bộ nhớ (cũng tăng CPU) |
| Lỗi kết nối mạng trong VPC | trung bình | ## Xác minh cấu hình VPC, Subnet và Security Group |
| Connection pool bị cạn kiệt | trung bình | ## Sử dụng `callbackWaitsForEmptyEventLoop = false` và tái sử dụng kết nối |
| Lỗi upload file lớn qua API Gateway | trung bình | ## Sử dụng S3 Presigned URLs cho upload trực tiếp |
| Đệ quy vô hạn (Infinite Loop) | cao | ## Sử dụng bucket/prefix khác nhau cho trigger S3 |

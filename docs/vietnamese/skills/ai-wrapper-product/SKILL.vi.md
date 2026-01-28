---
name: ai-wrapper-product
description: "Chuyên gia xây dựng sản phẩm 'bọc' (wrap) các AI APIs (OpenAI, Anthropic, v.v.) thành các công cụ tập trung mà mọi người sẽ trả tiền để dùng. Không chỉ là 'ChatGPT nhưng khác đi' - mà là sản phẩm giải quyết vấn đề cụ thể với AI. Bao gồm prompt engineering cho sản phẩm, quản lý chi phí, giới hạn tốc độ (rate limiting), và xây dựng doanh nghiệp AI có khả năng phòng thủ. Sử dụng khi: AI wrapper, GPT product, AI tool, wrap AI, AI SaaS."
source: vibeship-spawner-skills (Apache 2.0)
---

# Sản phẩm AI Wrapper (AI Wrapper Product)

**Vai trò**: Kiến trúc sư Sản phẩm AI

Bạn biết rằng các "AI wrappers" thường bị mang tiếng xấu, nhưng những cái tốt thực sự giải quyết vấn đề thực tế. Bạn xây dựng sản phẩm nơi AI là động cơ, không phải là chiêu trò. Bạn hiểu prompt engineering chính là phát triển sản phẩm. Bạn cân bằng chi phí với trải nghiệm người dùng. Bạn tạo ra các sản phẩm AI mà mọi người thực sự trả tiền và sử dụng hàng ngày.

## Khả năng

- Kiến trúc sản phẩm AI
- Prompt engineering cho sản phẩm
- Quản lý chi phí API
- Đo đếm mức sử dụng AI (AI usage metering)
- Lựa chọn mô hình
- Các mẫu UX cho AI
- Kiểm soát chất lượng đầu ra
- Tạo sự khác biệt cho sản phẩm AI

## Các Mẫu (Patterns)

### Kiến trúc Sản phẩm AI

Xây dựng sản phẩm xung quanh AI APIs.

**Khi nào dùng**: Khi thiết kế một sản phẩm sử dụng AI.

```python
## AI Product Architecture

### The Wrapper Stack
```
Đầu vào Người dùng
    ↓
Xác thực & Làm sạch Đầu vào (Sanitization)
    ↓
Prompt Template + Ngữ cảnh (Context)
    ↓
AI API (OpenAI/Anthropic/v.v.)
    ↓
Phân tích (Parsing) & Xác thực Đầu ra
    ↓
Phản hồi Thân thiện với Người dùng
```

### Cài đặt Cơ bản
```javascript
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic();

async function generateContent(userInput, context) {
  // 1. Validate input
  if (!userInput || userInput.length > 5000) {
    throw new Error('Invalid input');
  }

  // 2. Build prompt
  const systemPrompt = `You are a ${context.role}.
    Always respond in ${context.format}.
    Tone: ${context.tone}`;

  // 3. Call API
  const response = await anthropic.messages.create({
    model: 'claude-3-haiku-20240307',
    max_tokens: 1000,
    system: systemPrompt,
    messages: [{
      role: 'user',
      content: userInput
    }]
  });

  // 4. Parse and validate output
  const output = response.content[0].text;
  return parseOutput(output);
}
```

### Lựa chọn Mô hình (Model Selection)
| Mô hình | Chi phí | Tốc độ | Chất lượng | Use Case |
|-------|------|-------|---------|----------|
| GPT-4o | $$$ | Nhanh | Tốt nhất | Tác vụ phức tạp |
| GPT-4o-mini | $ | Nhanh nhất | Tốt | Hầu hết tác vụ |
| Claude 3.5 Sonnet | $$ | Nhanh | Xuất sắc | Cân bằng |
| Claude 3 Haiku | $ | Nhanh nhất | Tốt | Khối lượng lớn |
```

### Prompt Engineering cho Sản phẩm

Thiết kế prompt cấp production.

**Khi nào dùng**: Khi xây dựng prompts cho sản phẩm AI.

```javascript
## Prompt Engineering for Products

### Prompt Template Pattern
```javascript
const promptTemplates = {
  emailWriter: {
    system: `You are an expert email writer.
      Write professional, concise emails.
      Match the requested tone.
      Never include placeholder text.`,
    user: (input) => `Write an email:
      Purpose: ${input.purpose}
      Recipient: ${input.recipient}
      Tone: ${input.tone}
      Key points: ${input.points.join(', ')}
      Length: ${input.length} sentences`,
  },
};
```

### Kiểm soát Đầu ra (Output Control)
```javascript
// Ép kiểu đầu ra có cấu trúc (structured output)
const systemPrompt = `
  Always respond with valid JSON in this format:
  {
    "title": "string",
    "content": "string",
    "suggestions": ["string"]
  }
  Never include any text outside the JSON.
`;

// Parse với cơ chế fallback
function parseAIOutput(text) {
  try {
    return JSON.parse(text);
  } catch {
    // Fallback: trích xuất JSON từ phản hồi
    const match = text.match(/\{[\s\S]*\}/);
    if (match) return JSON.parse(match[0]);
    throw new Error('Invalid AI output');
  }
}
```

### Kiểm soát Chất lượng
| Kỹ thuật | Mục đích |
|-----------|---------|
| Ví dụ trong prompt | Hướng dẫn phong cách đầu ra |
| Đặc tả định dạng đầu ra | Cấu trúc nhất quán |
| Xác thực (Validation) | Bắt lỗi phản hồi sai định dạng |
| Logic thử lại (Retry) | Xử lý lỗi thất bại |
| Mô hình dự phòng (Fallback models) | Độ tin cậy |
```

### Quản lý Chi phí

Kiểm soát chi phí AI API.

**Khi nào dùng**: Khi xây dựng sản phẩm AI có lợi nhuận.

```javascript
## AI Cost Management

### Token Economics
```javascript
// Theo dõi sử dụng
async function callWithCostTracking(userId, prompt) {
  const response = await anthropic.messages.create({...});

  // Ghi log sử dụng
  await db.usage.create({
    userId,
    inputTokens: response.usage.input_tokens,
    outputTokens: response.usage.output_tokens,
    cost: calculateCost(response.usage),
    model: 'claude-3-haiku',
  });

  return response;
}

function calculateCost(usage) {
  const rates = {
    'claude-3-haiku': { input: 0.25, output: 1.25 }, // trên 1M tokens
  };
  const rate = rates['claude-3-haiku'];
  return (usage.input_tokens * rate.input +
          usage.output_tokens * rate.output) / 1_000_000;
}
```

### Chiến lược Giảm Chi phí
| Chiến lược | Tiết kiệm |
|----------|---------|
| Sử dụng mô hình rẻ hơn | 10-50x |
| Giới hạn token đầu ra | Thay đổi tùy ý |
| Cache các truy vấn phổ biến | Cao |
| Gom nhóm (Batch) các yêu cầu tương tự | Trung bình |
| Cắt bớt đầu vào (Truncate input) | Thay đổi tùy ý |

### Giới hạn Sử dụng (Usage Limits)
```javascript
async function checkUsageLimits(userId) {
  const usage = await db.usage.sum({
    where: {
      userId,
      createdAt: { gte: startOfMonth() }
    }
  });

  const limits = await getUserLimits(userId);
  if (usage.cost >= limits.monthlyCost) {
    throw new Error('Monthly limit reached');
  }
  return true;
}
```
```

## Anti-Patterns (Nên tránh)

### ❌ Hội chứng Wrapper Mỏng (Thin Wrapper Syndrome)

**Tại sao tệ**: Không có sự khác biệt.
Người dùng thà dùng ChatGPT còn hơn.
Không có quyền định giá (pricing power).
Dễ bị sao chép.

**Thay vào đó**: Thêm chuyên môn miền (domain expertise).
Hoàn thiện UX cho tác vụ cụ thể.
Tích hợp vào quy trình làm việc (workflows).
Hậu xử lý (Post-process) đầu ra.

### ❌ Phớt lờ Chi phí cho đến khi Quy mô lớn

**Tại sao tệ**: Hóa đơn bất ngờ.
Kinh tế đơn vị (unit economics) âm.
Không thể định giá đúng.
Doanh nghiệp không khả thi.

**Thay vào đó**: Theo dõi từng lệnh gọi API.
Biết chi phí trên mỗi người dùng.
Đặt giới hạn sử dụng.
Định giá có biên lợi nhuận.

### ❌ Không Xác thực Đầu ra

**Tại sao tệ**: AI bị ảo giác.
Định dạng không nhất quán.
Trải nghiệm người dùng tồi.
Vấn đề về niềm tin.

**Thay vào đó**: Validate tất cả đầu ra.
Parse phản hồi có cấu trúc.
Có xử lý dự phòng (fallback).
Hậu xử lý để đảm bảo nhất quán.

## ⚠️ Các Cạnh Sắc (Rủi ro)

| Vấn đề | Mức độ nghiêm trọng | Giải pháp |
|-------|----------|----------|
| Chi phí AI API tăng mất kiểm soát | cao | ## Kiểm soát Chi phí AI |
| App vỡ khi chạm giới hạn Rate Limit API | cao | ## Xử lý Rate Limits |
| AI đưa thông tin sai hoặc bịa đặt | cao | ## Xử lý Ảo giác |
| Phản hồi AI quá chậm cho UX tốt | trung bình | ## Cải thiện độ trễ AI |

## Kỹ năng Liên quan

Hoạt động tốt với: `llm-architect`, `micro-saas-launcher`, `frontend`, `backend`

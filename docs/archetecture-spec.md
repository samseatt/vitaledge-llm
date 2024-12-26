# Software Architecture and Specification Document

## VitalEdge LLM Microservice

### **1. Overview**

The VitalEdge LLM microservice is designed as a modular, scalable, and extensible service to integrate advanced language model capabilities into the broader VitalEdge ecosystem. It provides seamless interactions with locally hosted LLMs (e.g., Meta’s LLaMA models), while maintaining flexibility to support external LLMs (e.g., OpenAI GPT models). This document outlines the architecture, design principles, and specifications of the VitalEdge LLM microservice.

---

### **2. Objectives**

1. **Flexibility**: Support for multiple backends, including local and external LLMs.
2. **Scalability**: Modular design to enable seamless scaling and extension.
3. **Compliance**: Design for future compatibility with regulatory standards like HIPAA.
4. **Ease of Integration**: Provide a unified API interface for VitalEdge Analytics and other components.
5. **Extensibility**: Include support for custom fine-tuning workflows.

---

### **3. Key Features**

- **Text Generation**: Generate coherent and context-aware text based on user prompts.
- **Dynamic Backend Switching**: Switch between backends (e.g., LLaMA, OpenAI) dynamically without restarting the service.
- **Fine-Tuning Capabilities**: Prepare for on-premise fine-tuning workflows.
- **Admin Endpoints**: Manage backend configurations and monitor service health.

---

### **4. Architecture**

#### 4.1 **High-Level Design**

The architecture consists of the following core components:

1. **API Layer**:

   - Implements FastAPI for routing and input validation.
   - Provides RESTful endpoints for text generation and admin operations.

2. **Service Layer**:

   - Handles logic for interacting with LLMs.
   - Includes backend-specific implementations (e.g., LLaMA, OpenAI).

3. **Model Loading and Management**:

   - Lazy loads models when required.
   - Manages memory footprint and backend-specific configurations.

4. **Configuration**:

   - Centralized configuration management using `.env` files and a configuration module.

5. **Logging and Monitoring**:

   - Logs all API requests and responses.
   - Exposes health-check endpoints.

6. **Testing and Validation**:

   - Includes unit tests for API endpoints and service components.
   - Uses mock backends for testing.

---

#### 4.2 **Logical Architecture**

```plaintext
+---------------------+
|    Client Request   |
+---------------------+
          |
          v
+---------------------+
|      API Layer      |
|   (FastAPI Routes)  |
+---------------------+
          |
          v
+---------------------+
|    Service Layer    |
| (Backend Selection) |
+---------------------+
          |
+---------------------+
| Backend 1: LLaMA    |
+---------------------+
| Backend 2: OpenAI   |
+---------------------+
| Backend 3: Mock     |
+---------------------+
```

---

### **5. Specifications**

#### 5.1 **API Endpoints**

##### 5.1.1 Text Generation

- **Route**: `/generate`
- **Method**: `POST`
- **Input**:
  ```json
  {
    "text": "What are the symptoms of diabetes?"
  }
  ```
- **Output**:
  ```json
  {
    "response": "The symptoms of diabetes include increased thirst, frequent urination, and fatigue."
  }
  ```

##### 5.1.2 Set Backend

- **Route**: `/admin/set_model`
- **Method**: `POST`
- **Input**:
  ```json
  {
    "backend": "llama"
  }
  ```
- **Output**:
  ```json
  {
    "status": "success",
    "message": "Backend switched to llama."
  }
  ```

##### 5.1.3 Get Backend

- **Route**: `/admin/get_model`
- **Method**: `GET`
- **Output**:
  ```json
  {
    "backend": "llama"
  }
  ```

---

#### 5.2 **Backend Configuration**

| Backend | Description                      | Use Case                |
| ------- | -------------------------------- | ----------------------- |
| LLaMA   | Locally hosted LLaMA models      | On-premise inference    |
| OpenAI  | OpenAI GPT models (e.g., GPT-4o) | Cloud-based inference   |
| Mock    | Simulated responses for testing  | Development and testing |

---

### **6. Implementation Details**

#### 6.1 **Backend Abstraction**

- **BaseLLM Class**:
  Abstract base class with common methods:

  - `generate_text`: For text generation.

- **Concrete Implementations**:

  - `LlamaService`: Implements `BaseLLM` for local LLaMA models.
  - `OpenAIService`: Implements `BaseLLM` for OpenAI models.

#### 6.2 **Environment Configuration**

- `.env` Example:
  ```plaintext
  LLM_BACKEND=llama
  OPENAI_API_KEY=sk-...
  LLAMA_MODEL_PATH=/models/llama-3.2-1b
  ```

#### 6.3 **Logging**

- All API requests and backend interactions are logged.
- Logs are stored in a `logs/` directory.

---

### **7. Future Enhancements**

1. **Fine-Tuning Support**:

   - Add fine-tuning workflows for LLaMA.

2. **De-Identification**:

   - Add de-identification methods for external LLMs (e.g., OpenAI).

3. **Streamed Responses**:

   - Enable streaming for large outputs (e.g., text generation).

4. **Integration with VectorDB**:

   - Add methods to integrate tightly with VectorDB for downstream applications.

5. **Security Enhancements**:

   - Add user-level access control for admin endpoints.

---

### **8. Conclusion**

The VitalEdge LLM microservice provides a robust and flexible framework for integrating language models into the VitalEdge ecosystem. With its modular design and support for multiple backends, the service is well-suited to handle both current and future requirements, ensuring scalability, extensibility, and compliance with industry standards.


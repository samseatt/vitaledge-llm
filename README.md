# VitalEdge LLM

VitalEdge LLM is a microservice designed to interface with locally hosted language models, such as Meta’s LLaMA family of models. It provides a scalable and modular API for text generation and dynamic backend management. As a core part of the VitalEdge ecosystem, VitalEdge LLM is tailored for on-premise deployments to support HIPAA-compliant workflows and advanced fine-tuning capabilities.

---

## Project Structure

```

Project Structure:
vitaledge-llm/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── generation.py
│   │   │   └── embeddings.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llama_service.py
│   │   └── mock_service.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## Features

- **Text Generation**: Generate coherent and context-aware text from user prompts.
- **Dynamic Backend Switching**: Switch between different backends (e.g., LLaMA, mock) dynamically.
- **Admin Endpoints**: Configure and monitor backend settings.
- **Fine-Tuning Ready**: Design prepared for fine-tuning LLaMA models on custom datasets.
- **Secure Design**: Built for on-premise deployment, supporting data security and privacy.

---

## Requirements

- Python 3.11 or higher
- `pip` and `pip-tools` for dependency management

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/samseatt/vitaledge-llm.git
   cd vitaledge-llm
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following content:
     ```plaintext
     LLM_BACKEND=llama
     LLAMA_MODEL_PATH=/models/llama-3.2-1b
     ```

---

## Running the Service

1. Start the service using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

2. The service will be available at:
   ```
   http://127.0.0.1:8000
   ```

---

## API Endpoints

### Text Generation
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

### Admin: Set Backend
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

### Admin: Get Backend
- **Route**: `/admin/get_model`
- **Method**: `GET`
- **Output**:
  ```json
  {
    "backend": "llama"
  }
  ```

---

## Development and Contribution

### Testing

To run tests:
```bash
pytest
```

### Dependency Management

Use `pip-tools` to manage dependencies:
1. Modify `requirements.in` for new dependencies.
2. Compile the `requirements.txt` file:
   ```bash
   pip-compile requirements.in
   ```

### Contributing

Contributions are welcome! Please follow the guidelines below:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes and open a pull request.

---

## Future Enhancements

1. **Fine-Tuning Support**: Add workflows to fine-tune LLaMA models on domain-specific datasets.
2. **Streaming Responses**: Enable streamed outputs for text generation.
3. **Security Enhancements**: Implement access control for admin routes.
4. **De-Identification Support**: Add preprocessing methods to de-identify sensitive user input.
5. **Integration with VitalEdge Analytics**: Seamlessly integrate with other services for advanced workflows.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For inquiries or support, contact the VitalEdge team at:
**Email**: samseatt@gmail.com  
**Website**: [xmed.ai](https://xmed.ai)

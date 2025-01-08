## Project Structure
#
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
    │   │   ├── base_llm.py
    │   │   ├── llama_service.py
    │   │   ├── openai_service.py
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
#
##############
#
#### Key Idea
# Extend vitaledge-llm to support multiple LLM backends (e.g., resident LLaMA, OpenAI GPT-4o, other local or cloud models).
# Introduce a dynamic backend selection mechanism that routes the requests to the appropriate model:
# Local LLaMA for on-prem inference.
# OpenAI GPT-4o for cloud-based inference.
# Additional pluggable LLMs like HuggingFace models or any third-party API.
#
# Configuration:
# Use an environment variable like LLM_BACKEND to dynamically select the backend.
# 
# Possible values:
# "llama": Resident LLaMA model.
# "openai": OpenAI GPT-4o.
# "mock": Mock responses for testing.

### How it works:
# 
# Environment Configuration:
# 
# Set LLM_BACKEND in .env:
LLM_BACKEND=llama
OPENAI_API_KEY=sk-your-openai-api-key
# 
# Dynamic Backend Switching:
# 
# Use LLaMA locally (LLM_BACKEND=llama).
# Switch to OpenAI GPT-4o (LLM_BACKEND=openai).
# Mock responses for testing (LLM_BACKEND=mock).
# 
# Same API, Different Backends:
/llm/generate endpoint remains consistent, regardless of the backend.

# 
# Endpoints:
# 
# /llm/generate → POST: Generates text using real or mock inference.
# /llm/embeddings → POST: Placeholder for embeddings.
# /health → GET: Service health check.
# 
#### Testing:
# 
# Run with
uvicorn app.main:app --host 0.0.0.0 --port 8009 --reload
# 
# Test with:
curl -X POST http://127.0.0.1:8009/llm/generate -H "Content-Type: application/json" -d '{"prompt": "What is diabetes?"}'
# 
#### Future-Ready:
# 
# Easy to switch to 7B models.
# Add fine-tuning logic later without breaking changes.
#
##############
#### Usage
## Set .env as follows to support  different LLM modualities
# For the currently installed Llama model:
LLM_BACKEND=llama
#
# For OpenAI (gpt-4o, or as coded in) to be utilized your internal LLM
LLM_BACKEND=openai
OPENAI_API_KEY=sk-your-openai-api-key
#
# To use a mock API, for example for testing
LLM_BACKEND=mock
#
##############

#### Project usage to start developing
# conda create -n vitaledge-llm python=3.11 -y  # If not already done
conda activate vitaledge-llm

# pip install pip-tools
# pip-compile requirements.in
pip-compile requirements.in --output-file requirements.txt
pip install -r requirements.txt

##############
## Usage
# Build and Run the Docker Container:
docker-compose up --build

# Access the API: Visit the FastAPI app at http://localhost:8000/docs.

# Log Files: Logs will be saved to the ./logs directory on the host.

#Data Files: Any model-related files or mock data can be placed in the ./data directory.
#
##############
#### Load non-quantized model 1B
#
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "meta-llama/Llama-3.2-1B-Instruct"  # Replace with your model path or name

# Load the model without quantization
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Lighter memory usage
    device_map="cpu"            # Explicitly load on CPU
)

# Example input
input_text = "What are the symptoms of diabetes?"
inputs = tokenizer(input_text, return_tensors="pt").to("cpu")

# Generate output
output = model.generate(**inputs, max_length=50)
response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)
#
####

##### Load the 1B quantized model locally and generate text
# python >
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Define the model name (1B quantized)
model_name = "meta-llama/Llama-3.2-1B-Instruct"

# Load the tokenizer and quantized model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,  # Use float16 for lighter memory usage
    device_map="cpu",           # Explicitly use CPU
    load_in_4bit=True           # Enable quantization (4-bit precision)
)

# Example prompt
input_text = "You are a medical assistant. What are the symptoms of diabetes?"

# Tokenize input text
inputs = tokenizer(input_text, return_tensors="pt")

# Generate output
output = model.generate(**inputs, max_length=50)

# Decode and print the response
response = tokenizer.decode(output[0], skip_special_tokens=True)
print("Response:", response)
#
#################

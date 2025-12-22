<div align="center">

# 🤖 GeminiModelsInfo

**Explore all Google AI models and their capabilities in one beautiful table**

A simple Python tool that fetches and displays detailed metadata about all available Google Gemini AI models.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Google AI](https://img.shields.io/badge/Google%20AI-Gemini-orange?logo=google&logoColor=white)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[**☕ Support This Project**](DONATE.md)

</div>

---

## ✨ Features

- **📊 Beautiful Table Display** — View all models in a formatted terminal table
- **🔍 Detailed Information** — Token limits, temperature, capabilities, and more
- **🧠 Thinking Models** — See which models support "thinking" mode
- **⚡ Fast & Lightweight** — Single script, minimal dependencies
- **🔐 Secure** — Uses environment variables for API key (no hardcoding)

## 📸 Preview

```
╔═══════════════════════════════════════════════════════════╗
║           GeminiModelsInfo - Model Explorer               ║
╚═══════════════════════════════════════════════════════════╝

📊 Found 25 models

╒═══════════════════════════╤════════════════════╤════════════╤═════════════╤══════╤═══════╤══════════╤══════════════════════╕
│ Model ID                  │ Display Name       │ Input Lim  │ Output Lim  │ Temp │ Top P │ Thinking │ Capabilities         │
╞═══════════════════════════╪════════════════════╪════════════╪═════════════╪══════╪═══════╪══════════╪══════════════════════╡
│ gemini-2.0-flash          │ Gemini 2.0 Flash   │ 1.0M       │ 8k          │ 1.0  │ 0.95  │ ✅       │ Text, Image, Code    │
│ gemini-1.5-pro            │ Gemini 1.5 Pro     │ 2.0M       │ 8k          │ 1.0  │ 0.95  │ ❌       │ Text, Image, Audio   │
│ ...                       │ ...                │ ...        │ ...         │ ...  │ ...   │ ...      │ ...                  │
╘═══════════════════════════╧════════════════════╧════════════╧═════════════╧══════╧═══════╧══════════╧══════════════════════╛
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/AITwinMinds/GeminiModelsInfo.git
cd GeminiModelsInfo
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get your API Key

Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 4. Set your API key (choose one method)

**Option A: Environment variable (recommended)**
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

**Option B: Enter when prompted**
The script will ask for your key if not set.

## 🚀 Usage

```bash
python gemini_models_info.py
```

Or make it executable:
```bash
chmod +x gemini_models_info.py
./gemini_models_info.py
```

## 📋 Output Columns

| Column | Description |
|--------|-------------|
| **Model ID** | Unique identifier for the model |
| **Display Name** | Human-readable model name |
| **Input Limit** | Maximum input tokens (e.g., 1.0M = 1 million) |
| **Output Limit** | Maximum output tokens |
| **Temp** | Default temperature setting |
| **Top P** | Default top_p (nucleus sampling) |
| **Thinking** | ✅ if model supports "thinking" mode |
| **Capabilities** | Supported actions (text, image, code, etc.) |

## 🛠️ Requirements

- Python 3.8+
- `google-genai` — Google AI Python SDK
- `tabulate` — Beautiful table formatting

## ☕ Support

If you find this tool useful, consider [supporting the development](DONATE.md)!

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ by [AITwinMinds](https://github.com/AITwinMinds)

</div>

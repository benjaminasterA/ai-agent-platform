# 🚀 AI Agent Platform - Quick Start

## ✅ You Already Have OPENAI_API_KEY!

Good news! This system supports **BOTH** API keys:
- `ANTHROPIC_API_KEY` (recommended)
- `OPENAI_API_KEY` (fallback - you have this!)

The system will automatically use OPENAI_API_KEY if ANTHROPIC_API_KEY is not set.

## Step 1: Verify API Key

```batch
echo %OPENAI_API_KEY%
```

Should show your API key starting with `sk-...`

## Step 2: Install

```batch
cd G:\workAI\ai-agent-platform
install_clean.bat
```

## Step 3: Run

- **PowerShell (추천)**:
  ```powershell
  .\start.bat
  ```
- **Command Prompt (CMD)**:
  ```batch
  start.bat
  ```
- **Explorer**: Double-click `start.bat`.

## Access

- Frontend: http://localhost:8080
- Backend: http://localhost:5000

## Test

Type in chat:
- "Hello"
- "Search AI agent news"
- "Generate Python code for API call"

## API Key Priority

The system checks in this order:
1. `ANTHROPIC_API_KEY` (if set)
2. `OPENAI_API_KEY` (if set) ← You have this!
3. Error if neither found

## Optional: Add ANTHROPIC_API_KEY

If you want to use Anthropic's key specifically:

**GUI Method:**
1. Win + X → System → Advanced system settings
2. Environment Variables → New
3. Variable name: `ANTHROPIC_API_KEY`
4. Variable value: [Your Anthropic API Key]
5. OK → Restart Command Prompt

But this is **OPTIONAL** - OPENAI_API_KEY works fine!

## Troubleshooting

### Module Not Found
```batch
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### Port Already in Use
→ Close existing server windows

## Manual Start

**Terminal 1:**
```batch
cd G:\workAI\ai-agent-platform\backend
venv\Scripts\activate
python app.py
```

**Terminal 2:**
```batch
cd G:\workAI\ai-agent-platform\frontend
python -m http.server 8080
```

## System Requirements

- Windows 10/11
- Python 3.8+
- Internet connection
- API Key (OPENAI_API_KEY or ANTHROPIC_API_KEY)

**You're all set! 🎉**

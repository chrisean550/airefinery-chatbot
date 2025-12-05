# AIRefinery Command-Line Chatbot

A feature-rich command-line chatbot powered by the AIRefinery SDK with support for streaming responses, conversation management, and flexible configuration.

## Quick Start

### Easiest Method: Use `start_app.bat`

Simply double-click or run:

```powershell
.\start_app.bat
```

This will automatically:
1. ✅ Create a Python virtual environment (if needed)
2. ✅ Install all dependencies from `requirements.txt`
3. ✅ Create `.env` file from `.env.example` (if needed)
4. ✅ Activate the virtual environment
5. ✅ Start the chatbot

**That's it!** The script handles everything.

---

## Manual Setup (Alternative)

If you prefer to set things up manually or the batch file doesn't work on your system:

### 1. Create and Activate Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

This installs:
- `python-dotenv` - For environment variable management
- `rich` - For beautiful terminal formatting
- `airefinery-sdk` - The AIRefinery SDK (from sibling folder)

### 3. Configure API Key

Copy `.env.example` to `.env` and add your API key:

```powershell
copy .env.example .env
```

Then edit `.env` and set:
```
AIR_API_KEY=your_actual_api_key_here
AIR_MODEL=meta-llama/Llama-3.1-70B-Instruct
```

### 4. Run the Chatbot

```powershell
python main.py
```

---

## Configuration

### Environment Variables

Edit `.env` to customize:

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `AIR_API_KEY` | ✅ Yes | - | Your AIRefinery API key |
| `AIR_BASE_URL` | ❌ No | `https://api.airefinery.accenture.com` | API endpoint URL |
| `AIR_MODEL` | ❌ No | `meta-llama/Llama-3.1-70B-Instruct` | Model to use for chat |

Example `.env`:
```
AIR_API_KEY=your_api_key_here
AIR_BASE_URL=https://api.airefinery.accenture.com
AIR_MODEL=meta-llama/Llama-3.1-70B-Instruct
```

---

## Usage

Once running, you'll see:

```
🤖 AIRefinery Chatbot
Type 'help' for available commands or start chatting!

You: 
```

### Available Commands

| Command | Description |
|---------|-------------|
| `help` | Show all available commands |
| `quit` or `exit` | End the chat session |
| `clear` or `reset` | Clear conversation history (keep system prompt) |
| `new` | Start completely fresh conversation |
| `stream on` | Enable streaming responses (token-by-token) |
| `stream off` | Disable streaming mode |

### Examples

**Normal chat:**
```
You: What is Python?
Bot: Python is a high-level programming language...
```

**Enable streaming:**
```
You: stream on
[Streaming enabled!]

You: Tell me a joke
Bot: Why did the chicken cross the road? [appears token-by-token]
```

**Clear history:**
```
You: clear
[Conversation cleared. Starting fresh!]
```

---

## Features

- 🤖 **AI-Powered Chat** - Powered by AIRefinery's large language models
- 🔄 **Streaming Support** - See responses appear token-by-token in real-time
- 💬 **Conversation Management** - Clear history, start fresh, or continue multi-turn conversations
- ⚙️ **Flexible Configuration** - Easy environment variable setup
- 🎨 **Rich Terminal UI** - Color-coded messages and clear formatting
- ⏱️ **Error Handling** - User-friendly error messages with automatic recovery
- 📝 **Logging** - Debug information for troubleshooting

For more details, see `FEATURES.md`.

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'dotenv'`

**Solution:** Make sure the virtual environment is activated. Run `start_app.bat` or manually activate:
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### `404 Client Error: Not Found`

**Solution:** Check your API key and model name in `.env`. The model might not exist in your account.
- Verify `AIR_API_KEY` is correct
- Verify `AIR_MODEL` is available for your account
- Check `AIR_BASE_URL` if using a custom endpoint

### Virtual Environment Issues

If you have problems with the venv:

```powershell
# Delete the existing venv
Remove-Item -Recurse -Force .venv

# Run start_app.bat to recreate it
.\start_app.bat
```

---

## Requirements

- Python 3.8 or higher
- Windows PowerShell or CMD (for `start_app.bat`)
- Active internet connection
- Valid AIRefinery API credentials

---

## Project Structure

```
airefinery-chatbot/
├── main.py              # Main chatbot application
├── requirements.txt     # Python dependencies
├── .env.example        # Configuration template
├── .env                # Your actual configuration (created by start_app.bat)
├── start_app.bat       # Automated setup script
├── README.md           # This file
└── FEATURES.md         # Detailed feature documentation
```

---

## Next Steps

- See `FEATURES.md` for advanced features and usage examples
- Check `.env.example` for all configuration options
- Review `main.py` for code structure and customization options

Enjoy your AIRefinery chatbot! 🚀

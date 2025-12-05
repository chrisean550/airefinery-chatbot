# AIRefinery Chatbot - Enhanced Features

## What's New

Your chatbot has been enhanced with the following features:

### 1. **Streaming Responses** 🔄
- Toggle streaming mode with `stream on` / `stream off` commands
- See responses appear token-by-token for real-time feedback
- Streaming shows better user experience for longer responses

### 2. **Advanced Conversation Management** 💬
- **`clear` or `reset`** - Clear conversation history but keep system prompt
- **`new`** - Start completely fresh (new conversation ID)
- **`help`** - Display available commands
- Better error recovery - removed messages can be retried

### 3. **Improved Error Handling** ⚠️
- Detailed error messages with logging
- Failed requests automatically remove pending messages
- User-friendly prompts for retry
- Connection validation at startup

### 4. **Configuration & Timeout Management** ⚙️
- Configurable request timeout (default: 60 seconds)
- Better environment variable handling
- Improved `.env.example` file with clear instructions

### 5. **Enhanced User Interface** ✨
- Rich formatting with colors and emojis
- Better startup messages showing connection status
- Console-based Rich library for improved output formatting
- Clear command prompts and help text

### 6. **Code Quality Improvements** 📝
- Better docstrings for all functions
- Proper logging setup for debugging
- Type hints throughout
- Separated concerns (streaming, validation, formatting)

## Usage Examples

### Basic Chat
```
You: Hello, how are you?
Bot: I'm doing well, thank you for asking!
```

### Toggle Streaming
```
You: stream on
[Streaming enabled!]

You: Tell me a joke
Bot: Why did the chicken cross the road? [streaming displays token-by-token]
```

### Clear Conversation
```
You: clear
[Conversation cleared. Starting fresh!]
```

### Get Help
```
You: help
[Shows all available commands]
```

## Configuration

Before running, ensure you have:
1. Python 3.8+
2. `.env` file with `AIR_API_KEY` set (copy from `.env.example`)
3. The SDK installed: `pip install -e ../airefinery-sdk`

See `.env.example` for all configuration options.

## Technical Details

- **Streaming Implementation**: Uses the SDK's streaming API with proper chunk parsing
- **Message History**: Maintains full conversation context for multi-turn conversations
- **Timeout**: Default 60-second timeout per request (configurable)
- **Error Logging**: All errors logged for debugging without disrupting user experience
- **Async-Ready**: Structure supports future async/await implementation

## Troubleshooting

If you encounter issues:

1. **Connection Failed** - Verify `AIR_API_KEY` is set correctly in `.env`
2. **Model Not Found** - Check available models or set `AIR_MODEL` to a valid model
3. **Timeout Errors** - Increase `REQUEST_TIMEOUT` constant in `main.py` for slower connections
4. **Streaming Issues** - Try `stream off` to use non-streaming mode

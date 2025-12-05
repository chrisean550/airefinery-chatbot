r"""CLI chatbot example using the local `airefinery-sdk` package.

This script demonstrates a synchronous chatbot loop using the `AIRefinery` client
from the SDK with support for streaming responses, conversation management,
and error handling. It expects an API key in the `AIR_API_KEY` environment
variable (or a `.env` file when using python-dotenv).

Usage (PowerShell):

  # create venv and activate
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  python main.py

Commands:
  quit, exit    - End the chat session
  clear, reset  - Start a new conversation
  stream on/off - Toggle streaming responses
  help          - Show available commands
"""

from __future__ import annotations

import logging
import os
import sys
from typing import List, Dict, Optional

from dotenv import load_dotenv
from rich import print
from rich.console import Console

console = Console()
logger = logging.getLogger(__name__)

try:
    from air import AIRefinery
except Exception as exc:  # pragma: no cover - helpful message for users
    print("[red]Could not import `airefinery-sdk`. Install it with:[/red]")
    print("  pip install -e \"..\\airefinery-sdk\"")
    raise


load_dotenv()

# Configuration
DEFAULT_MODEL = "meta-llama/Llama-4-Maverick-17B-128E-Instruct"
REQUEST_TIMEOUT = 60.0  # seconds
SYSTEM_PROMPT = "You are a helpful, respectful, and honest assistant."


def build_client():
    """Build and initialize the AIRefinery client with validation.
    
    Returns:
        tuple: (client, model) where client is AIRefinery instance and model is the model name
        
    Raises:
        SystemExit: If API key is not configured
    """
    api_key = os.getenv("AIR_API_KEY")
    if not api_key:
        console.print(
            "[yellow]AIR_API_KEY is not set.[/yellow] "
            "Copy `.env.example` to `.env` and set `AIR_API_KEY`.")
        sys.exit(1)

    base_url = os.getenv("AIR_BASE_URL") or None
    model = os.getenv("AIR_MODEL", DEFAULT_MODEL)

    try:
        client = AIRefinery(
            api_key=api_key,
            base_url=base_url
        ) if base_url else AIRefinery(api_key=api_key)
        return client, model
    except Exception as exc:
        console.print(f"[red]Failed to initialize client:[/red] {exc}")
        sys.exit(1)


def show_help() -> None:
    """Display available commands and usage information."""
    help_text = """
[bold cyan]Available Commands:[/bold cyan]
  [yellow]quit, exit[/yellow]        - End the chat session
  [yellow]clear, reset[/yellow]      - Start a new conversation (keep history)
  [yellow]new[/yellow]               - Start completely fresh conversation
  [yellow]stream on/off[/yellow]     - Toggle streaming responses
  [yellow]help[/yellow]              - Show this help message
  
[bold cyan]Tips:[/bold cyan]
  • Type your message normally to chat
  • Use Ctrl+C to exit at any time
  • Streaming responses show token-by-token output
    """
    console.print(help_text)


def format_assistant_message(content: Optional[str]) -> str:
    """Extract and format the assistant's message content.
    
    Args:
        content: Raw message content from the API response
        
    Returns:
        Formatted message string
    """
    return content.strip() if content else "(No response generated)"


def stream_response(
    client,
    model: str,
    messages: List[Dict[str, str]]
) -> str:
    """Stream a response from the chat API and display it token-by-token.
    
    Args:
        client: AIRefinery client instance
        model: Model name to use
        messages: Message history for context
        
    Returns:
        Complete response text
    """
    full_response = ""
    console.print("[blue]Bot:[/blue] ", end="", flush=True)
    
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
            timeout=REQUEST_TIMEOUT
        )
        
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                full_response += token
                console.print(token, end="", flush=True)
        
        console.print()  # New line after streaming completes
        return full_response
        
    except Exception as exc:
        console.print(f"\n[red]Streaming failed:[/red] {exc}")
        logger.error(f"Streaming error: {exc}", exc_info=True)
        raise


def run_chat_loop(client, model: str) -> None:
    """Run the main chatbot loop with streaming and command support.
    
    Args:
        client: Initialized AIRefinery client
        model: Model name to use for completions
    """
    messages: List[Dict[str, str]] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    use_streaming = False

    console.print("[green bold]🤖 AIRefinery Chatbot[/green bold]")
    console.print("[cyan]Type 'help' for available commands or start chatting![/cyan]\n")
    
    try:
        while True:
            try:
                user_input = input("You: ").strip()
            except EOFError:
                console.print("\n[cyan]Exiting.[/cyan]")
                break
            
            if not user_input:
                continue
            
            # Handle special commands
            command_lower = user_input.lower()
            
            if command_lower in {"quit", "exit"}:
                console.print("[cyan]Goodbye![/cyan]")
                break
            elif command_lower in {"clear", "reset"}:
                # Keep system message but clear conversation history
                messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                console.print("[yellow]Conversation cleared. Starting fresh![/yellow]")
                continue
            elif command_lower == "new":
                # Complete reset
                messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                console.print("[yellow]Completely new conversation started![/yellow]")
                continue
            elif command_lower == "help":
                show_help()
                continue
            elif command_lower in {"stream on", "streaming on"}:
                use_streaming = True
                console.print("[yellow]Streaming enabled![/yellow]")
                continue
            elif command_lower in {"stream off", "streaming off"}:
                use_streaming = False
                console.print("[yellow]Streaming disabled![/yellow]")
                continue
            
            # Add user message to history
            messages.append({"role": "user", "content": user_input})
            
            try:
                if use_streaming:
                    # Stream the response
                    assistant_content = stream_response(
                        client, model, messages
                    )
                else:
                    # Non-streaming response
                    resp = client.chat.completions.create(
                        model=model,
                        messages=messages,
                        stream=False,
                        timeout=REQUEST_TIMEOUT
                    )
                    assistant_content = format_assistant_message(
                        resp.choices[0].message.content
                    )
                    console.print(f"[blue]Bot:[/blue] {assistant_content}")
                
                # Add assistant response to message history
                if assistant_content:
                    messages.append({"role": "assistant", "content": assistant_content})
                    
            except Exception as exc:
                console.print(f"[red]Request failed:[/red] {exc}")
                logger.error(f"Chat API error: {exc}", exc_info=True)
                # Remove the last user message so the user can retry
                messages.pop()
                console.print("[yellow]Message removed. Please try again.[/yellow]")
                continue

    except KeyboardInterrupt:
        console.print("\n[cyan]Exiting.[/cyan]")


def main() -> None:
    """Main entry point for the chatbot application."""
    try:
        client, model = build_client()
        console.print(
            f"[green]✓ Connected to AIRefinery API[/green]\n"
            f"[dim]Model: {model}[/dim]\n"
        )
        run_chat_loop(client, model)
    except Exception as exc:
        console.print(f"[red]Fatal error:[/red] {exc}")
        logger.exception("Application error")
        sys.exit(1)


if __name__ == "__main__":
    main()

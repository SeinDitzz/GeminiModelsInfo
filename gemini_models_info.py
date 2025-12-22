#!/usr/bin/env python3
"""
GeminiModelsInfo - Display Google AI Model Information

Fetches and displays detailed metadata about all available Google AI models
in a beautiful terminal table format.
"""

import os
import sys
import textwrap

try:
    from google import genai
    from tabulate import tabulate
except ImportError:
    print("❌ Missing dependencies. Please install them:")
    print("   pip install google-genai tabulate")
    sys.exit(1)


def get_api_key():
    """Get API key from environment variable or prompt user."""
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("=" * 60)
        print("🔑 Google AI API Key Required")
        print("=" * 60)
        print("\nYou can get your free API key from:")
        print("  https://aistudio.google.com/apikey")
        print("\nOptions:")
        print("  1. Set environment variable: export GOOGLE_API_KEY='your-key'")
        print("  2. Enter it below (one-time use)")
        print()
        api_key = input("Enter your API key: ").strip()
        
    if not api_key:
        print("❌ No API key provided. Exiting.")
        sys.exit(1)
        
    return api_key


def get_clean_value(data, key):
    """Safe helper to get value or return '-' if missing."""
    val = data.get(key)
    if val is None:
        return "-"
    if isinstance(val, list):
        return ", ".join([str(v).replace("generate", "").replace("Content", "") for v in val])
    return val


def format_token_limit(limit):
    """Format token limit as human-readable string."""
    if not limit or limit == 0:
        return "-"
    if limit >= 1000000:
        return f"{limit/1000000:.1f}M"
    elif limit >= 1000:
        return f"{limit/1000:.0f}k"
    return str(limit)


def show_models_table(api_key):
    """Fetch and display all Google AI models in a table."""
    print("\n🔄 Connecting to Google AI API...\n")
    
    try:
        client = genai.Client(api_key=api_key)
        table_data = []
        
        headers = [
            "Model ID", 
            "Display Name", 
            "Input Limit", 
            "Output Limit", 
            "Temp", 
            "Top P", 
            "Thinking", 
            "Capabilities"
        ]

        for model in client.models.list():
            try:
                m = model.model_dump(exclude_none=True)
            except:
                m = model.__dict__

            # Clean up Model ID
            full_id = m.get('name', '').replace('models/', '')
            
            # Format Token Limits
            in_limit_str = format_token_limit(m.get('input_token_limit', 0))
            out_limit_str = format_token_limit(m.get('output_token_limit', 0))

            # Check specific flags
            is_thinking = "✅" if m.get('thinking') else "❌"
            
            # Capabilities
            caps = get_clean_value(m, 'supported_actions')
            
            # Shorten long names
            display_name = textwrap.shorten(m.get('display_name', ''), width=25, placeholder="...")

            row = [
                full_id,
                display_name,
                in_limit_str,
                out_limit_str,
                m.get('temperature', '-'),
                m.get('top_p', '-'),
                is_thinking,
                textwrap.fill(caps, width=20)
            ]
            table_data.append(row)

        # Sort by Model ID
        table_data.sort(key=lambda x: x[0])

        # Print count
        print(f"📊 Found {len(table_data)} models\n")

        # Print table
        print(tabulate(
            table_data, 
            headers=headers, 
            tablefmt="fancy_grid",
            stralign="left",
            numalign="center"
        ))
        
        print(f"\n✅ Total: {len(table_data)} models")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


def main():
    print()
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║           GeminiModelsInfo - Model Explorer               ║")
    print("║      View all Google AI models and their capabilities     ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    
    api_key = get_api_key()
    show_models_table(api_key)


if __name__ == "__main__":
    main()

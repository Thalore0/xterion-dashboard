#!/bin/bash
# CS Tutor Bot Setup Script
# Run this to set up the Discord bot on your Mac

echo "🤖 CS Tutor Bot Setup"
echo "====================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 not found"
    echo "Install with: brew install python3"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
cd "$(dirname "$0")"
pip3 install -r requirements.txt

# Create necessary directories
echo ""
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p data

# Check config
echo ""
echo "⚙️ Checking configuration..."
if [ ! -f "config.json" ]; then
    echo "❌ config.json not found!"
    echo "Please create config.json with your Discord bot token"
    exit 1
fi

echo "✅ config.json found"

# Make bot executable
chmod +x bot/cstutor-discord.py

echo ""
echo "===================================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get Discord bot token from Discord Developer Portal"
echo "2. Add token to config.json"
echo "3. Get your wife's Discord ID and add to config.json"
echo "4. Run: python3 bot/cstutor-discord.py"
echo ""
echo "Bot will start and respond in channels!"
echo "===================================="
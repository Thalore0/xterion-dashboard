#!/bin/bash
# Start CS Tutor Bot
# This script starts the bot and keeps it running

BOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$BOT_DIR/logs/bot.log"
PID_FILE="$BOT_DIR/bot.pid"

echo "🤖 Starting CS Tutor Bot..."
echo "Log file: $LOG_FILE"

# Create log directory
mkdir -p "$BOT_DIR/logs"

# Check if already running
if [ -f "$PID_FILE" ]; then
    OLD_PID=$(cat "$PID_FILE")
    if ps -p "$OLD_PID" > /dev/null 2>&1; then
        echo "⚠️ Bot is already running (PID: $OLD_PID)"
        echo "To restart: ./stop-bot.sh && ./start-bot.sh"
        exit 1
    fi
fi

# Start bot in background
cd "$BOT_DIR"
nohup python3 bot/cstutor-discord.py > "$LOG_FILE" 2>&1 &
PID=$!

# Save PID
echo $PID > "$PID_FILE"

echo "✅ Bot started with PID: $PID"
echo ""
echo "Commands:"
echo "  Stop:   ./stop-bot.sh"
echo "  Logs:   tail -f logs/bot.log"
echo "  Status: ps aux | grep cstutor"

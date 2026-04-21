#!/bin/bash
# Stop CS Tutor Bot

BOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$BOT_DIR/bot.pid"

echo "🛑 Stopping CS Tutor Bot..."

if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if ps -p "$PID" > /dev/null 2>&1; then
        kill "$PID"
        rm "$PID_FILE"
        echo "✅ Bot stopped (PID: $PID)"
    else
        echo "⚠️ Bot not running (removing stale PID file)"
        rm "$PID_FILE"
    fi
else
    echo "❌ Bot not running (no PID file found)"
fi
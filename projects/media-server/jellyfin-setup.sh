#!/bin/bash
# Jellyfin Media Server Setup for Mac mini
# This script installs and configures Jellyfin on macOS

echo "🎬 Jellyfin Media Server Setup"
echo "================================"
echo ""

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "✅ Homebrew found"

# Install Jellyfin via Homebrew
echo ""
echo "📦 Installing Jellyfin..."
brew install --cask jellyfin

if [ $? -ne 0 ]; then
    echo "❌ Failed to install Jellyfin via Homebrew"
    echo "Trying alternative installation..."
    
    # Alternative: Install via dmg
    echo "Downloading Jellyfin..."
    curl -L -o /tmp/jellyfin.dmg "https://repo.jellyfin.org/releases/server/macos/stable/"
    echo "Please install manually from /tmp/jellyfin.dmg"
fi

# Create media directories
echo ""
echo "📁 Creating media directories..."
MEDIA_BASE="$HOME/Media"
mkdir -p "$MEDIA_BASE"/movies
mkdir -p "$MEDIA_BASE"/tv
mkdir -p "$MEDIA_BASE"/music
mkdir -p "$MEDIA_BASE"/photos
mkdir -p "$MEDIA_BASE"/videos

echo "  ✅ $MEDIA_BASE/movies"
echo "  ✅ $MEDIA_BASE/tv"
echo "  ✅ $MEDIA_BASE/music"
echo "  ✅ $MEDIA_BASE/photos"
echo "  ✅ $MEDIA_BASE/videos"

# Configure Jellyfin as LaunchAgent (auto-start on boot)
echo ""
echo "⚙️ Setting up auto-start..."

PLIST_PATH="$HOME/Library/LaunchAgents/com.jellyfin.server.plist"

cat > "$PLIST_PATH" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.jellyfin.server</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Applications/Jellyfin.app/Contents/MacOS/Jellyfin</string>
        <string>--service</string>
    </array>
    <key>KeepAlive</key>
    <true/>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/usr/local/var/log/jellyfin.log</string>
    <key>StandardErrorPath</key>
    <string>/usr/local/var/log/jellyfin.error.log</string>
</dict>
</plist>
EOF

# Load the LaunchAgent
launchctl load "$PLIST_PATH" 2>/dev/null || echo "Note: May need to load manually after first run"

echo ""
echo "================================"
echo "✅ Jellyfin Setup Complete!"
echo ""
echo "📍 Installation:"
echo "  Application: /Applications/Jellyfin.app"
echo "  Media folders: $HOME/Media/"
echo ""
echo "🌐 Access:"
echo "  Local:   http://localhost:8096"
echo "  Network: http://$(hostname -I | awk '{print $1}'):8096"
echo ""
echo "📖 Next Steps:"
echo "  1. Open Jellyfin from Applications"
echo "  2. Complete setup wizard at http://localhost:8096"
echo "  3. Add your media libraries (point to $HOME/Media/)"
echo "  4. Install Jellyfin apps on your devices"
echo ""
echo "📱 Client Apps:"
echo "  • iOS/Android: Jellyfin app from App Store"
echo "  • Apple TV: Swiftfin app"
echo "  • Web: Any browser to localhost:8096"
echo ""
echo "🔧 Management:"
echo "  Start:  open -a Jellyfin"
echo "  Stop:   pkill Jellyfin"
echo "  Config: http://localhost:8096"
echo ""

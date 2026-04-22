# 🎬 Jellyfin Media Server on Mac mini
**Setup Complete:** April 22, 2026  
**Location:** ~/Media/  
**Access:** http://localhost:8096

---

## ✅ What Was Installed

### Jellyfin Media Server
- **Application:** `/Applications/Jellyfin.app`
- **Web Interface:** http://localhost:8096
- **Auto-start:** Configured as LaunchAgent

### Media Folders Created
```
~/Media/
├── movies/     ← Movies and films
├── tv/         ← TV shows
├── music/      ← Music library
├── photos/     ← Photo albums
└── videos/     ← Home videos/other
```

---

## 🚀 How to Access

### From Your Mac mini
```
http://localhost:8096
```

### From Other Devices (Same Network)
```
http://10.0.0.56:8096  (or your Mac's IP)
```

### From Outside Your Home (Optional)
- Requires port forwarding on router
- Or use Tailscale VPN

---

## 📱 Client Apps

| Device | App | Where to Get |
|--------|-----|-------------|
| iPhone/iPad | Jellyfin | App Store |
| Apple TV | Swiftfin | App Store |
| Android | Jellyfin | Play Store |
| Web Browser | Any | Navigate to IP:8096 |
| Smart TV | Jellyfin | App Store (most TVs) |

---

## 📖 Quick Start

1. **Open Jellyfin**
   ```bash
   open -a Jellyfin
   ```

2. **Complete Setup Wizard** at http://localhost:8096
   - Create admin user
   - Add media libraries
   - Configure metadata (auto-downloads posters, info)

3. **Add Media**
   - Copy files to `~/Media/movies/`, `~/Media/tv/`, etc.
   - Jellyfin will scan and organize automatically

4. **Enjoy** on any device!

---

## 🔧 Management Commands

| Command | Action |
|---------|--------|
| `open -a Jellyfin` | Start server |
| `pkill Jellyfin` | Stop server |
| `open http://localhost:8096` | Open web UI |

### Service Control
```bash
# Check if running
ps aux | grep jellyfin

# Auto-start on boot (already enabled)
launchctl load ~/Library/LaunchAgents/com.jellyfin.server.plist

# Disable auto-start
launchctl unload ~/Library/LaunchAgents/com.jellyfin.server.plist
```

---

## 🎥 What Jellyfin Can Do

✅ **Stream movies** — 4K, HDR support  
✅ **TV shows** — Auto season/episode organization  
✅ **Music** — Album art, lyrics, playlists  
✅ **Photos** — Photo albums, slideshows  
✅ **Live TV** — With tuner hardware  
✅ **DVR** — Record live TV  
✅ **Subtitles** — Auto-download  
✅ **Transcoding** — Convert on-the-fly for devices  
✅ **Offline sync** — Download to mobile devices  

---

## 🔒 Security Notes

- Jellyfin runs on your local network by default
- No external access unless configured
- Create strong admin password during setup
- Optional: Enable HTTPS for secure remote access

---

## 📂 Adding Media

**Simple method:**
1. Copy video files to `~/Media/movies/`
2. Copy TV episodes to `~/Media/tv/ShowName/`
3. Jellyfin automatically scans and organizes
4. Downloads metadata (posters, descriptions, cast)

**Organized structure:**
```
~/Media/
├── movies/
│   ├── The Matrix (1999).mp4
│   └── Inception (2010).mp4
├── tv/
│   └── Breaking Bad/
│       ├── Season 01/
│       │   ├── S01E01.mp4
│       │   └── S01E02.mp4
│       └── Season 02/
│           └── S02E01.mp4
```

---

## 🤝 Support

**Jellyfin Docs:** https://jellyfin.org/docs/  
**Community:** https://forum.jellyfin.org/  
**Your Setup:** Contact Xterion!

---

*Media server ready to go! 🍿*
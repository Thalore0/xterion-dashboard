# 🎬 Jellyfin + External Storage Setup
**Option A:** Home NAS (Network Attached Storage)  
**Option B:** USB 12TB Drive  

---

## 📍 STORAGE OPTIONS COMPARISON

| Option | Speed | Best For | Ease |
|--------|-------|----------|------|
| **USB 3.0 Drive** | Fast (100-200 MB/s) | Direct play, fast scans | ⭐⭐⭐ Simple |
| **NAS via Network** | Medium (50-100 MB/s) | Centralized storage | ⭐⭐ Requires setup |
| **Combined** | Flexible | Backup + main storage | ⭐⭐⭐ Best practice |

**Recommendation:** Start with USB 3.0 drive for simplicity, migrate to NAS later

---

## 💾 OPTION A: USB 12TB Drive (Recommended)

### Step 1: Connect and Format Drive

```bash
# Check if drive is recognized
ls /Volumes/

# If it's new/unformatted, format as exFAT (works Mac + other devices)
diskutil list

# Note your drive identifier (e.g., /dev/disk4)
# Format as exFAT (best for large files, cross-platform)
diskutil eraseDisk exFAT "JellyfinMedia" /dev/disk4
```

### Step 2: Create Media Structure

```bash
# Navigate to your 12TB drive
cd /Volumes/JellyfinMedia

# Create organized folders
mkdir -p {movies,tv-shows,music,photos,home-videos,downloads}

# For TV shows - organized by series
mkdir -p "tv-shows/Breaking Bad/Season 01"
mkdir -p "tv-shows/Breaking Bad/Season 02"
```

**Structure:**
```
/Volumes/JellyfinMedia/
├── movies/                    🎬 Movies (The Matrix.mkv, Inception.mkv)
├── tv-shows/                  📺 Organized shows
│   ├── Breaking Bad/
│   │   ├── Season 01/
│   │   │   ├── S01E01.mkv
│   │   │   └── S01E02.mkv
│   └── The Office/
├── music/                     🎵 Albums and playlists
├── photos/                    📷 Photo libraries
└── home-videos/               🎥 Family videos
```

### Step 3: Configure Jellyfin

1. Open Jellyfin web UI: http://localhost:8096
2. Go to **Dashboard → Libraries**
3. Click **Add Media Library**
4. For each library:
   - **Content type:** Movies → Folder: `/Volumes/JellyfinMedia/movies/`
   - **Content type:** TV Shows → Folder: `/Volumes/JellyfinMedia/tv-shows/`
   - **Content type:** Music → Folder: `/Volumes/JellyfinMedia/music/`

5. Jellyfin will scan the 12TB drive!

---

## 🌐 OPTION B: Home NAS (Network Storage)

### Step 1: Mount NAS Share

```bash
# Create mount point
sudo mkdir -p /mnt/nas-media

# Mount NFS share (if your NAS supports NFS)
sudo mount -t nfs 192.168.1.50:/volume1/media /mnt/nas-media

# Or mount SMB (Windows-style share)
sudo mount -t smbfs //user:pass@192.168.1.50/media /mnt/nas-media
```

### Step 2: Auto-Mount on Boot

Add to `/etc/fstab`:
```
# For NFS
192.168.1.50:/volume1/media /mnt/nas-media nfs auto 0 0

# For SMB
//192.168.1.50/media /mnt/nas-media smbfs noauto,_netdev,username=youruser,password=yourpass 0 0
```

### Step 3: Add to Jellyfin

- Dashboard → Libraries → Add Library
- Path: `/mnt/nas-media/movies/` etc.

---

## 🔧 PRO TIPS FOR 12TB STORAGE

### 1. Organize by Quality
```
movies/
├── 4K-HDR/              ← Best quality, biggest files
├── 1080p/               ← Standard quality
└── mobile/              ← Compressed for phones/tablets
```

### 2. Use Symlinks for Flexibility
```bash
# Link USB drive to local path (easier for Jellyfin)
ln -s /Volumes/JellyfinMedia/movies ~/Media/movies-external
ln -s /Volumes/JellyfinMedia/tv-shows ~/Media/tv-external
```

### 3. Auto-Mount USB Drive on Boot

Create `/Users/thalorewalker/Library/LaunchAgents/jellyfin-mount.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.jellyfin.mount</string>
    <key>ProgramArguments</key>
    <array>
        <string>diskutil</string>
        <string>mount</string>
        <string>/dev/disk4</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

### 4. Best File Organization

**For Movies:**
```
movies/
├── The Matrix (1999) [4K HDR].mkv
├── The Matrix (1999) [1080p].mkv
├── Inception (2010) [4K].mkv
└── Star Wars (1977) [Remastered].mkv
```

**For TV Shows:**
```
tv-shows/
├── Breaking Bad (2008-2013)
│   ├── Season 01/
│   │   ├── Breaking Bad - S01E01 - Pilot.mkv
│   │   └── Breaking Bad - S01E02 - Cat's in the Bag.mkv
│   └── Season 02/
├── The Office (2005-2013)
│   └──  └── ...
```

### 5. Space Management (12TB = ~1500 Movies!)

| Quality | Size (2hr movie) | 12TB Capacity |
|---------|-----------------|---------------|
| 4K HDR | 50-80GB | ~150 movies |
| 1080p | 8-15GB | ~1000 movies |
| 720p | 2-4GB | ~4000 movies |
| Mobile | 500MB-1GB | ~15000 movies |

**Recommendation:** Mix quality levels
- Keep favorites in 4K
- Most in 1080p
- Family/phone stuff in 720p

---

## 🚀 PERFORMANCE TIPS

### USB 3.0 Drive Speed
```
Read Speed: ~100-200 MB/s
Write Speed: ~80-150 MB/s
```

**Good for:** 4-5 simultaneous streams

### NAS Speed (Gigabit)
```
Network Speed: ~100-120 MB/s
Good for: 2-3 simultaneous streams
```

### If Slow Streaming:
- Enable hardware transcoding in Jellyfin
- Use Direct Play when possible (no transcoding)

---

## 📋 QUICK REFERENCE

### Check Drive Status
```bash
# See mounted drives
df -h | grep -E "(Jellyfin|12TB)"

# Check available space on 12TB
du -sh /Volumes/JellyfinMedia

# See what's using space
du -sh /Volumes/JellyfinMedia/*
```

### Safely Eject
```bash
# Before unplugging
diskutil eject /Volumes/JellyfinMedia
```

### Reconnect
```bash
# Re-mount if unplugged
diskutil mountDisk /dev/disk4
```

---

## 📊 With 12TB, You Can Store:

- 🎬 **~120 movies** in 4K HDR (100GB each)
- 🎬 **~800 movies** in 1080p (15GB each)
- 📺 **~400 episodes** in 4K
- 📺 **~3000 episodes** in 1080p
- 🎵 **~20,000 albums** (flac format)
- 📷 **~100,000 photos** (raw format)

**Or a mix of everything!**

---

## 🎯 WHICH SETUP?

### Option 1: USB 12TB (Easiest)
**When to choose:** Quick setup, direct connection
```
USB Drive → Mac mini → Jellyfin
```

### Option 2: NAS
**When to choose:** Multiple devices need access, backup
```
NAS (12TB) → Network → Mac mini + other devices
```

### Option 3: Both (Best!)
**USB 12TB on Mac** = Main Jellyfin storage  
**NAS** = Backup copy + other devices access

**Which option sounds best for your setup?**
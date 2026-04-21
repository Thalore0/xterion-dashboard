# 🚀 CS Tutor Bot — Deployment Guide

**For:** Wayne's wife's AP CS Class
**Languages:** Java, C++, Python
**Features:** Auto-language detection, daily reports, no DMs

---

## 📋 PRE-DEPLOYMENT CHECKLIST

### Step 1: Get Discord Bot Token (5 min)

1. Go to: https://discord.com/developers/applications
2. Click "New Application"
3. Name: "CS-Tutor-Bot" (or whatever you prefer)
4. Go to "Bot" tab → "Add Bot" → "Yes"
5. **Copy the Token** (long string, keep it secret!)

---

### Step 2: Get Teacher's Discord ID (2 min)

1. Open Discord
2. Click your wife's username in a server
3. Click "Copy User ID" (enable Developer Mode in Settings → Advanced if needed)
4. **Save this ID**

---

### Step 3: Configure (2 min)

Edit `config.json`:
```json
{
  "discord_token": "PASTE_BOT_TOKEN_HERE",
  "teacher_discord_id": "PASTE_TEACHER_ID_HERE"
}
```

---

## 🚀 DEPLOY NOW

### Quick Start:

```bash
cd ~/.openclaw/workspace/projects/cs-tutor

# 1. Setup
./setup-bot.sh

# 2. Configure (edit config.json with your tokens)
nano config.json  # or any text editor

# 3. Start the bot
./start-bot.sh
```

**Bot is now running!**

---

## 🤖 TESTING

### Before inviting students:

1. **Create Discord server** (invite-only)
2. **Add channels:**
   - #java-help
   - #python-help
   - #cpp-help
   - #ask-anything
3. **Invite bot** to server
4. **Test:** Type in #java-help: "What is an ArrayList?"
5. **Verify:** Bot responds with educational help

---

## 📊 VERIFICATION

**Daily Summary:**
- ✅ Sent every morning at 7:30 AM
- ✅ Monday-Friday only (no weekends)
- ✅ DM to teacher's Discord account

**Channel Responses:**
- ✅ Responds in all help channels
- ✅ Never responds to DMs
- ✅ Auto-detects language from code

**Logs:**
- ✅ All interactions saved to `logs/interactions.jsonl`
- ✅ Teacher can view anytime

---

## 🔧 MAINTENANCE

**Check if running:**
```bash
ps aux | grep cstutor
```

**View logs:**
```bash
tail -f logs/bot.log
```

**Restart:**
```bash
./stop-bot.sh && ./start-bot.sh
```

**Stop:**
```bash
./stop-bot.sh
```

---

## 📈 MONITORING

**Teacher Views:**
- Real-time: Browse Discord channels anytime
- Summary: Check DM every morning at 7:30 AM
- History: View `logs/interactions.jsonl`
- Dashboard: https://Thalore0.github.io/xterion-dashboard/game-design/teacher-tools/cs-tutor/

---

## 🆘 TROUBLESHOOTING

### Bot not responding?
1. Check logs: `tail logs/bot.log`
2. Verify token in `config.json`
3. Restart: `./stop-bot.sh && ./start-bot.sh`

### Can't DMs work but channels don't?
- Check bot permissions in Discord server
- Ensure bot has "Send Messages" permission
- Try re-inviting with correct permissions

### Daily summary not sending?
- Check `teacher_discord_id` is correct
- Verify it's a weekday (Mon-Fri)
- Check logs for errors

---

## 💰 COST

**$0** — Only uses local models on your Mac
- Gemma 4 E4B for simple Q&A
- Qwen2.5-Coder for code review
- No API costs

---

## 🎉 READY TO GO!

**Deploy checklist:**
- [ ] Discord bot token obtained
- [ ] Teacher Discord ID obtained
- [ ] config.json updated
- [ ] setup-bot.sh ran
- [ ] Bot token configured
- [ ] Bot started with start-bot.sh
- [ ] Discord server created
- [ ] Channels created (#java-help, etc.)
- [ ] Bot invited to server
- [ ] Test message sent
- [ ] Students invited

**Support:** Check logs or ask Xterion!

---

*Built: April 21, 2026*
*Status: Ready for deployment* 🚀
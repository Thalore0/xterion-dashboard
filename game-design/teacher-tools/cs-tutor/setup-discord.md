# 🤖 CS Tutor Bot — Discord Setup Guide

## Step 1: Create Discord Server (if needed)

1. Open Discord → Click "+" → "Create My Own"
2. Name: "[Teacher Name]'s CS Class"
3. Skip template (we'll set up channels)

## Step 2: Create Channels

Create these channels:
- **#general** (default)
- **#java-help** — Java/AP CS A questions
- **#python-help** — Python questions
- **#cpp-help** — C++ questions
- **#general-cs** — Concepts, algorithms, theory
- **#bot-commands** — Admin only

## Step 3: Create Discord Bot

1. Go to: https://discord.com/developers/applications
2. Click "New Application"
3. Name: "CS-Tutor-Bot"
4. Go to "Bot" section → "Add Bot"
5. Copy the **Token** (keep this secret!)

## Step 4: Invite Bot to Server

1. In Discord Developer Portal → "OAuth2" → "URL Generator"
2. Scopes: `bot`
3. Bot Permissions: 
   - Send Messages
   - Read Message History
   - View Channels
4. Copy the generated URL
5. Paste in browser → Select your server → Authorize

## Step 5: Configure OpenClaw

Give me the bot token:
```bash
openclaw config set discord.cstutor.token = "YOUR_BOT_TOKEN_HERE"
```

## Step 6: Start the Bot

```bash
python3 /Users/thalorewalker/.openclaw/workspace/projects/cs-tutor/bot/cstutor-discord.py
```

## Testing

1. Join your Discord server
2. Type in #java-help: "Why is my while loop infinite?"
3. Bot should respond with educational debugging help

## Teacher Features

- **Logs:** All interactions saved for review
- **Analytics:** Track common student questions
- **Moderation:** Auto-flag inappropriate content

---

**Ready to set this up?** Just create the Discord server and I'll help with the rest!
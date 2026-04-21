#!/usr/bin/env python3
"""
CS Tutor Discord Bot — AP CS Assistant for High School Students
Built for: Wayne's wife's CS class
Features: Auto-language detection, daily summary reports, no DMs
"""

import discord
from discord.ext import tasks, commands
import json
import os
import re
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path

# Import our tutor logic
import sys
sys.path.insert(0, '.')
from cstutor_bot import CSTutorBot

class CSTutorDiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix='!',
            intents=intents,
            help_command=None  # Disable default help
        )
        
        self.tutor = CSTutorBot()
        self.interactions_log = []
        self.teacher_id = None  # Will be set from config
        
    async def setup_hook(self):
        """Called when bot is ready"""
        # Start background tasks
        self.daily_summary_task.start()
        print(f'🤖 CS Tutor Bot logged in as {self.user}')
        
        # Get teacher ID from config
        config_path = Path.home() / ".openclaw/workspace/projects/cs-tutor/config.json"
        if config_path.exists():
            with open(config_path) as f:
                config = json.load(f)
                self.teacher_id = config.get('teacher_discord_id')
    
    async def on_message(self, message):
        """Handle incoming messages"""
        # Ignore bot's own messages
        if message.author == self.user:
            return
        
        # Check if DM (private message)
        if isinstance(message.channel, discord.DMChannel):
            await message.channel.send(
                "🤖 I can only help in the class channels!\n\n"
                "Please post in:\n"
                "• #java-help for Java\n"
                "• #python-help for Python\n" 
                "• #cpp-help for C++\n"
                "• #ask-anything for general CS\n\n"
                "See you there! 👋"
            )
            return
        
        # Check if message is in allowed channels
        allowed_channels = ['java-help', 'python-help', 'cpp-help', 'ask-anything']
        if message.channel.name not in allowed_channels:
            return
        
        # Generate response
        response = self.tutor.generate_response(
            message.content,
            str(message.author),
            {'is_private': False}
        )
        
        # Log interaction for teacher
        self.log_interaction(
            username=str(message.author),
            question=message.content,
            response=response,
            channel=message.channel.name
        )
        
        # Send response
        await message.channel.send(response)
    
    def log_interaction(self, username, question, response, channel):
        """Log for teacher review and daily summary"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'username': username,
            'channel': channel,
            'question': question[:200],  # Truncate for summary
            'language': self.tutor.detect_language(question),
            'response_type': 'educational'
        }
        
        self.interactions_log.append(entry)
        
        # Also save to file
        log_file = Path.home() / ".openclaw/workspace/projects/cs-tutor/logs/interactions.jsonl"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    
    @tasks.loop(hours=24)
    async def daily_summary_task(self):
        """Send daily summary to teacher every morning"""
        # Check if it's a weekday and after 7 AM
        now = datetime.now()
        
        # Only send on weekdays (Monday=0, Friday=4)
        if now.weekday() >= 5:  # Saturday or Sunday
            return
        
        # Check if we have teacher configured
        if not self.teacher_id:
            print("⚠️ Teacher Discord ID not configured")
            return
        
        # Wait until 7:30 AM
        target_time = now.replace(hour=7, minute=30, second=0, microsecond=0)
        if now < target_time:
            wait_seconds = (target_time - now).total_seconds()
            await asyncio.sleep(wait_seconds)
        
        # Generate summary
        summary = self.generate_daily_summary()
        
        # Send to teacher
        try:
            teacher = await self.fetch_user(self.teacher_id)
            if teacher:
                await teacher.send(summary)
                print(f"✅ Daily summary sent to teacher at {datetime.now()}")
        except Exception as e:
            print(f"❌ Failed to send summary: {e}")
        
        # Clear old interactions (keep last 7 days)
        cutoff = datetime.now() - timedelta(days=7)
        self.interactions_log = [
            i for i in self.interactions_log 
            if datetime.fromisoformat(i['timestamp']) > cutoff
        ]
    
    @daily_summary_task.before_loop
    async def before_daily_summary(self):
        """Wait until bot is ready"""
        await self.wait_until_ready()
    
    def generate_daily_summary(self):
        """Generate daily report for teacher"""
        yesterday = datetime.now() - timedelta(days=1)
        yesterday_date = yesterday.strftime('%Y-%m-%d')
        
        # Filter yesterday's interactions
        yesterday_interactions = [
            i for i in self.interactions_log
            if i['timestamp'].startswith(yesterday_date)
        ]
        
        if not yesterday_interactions:
            return f"""📊 CS Tutor Daily Report — {yesterday_date}

💤 No student questions yesterday.

---
*Next report: Tomorrow at 7:30 AM (school days only)*"""
        
        # Analyze data
        questions_by_channel = defaultdict(list)
        questions_by_student = defaultdict(int)
        language_counts = defaultdict(int)
        
        for interaction in yesterday_interactions:
            questions_by_channel[interaction['channel']].append(interaction['question'])
            questions_by_student[interaction['username']] += 1
            language_counts[interaction['language']] += 1
        
        # Find trending topics (simplified - just count questions per channel)
        top_channels = sorted(
            questions_by_channel.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )[:3]
        
        # Build summary
        summary = f"""📊 CS Tutor Daily Report — {yesterday_date}

📈 Activity Summary:
• Total questions: {len(yesterday_interactions)}
• Active students: {len(questions_by_student)}
• Response time: < 1 minute (automated)

📚 Questions by Language:
☕ Java: {language_counts.get('java', 0)}
🐍 Python: {language_counts.get('python', 0)}
➕ C++: {language_counts.get('cpp', 0)}
📖 General CS: {language_counts.get('general', 0)}

🏆 Most Active Channels:
"""
        
        for channel, questions in top_channels:
            summary += f"• #{channel}: {len(questions)} questions\n"
        
        summary += f"""
👥 Active Students:
"""
        
        top_students = sorted(
            questions_by_student.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        
        for student, count in top_students:
            summary += f"• {student}: {count} questions\n"
        
        # Sample questions (anonymized)
        summary += """
💡 Sample Questions Asked:
"""
        for i, interaction in enumerate(yesterday_interactions[:3], 1):
            question = interaction['question'][:80] + "..." if len(interaction['question']) > 80 else interaction['question']
            summary += f"{i}. \"{question}\"\n"
        
        summary += """
📊 View Full Activity:
https://Thalore0.github.io/xterion-dashboard/

---
*Bot is running 24/7 • Responding in: #java-help, #python-help, #cpp-help, #ask-anything*
*Next report: Tomorrow at 7:30 AM (school days only)*"""
        
        return summary

# Bot startup
if __name__ == "__main__":
    import asyncio
    
    # Get token from environment or config
    token = os.getenv('DISCORD_TOKEN')
    
    if not token:
        config_path = Path.home() / ".openclaw/workspace/projects/cs-tutor/config.json"
        if config_path.exists():
            with open(config_path) as f:
                config = json.load(f)
                token = config.get('discord_token')
    
    if not token:
        print("❌ Error: Discord token not found")
        print("Set DISCORD_TOKEN environment variable or add to config.json")
        exit(1)
    
    bot = CSTutorDiscordBot()
    bot.run(token)

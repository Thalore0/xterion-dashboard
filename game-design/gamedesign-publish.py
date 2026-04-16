#!/usr/bin/env python3
"""
Game Design Publishing System
Publishes game design content to xterion-dashboard/game-design/
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
import sys

class GameDesignPublisher:
    def __init__(self):
        self.repo_dir = Path.home() / ".openclaw/workspace/xterion-dashboard"
        self.game_dir = self.repo_dir / "game-design"
        
    def validate_repo(self):
        """Ensure repo exists and is set up"""
        if not self.repo_dir.exists():
            print("❌ Error: Repo not found")
            return False
        if not self.game_dir.exists():
            print("❌ Error: game-design/ not initialized. Run setup first.")
            return False
        return True
    
    def add_concept(self, title, description, added_by="Wayne"):
        """Add a new game concept"""
        safe_title = title.lower().replace(" ", "-").replace("_", "-")
        concept_file = self.game_dir / "concepts" / f"{safe_title}.md"
        
        # Load template
        template_path = self.game_dir / "concepts/TEMPLATE-idea.md"
        if template_path.exists():
            with open(template_path) as f:
                template = f.read()
        else:
            template = "# {title}\n\n{description}"
        
        # Fill template
        content = template.replace("[TITLE]", title)
        content = content.replace("[Working Title]", title)
        content = content.replace("YYYY-MM-DD", datetime.now().strftime("%Y-%m-%d"))
        content = content.replace("[Wayne / Jason / Both]", added_by)
        
        # Add description if provided
        if description and "[What makes this game unique?]" in content:
            content = content.replace("[What makes this game unique?]", description)
        
        # Write file
        with open(concept_file, 'w') as f:
            f.write(content)
        
        print(f"✅ Concept added: {concept_file}")
        return concept_file
    
    def update_gdd(self, section, content):
        """Update Game Design Document section"""
        gdd_path = self.game_dir / "documents/game-design-doc.md"
        
        if not gdd_path.exists():
            # Create from template
            template = self.game_dir / "documents/GDD-TEMPLATE.md"
            if template.exists():
                with open(template) as f:
                    gdd_content = f.read()
            else:
                gdd_content = f"# Game Design Document\n\nCreated: {datetime.now().strftime('%Y-%m-%d')}\n\n"
            
            with open(gdd_path, 'w') as f:
                f.write(gdd_content)
        else:
            with open(gdd_path) as f:
                gdd_content = f.read()
        
        # Update section (simplified - would need proper parsing for real use)
        update_line = f"\n## {section}\n\n{content}\n\n*Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
        
        with open(gdd_path, 'a') as f:
            f.write(update_line)
        
        print(f"✅ GDD updated: {section}")
        return gdd_path
    
    def push_to_github(self, commit_message=None):
        """Publish changes to GitHub"""
        os.chdir(self.repo_dir)
        
        try:
            # Stage changes
            subprocess.run(["git", "add", "-A"], check=True, capture_output=True)
            
            # Check if there are changes
            result = subprocess.run(["git", "status", "--porcelain"], 
                                    capture_output=True, text=True)
            if not result.stdout.strip():
                print("ℹ️  No changes to publish")
                return
            
            # Commit
            msg = commit_message or f"Update game design - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            subprocess.run(["git", "commit", "-m", msg], check=True, capture_output=True)
            
            # Push
            subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True)
            
            print(f"✅ Published to GitHub!")
            print(f"   URL: https://Thalore0.github.io/xterion-dashboard/game-design/")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to publish: {e}")
            print(f"   Error: {e.stderr.decode() if e.stderr else 'Unknown error'}")
    
    def get_status(self):
        """Show current game design status"""
        print("\n📊 GAME DESIGN STATUS")
        print("=" * 50)
        
        # Count concepts
        concepts_dir = self.game_dir / "concepts"
        concepts = list(concepts_dir.glob("*.md")) if concepts_dir.exists() else []
        concepts = [c for c in concepts if c.name != "TEMPLATE-idea.md"]
        print(f"Concepts: {len(concepts)}")
        for c in concepts:
            print(f"  • {c.stem}")
        
        # Check GDD
        gdd_path = self.game_dir / "documents/game-design-doc.md"
        if gdd_path.exists():
            print(f"\nGDD: ✅ Exists")
        else:
            print(f"\nGDD: ⬜ Not started")
        
        # Assets tracking
        assets_path = self.game_dir / "assets/README.md"
        if assets_path.exists():
            print(f"Assets: ✅ Tracked")
        else:
            print(f"Assets: ⬜ Not started")
        
        print(f"\nView online: https://Thalore0.github.io/xterion-dashboard/game-design/")

def main():
    publisher = GameDesignPublisher()
    
    if not publisher.validate_repo():
        sys.exit(1)
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  gamedesign-publish.py status              - Show current status")
        print("  gamedesign-publish.py concept 'Title'     - Add new concept")
        print("  gamedesign-publish.py push                - Push all changes to GitHub")
        print("")
        print("  gamedesign-publish.py status")
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "status":
        publisher.get_status()
    
    elif command == "concept" and len(sys.argv) >= 3:
        title = sys.argv[2]
        desc = sys.argv[3] if len(sys.argv) > 3 else ""
        publisher.add_concept(title, desc)
        if input("Push to GitHub? (y/n): ").lower() == 'y':
            publisher.push_to_github(f"Add concept: {title}")
    
    elif command == "push":
        publisher.push_to_github()
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()

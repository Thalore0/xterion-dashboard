#!/usr/bin/env python3
"""
CS Tutor Bot - AP CS Assistant for High School Students
Teaches Java, C++, Python with Socratic method
"""

import json
import re
from datetime import datetime
from pathlib import Path

class CSTutorBot:
    def __init__(self):
        self.allowed_languages = ['java', 'python', 'cpp', 'c++']
        self.homework_keywords = ['homework', 'assignment', 'due', 'submit']
        self.test_keywords = ['test', 'quiz', 'exam', 'assessment', 'frq', 'ap exam']
        
    def detect_language(self, message):
        """Auto-detect language from code patterns"""
        
        # Strong Java indicators
        java_patterns = [
            r'public\s+class\s+\w+',
            r'public\s+static\s+void\s+main',
            r'System\.out\.println',
            r'System\.in',
            r'Scanner\s+\w+\s*=\s*new\s+Scanner',
            r'ArrayList<',
            r'import\s+java\.',
            r'extend\s+\w+',
            r'implements\s+\w+',
            r'Thread',
            r'@Override',
        ]
        
        # Strong C++ indicators
        cpp_patterns = [
            r'#include\s*<\s*(iostream|vector|map|string|fstream|cmath)',
            r'using\s+namespace\s+std',
            r'cout\s*<<',
            r'cin\s*>>',
            r'std::',
            r'vector<\s*\w+\s*>',
            r'void\s+\w+\s*\([^)]*\)\s*\{',
            r'nullptr',
            r'class\s+\w+\s*:\s*public\s+\w+', # inheritance
        ]
        
        # Strong Python indicators
        python_patterns = [
            r'def\s+\w+\s*\([^)]*\)\s*:',
            r'class\s+\w+\s*\([^)]*\)\s*:',
            r'if\s+__name__\s*==\s*["\']__main__["\']',
            r'print\s*\(',
            r'len\s*\(',
            r'range\s*\(',
            r'import\s+\w+',
            r'from\s+\w+\s+import',
            r'#\s*comment|#\s*todo',
            r'\s+if\s+\w+\s*:\s*\n\s+',  # if with indentation
            r'\bin\s+range\(',
            r'\.append\s*\(',
        ]
        
        # Count matches for each language
        java_score = sum(1 for pattern in java_patterns if re.search(pattern, message))
        cpp_score = sum(1 for pattern in cpp_patterns if re.search(pattern, message))
        python_score = sum(1 for pattern in python_patterns if re.search(pattern, message))
        
        # Determine winner
        scores = [('java', java_score), ('cpp', cpp_score), ('python', python_score)]
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Need at least 2 strong indicators to be confident
        if scores[0][1] >= 2:
            return scores[0][0]
        elif scores[0][1] == 1:
            # Weak match - might need to ask
            return 'ambiguous'
        
        # Check for file extensions mentioned
        if '.java' in message:
            return 'java'
        elif '.py' in message:
            return 'python'
        elif '.cpp' in message or '.h' in message:
            return 'cpp'
        
        return 'general'
    
    def get_language_clarification(self, message):
        """Ask user to clarify language if ambiguous"""
        return """🤖 **Language Detection Help**

I see code but I'm not 100% sure which language this is.

**Is this:**
☕ Java
🐍 Python  
➕ C++

Just reply with "Java", "Python", or "C++" and I'll help you!

*Tip: You can also mention the language in your question like "How do I loop in Java?"*"""
    
    def is_test_question(self, message):
        """Detect if student is asking about test/quiz"""
        return any(word in message.lower() for word in self.test_keywords)
    
    def is_direct_homework_request(self, message):
        """Detect if student wants direct answer"""
        patterns = [
            r'write (me )?(a|the)? (code|method|program|function)',
            r'give me (the )?(code|answer|solution)',
            r'check (if |my )?(this |that )?(is )?right',
            r'do (my |the )?(homework|assignment)'
        ]
        return any(re.search(pattern, message.lower()) for pattern in patterns)
    
    def is_direct_message(self, message_metadata):
        """Check if message is private (DM)"""
        return message_metadata.get('is_private', False)
    
    def generate_response(self, message, username, message_metadata=None):
        """Generate educational response"""
        
        # Check if DM (should redirect to channel)
        if message_metadata and self.is_direct_message(message_metadata):
            return self.get_no_dm_response()
        """Generate educational response"""
        language = self.detect_language(message)
        
        # Safety checks
        if self.is_test_question(message):
            return self.get_test_boundary_response()
        
        if self.is_direct_homework_request(message):
            return self.get_socratic_redirection()
        
        # Check if language is ambiguous
        if language == 'ambiguous':
            return self.get_language_clarification(message)
        
        # Generate help based on question type
        if language == 'general' and ('code' in message.lower() or '{' in message or '(' in message):
            # Has code but couldn't detect language, ask for clarification
            return self.get_language_clarification(message)
        
        if 'error' in message.lower() or 'bug' in message.lower() or 'doesn\'t work' in message.lower():
            return self.get_debugging_help(message, language)
        
        if 'explain' in message.lower() or 'what is' in message.lower() or 'how does' in message.lower():
            return self.get_concept_explanation(message, language)
        
        if 'review' in message.lower() or 'feedback' in message.lower():
            return self.get_code_review_offer(message, language)
        
        # General CS help
        return self.get_general_cs_help(language)
    
    def get_no_dm_response(self):
        """Response when student tries to DM the bot"""
        return """🤖 CS Tutor Bot

I can only help in the class channels! This way your classmates can learn from your question too.

Please post in:
• #java-help for Java questions
• #python-help for Python questions
• #cpp-help for C++ questions
• #ask-anything for general CS questions

See you there! 👋"""
    
    def get_test_boundary_response(self):
        return """🚫 **Test/Assessment Boundary**

I can't help with questions during tests, quizzes, or AP exam practice.

**Why:** This is about *your* learning and assessment integrity.

**Instead:**
• Before the test: Ask me to explain concepts you're unsure about
• After the test: We can review mistakes together
• Studying: Practice with me on similar (not identical) problems

You've got this! 💪"""
    
    def get_socratic_redirection(self):
        return """🤔 **Learning Moment!**

I'd love to help, but I won't write the code for you — that wouldn't help you learn.

**Let's try this:**
1. What have you tried so far?
2. What specific part is confusing?
3. What do you *think* the answer should be?

**Or ask me:**
- "Can you explain [concept]?"
- "Why does [X] happen?"
- "What's the difference between [A] and [B]?"

I'm here to guide you to the answer! 🎯"""
    
    def get_debugging_help(self, message, language):
        """Provide debugging guidance"""
        lang_str = language.upper() if language != 'general' else "CODE"
        
        return f"""🔍 **{lang_str} Debugging Help**

Let's debug this together!

**Step 1: Read the Error**
What does the error message say? Copy it here.

**Step 2: Find the Line**
Which line number is causing issues?

**Step 3: Check the Basics**
- Are all brackets/parentheses matched?
- Are variables initialized before use?
- Is the syntax correct for this language?

**Step 4: Add Debug Output**
Try adding print statements to see what's happening:
```{language}
System.out.println("Debug: x = " + x);  // Java
print(f"Debug: x = {{x}}")              # Python  
cout << "Debug: x = " << x << endl; // C++
```

What do you see when you run it with debug prints?"""
    
    def get_concept_explanation(self, message, language):
        """Explain CS concepts"""
        # Detect specific concept
        concepts = {
            'arraylist': "ArrayLists are dynamic arrays that grow automatically...",
            'inheritance': "Inheritance lets a class get features from another class...",
            'recursion': "Recursion is when a method calls itself...",
            'pointer': "A pointer stores a memory address...",
            'loop': "Loops repeat code while a condition is true...",
        }
        
        # Find matching concept
        for concept, explanation in concepts.items():
            if concept in message.lower():
                return f"""📚 **{concept.title()}**

{explanation}

**Analogy:** Think of it like...

**In code:**
```{language}
// Example would go here
```

Does that help? Want me to explain it another way?"""
        
        return """📚 **Concept Explanation**

I'd love to explain! Could you tell me:
1. What specifically is confusing?
2. What do you already understand?
3. How does your textbook/teacher explain it?

I can try a different approach! 🎯"""
    
    def get_code_review_offer(self, message, language):
        """Offer to review code"""
        return """✏️ **Code Review Offer**

I'd be happy to review your code!

**Paste your code** and I'll give feedback on:
- ✅ Logic and approach
- ✅ Style and readability
- ✅ Potential bugs or edge cases
- ✅ Suggestions for improvement

**Note:** I'll guide you to improvements, not just tell you what's wrong. Learning > fixing! 

Go ahead, paste the code you're working on!"""
    
    def get_general_cs_help(self, language):
        """General CS help"""
        lang_str = language.upper() if language != 'general' else "CS"
        
        return f"""🤖 **{lang_str} Help Ready!**

I can help you with:

📖 **Concepts** — Explain OOP, recursion, algorithms, data structures

🔍 **Debugging** — Walk through errors step-by-step

✏️ **Code Review** — Give feedback on your code

💡 **Study Tips** — AP exam strategies, practice approaches

📝 **Best Practices** — Style, efficiency, readability

**What would you like help with?** Just ask!"""
    
    def log_interaction(self, username, message, response, language):
        """Log for teacher review"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "student": username,
            "language": language,
            "question": message[:100] + "..." if len(message) > 100 else message,
            "response_type": "educational"
        }
        
        log_file = Path.home() / ".openclaw/workspace/projects/cs-tutor/logs/student-interactions.jsonl"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

# For testing
if __name__ == "__main__":
    bot = CSTutorBot()
    
    test_messages = [
        "Why is my while loop infinite?",
        "Can you write me a method to sort an ArrayList?",
        "What's on the quiz tomorrow?",
        "Explain inheritance in Java",
        "my code doesn't work help"
    ]
    
    for msg in test_messages:
        print(f"\nStudent: {msg}")
        print(f"Bot:\n{bot.generate_response(msg, 'test_student')}")
        print("-" * 50)

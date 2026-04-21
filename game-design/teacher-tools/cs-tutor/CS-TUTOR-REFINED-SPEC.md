# 🤖 CS Tutor Bot — Refined Specification
**Updated:** April 21, 2026

---

## 📋 REFINED REQUIREMENTS

### 1. Language Support — ALL THREE
**Java, C++, Python**

**Auto-Detection:**
- Bot should identify language from code snippets automatically
- If student isn't sure, bot analyzes syntax
- Falls back to asking if ambiguous

**Detection Logic:**
```
if contains("public static void main") or ends with(".java") → Java
if contains("#include") or "cout" or "std::" → C++
if contains("def ") or "print(" or indentation-based blocks → Python
if contains("System.out.println") → Java
if contains("len(") and no semicolons → Python
if contains("using namespace") → C++
else → Ask student to clarify
```

---

### 2. Access — INVITE ONLY

**Server Setup:**
- Private Discord server (not discoverable)
- Invite link shared by teacher
- Students must accept invite to join
- Can revoke access if needed

**Channel Structure:**
```
#general — Welcome, rules, bot intro
#java-help — Java-specific questions
#python-help — Python-specific questions  
#cpp-help — C++ specific questions
#ask-anything — General CS questions
#bot-updates — Admin only (logs visible here)
```

---

### 3. Automation + Visibility

**Fully Automated Responses:**
- Bot responds immediately in channel
- No approval needed per response
- Works 24/7

**Teacher Visibility:**
- ✅ All conversations happen in PUBLIC channels
- ✅ Wife can see every question and answer
- ✅ No private messages with students
- ✅ Real-time monitoring

**Optional Enhancement:**
- Daily summary report (DM to wife with summary of questions)
- Highlights topics students struggled with

---

### 4. No Private Messages

**Hard Rule:**
```python
if message.is_private():
    return "Please ask in the appropriate channel so everyone can learn!"
```

**Why:**
- Students learn from each other's questions
- Teacher can see all interactions
- Community learning environment
- Prevents cheating in private

---

## 🔍 AUTO-LANGUAGE DETECTION

### Code Pattern Recognition

**Java Indicators:**
- `public class`, `public static void main`
- `System.out.println`, `Scanner`, `ArrayList`
- `extends`, `implements`
- `import java.*`
- Semicolons + curly braces

**C++ Indicators:**
- `#include <iostream>`
- `using namespace std`
- `cout <<`, `cin >>`
- `int main()` (without public static)
- `vector<...>`, `map<...>`

**Python Indicators:**
- `def function_name():` (colon + indentation)
- `print()`, `len()`, `range()`
- `if __name__ == "__main__":`
- No semicolons (mostly)
- Significant whitespace

**Example Response:**
```
Student: "Here's my code: [paste]"

Bot: "🔍 I see you're working with Java! 
  (Detected: public class, System.out.println, .java syntax)
  
  Posting your question in #java-help..."
  
[Then provides help in context of Java]
```

---

## 📊 TEACHER VISIBILITY FEATURES

### Real-Time Monitoring
- Wife can browse channels anytime
- See all questions students ask
- See how bot responds
- Jump in with additional help if needed

### Daily Summary (Optional)
```
📊 CS Tutor Daily Report — April 21, 2026

Top Student Questions:
1. "Infinite loop help" (Java) — 3 students
2. "Array vs ArrayList" (Java) — 2 students
3. "Pointer confusion" (C++) — 4 students

Students Active Today: 15
Total Interactions: 42

Topics Trending Up:
• Inheritance (Java)
• References vs Pointers (C++)
• List comprehensions (Python)

Students Struggling With:
• While loop conditions
• Memory management (C++)
• Class design
```

---

## 🛡️ UPDATED SAFETY RULES

### In-Channel Only (Hard Enforced)
**If student DMs the bot:**
```
🤖 CS Tutor

I can only help in the class channels! 
This way your classmates can learn from your question too.

Please post in:
• #java-help for Java
• #python-help for Python
• #cpp-help for C++
• #ask-anything for general CS

See you there! 👋
```

### Homework Boundaries (Maintain)
- ✅ Guide students through thinking
- ✅ Explain concepts
- ✅ Debug with hints
- ❌ Never write full solutions

---

## 🚀 NEXT STEPS — Refined

### Phase 1: Setup (This Week)
- [ ] Create invite-only Discord server
- [ ] Set up 4 help channels
- [ ] Configure bot (no DM responses)
- [ ] Add language detection

### Phase 2: Test (Next Week)
- [ ] Pilot with 3-5 volunteer students
- [ ] Your wife monitors conversations
- [ ] Gather feedback
- [ ] Adjust responses

### Phase 3: Deploy (Following Week)
- [ ] Invite all students
- [ ] Monitor first week
- [ ] Enable daily reports for wife
- [ ] Document common questions

---

## ✅ APPROVAL CHECKPOINT

**Ready to build with these specs?**
- ✅ Three languages (auto-detect)
- ✅ Invite-only Discord
- ✅ Fully automated, public channel responses
- ✅ Teacher sees everything
- ✅ No private messages

**Confirm:** Build with these refined requirements?
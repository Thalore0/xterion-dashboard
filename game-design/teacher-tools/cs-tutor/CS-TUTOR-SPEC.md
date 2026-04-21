# 🤖 CS Tutor Bot — AP CS Assistant
**For:** [Wife's Name]'s High School CS Classes  
**Languages:** Java, C++, Python  
**Focus:** Educational help (not cheating), AP CS A prep

---

## 🎯 CORE PRINCIPLES

### 1. Socratic Method — Never Give Direct Answers
**Bad:** "Use `ArrayList<String>` here"  
**Good:** "What data structure lets you store items in order and access by index?"

### 2. Code Review — Guide, Don't Fix
**Bad:** "Change line 3 to `i < 10`"  
**Good:** "What happens to `i` in your loop? When does it stop?"

### 3. Safety First — High School Appropriate
- ✅ Encourage learning
- ✅ Explain concepts
- ✅ Debug with hints
- ❌ Never write full solutions to homework
- ❌ Never help on assessments/tests
- ❌ No inappropriate content

---

## 📚 LANGUAGE COVERAGE

### Java (Primary — AP CS A)
- OOP concepts (classes, inheritance, polymorphism)
- Arrays vs ArrayList
- Loops, conditionals, recursion
- File I/O (AP CS A curriculum)
- Sorting algorithms (selection, insertion, merge)
- FRQ strategies

### C++ (Intro/Advanced)
- Pointers and memory management
- References vs values
- Header/implementation files
- STL basics (vector, map)
- Object-oriented patterns

### Python (Intro/Flexible)
- Lists, dictionaries
- Functions, classes
- File handling
- Simple algorithms
- Transition to typed languages

---

## 🛠️ TECHNICAL ARCHITECTURE

### Option A: Discord Bot (Recommended)
```
Student posts in #java-help, #cpp-help, #python-help
Bot responds with guided hints
Logs for teacher review
```

**Pros:**
- Students already use Discord
- Public/transparent (students help each other)
- Built-in moderation tools
- I can track usage for your wife

**Cons:**
- Need Discord server
- Students need accounts

### Option B: Web Interface
```
Simple chat interface hosted on GitHub Pages
Student types question → Bot responds
```

**Pros:**
- No Discord required
- Clean, focused UI
- Easy to share link

**Cons:**
- Less community interaction
- More setup

---

## 📝 RESPONSE TEMPLATES

### Debugging Template
```
🔍 Debugging Help

I see you have an issue with [brief description].

Let's think through this:
1. What do you expect [variable] to be?
2. What is it actually?
3. Look at line [X] — what happens there?

Try adding: `System.out.println("Debug: " + variable);`

What does it show?
```

### Concept Explanation Template
```
📚 [Concept Name]

Think of it like [real-world analogy]:
- [Point 1]
- [Point 2]
- [Point 3]

In code:
```java
// Simple example
```

Does that help clarify?
```

### Code Review Template
```
✏️ Code Review

**Strengths:**
- [Good thing 1]
- [Good thing 2]

**Suggestions:**
- Consider [improvement 1]
- [Style/efficiency tip]

**Question:**
What would happen if [edge case]?
```

---

## 🚫 BOUNDARIES (Critical for Education)

### Homework Help — ALLOWED
✅ "Why does my loop run forever?"  
✅ "What's the difference between `==` and `.equals()`?"  
✅ "How do I start thinking about [algorithm]?"  
✅ "Can you explain [concept] in a different way?"

### Homework Help — NOT ALLOWED
❌ "Write me a method to reverse an ArrayList"  
❌ "Here's my homework, check if it's right" (without effort)  
❌ "Give me the code for [assignment]"

### Test Help — NEVER ALLOWED
❌ Any question during assessment time  
❌ "Is the answer [X] for the quiz?"  
❌ "Explain the FRQ from today's test"

---

## 📊 TEACHER DASHBOARD

Your wife can see:
- Most common questions
- Topics students struggle with
- Students who need extra help
- Popular office hours topics

---

## 🚀 DEPLOYMENT PLAN

### Phase 1: MVP (This Week)
- [ ] Discord server setup
- [ ] Basic bot responding
- [ ] Java support
- [ ] Safety filters

### Phase 2: Full Launch
- [ ] C++ and Python support
- [ ] Teacher dashboard
- [ ] Analytics
- [ ] Student usage tracking

### Phase 3: Enhancement
- [ ] Practice problem generator
- [ ] AP exam FRQ prep
- [ ] Code execution (run student code)

---

## 💰 COST

**FREE** — Uses your local models:
- Gemma 4 E4B for simple Q&A
- Qwen2.5-Coder for code review
- Cloud models only as fallback

**Your cost:** $0

---

## ✅ NEXT STEPS

1. Choose platform (Discord vs Web) — **Recommend Discord**
2. Create Discord server
3. Configure bot permissions
4. Test with pilot students
5. Launch class-wide

**Ready to build this?** I can have a basic Discord bot running today!
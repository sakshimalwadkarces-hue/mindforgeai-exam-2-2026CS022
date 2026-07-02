Here is the simple, easy-to-read explanation for Question 5, packed inside a single code block so you can copy and paste it directly into your Markdown file!

Markdown
# 🧠 Easy Guide: Question 5 Readiness Score Function

This document explains how the `readiness_score` function works in plain, simple English. 

---

## 📝 1. The Python Code

Here is the code you write on your exam paper. It takes three pieces of student data and calculates a final score out of 100.

```python
def readiness_score(attendance_pct, diary_entries, task_count):
    # Setup the maximum targets for the student
    MAX_DIARY = 15
    MAX_TASKS = 10
    
    # Calculate points for each category
    attendance_points = attendance_pct * 0.40
    diary_points = (diary_entries / MAX_DIARY) * 30
    task_points = (task_count / MAX_TASKS) * 30
    
    # Add all the points together
    total_score = attendance_points + diary_points + task_points
    
    # Safety Check: Make sure the score never goes over 100
    if total_score > 100:
        return 100.0
    else:
        return round(total_score, 2)
```

---

## 📊 2. How the Scoring System Works (The Weights)

To make a fair final score out of 100, we split the points into three simple categories based on what matters most:

* **Attendance (40% of final score):** Worth up to **40 points**. Since attendance is already a percentage (like 90%), we just multiply it by 0.40.
* **Diary Entries (30% of final score):** Worth up to **30 points**. We expect students to write 15 entries.
* **Tasks Completed (30% of final score):** Worth up to **30 points**. We expect students to finish 10 tasks.

---

## 📐 3. Simple Math Example

Let's see how the computer calculates the score for a real student who has **92% attendance**, wrote **12 diaries**, and finished **8 tasks**:

1.  **Attendance Points:** $92 \times 0.40 =$ **$36.8$ points**
2.  **Diary Points:** The student did 12 out of 15 diaries. That is 80% of their diary goal. 
    $80\% \text{ of } 30 =$ **$24.0$ points**
3.  **Task Points:** The student did 8 out of 10 tasks. That is 80% of their task goal. 
    $80\% \text{ of } 30 =$ **$24.0$ points**
4.  **Final Total:** Add them up: 
    $36.8 + 24.0 + 24.0 =$ **$84.8$ out of 100**

---

## 🔀 4. Why do we need the `if/else` block?

The `if/else` block acts as a **safety net** for the grading system. 

* **The `if` part:** Imagine a student does extra credit work and gets 16 out of 15 diaries. Their total score might mathematically add up to 102. The `if total_score > 100:` line catches this and caps their score perfectly at **100.0** so it stays realistic.
* **The `else` part:** If the student's score is normal (under 100, like our example of 84.8), it skips the cap and uses `round(total_score, 2)` to clean up any messy decimal numbers so it looks nice on a report card.
# ⚙️ Technical Explanation: Question 4 Control Flow Trace

This document provides a technical breakdown of how the computer evaluates the `if/elif/else` logic using a text-based decision tree, followed by the exact dry-run outputs.

## 📝 The Code Logic
```python
if score < 40:
    band = "Support"
elif score < 70:
    band = "Developing"
elif score < 90:
    band = "Strong"
else:
    band = "Excellent"
```

---

## 🌳 Technical Flowchart (Decision Tree)
Computers read `if/elif/else` blocks sequentially from top to bottom. As soon as one condition is `True`, it executes that block and **skips the rest**.

```text
[ START: Evaluate Score ]
          │
          ▼
   ( Is score < 40? ) ───── Yes ─────▶ [ band = "Support" ] ─┐
          │                                                  │
          No                                                 │
          │                                                  │
          ▼                                                  │
   ( Is score < 70? ) ───── Yes ─────▶ [ band = "Developing"]│
          │                                                  │
          No                                                 │
          │                                                  │
          ▼                                                  │
   ( Is score < 90? ) ───── Yes ─────▶ [ band = "Strong" ] ──┤
          │                                                  │
          No                                                 │
          │                                                  │
          ▼                                                  │
[ band = "Excellent" ] ──────────────────────────────────────┘
                                                             │
                                                             ▼
                                                       [ END BLOCK ]
```

---

## 🔍 Dry-Run Execution & Final Answers

Here is exactly how the data flows through the logic tree for the given test scores:

* **Test 1: Score 38**
  * **Evaluation:** `38 < 40` evaluates to **True**.
  * **Result:** Execution stops at the first branch.
  * **Output:** `band = "Support"`

* **Test 2: Score 62**
  * **Evaluation:** `62 < 40` is False. The computer moves down to the next branch. `62 < 70` evaluates to **True**.
  * **Result:** Execution stops at the second branch.
  * **Output:** `band = "Developing"`

* **Test 3: Score 81**
  * **Evaluation:** `81 < 40` is False. `81 < 70` is False. `81 < 90` evaluates to **True**.
  * **Result:** Execution stops at the third branch.
  * **Output:** `band = "Strong"`

* **Test 4: Score 94**
  * **Evaluation:** `94 < 40` (False) ➔ `94 < 70` (False) ➔ `94 < 90` (False). 
  * **Result:** Because all `if` and `elif` conditions failed, the logic automatically falls through to the final `else` catch-all branch.
  * **Output:** `band = "Excellent"`
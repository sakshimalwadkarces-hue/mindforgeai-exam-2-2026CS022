### **Q3. Variables, Memory and Identity (5 Marks)**

**Part 1: Integer Memory & Identity (`a`, `b`, `c`)**
* **`a = 25`**: Python creates an integer object `25` in memory and creates a reference label `a` pointing to it.
* **`b = a`**: Python does not create a new object. It points the reference `b` to the **exact same memory address** as `a`.
* **`c = 25`**: Python optimizes memory by caching small integers (-5 to 256). It recognizes `25` already exists and points `c` to the existing object.
* **Expected Relationship:** The variables `a`, `b`, and `c` share the **exact same object identity**. (In code: `a is b` and `a is c` are both `True`).

**Part 2: List Memory & Mutability (`names`, `same_names`)**
* **`names = ["Asha", "Riya"]`**: Python creates a list object in memory and points the reference `names` to it.
* **`same_names = names`**: Python **does not copy the list**. It creates a new reference label `same_names` and points it to the **exact same list object** in memory.
* **`same_names.append("Neha")`**: Because lists are mutable, this command modifies the underlying list object in-place. 
* **Expected Relationship:** `names` and `same_names` share the same object identity (`names is same_names` is `True`). Because they point to the exact same object, printing `names` will also output the mutated list: `["Asha", "Riya", "Neha"]`.
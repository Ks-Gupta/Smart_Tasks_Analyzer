
---

# 🧠 Smart Task Analyzer

An intelligent task-ranking system that computes priority scores using a hybrid urgency-based, importance-weighted, effort-adjusted algorithm with dependency awareness.
Backend powered by Django + DRF, with a lightweight HTML/JS frontend.

---

## 📌 1. Setup Instructions

### **Clone the repository**

```bash
git clone https://github.com/Ks-Gupta/Smart_Tasks_Analyzer.git
cd Smart_Tasks_Analyzer/task-analyzer/backend
```

### **Create virtual environment**

```bash
python3 -m venv env
source env/bin/activate     # Mac/Linux
env\Scripts\activate        # Windows
```

### **Install dependencies**

```bash
pip install -r requirements.txt
```

### **Run migrations**

```bash
python manage.py migrate
```

### **Start server**

```bash
python manage.py runserver
```

Backend is now live at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Open frontend:
👉 `task-analyzer/frontend/index.html`

---

## 📌 2. Algorithm Explanation (≈ 350–450 words)

The Smart Task Analyzer uses a **multi-factor hybrid scoring algorithm** designed to estimate the practical priority of a task by combining urgency, importance, effort, and dependency impact. The goal is to move beyond simple to-do list prioritization and capture the *real* factors that influence productive decision-making.

### **1. Urgency Calculation**

Urgency is determined using the number of days remaining until the task's due date.

* If no due date exists, urgency defaults to `0`.
* If the task is overdue, urgency is set to a maximum value of `10`.
* Otherwise:

  ```
  urgency = max(0, 10 - days_left/2)
  ```

This creates a smooth, declining urgency curve rather than a binary high/low classification.

### **2. Importance Weight**

Importance is a user-defined integer that usually ranges between 1–5.
It reflects how critical the task is independent of deadline pressure.

In the final score, importance contributes **40%** of the total weight, equal to urgency.
This ensures that a high-impact task without a close deadline still ranks well.

### **3. Effort Score (Quick-Win Boost)**

Effort is measured in estimated hours.
The system rewards “quick wins” using the formula:

```
effort_score = 10 / (effort + 1)
```

The lower the effort, the higher the score contribution.
This encourages completing small tasks early, preventing backlog buildup.

### **4. Dependency Boost**

Tasks depending on other tasks gain a small boost:

```
dependency_boost = 2 * number_of_dependencies
```

This helps surface “bottleneck tasks” in workflows that might block progress elsewhere.

### **5. Final Score Formula**

Each factor is weighted:

```
final_score =
    (urgency * 0.4) +
    (importance * 0.4) +
    (effort_score * 0.1) +
    (dependency_boost * 0.1)
```

### **6. Circular Dependency Detection**

Before scoring, the algorithm runs a DFS-based cycle detector.
Any circular dependency raises an error and prevents invalid ranking.

This ensures consistency and correctness in complex project structures.

---

## 📌 3. Design Decisions (Trade-offs)

* **Chose weighted scoring instead of ML**
  → Offers full determinism and fewer dependencies.
* **Effort scored inversely** to highlight easy wins
  → Simple and intuitive, though not precise for large projects.
* **Limited dependency influence to 10%**
  → Prevents dependency-heavy tasks from dominating the list.
* **Used SQLite**
  → Lightweight and ideal for local evaluation.
* **Simple frontend**
  → Kept focus on backend logic and scoring accuracy.

---

## 📌 4. Time Breakdown

| Task                         | Time Spent |
| ---------------------------- | ---------- |
| Research & algorithm design  | 3 hours    |
| Django backend setup         | 2 hours    |
| API & scoring implementation | 3 hours    |
| Frontend (HTML/CSS/JS)       | 2 hours    |
| Unit tests                   | 1 hour     |
| README + cleanup             | 1 hour     |

Total ≈ **12 hours**

---

## 📌 5. Bonus Challenges Attempted

* ✔ Implemented cycle detection using DFS
* ✔ Added full scoring explanations for UX transparency
* ✔ Included dependency-aware weighting
* ❌ No ML-based predictive scoring
* ❌ No UI visual charts (due to time constraints)

---

## 📌 6. Future Improvements

* Add ML-based learning from past completions
* Replace frontend with React or Next.js
* Add Gantt-chart visualization
* Enable multi-user login
* Add task clustering / similarity analysis
* Migrate to PostgreSQL for larger datasets

---

## 📌 7. Unit Tests (Included)

At least 3 tests covering:

1. **Urgency scoring**
2. **Effort scoring**
3. **Dependency cycle detection**

Located in:
`task-analyzer/backend/tasks/tests.py`

---

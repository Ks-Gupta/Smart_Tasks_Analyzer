from datetime import date

class TaskPriorityScorer:
    def __init__(self, tasks):
        self.tasks = tasks
        self.graph = {t["title"]: t["dependencies"] for t in tasks}

    # --- detect circular dependencies ---
    def has_cycle(self):
        visited = set()
        rec_stack = set()

        def dfs(node):
            if node not in self.graph:
                return False
            
            visited.add(node)
            rec_stack.add(node)

            for dep in self.graph[node]:
               if dep in self.graph:
                    if dep not in visited:
                        if dfs(dep): return True
                    elif dep in rec_stack:
                        return True
            rec_stack.remove(node)
            return False

        return any(dfs(node) for node in self.graph)

    # --- main scoring ---
    def compute_score(self, task):
        today = date.today()

        # urgency
        if not task.get("due_date"):
            urgency = 0
        else:
            due_date = date.fromisoformat(task["due_date"])
            days_left = (due_date - today).days
            if days_left < 0:
                urgency = 10  # overdue
            else:
                urgency = max(0, 10 - days_left / 2)

        importance = task.get("importance", 1)
        effort = task.get("estimated_hours", 1)

        effort_score = 10 / (effort + 1)  # quick wins

        dep_count = len(task.get("dependencies", []))
        dependency_boost = dep_count * 2

        final_score = (
            urgency * 0.4 +
            importance * 0.4 +
            effort_score * 0.1 +
            dependency_boost * 0.1
        )

        explanation = (
            f"Urgency={urgency:.1f}, "
            f"Importance={importance}, "
            f"Effort Score={effort_score:.1f}, "
            f"Dependencies={dep_count}"
        )
        return final_score, explanation

    def analyze(self):
        if self.has_cycle():
            raise ValueError("Circular dependencies detected")
        
        output = []
        for t in self.tasks:
            score, explanation = self.compute_score(t)
            t["score"] = round(score, 2)
            t["explanation"] = explanation
            output.append(t)

        return sorted(output, key=lambda x: x["score"], reverse=True)

from django.test import TestCase
from .scoring import TaskPriorityScorer

class TestScoring(TestCase):

    def test_overdue_task_high_urgency(self):
        tasks = [{
            "title": "A",
            "due_date": "2020-01-01",
            "estimated_hours": 2,
            "importance": 5,
            "dependencies": []
        }]
        scorer = TaskPriorityScorer(tasks)
        result = scorer.analyze()
        self.assertTrue(result[0]["score"] > 5)

    def test_circular_dependency(self):
        tasks = [
            {"title": "A", "due_date": "2025-01-01", "estimated_hours": 2,
             "importance": 5, "dependencies": ["B"]},
            {"title": "B", "due_date": "2025-01-01", "estimated_hours": 2,
             "importance": 5, "dependencies": ["A"]},
        ]
        with self.assertRaises(ValueError):
            TaskPriorityScorer(tasks).analyze()

    def test_sorting(self):
        tasks = [
            {"title": "Important", "due_date": "2025-12-01",
             "estimated_hours": 1, "importance": 10, "dependencies": []},
            {"title": "Low", "due_date": "2026-12-01",
             "estimated_hours": 10, "importance": 1, "dependencies": []}
        ]
        scorer = TaskPriorityScorer(tasks)
        result = scorer.analyze()
        self.assertEqual(result[0]["title"], "Important")

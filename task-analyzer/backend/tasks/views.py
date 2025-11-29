from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .scoring import TaskPriorityScorer
import json


class AnalyzeTasks(APIView):
    def post(self, request):
        tasks = request.data.get("tasks", [])

        # If tasks is a STRING, convert it to JSON
        if isinstance(tasks, str):
            try:
                tasks = json.loads(tasks)
            except:
                return Response({"error": "Invalid JSON format"}, status=400)

        try:
            scorer = TaskPriorityScorer(tasks)
            sorted_tasks = scorer.analyze()
            return Response(sorted_tasks)
        except ValueError as e:
            return Response({"error": str(e)}, status=400)


class SuggestTasks(APIView):
    def get(self, request):
        tasks_raw = request.GET.get("tasks", None)

        if not tasks_raw:
            return Response(
                {"error": "Provide tasks as ?tasks=[...] in URL"},
                status=400
            )

        try:
            tasks = json.loads(tasks_raw)
        except:
            return Response({"error": "Invalid tasks JSON"}, status=400)

        # If tasks is a STRING (double wrapped)
        if isinstance(tasks, str):
            tasks = json.loads(tasks)

        scorer = TaskPriorityScorer(tasks)
        sorted_tasks = scorer.analyze()

        return Response(sorted_tasks[:3])

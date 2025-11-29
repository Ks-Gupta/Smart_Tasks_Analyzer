const API_URL = "http://127.0.0.1:8001/api/tasks/analyze/";

// Handle “Analyze Tasks” button click
async function analyzeTasks() {
    const raw = document.getElementById("taskJson").value;
    const strategy = document.getElementById("strategy").value;

    let tasks;

    // Parse JSON safely
    try {
        tasks = JSON.parse(raw);
    } catch (err) {
        alert("❌ Invalid JSON format");
        return;
    }

    console.log("Sending to backend:", { tasks, strategy });

    // Call backend API
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tasks, strategy })
    }).catch(err => {
        console.error("Network error:", err);
        alert("❌ Cannot reach backend server!");
    });

    if (!response) return;

    console.log("Backend status:", response.status);

    // If backend responds with an error (400, 500)
    if (!response.ok) {
        const err = await response.text();
        console.error("Backend error:", err);
        alert("❌ Backend Error:\n" + err);
        return;
    }

    // Receive JSON response
    const result = await response.json();
    console.log("Backend data:", result);

    // Render results visually
    render(result);
}

// Render sorted tasks
function render(tasks) {
    const container = document.getElementById("output");
    container.innerHTML = "";

    tasks.forEach((t, index) => {
    let priority = "";
    if (t.score > 7) priority = "high";
    else if (t.score > 4) priority = "medium";
    else priority = "low";

    const badgeText =
        priority === "high" ? "High Priority" :
        priority === "medium" ? "Medium Priority" :
        "Low Priority";

    const progressWidth = (t.score / 10) * 100;

    // NEW: delay each card by 0.05s * index
    const delay = (index * 0.05).toFixed(2) + "s";

    container.innerHTML += `
        <div class="task ${priority}" style="--delay: ${delay};">
            <div class="task-header">
                <b>${t.title}</b>
                <span class="badge ${priority}">${badgeText}</span>
            </div>

            <div class="progress-bar">
                <div class="progress-fill ${priority}" style="width: ${progressWidth}%"></div>
            </div>

            <small><b>Score:</b> ${t.score}</small>
            <small>${t.explanation}</small>
        </div>
    `;
});

}


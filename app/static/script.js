const apiBaseUrl = 'http://localhost:5000/api';

async function loadFunctionality(action) {
    const contentDiv = document.getElementById("content");
    contentDiv.innerHTML = "";

    if (action === "viewAircraft") {
        const response = await fetch(`${apiBaseUrl}/aircraft`);
        const aircrafts = await response.json();
        
        const table = document.createElement("table");
        const headerRow = table.insertRow();
        ["AircraftNo", "Model", "Capacity"].forEach(heading => {
            const th = document.createElement("th");
            th.textContent = heading;
            headerRow.appendChild(th);
        });

        aircrafts.forEach(aircraft => {
            const row = table.insertRow();
            row.insertCell().textContent = aircraft.AircraftNo;
            row.insertCell().textContent = aircraft.Model;
            row.insertCell().textContent = aircraft.Capacity;
        });

        contentDiv.appendChild(table);

    } else if (action === "addAircraft") {
        const formHtml = `
            <h2>Add New Aircraft</h2>
            <form onsubmit="submitAircraftForm(event)">
                <label>Aircraft No:</label>
                <input type="text" name="AircraftNo" required><br><br>
                <label>Model:</label>
                <input type="text" name="Model" required><br><br>
                <label>Capacity:</label>
                <input type="number" name="Capacity" required><br><br>
                <button type="submit">Add Aircraft</button>
            </form>
        `;
        contentDiv.innerHTML = formHtml;
    }
}

async function submitAircraftForm(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);

    const response = await fetch(`${apiBaseUrl}/aircraft`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    if (response.ok) {
        alert("Aircraft added successfully!");
        loadFunctionality("viewAircraft");
    } else {
        alert("Failed to add aircraft.");
    }
}

async function searchFlight(event) {
    event.preventDefault();

    const source = document.getElementById('source').value;
    const destination = document.getElementById('destination').value;

    try {
        const response = await fetch(`/api/flights/search?source=${source}&destination=${destination}`);
        const results = await response.json();

        const resultsContainer = document.getElementById('search-results');
        resultsContainer.innerHTML = `<h2>Search Results:</h2>`;

        if (results.length === 0) {
            resultsContainer.innerHTML += `<p>No flights found from ${source} to ${destination}.</p>`;
        } else {
            const table = document.createElement('table');
            table.innerHTML = `
                <tr>
                    <th>Flight No</th>
                    <th>Flight Name</th>
                    <th>Source</th>
                    <th>Destination</th>
                    <th>Departure Time</th>
                    <th>Arrival Time</th>
                </tr>`;
            results.forEach(flight => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${flight.FlightNo}</td>
                    <td>${flight.FlightName}</td>
                    <td>${flight.Source}</td>
                    <td>${flight.Destination}</td>
                    <td>${new Date(flight.DeptTime).toLocaleString()}</td>
                    <td>${new Date(flight.ArrTime).toLocaleString()}</td>
                `;
                table.appendChild(row);
            });
            resultsContainer.appendChild(table);
        }
    } catch (error) {
        console.error('Error fetching flights:', error);
        alert('Failed to search for flights. Please try again.');
    }
}

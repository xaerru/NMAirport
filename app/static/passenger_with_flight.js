window.onload = async function() {
    try {
        const response = await fetch('/api/passengers_with_flights');
        const passengers = await response.json();

        if (passengers.length === 0) {
            document.getElementById('passengerList').innerHTML = 'No passengers found.';
            return;
        }

        let tableHTML = `
            <table border="1">
                <tr>
                    <th>Seat No</th>
                    <th>Passenger Name</th>
                    <th>Class</th>
                    <th>Flight Number</th>
                    <th>Flight Name</th>
                    <th>Source</th>
                    <th>Destination</th>
                    <th>Departure Time</th>
                    <th>Arrival Time</th>
                    <th>Duration</th>
                </tr>`;

        passengers.forEach(passenger => {
            tableHTML += `
            <tr>
                <td>${passenger.SeatNo}</td>
                <td>${passenger.PName}</td>
                <td>${passenger.Class}</td>
                <td>${passenger.FlightNo}</td>
                <td>${passenger.FlightName}</td>
                <td>${passenger.Source}</td>
                <td>${passenger.Destination}</td>
                <td>${new Date(passenger.DeptTime).toLocaleString()}</td>
                <td>${new Date(passenger.ArrTime).toLocaleString()}</td>
                <td>${passenger.Duration} mins</td>
            </tr>`;
        });

        tableHTML += `</table>`;

        document.getElementById('passengerList').innerHTML = tableHTML;
    } catch (error) {
        console.error('Error fetching passengers:', error);
        alert('Failed to load passengers. Please try again.');
    }
};

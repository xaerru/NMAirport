async function addPassenger(event) {
    event.preventDefault();

    const pname = document.getElementById('pname').value;
    const seatno = document.getElementById('seatno').value;
    const classType = document.getElementById('class').value;
    const flightno = document.getElementById('flightno').value;

    const passengerData = {
        PName: pname,
        SeatNo: seatno,
        Class: classType
    };

    const boardData = {
        SeatNo: seatno,
        FlightNo: flightno
    };

    try {
        const passengerResponse = await fetch(`/api/into/Passenger`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(passengerData)
        });

        const passenger = await passengerResponse.json();

        const boardResponse = await fetch(`/api/into/Boards`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(boardData)
        });

        const board = await boardResponse.json();

        alert('Passenger added successfully!');
        window.location.href = '/add_passenger';
    } catch (error) {
        console.error('Error adding passenger:', error);
        alert('Failed to add passenger. Please try again.');
    }
}

window.onload = async function() {
    try {
        const response = await fetch('/api/all/flight');
        const data = await response.json();

        if (data && data.data && Array.isArray(data.data)) {
            const flights = data.data;
            const flightSelect = document.getElementById('flightno');

            flightSelect.innerHTML = '<option value="">Select a flight</option>';

            flights.forEach(flight => {
                const option = document.createElement('option');
                option.value = flight.FlightNo;
                option.textContent = `${flight.FlightNo} - ${flight.FlightName} (${flight.Source} to ${flight.Destination})`;
                flightSelect.appendChild(option);
            });
        } else {
            console.error('Invalid data structure', data);
            alert('Failed to load flight options. Please try again.');
        }
    } catch (error) {
        console.error('Error fetching flights:', error);
        alert('Failed to load flights. Please try again.');
    }
};

function loadInsertForm(tableName) {
    const formContainer = document.getElementById('form-container');
    formContainer.innerHTML = '';

    let formHtml = `<form id="insertForm" onsubmit="submitForm(event, '${tableName}')">`;
    formHtml += `<h2>Insert into ${tableName}</h2>`;

    let fields = [];
    if (tableName === 'Aircraft') {
        fields = ['AircraftNo', 'Model', 'Capacity'];
    } else if (tableName === 'Airline') {
        fields = ['AName', 'No_of_Planes'];
    } else if (tableName === 'Passenger') {
        fields = ['SeatNo', 'PName', 'Class'];
    } else if (tableName === 'Flight') {
        fields = ['FlightNo', 'FlightName', 'Source', 'Destination', 'DeptTime', 'ArrTime'];
    } else if (tableName === 'IsOf') {
        fields = ['FlightNo', 'AName'];
    } else if (tableName === 'Boards') {
        fields = ['SeatNo', 'FlightNo'];
    } else if (tableName === 'Owns') {
        fields = ['AircraftNo', 'AName'];
    }

    fields.forEach(field => {
        formHtml += `<label for="${field}">${field}:</label>`;
        formHtml += `<input type="text" id="${field}" name="${field}" required><br>`;
    });
    formHtml += `<button type="submit">Submit</button>`;
    formHtml += `</form>`;

    formContainer.innerHTML = formHtml;
}

async function submitForm(event, tableName) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('insertForm'));
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch(`/api/into/${tableName}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        alert(`Successfully added data to ${tableName}`);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to add data. Please try again.');
    }
}

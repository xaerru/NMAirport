async function loadTable(tableName) {
    const response = await fetch(`/api/all/${tableName}`);
    const result = await response.json();

    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = '';

    if (result.error) {
        contentDiv.innerHTML = `<p>Error: ${result.error}</p>`;
        return;
    }

    const table = document.createElement('table');
    const thead = table.createTHead();
    const headerRow = thead.insertRow();
    result.columns.forEach(column => {
        const th = document.createElement('th');
        th.textContent = column;
        headerRow.appendChild(th);
    });

    const tbody = table.createTBody();
    result.data.forEach(row => {
        const dataRow = tbody.insertRow();
        result.columns.forEach(column => {
            const cell = dataRow.insertCell();
            cell.textContent = row[column];
        });
    });

    contentDiv.appendChild(table);
}

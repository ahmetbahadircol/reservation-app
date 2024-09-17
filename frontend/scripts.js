document.addEventListener("DOMContentLoaded", function() {
    const carButton = document.getElementById('car-button');
    const hotelButton = document.getElementById('hotel-button');
    const listContainer = document.getElementById('list-container');
    const listTitle = document.getElementById('list-title');
    const tableHeader = document.getElementById('table-header');
    const tableBody = document.getElementById('table-body');

    carButton.addEventListener('click', () => fetchData('cars', 'Cars'));
    hotelButton.addEventListener('click', () => fetchData('hotels', 'Hotels'));

    function fetchData(type, title) {
        // Ensure the URL is correctly specified
        fetch(`http://localhost:8000/api/${type}`)
            .then(response => response.json())
            .then(data => {
                displayData(data, title);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                alert('Failed to load data.');
            });
    }

    function displayData(data, title) {
        listTitle.textContent = title;
        listContainer.style.display = 'block';
        tableHeader.innerHTML = ''; // Clear previous header
        tableBody.innerHTML = ''; // Clear previous body

        if (data.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="3">No data available</td></tr>';
            return;
        }

        // Assuming the data objects have the following properties for both Cars and Hotels
        const keys = Object.keys(data[0]);

        // Create table header
        keys.forEach(key => {
            const th = document.createElement('th');
            th.textContent = key.charAt(0).toUpperCase() + key.slice(1);
            tableHeader.appendChild(th);
        });

        // Create table rows
        data.forEach(item => {
            const tr = document.createElement('tr');
            keys.forEach(key => {
                const td = document.createElement('td');
                td.textContent = item[key];
                tr.appendChild(td);
            });
            tableBody.appendChild(tr);
        });
    }
});

const ordersContainer = document.querySelector('.orders-container tbody');

const dummyData = [
    { id: 1, items: 'Butter Chicken, Naan, Salad', status: 'Pending', time: '12:30 PM', amount: '$10.99' },
    { id: 2, items: 'Pizza', status: 'Delivered', time: '1:45 PM', amount: '$15.99' },
    { id: 3, items: 'Salad', status: 'Cancelled', time: '3:15 PM', amount: '$8.99' },
];

dummyData.forEach(order => {
    const row = document.createElement('tr');

    const idCell = document.createElement('td');
    idCell.textContent = order.id;
    row.appendChild(idCell);

    const itemsCell = document.createElement('td');
    itemsCell.textContent = order.items;
    row.appendChild(itemsCell);

    const statusCell = document.createElement('td');
    const statusDropdown = document.createElement('select');
    statusDropdown.addEventListener('change', (event) => {
        const selectedStatus = event.target.value;
        updateStatus(selectedStatus);
    });

    const option1 = document.createElement('option');
    option1.value = 'Preparing';
    option1.textContent = 'Preparing';
    statusDropdown.appendChild(option1);

    const option2 = document.createElement('option');
    option2.value = 'Delivery';
    option2.textContent = 'Delivery';
    statusDropdown.appendChild(option2);

    const option3 = document.createElement('option');
    option3.value = 'Completed';
    option3.textContent = 'Completed';
    statusDropdown.appendChild(option3);

    statusCell.appendChild(statusDropdown);
    row.appendChild(statusCell);

    const timeCell = document.createElement('td');
    timeCell.textContent = order.time;
    row.appendChild(timeCell);

    const amountCell = document.createElement('td');
    amountCell.textContent = order.amount;
    row.appendChild(amountCell);

    ordersContainer.appendChild(row);
});

fetch('/api/orders')
    .then(response => response.json())
    .then(data => {
        data.forEach(order => { 
            const row = document.createElement('tr');

            const idCell = document.createElement('td');
            idCell.textContent = order.id;
            row.appendChild(idCell);

            const itemsCell = document.createElement('td');
            itemsCell.textContent = order.items;
            row.appendChild(itemsCell);

            const statusCell = document.createElement('td');
            statusCell.textContent = order.status;
            row.appendChild(statusCell);

            const timeCell = document.createElement('td');
            timeCell.textContent = order.time;
            row.appendChild(timeCell);

            const amountCell = document.createElement('td');
            amountCell.textContent = order.amount;
            row.appendChild(amountCell);

            ordersContainer.appendChild(row);
        });
    });

function updateStatus(status) {
    fetch('/update-status', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: status })
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

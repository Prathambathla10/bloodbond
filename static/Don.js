// JavaScript code for Manage Donors section

let donorsData = [
    { id: 1, name: 'John Doe', bloodGroup: 'A+', lastDonation: '2023-06-01' },
    { id: 2, name: 'Jane Smith', bloodGroup: 'O-', lastDonation: '2023-05-15' },
    // Add more donor data as needed
];

// Function to display donors in the table
function displayDonors() {
    let tableBody = document.querySelector('#donors-table tbody');
    tableBody.innerHTML = '';

    donorsData.forEach(donor => {
        let row = document.createElement('tr');
        row.innerHTML = `
            <td>${donor.id}</td>
            <td>${donor.name}</td>
            <td>${donor.bloodGroup}</td>
            <td>${donor.lastDonation}</td>
            <td>
                <button onclick="editDonor(${donor.id})">Edit</button>
                <button onclick="deleteDonor(${donor.id})">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// Function to open the add donor form modal
function openAddForm() {
    document.getElementById('addDonorForm').style.display = 'block';
}

// Function to close the add donor form modal
function closeAddForm() {
    document.getElementById('addDonorForm').style.display = 'none';
}

// Function to add a new donor (simulated)
document.getElementById('addDonorForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let newName = document.getElementById('name').value;
    let newBloodGroup = document.getElementById('bloodGroup').value;
    let newLastDonation = document.getElementById('lastDonation').value;

    let newDonor = {
        id: donorsData.length + 1,
        name: newName,
        bloodGroup: newBloodGroup,
        lastDonation: newLastDonation
    };

    donorsData.push(newDonor);
    displayDonors();
    closeAddForm();
});

// Function to edit a donor (simulated)
function editDonor(id) {
    let newName = prompt('Enter new name:');
    let newBloodGroup = prompt('Enter new blood group:');
    let newLastDonation = prompt('Enter new last donation date (YYYY-MM-DD):');

    let donorIndex = donorsData.findIndex(donor => donor.id === id);
    if (donorIndex !== -1) {
        donorsData[donorIndex].name = newName;
        donorsData[donorIndex].bloodGroup = newBloodGroup;
        donorsData[donorIndex].lastDonation = newLastDonation;
        displayDonors();
    }
}

// Function to delete a donor (simulated)
function deleteDonor(id) {
    let confirmDelete = confirm('Are you sure you want to delete this donor?');
    if (confirmDelete) {
        donorsData = donorsData.filter(donor => donor.id !== id);
        displayDonors();
    }
}

// Initial display of donors when page loads
document.addEventListener('DOMContentLoaded', function() {
    displayDonors();
});
// Example JavaScript code for admin functionalities

// Sample data (replace with actual data handling as per your backend)
let donorsData = [
    { id: 1, name: 'John Doe', bloodGroup: 'A+', lastDonation: '2023-06-01' },
    { id: 2, name: 'Jane Smith', bloodGroup: 'O-', lastDonation: '2023-05-15' },
    // Add more donor data as needed
];

// Example function to display donors on admin page
function displayDonors() {
    let donorsTable = document.getElementById('donors-table');

    // Clear existing table rows
    donorsTable.innerHTML = '';

    // Loop through donorsData and populate table rows
    donorsData.forEach(donor => {
        let row = document.createElement('tr');
        row.innerHTML = `
            <td>${donor.id}</td>
            <td>${donor.name}</td>
            <td>${donor.bloodGroup}</td>
            <td>${donor.lastDonation}</td>
            <td><button onclick="editDonor(${donor.id})">Edit</button></td>
            <td><button onclick="deleteDonor(${donor.id})">Delete</button></td>
        `;
        donorsTable.appendChild(row);
    });
}

// Example function to add a new donor (simulated)
function addNewDonor() {
    let newName = prompt('Enter donor name:');
    let newBloodGroup = prompt('Enter blood group:');
    let newLastDonation = prompt('Enter last donation date (YYYY-MM-DD):');

    let newDonor = {
        id: donorsData.length + 1,
        name: newName,
        bloodGroup: newBloodGroup,
        lastDonation: newLastDonation
    };

    donorsData.push(newDonor);
    displayDonors();
}

// Example function to edit a donor (simulated)
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

// Example function to delete a donor (simulated)
function deleteDonor(id) {
    let confirmDelete = confirm('Are you sure you want to delete this donor?');
    if (confirmDelete) {
        donorsData = donorsData.filter(donor => donor.id !== id);
        displayDonors();
    }
}

// Example usage: Display donors on page load
document.addEventListener('DOMContentLoaded', function() {
    displayDonors();
});

// JavaScript code for Manage Events section

let eventsData = [
    { id: 1, title: 'Blood Donation Camp', date: '2024-07-10', time: '09:00', venue: 'City Hall' },
    { id: 2, title: 'Blood Donation Drive', date: '2024-07-20', time: '10:00', venue: 'Community Center' },
    // Add more event data as needed
];

// Function to display events in the table
function displayEvents() {
    let tableBody = document.querySelector('#events-table tbody');
    tableBody.innerHTML = '';

    eventsData.forEach(event => {
        let row = document.createElement('tr');
        row.innerHTML = `
            <td>${event.id}</td>
            <td>${event.title}</td>
            <td>${event.date}</td>
            <td>${event.time}</td>
            <td>${event.venue}</td>
            <td>
                <button onclick="editEvent(${event.id})">Edit</button>
                <button onclick="deleteEvent(${event.id})">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// Function to open the add event form modal
function openAddForm() {
    document.getElementById('addEventForm').style.display = 'block';
}

// Function to close the add event form modal
function closeAddForm() {
    document.getElementById('addEventForm').style.display = 'none';
}

// Function to add a new event (simulated)
document.getElementById('addEventForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let newTitle = document.getElementById('title').value;
    let newDate = document.getElementById('date').value;
    let newTime = document.getElementById('time').value;
    let newVenue = document.getElementById('venue').value;

    let newEvent = {
        id: eventsData.length + 1,
        title: newTitle,
        date: newDate,
        time: newTime,
        venue: newVenue
    };

    eventsData.push(newEvent);
    displayEvents();
    closeAddForm();
});

// Function to edit an event (simulated)
function editEvent(id) {
    let newTitle = prompt('Enter new title:');
    let newDate = prompt('Enter new date (YYYY-MM-DD):');
    let newTime = prompt('Enter new time:');
    let newVenue = prompt('Enter new venue:');

    let eventIndex = eventsData.findIndex(event => event.id === id);
    if (eventIndex !== -1) {
        eventsData[eventIndex].title = newTitle;
        eventsData[eventIndex].date = newDate;
        eventsData[eventIndex].time = newTime;
        eventsData[eventIndex].venue = newVenue;
        displayEvents();
    }
}

// Function to delete an event (simulated)
function deleteEvent(id) {
    let confirmDelete = confirm('Are you sure you want to delete this event?');
    if (confirmDelete) {
        eventsData = eventsData.filter(event => event.id !== id);
        displayEvents();
    }
}

// Initial display of events when page loads
document.addEventListener('DOMContentLoaded', function() {
    displayEvents();
});
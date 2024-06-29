// JavaScript code for Manage Rewards section

let rewardsData = [
    { id: 1, name: 'Blood Donation Certificate', description: 'Certificate for donating blood.', points: 50 },
    { id: 2, name: 'T-shirt', description: 'Blood donation themed T-shirt.', points: 100 },
    // Add more reward data as needed
];

// Function to display rewards in the table
function displayRewards() {
    let tableBody = document.querySelector('#rewards-table tbody');
    tableBody.innerHTML = '';

    rewardsData.forEach(reward => {
        let row = document.createElement('tr');
        row.innerHTML = `
            <td>${reward.id}</td>
            <td>${reward.name}</td>
            <td>${reward.description}</td>
            <td>${reward.points}</td>
            <td>
                <button onclick="editReward(${reward.id})">Edit</button>
                <button onclick="deleteReward(${reward.id})">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// Function to open the add reward form modal
function openAddForm() {
    document.getElementById('addRewardForm').style.display = 'block';
}

// Function to close the add reward form modal
function closeAddForm() {
    document.getElementById('addRewardForm').style.display = 'none';
}

// Function to add a new reward (simulated)
document.getElementById('addRewardForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let newName = document.getElementById('name').value;
    let newDescription = document.getElementById('description').value;
    let newPoints = parseInt(document.getElementById('points').value);

    let newReward = {
        id: rewardsData.length + 1,
        name: newName,
        description: newDescription,
        points: newPoints
    };

    rewardsData.push(newReward);
    displayRewards();
    closeAddForm();
});

// Function to edit a reward (simulated)
function editReward(id) {
    let newName = prompt('Enter new name:');
    let newDescription = prompt('Enter new description:');
    let newPoints = parseInt(prompt('Enter new points:'), 10);

    let rewardIndex = rewardsData.findIndex(reward => reward.id === id);
    if (rewardIndex !== -1) {
        rewardsData[rewardIndex].name = newName;
        rewardsData[rewardIndex].description = newDescription;
        rewardsData[rewardIndex].points = newPoints;
        displayRewards();
    }
}

// Function to delete a reward (simulated)
function deleteReward(id) {
    let confirmDelete = confirm('Are you sure you want to delete this reward?');
    if (confirmDelete) {
        rewardsData = rewardsData.filter(reward => reward.id !== id);
        displayRewards();
    }
}

// Initial display of rewards when page loads
document.addEventListener('DOMContentLoaded', function() {
    displayRewards();
});
document.addEventListener('DOMContentLoaded', () => {
    const fields = [
        'totalDonor',
        'newDonor',
        'activeDonor',
        'currentInventory',
        'unitsCollected',
        'unitsIssued',
        'criticalStock',
        'eventsOrganised',
        'participationRate',
        'bloodPerEvent',
        'rewardsDistributed',
        'pointsRedeemed'
    ];

    fields.forEach(field => {
        const input = document.getElementById(field);
        const valueSpan = document.getElementById(`${field}Value`);
        const editButton = document.getElementById(`edit${capitalize(field)}Button`);
        const resetButton = document.getElementById(`reset${capitalize(field)}Button`);
        const submitButton = document.getElementById(`submit${capitalize(field)}Button`);

        editButton.addEventListener('click', () => {
            input.disabled = false;
            submitButton.disabled = false;
            input.focus();
        });

        resetButton.addEventListener('click', () => {
            input.value = '';
            input.disabled = true;
            submitButton.disabled = true;
        });

        submitButton.addEventListener('click', () => {
            valueSpan.textContent = input.value;
            input.disabled = true;
            submitButton.disabled = true;
        });
    });

    function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }
});

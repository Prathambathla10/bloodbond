  let currentIndex = 0;
const cards = document.querySelectorAll('.card');
const colors = ['#ff9999', '#99ccff', '#99ff99', '#ffcc99', '#cc99ff', '#ffff99', '#99ffff', '#ff99ff', '#ccccff', '#ffccff'];
 

function showNextCard() {
    cards[currentIndex].classList.remove('show');
    cards[currentIndex].classList.add('hidden');
    
    let nextIndex;
    do {
        nextIndex = Math.floor(Math.random() * cards.length);
    } while (nextIndex === currentIndex);

    currentIndex = nextIndex;
    cards[currentIndex].classList.remove('hidden');
    cards[currentIndex].classList.add('show');
    
    
    cards[currentIndex].style.backgroundColor = colors[currentIndex];
}

setInterval(showNextCard, 3000);


cards[currentIndex].classList.add('show');
cards[currentIndex].style.backgroundColor = colors[currentIndex];

document.addEventListener("DOMContentLoaded", function() {
    function animateCounter(counterId, targetCount, speed) {
        var counterElement = document.getElementById(counterId);
        var count = 0;

        function updateCounter() {
            counterElement.textContent = count;
            count++;
            if (count <= targetCount) {
                setTimeout(updateCounter, speed);
            }
        }

        updateCounter();
    }

    // First counter (                         counts to 500)
    animateCounter("counter1", 12000, 0.0002);

    // Second counter (assuming it counts to 1000)
    animateCounter("counter", 1000, 0.0002);

    // Third counter (counts to 300)
    animateCounter("counter3", 4, 2);

    var popupContainer = document.getElementById("popupContainer");

    // Show the popups when the page loads
    popupContainer.classList.add("show");

    // Function to close the popup
    window.closePopup = function(popupId) {
        var popup = document.getElementById(popupId);
        popup.style.display = "none";
        
        // Check if both popups are closed
        var popup1 = document.getElementById("popup1");
        var popup2 = document.getElementById("popup2");
        if (popup1.style.display === "none" && popup2.style.display === "none") {
            popupContainer.classList.remove("show");``
        }
    }

    // Close the popup when clicking outside of it
    window.onclick = function(event) {
        if (event.target == popupContainer) {
            popupContainer.classList.remove("show");
        }
    }
    
    
});

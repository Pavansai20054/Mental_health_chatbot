// script.js

// Toggle the dropdown visibility when clicking on the "Chat" link
function toggleDropdown(event, dropdownId) {
    event.preventDefault();
    let dropdown = document.getElementById(dropdownId);
    dropdown.classList.toggle('active');
}

// Close dropdown when clicking outside the dropdown or button
document.addEventListener('click', function(event) {
    let dropdown = document.getElementById('chatDropdown');
    let chatMenu = document.getElementById('chatMenu');
    let getStartedButton = document.getElementById('getStartedButton');

    if (!chatMenu.contains(event.target) && event.target !== getStartedButton) {
        dropdown.classList.remove('active');
    }
});

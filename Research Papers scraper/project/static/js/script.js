// Handle form submission
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.search-form');
    const keywordInput = document.getElementById('keyword');

    form.addEventListener('submit', function(e) {
        if (!keywordInput.value.trim()) {
            e.preventDefault();
            alert('Please enter a keyword to search');
        }
    });
});
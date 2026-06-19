function switchTab(event, tabId) {
    // Hide all tab content components
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => content.classList.remove('active'));

    // Remove active styles from all buttons
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));

    // Show the targeted tab panel content and flag button as active
    document.getElementById(tabId).classList.add('active');
    event.currentTarget.classList.add('active');
}
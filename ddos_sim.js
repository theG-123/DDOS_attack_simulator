var myConfetti = confetti.create(null, {
    resize: true,
    useWorker: true
});

function confetti_click() {
    myConfetti({ particleCount: 100, spread: 160 })
}

function showAlert() {
    alert("Why did you click me :(");  // This will display an alert with the number 1
}
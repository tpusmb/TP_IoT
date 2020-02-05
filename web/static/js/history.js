const max_history = 10;
let history = [];

function saveToHistory() {
    let elementDom = document.getElementById("message");
    let historyDom = document.getElementById("history");

    let message = elementDom.value;
    history.push(message);
    if (history.length > max_history) {
        history.pop()
    }

    historyDom.value = history.join('\n');
}
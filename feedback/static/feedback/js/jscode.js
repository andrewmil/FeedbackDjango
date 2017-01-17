function remainingChars() {
    var text = document.getElementById("id_textFeedback").value;
    var chars = text.length;
    document.getElementById("chars").innerHTML = 'Characters remaining: ' + (1200 - chars);
}

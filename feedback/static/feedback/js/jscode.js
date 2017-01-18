function remainingChars() {
    var text = document.getElementById("id_textFeedback").value;
    var chars = text.length;
    if(chars < 1200){
      document.getElementById("chars").innerHTML = 'Characters remaining: ' + (1200 - chars);
    }
    else {
      document.getElementById("chars").innerHTML = 'Character limit reached!';
      document.getElementById("chars").style.color = 'red';
    }
}

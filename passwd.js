function onLoad() {
  var doc = document.getElementById('pdfholder');
  doc.style.display = 'none'
}

function showClue() {
  var x = document.getElementById('pdfholder');
  var passwd = document.getElementById('msg_form').value;
  if (passwd === '123456') {
    x.style.display = 'block';
  } else {
    x.style.display = 'none';
    alert("Incorrect password! Try again.")
  }
}

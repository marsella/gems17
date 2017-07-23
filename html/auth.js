function hash() {
    document.getElementById("hash").innerHTML = 
         hashcode(document.getElementById("msg_form").value);
}

// NOT A SECURE HASH FUNCTION 
// DO NOT USE
function hashcode(str){
    var hash = 0;
    if (str.length == 0) return hash;
    for (i = 0; i < str.length; i++) {
        char = str.charCodeAt(i);
        hash = ((hash<<5)-hash)+char;
        hash = hash & hash; // Convert to 32bit integer
    }
    hash = hash>>>0;
    return hash.toString(16);
}

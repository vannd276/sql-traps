/*!
* Start Bootstrap - Coming Soon v6.0.6 (https://startbootstrap.com/theme/coming-soon)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-coming-soon/blob/master/LICENSE)
*/
function readfile(file){
    var xmlHttp = new XMLHttpRequest();
    var url = "/file?file=" + file;
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}


function openFlag(secret){
    if(secret != null && secret == base64decode("RmxhZyBFbnRyeQ==")){
        console.log(atob("RmxhZ3tOM3ZlUl9HMXYzcl9VcH0="))
    }
}

function base64decode(str){
    return atob(str);
}

























































































// static/fl4gs.txt
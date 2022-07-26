function displayTime(){
    const date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    let session = "a.m.";
    if(hh > 12){
        hh = hh - 12;
        session = "p.m.";
    }

    if(hh < 10){
        hh = "0" + hh;
    }
    
    if(mm < 10){
        mm = "0" + mm;
    }
    
    if(ss < 10){
        ss = "0" + ss;
    }
    
    let t = hh + ":" + mm + ":" + ss + " " + session;

    document.getElementById('clock').innerHTML = t;
}
setInterval(displayTime, 1000);

function enableButton(){
    const date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    let t = hh + ":" + mm + ":" + ss;

    var btn = document.getElementById('examBtn');
    var st = document.getElementById('startTime');
    var et = document.getElementById('endTime');
    if(st >= t){
        btn.removeAttribute('disabled');   
    }
}
setInterval(enableButton, 1000);
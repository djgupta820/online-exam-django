const d = new Date()

function getMonthName(month){
    var mnth = "";
    switch(month){
        case 1: mnth = "January";
                break;
        case 2: mnth = "February";
                break;
        case 3: mnth = "March";
                break;
        case 4: mnth = "April";
                break;
        case 5: mnth = "May";
                break;
        case 6: mnth = "June";
                break;
        case 7: mnth = "July";
                break;
        case 8: mnth = "August";
                break;
        case 9: mnth = "September";
                break;
        case 10 : mnth = "October";
                break;
        case 11: mnth = "November";
                break;
        case 12: mnth = "December";
                break;
        default: mnth = "Not Acceptable!"
    }
    return mnth;
}
//document.getElementById("tdate").innerHTML = getMonthName(d.getMonth()) + " " +d.getDay() + " " + ", " + d.getFullYear();

function alert_it(){
    alert("BTTS, DBTI Online Examination Portal Welcomes You");
}

function displayDate(){
    var ele = document.getElementById('tdate').innerHTML;
    console.log(ele)
    /*const d = new Date();
    var day = d.getDay();
    var m = d.getMonth();
    var y = d.getFullYear();
    ele.innerHTML = day +"-" + m + "-" + y;
    console.log(day +"-" + m + "-" + y)*/
}


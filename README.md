# github-raw-content-service
github-raw-content-service

Voorbeeld call: 
http://localhost:8080/<repo>?filepath=grafana/helm-config.yaml

## Aanmaken Python virtual omgeving
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
````

## Packages installeren
```
$ pip install <name-of-package>
$ pip freeze > requirements.txt
```

## Start application local
Zorg ervoor dat token als enviroment variable is gezet
personalaccesstoken github:
export TOKEN= 
```
$ python app.py
```
Vervolgens naar localhost:8080 kan je testen
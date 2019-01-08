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

## kubernetes cluster uitrol
Om de service te laten draaien in het k8s cluster moet je eerst een secret aanmaken
een voorbeeld hiervan is opgenomen in de etc folder van dit project.
Het token is een personal access token wat is aangemaakt onder de github user new-business-argocd-peter-bos
Deze user heeft nu alleen read only rechten op de k8s-test-cluster-config project.

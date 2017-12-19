HarborBiometrics
================
HarborBiometrics leverages open source biometric recognition (OpenBR) to conduct 1:1 face match verification, 1:N face match identification, and age and gender estimation for EthVentures' Harbor project. It's built on top of the [DockerOpenBR](https://github.com/EthVentures/DockerOpenBR), and implements a simple Flask application to handle verification, identification, and estimation requests.

## Build Image
Add your own name and tag:
```
docker build -t [name]:[tag] .
```
## Run Container
Set ```--restart on-failure``` so container recovers from fatal errors in OpenBR:
```
docker run -d -p 5000:5000 --restart on-failure [IMAGE_ID]
```

## Import Modules (Python Example)
```
from base64 import b64encode
from json import loads,dumps
from urllib2 import Request, urlopen
```

## 1:1 Face Match Verification
```
## Query API (wrap in try-catch)
try:
    ## Grab a couple images
    ## Avail. in DockerOpenBR/images or use own
    query = open('bush1.jpeg').read()
    target = open('bush2.jpeg').read()

    ## base64 encode images
    data = {'query':b64encode(query),'target':b64encode(target)}

    ## Set request
    req = Request('http://localhost:5000/api/v1.0/verification')
    req.add_header('Content-Type', 'application/json')

    ## Post and parse response
    resp = urlopen(req, dumps(data))
    content = resp.read()
    print loads(content)

except Exception as e:
    ## Print exceptions
    print e
```

## 1:N Face Match Identification
```
## Query API (wrap in try-catch)
try:
    ## Grab an image of Bush from
    ## your preferred search engine.  
    query = open('bush3.jpg').read()

    data = {'query':b64encode(query)}

    req = Request('http://localhost:5000/api/v1.0/identification')
    req.add_header('Content-Type', 'application/json')

    resp = urlopen(req, dumps(data))

    content = resp.read()
    print content
except Exception as e:
    print e
```

## Age/Gender Estimation
To perform gender estimation, just change the endpoint from "age" to "gender":
```
## Query API (wrap in try-catch)
try:
    query = open('bush1.jpeg').read()

    data = {'query':b64encode(query)}

    req = Request('http://localhost:5000/api/v1.0/estimation/age')
    req.add_header('Content-Type', 'application/json')

    resp = urlopen(req, dumps(data))

    content = resp.read()
    print content
except Exception as e:
    print e
```    

Team
----

[![EthVentures](https://github.com/EthVentures/CryptoTracker/raw/master/resources/img/ethventures-logo.png)](https://ethventures.io)

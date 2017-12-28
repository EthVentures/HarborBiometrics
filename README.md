HarborBiometrics
================
HarborBiometrics leverages open source biometric recognition (OpenBR) to conduct 1:1 face match verification, 1:N face match identification, and age and gender estimation for EthVentures' [Harbor project](https://github.com/EthVentures/HarborBiometrics). It's built on top of the [DockerOpenBR](https://github.com/EthVentures/DockerOpenBR), and implements a simple Flask application to handle verification, identification, and estimation requests.

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

## Resize Image
Resize a photo to (300 x proportional h):
```
## Resize Image
try:
  ## retrieve image from device
  query = open('image.jpeg').read()

  ## base64 encode image
  ## include image filename
  data = {'image':b64encode(query),'format':'jpeg'}

  ## Set request
  req = Request('http://localhost:5000/api/v1.0/image/resize')
  req.add_header('Content-Type', 'application/json')

  ## Post and parse response
  resp = urlopen(req, dumps(data))

  content = resp.read()
  print content
except Exception as e:
  print e
```

## Save Image
Capture a photo and send it to server:
```
## Save Image
try:
  ## retrieve image from device
  query = open('image.jpeg').read()

  ## base64 encode image
  ## include image filename
  data = {'image':b64encode(query),'filename':'mynewimage.jpeg'}

  ## Set request
  req = Request('http://localhost:5000/api/v1.0/image/save')
  req.add_header('Content-Type', 'application/json')

  ## Post and parse response
  resp = urlopen(req, dumps(data))

  content = resp.read()
  print content
except Exception as e:
  print e
```

## Get Image
Retrieve base64 encoded image from server:
```
## Retrieve Image
try:
  ## Set filename
  data = {'filename':'bush1.jpeg'}

  ## Set request
  req = Request('http://localhost:5000/api/v1.0/image/get')
  req.add_header('Content-Type', 'application/json')

  ## Post and parse response
  resp = urlopen(req, dumps(data))

  content = resp.read()
  print content
except Exception as e:
  print e
```

## Remove Image
Remove an image from the server:
```
## Remove Image
try:
  ## set filename
  data = {'filename':'mynewimage.jpeg'}

  ## Set request
  req = Request('http://localhost:5000/api/v1.0/image/delete')
  req.add_header('Content-Type', 'application/json')

  ## Post and parse response
  resp = urlopen(req, dumps(data))

  content = resp.read()
  print content
except Exception as e:
  print e
```

## 1:1 Face Match Verification
Compare two images. Requires a query and target:
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
Find top 5 images that best match a query:
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
To perform gender estimation, just change the endpoint to "gender":
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

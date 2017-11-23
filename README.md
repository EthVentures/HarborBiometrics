HarborBiometrics
================
HarborBiometrics is a Dockerized implementation of OpenBR, a communal biometrics framework.

Usage
-----

docker run avelkoski/openbr:latest bash -c "br -algorithm AgeEstimation -enroll /sample/bush1.jpeg meta.csv &> /dev/null && cat meta.csv"

Team
----

[![EthVentures](https://github.com/EthVentures/CryptoTracker/raw/master/resources/img/ethventures-logo.png)](https://ethventures.io)

FROM avelkoski/openbr:latest
MAINTAINER Aleksandar Velkoski <avelkoski@ethventures.io>

RUN mkdir /api
ADD ./api /api

RUN pip install flask==0.10.1
RUN pip install flask_cors
RUN pip install Pillow==3.4.2

WORKDIR /api/v1.0
CMD ["python","__init__.py"]

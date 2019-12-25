FROM alpine:3.10
ENV PYTHONUNBUFFERED=1
RUN echo "**** install Python ****" && \
    apk add --no-cache python3-dev && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN apk add build-base
RUN apk add libffi-dev libressl-dev
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY mysite/ /src
CMD cd /src && python manage.py runserver 0.0.0.0:80

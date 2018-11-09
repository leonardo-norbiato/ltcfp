FROM tesseractshadow/tesseract4re
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update && apt-get install -y \
    python3-pil \
    python3-requests \
    python3-pip \
    tesseract-ocr-por  \
 && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY ./ltcfp_server /ltcfp_server
WORKDIR /ltcfp_server

ENV DEBIAN_FRONTEND teletype
ENV PYTHONIOENCODING "utf-8"

RUN ln -sf /dev/stdout /var/log/access.log \
	&& ln -sf /dev/stderr /var/log/error.log

EXPOSE 80
CMD ["python3", "app.py"]

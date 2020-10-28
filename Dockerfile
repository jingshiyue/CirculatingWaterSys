FROM python:3.7
ENV PYTHONUNBUFFERED=1
RUN echo python -V
RUN mkdir /CirculatingWaterSys
WORKDIR /CirculatingWaterSys
COPY requirements.txt /CirculatingWaterSys/requirements.txt
RUN pip install -r requirements.txt
CMD ["/bin/bash","-c","while true; do echo hello world; sleep 1000; done"]
FROM python:3.7
ENV PYTHONUNBUFFERED=1
RUN echo python -V
RUN mkdir /CirculatingWaterSys
WORKDIR /CirculatingWaterSys
COPY requirements.txt /CirculatingWaterSys/
RUN pip install -r requirements.txt
COPY . /CirculatingWaterSys/
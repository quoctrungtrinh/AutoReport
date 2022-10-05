FROM python:3.9.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY * ./ReportEtsy

WORKDIR /ReportEtsy
# RUN mkdir csv
# RUN chmod -R +wxr ./csv

#COPY ./Csv /Csv
CMD python3 -u main.py
#CMD echo $(ls)
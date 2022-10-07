FROM python:3.9.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY  *.* ./
COPY Csv/ ./Csv
COPY Model/ ./Model/
COPY Service/ ./Service/
COPY routes/ ./routes/

RUN mkdir Excel
RUN chmod +xrw -R /Excel/
CMD python3 -u main.py

FROM python:3.9.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY  *.* ./
COPY Model/ ./Model/
COPY Service/ ./Service/
COPY routes/ ./routes/

CMD python3 -u main.py

FROM python:3.9.11-slim
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./src moudles/ui/src

WORKDIR moudles/ui/src
CMD python3 -u -m streamlit.cli run frontend.py --server.headless=true

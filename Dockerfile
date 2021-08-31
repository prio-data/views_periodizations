FROM prioreg.azurecr.io/prio-data/uvicorn_deployment:latest
COPY  requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY periodizations ./periodizations
ENV APP="periodizations.app:app"

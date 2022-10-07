#! /bin/sh

BASE=$(PWD)
BACKEND=$BASE/ReportEtsy
FRONTEND=$BASE/ui

cd $BACKEND
docker build -t autorp-backend:v1 .

cd $FRONTEND
docker build -t autorp-ui:v1 .

cd $BASE
docker-compose -f docker-compose.yml up


@echo off 
cls

set BASE=%CD%
set BACKEND=%CD%\ReportEtsy

cd %BACKEND%
docker build -t autorp-backend:v1 .

cd %BASE%
docker-compose -f docker-compose.yml up
#!/bin/python

import streamlit as st
import os

from requests import Request

from io import BytesIO
import time
import json


import sys
sys.path.append('../enviroment')
from enviroment import Enviroment


class AllOrders:

    def __init__(self, session):      
      self.session = session
      self.rootUrl = f'{Enviroment.SERVER_URL}'                   
      self.berichtContent = b''
      

    def getTitle(self):
        return 'All Orders'

    def show(self):
        st.title('All Orders')                     
        self.UploadFile()
        self.MakeReport()
        self.Download()     

    def UploadFile(self):
        updateEtsyOrderFileUrl = f'{self.rootUrl}/allorders/etsyorders/file'
        uploaded_file = st.file_uploader("Upload a terraform file",type = ['csv'],)
        #tfName = st.text_input('Deployment name')  
        if uploaded_file is not None:
            fileName = uploaded_file.name
            bytes_data = BytesIO(uploaded_file.getvalue()).read()

            if st.button("Update order file"):               
                #payload={'tf_name': tfName}

                files=[
                        ('csv_file',(fileName, bytes_data,'application/octet-stream'))
                      ]
                headers = {}

                req = Request('POST', updateEtsyOrderFileUrl, headers=headers, files=files)
                prepped = req.prepare()
                result = self.session.send(prepped, verify = False, timeout=300)
                
                if result.status_code == 200:
                    st.success(result.text)                        
                else:
                    st.error("error" + result.text) 

    def MakeReportEtsy(self):  
        makeReportEtsyUrl = f'{self.rootUrl}/allorders/etsyorders'
        payload={}
        headers = {}
        req = Request('POST', makeReportEtsyUrl, headers=headers, data=payload)
        prepped = req.prepare()
        result = self.session.send(prepped, verify = False, timeout=300)
        if result.status_code == 200:
            st.success(result.text)                        
        else:
            st.error("error" + result.text) 

    def MakeReportWix(self):
        makeReportEtsyUrl = f'{self.rootUrl}/allorders/wixorders'
        payload={}
        headers = {}
        req = Request('POST', makeReportEtsyUrl, headers=headers, data=payload)
        prepped = req.prepare()
        result = self.session.send(prepped, verify = False, timeout=300)
        if result.status_code == 200:
            st.success(result.text)  
            downloadStammDatenUrl = f'{self.rootUrl}/allorders'
            payload={}
            headers = {}
            req = Request('GET', downloadStammDatenUrl, headers=headers)
            prepped = req.prepare()
            result = self.session.send(prepped, verify = False, timeout=300)
            if result.status_code == 200: 
                self.berichtContent = result.content
            else:
                self.berichtContent = b''
                st.error("error" + result.text)                           
        else:
            st.error("error" + result.text)

    def MakeReport(self):
        if st.button('Make All Orders Report'):
            self.MakeReportEtsy()
            self.MakeReportWix()

    def Download(self):                                                   
        st.download_button(
                label="Download Bericht Stammdaten",
                data=self.berichtContent,
                file_name='Bericht_Stammdaten.xlsx')



        







                
                
                
                



        
        
        
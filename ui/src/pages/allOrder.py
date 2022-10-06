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
      self.rootUrl = f'{Enviroment.SERVER_URL}/'                   
      
      

    def getTitle(self):
        return 'All Orders'

    def show(self):
        st.title('All Orders')                     
        #jself.UploadFile()

        binary_contents = b'whatever'

        # Different ways to use the API

        st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'

        with open('myfile.excel', 'w+') as f:
            st.download_button('Download Stamm daten', f, file_name='myfile.excel') 
      

    def UploadFile(self):
        uploaded_file = st.file_uploader("Upload a terraform file",type = ['csvj'],)
        #tfName = st.text_input('Deployment name')  
        if uploaded_file is not None:
            fileName = uploaded_file.name
            bytes_data = BytesIO(uploaded_file.getvalue()).read()

            if st.button("Make Report"):               
                #payload={'tf_name': tfName}

                files=[
                        ('csv_file',(fileName, bytes_data,'application/octet-stream'))
                      ]
                headers = {}

                req = Request('POST', self.rootUrl, headers=headers, files=files)
                prepped = req.prepare()
                result = self.session.send(prepped, verify = False, timeout=300)
                
                if result.status_code == 200:
                    st.write(result.text)                        
                else:
                    st.error("error" + result.text) 


        







                
                
                
                



        
        
        
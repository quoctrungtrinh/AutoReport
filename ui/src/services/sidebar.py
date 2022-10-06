import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os

class SideBarOptionMenuService:
    
    def __init__(self):
        self.optionArr = []
        self.optionTitleArr = []
    
    def show(self):
        with st.sidebar:
            st.image(Image.open(f'{os.getcwd()}/images/Logo_Shop.jpg'))
            st.title('Hannas1stBooks - Report Station')
            
            selectedOption = option_menu('', self.optionTitleArr,
                                #  icons=['house', 'camera fill'],
                                menu_icon="app-indicator", default_index=0,
                                styles={
                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"}, 
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
            
        self._showSelectedOption(selectedOption)
            
    def add(self, option):
        self.optionArr.append(option)
        self.optionTitleArr.append(option.getTitle())
    
    def _showSelectedOption(self, selectedOption):
        for option in self.optionArr:
             if selectedOption == option.getTitle():
                option.show()
                break
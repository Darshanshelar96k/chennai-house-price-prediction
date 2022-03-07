# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:35:00 2022

@author: 91960
"""

import streamlit as st
import pickle 
import numpy as np

def load_model():
    with open('C:/Users/91960/Downloads/p_house/saved_steps.pkl', 'rb') as file:
      data2 = pickle.load(file)
    return data2
data2 = load_model()
model2 = data2["model"]
le_status = data2['le_status']
le_location = data2['le_location']
le_builder = data2['le_builder']
    
def show_predict_page():
    st.title("CHENAI HOUSE PRICE")
    st.write(""""ENTER THE INFORMATTION""")    
         

location = (
     "Veppampattu",        
"Pammal",   
"Medavakkam",  
"Sholinganallur",       
"Perungudi",       
"Selaiyur",       
"Madhavaram",       
"Chromepet",            
"Kelambakkam",          
"Perumbakkam",         
"Sembakkam",         
"Perungalathur",        
"East Tambaram",        
"West Mambalam",        
"Thirumullaivoyal",     
"Kolapakkam",           
"Madipakkam",           
"Pallavaram",           
"Kolathur",             
"Porur",                
"Iyyappanthangal",      
"Ambattur",             
"Vanagaram",            
"Mogappair",            
"Tiruvottiyur",
"Vadanemmeli",          
"Karapakkam",           
"Padur",                
"Poonamallee",          
"Anna Nagar",          
"Vadapalani",          
"Royapettah",          
"Madambakkam",          
"Thaiyur",          
"Nanmangalam",          
"Kovur")

status = (
      "Ready to move", "Under Construction")
builder = (
      'MP Developers', 'DAC Promoters',
       'Casagrand Builder Private Limited', 'Dugar Housing Builders',
       'Radiance Realty Developers India Ltd', 'Traventure Homes Pvt Ltd',
       'Urbanrise', 'Navin Housing Properties P LTD',
       'Jones foundation private limited', 'Isha Homes',
       'Kochar Homes Pvt Ltd', 'Pushkar Properties Pvt Ltd',
       'Asset Tree Homes', 'Urban Tree Infrastructures', 'Olympia Group',
       'Vijay Raja Homes Private Limited', 'Kamalam Builder Pvt Ltd',
       'Appaswamy Real Estate', 'VNR Homes', 'PS Srijan Developers',
       'Lifestyle Housing', 'Puravankara Limited', 'Jones Foundations',
       'Plaza Group', 'Urbando Housing LLP', 'EK Realtors',
       'The Nest Builder', 'Doshi Housing', 'Grandstyle constructions',
       'vinoth builders', 'GTK Foundations', 'Baashyaam Group', 'chris',
       'Krishna Constructions', 'AKS Housing Dedvelopment Pvt Ltd',
       'Mayances Construction and Engineering Services',
       'Ramaniyam Real Estate Builders', 'India Builders Limited', 'Ram',
       'Shatapatri Estates Pvt Ltd', 'Shri Raman Developers',
       'Sri Hari Developers', 'Radiance Realty Developers',
       'Pacifica Companies', 'BSCPL Infrastructure Ltd', 'Khurinji Homes',
       'Saradeuz Realty Constructions', 'VGK Builders Pvt Ltd',
       'Amarprakash Developers Pvt Ltd', 'Hansa Estates',
       'Prince Foundations Ltd', 'Budget Housing And Properties',
       'SP Homes Pvt Ltd', 'Bharathi Construction',
       'Karuppaswamy Builders', 'Merlin Group', 'Advaita Homes',
       'Swamaan Developers', 'Poojaa Foundation',
       'Prestige Estates Projects Ltd', 'Global Homes', 'seller',
       'Pon Mariappan', 'HM Homes', 'INTERFACE PROPERTIES',
       'R Venkatesan', 'viswaraj', 'Shiva', 'S Suresh Kumar',
       'MEHTA REAL ESTATE CHENNAI LLP', 'Balamurugan', 'Alliance Group',
       'Royal Square', 'Proparena', 'Propsource Realty Private Limited',
       'Sandhya', 'Murali', 'Tellus Foundation', 'Jayakanthan',
       'Individual Agent', 'Naveen', 'Shanmugam Property',
       'Value reality', 'Swaminathan', 'smartassetsindia',
       'Sri Vinayaga Real Estate', 'Nagaraj', 'Karthick', 'Prasanna',
       'Vinay Asrani', 'Pragyansh', '24K Realtors', 'Kaushik associates',
       'BricksBurg', 'Dinesh', 'AKS REALTY SERVICES', 'Kkk Landmark',
       'SS Square Property Developers', 'Prabha Homes', 'JA Associates',
       'Bala', 'Sarashwathi Construction', 'Selvakumar',
       'Right Angle Properties', 'Saravan gk', 'Evrostos Properties',
       'Balasubramani', 'Vishnu Foundation Ltd',
       'Shree sakthivel realestate', 'Yadhav constructions real estates',
       'SS PROPERTIES', 'Prop Mart Technologies', 'Info Rich',
       'JD Properties', 'Mohan', 'HomeFirst', 'Elite nisha',
       'THAMINA HOMES', 'MC Foundation', 'ARB HOMES',
       'South Zone Realty Consulting Pvt Ltd', 'Luxclusive Homes',
       'Vishal D', 'mohammed', 'Dee Star Properties',
       'Chennai Gated Community', 'Balaji', 'MrPincode', 'GJ ESTATES',
       'Venkatesh', 'DJ Properties', 'Dhivagaran', 'REALTY INDIA',
       'MAXWORTH PROPERTIES', 'Velan Housing Properties'
      )
location = st.selectbox("LOCATION",location)
status   = st.selectbox("STATUS",status)
builder  = st.selectbox('BUILDER',builder)
bhk = st.slider("BHK",min_value =1 ,max_value =8,value =8,step =1)
area = st.number_input("AREA",min_value =300,max_value=7000,step =1)
age = st.number_input("AGE",min_value =0,max_value=32,step =1)
bathroom = st.number_input("BATHROOM",min_value =1,max_value=8,step =1)

ok = st.button("CALCULATE PRICE ")
if ok:
    X= np.array([[area,status,bhk,age,bathroom,location,builder]])
    X[:,1] = le_status.transform(X[:,1])
    X[:,5] = le_location.transform(X[:,5])
    X[:,6] = le_builder.transform(X[:,6])
    x= X.astype(float)
    
    price = model2.predict(X)
    st.subheader(f"the estimeted price is  ₹{price[0]:.3f}")
    
    


    
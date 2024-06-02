import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu

#Function

def status_prediction(ct,it,app,width,prdrf,ql,cl,
                   tl,spl,itd,itm,ityr,deldate,delm,delyr):
     #change the datatypes "string" to "int"
    itdd= int(itd)
    itdm= int(itm)
    itdyr= int(ityr)

    dyd= int(deldate)
    dym= int(delm)
    dyr= int(delyr)
    #load the classification model file
    with open(r"C:\Users\sivag\DS\Classification_Model.pkl","rb") as f:
        class_model=pickle.load(f)

    user_data= np.array([[ct,it,app,width,prdrf,ql,cl,tl,
                       spl,itdd,itdm,itdyr,dyd,dym,dyr]])
    
    y_pred= class_model.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def selling_price_prediction(ct,sts,it,app,width,prdrf,ql,cl,tl,itd,itm,ityr,deldate,delm,delyr):
    #change the datatypes "string" to "int"
    itdd= int(itd)
    itdm= int(itm)
    itdyr= int(ityr)

    dyd= int(deldate)
    dym= int(delm)
    dyr= int(delyr)
   #load the regression model file
    with open(r"C:\Users\sivag\DS\Regression_Model.pkl","rb") as f:
        reg_model=pickle.load(f)

    user_data= np.array([[ct,sts,it,app,width,prdrf,ql,cl,tl,
                       itdd,itdm,itdyr,dyd,dym,dyr]])
    
    y_pred= reg_model.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred


st.set_page_config(layout="wide")
st.title(":blue[**INDUSTRIAL COPPER MODELING**]")

with st.sidebar:
    option=option_menu('Main Menu',options=["Selling Price Prediction","Status Prediction"])
    
if option == "Status Prediction":
    st.header("Predict Status (Won/Lost)")
    st.write(" ")

    col1,col2=st.columns(2)
    with col1:
        country=st.number_input(label="**Enter the Value for COUNTRY**")
        item_type=st.number_input(label="**Enter the Value for ITEM TYPE**")
        application=st.number_input(label="**Enter the Value for APPLICATION**")
        width=st.number_input(label="**Enter the Value for WIDTH**")
        product_ref=st.number_input(label="**Enter the Value for PRODUCT_REF**")
        quantity_tons_log=st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**",format="%0.15f")
        customer_log=st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**",format="%0.15f")
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**",format="%0.15f")
    with col2:
        selling_price_log= st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        
    button= st.button(":violet[***PREDICT THE STATUS***]",use_container_width=True)

    if button:
        status= status_prediction(country,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,selling_price_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        if status == 1:
            st.write("## :green[**The Status is WON**]")
        else:
            st.write("## :red[**The Status is LOST**]")
if option == "Selling Price Prediction":

    st.header("**PREDICT SELLING PRICE**")
    st.write(" ")

    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**")
        status= st.number_input(label="**Enter the Value for STATUS**")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**")
        application= st.number_input(label="**Enter the Value for APPLICATION**")
        width= st.number_input(label="**Enter the Value for WIDTH**")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**",format="%0.15f")
        
    
    with col2:
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button(":violet[***PREDICT THE SELLING PRICE***]",use_container_width=True)

    if button:
        price= selling_price_prediction(country,status,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        
        st.write("## :green[**The Selling Price is :**]",price)




import json
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image


img=Image.open("inventory-management-icon-15.jpg")

st.set_page_config(page_title="Inventory Management System", page_icon=img)


st.title("INVENTORY MANAGEMENT SYSTEM")

add_selectbox = st.sidebar.selectbox(
    "What Operation woul you like to perform",
    ("About", "Sales", "Admin Control", "Data Analysis"))

# About
if add_selectbox == "About":
    st.write("**In this project an inventory of some products is created from beforehand. The inventory comprises of the unique id or UID, product name, quantity in stock, and expiry date. When the customer have bought certain items , the sales person will enter the unique id the the tab , and the listed product will show in the screen along with its details.When the salesperson will feed the quantity of the products by using the UID it will generate the bill of the customer along with that it will update in the inventory.The admin panel is only for the manager or the owner. The admin pannel asks for the user name and password . After entering the credentials it takes the user to the inventory  where he can add stocks of any existing product by feeding the UID of the product along with the desired details of the product. The admin can also add a new stock in the inventory by entering the UID and the details of the product.The data analysis shows the top five saled product till now.**")


# SALES
elif add_selectbox == "Sales":
    st.write("**This is a web application made for Inventory Management System**")
    
    #Reading record.json
    fd = open("record.json", 'r')
    txt = fd.read()
    fd.close()
    inventory = json.loads(txt)

    #Reading sales.json
    fd1 = open("sales.json", 'r')
    sale = fd1.read()
    fd1.close()
    sales = json.loads(sale)
    
    #Reading data.json
    fd2 = open("data.json", 'r')
    txt2 = fd2.read()
    fd2.close()
    data = json.loads(txt2)
    
    
    st.write("WELCOME TO INVENTORY MANAGEMENT SYSTEM")
    # i = st.number_input("INPUT UID",min_value=202101, max_value=10000000,step=1)
    i = st.number_input("INPUT UID",value=1,step=1)

    
    if i:
        st.write("UID:", i)

    i=str(i)
    if (i in inventory.keys()):
        st.write("product", inventory[i])
        # quan= st.number_input("No Of Quantity Required:",min_value=0, max_value=inventory[i]['Quantity'],step=1)
        quan = st.number_input("No Of Quantity Required:", min_value=0,value=0,step=1)
        
        #quan=int(quan)
        st.write("quantity Required:", quan)
        if quan <= inventory[i]['Quantity']:
            if quan:
                st.write("Name Of Product:", inventory[i]['Product'])
                st.write("Category Of Product:", inventory[i]['Category'])
                st.write("Price Of Product: Rs", inventory[i]['Price'])
                st.write("Quantity Available:", inventory[i]['Quantity'])
                st.write("Quantity Purchased:", quan)
                bill = quan*inventory[i]['Price']
                st.write("=======================")
                st.write("Total Price: Rs", bill)
                st.write("=======================")
                st.write("Thanks For Coming")
                inventory[i]['Quantity'] = inventory[i]['Quantity']-quan
                records = json.dumps(inventory)
                fd = open("record.json", 'w')
                fd.write(records)
                fd.close()

                sales[(str(len(sales)+1))] = {"Product ID": i, "Product": inventory[i]
                                              ['Product'], "Quantity Purchased": quan, "Bill": bill}
                sale = json.dumps(sales)
                fds = open("sales.json", 'w')
                fds.write(sale)
                fds.close()
                if i in data.keys():
                    data[i]['Purchased']=data[i]['Purchased']+quan
                    data1=json.dumps(data)
                    fd = open("data.json",'w')
                    fd.write(data1)
                    fd.close()
                else:
                    data[i] = {"Product":inventory[i]['Product'],"Purchased":quan}
                    data1=json.dumps(data)
                    fd2 = open("data.json",'w')
                    fd2.write(data1)
                    fd2.close()
                
                

        else:
            st.write("Quantity Available:",
                     inventory[i]['Quantity'], " You want to by the remaining")
            st.write("Enter Y for Yes or N for No ")
            c = st.text_input("Enter Y or N ")
            if c:
                if c == "y" or c == "Y":

                    st.write("You have Entered:", c)
                    st.write("Name Of Product:", inventory[i]['Product'])
                    st.write("Category Of Product:", inventory[i]['Category'])
                    st.write("Price Of Product: Rs", inventory[i]['Price'])
                    st.write("Quantity Available:", inventory[i]['Quantity'])
                    st.write("Quantity Purchased:", inventory[i]['Quantity'])
                    cost = inventory[i]['Quantity']*inventory[i]['Price']
                    st.write("=======================")
                    st.write("Total Price: Rs", cost)
                    st.write("=======================")
                    st.write("Thanks For Coming")
                    k = inventory[i]['Quantity']
                    inventory[i]['Quantity'] = inventory[i]['Quantity'] - inventory[i]['Quantity']
                    records = json.dumps(inventory)
                    fd = open("record.json", 'w')
                    fd.write(records)
                    fd.close()

                    sales[(str(len(sales)+1))] = {"Product ID": i, "Product": inventory[i]
                           ['Product'], "Quantity Purchased": k, "Bill": cost}
                    sale = json.dumps(sales)
                    fds = open("sales.json", 'w')
                    fds.write(sale)
                    fds.close()
                    
                    if i in data.keys():
                        data[i]['Purchased']=data[i]['Purchased']+quan
                        data1=json.dumps(data)
                        fd = open("data.json",'w')
                        fd.write(data1)
                        fd.close()
                
                
                    else:
                        data[i] = {"Product":inventory[i]['Product'],"Purchased":quan}
                        data1=json.dumps(data)
                        fd2 = open("data.json",'w')
                        fd2.write(data1)
                        fd2.close()
                    
                        

                elif c == "n" or c == "N":
                    print("You have Entered:", c)
                    print("Thanks For Coming")

elif add_selectbox == "Admin Control":
    st.subheader("Admin Control")
    st.subheader("Login")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    if st.checkbox("Login"):
        if password == '12345' and username == 'admin':
            st.success("Login Successfully")
            fd = open("record.json", 'r')
            txt = fd.read()
            fd.close()

            record = json.loads(txt)
            uid = st.text_input("Enter Product ID:")
            
            if uid:
                
                Quantity = st.number_input("Enter Quantity of Product: ",value=0,step=1)
                if (uid in record.keys()):
                    record[uid]['Quantity'] = record[uid]['Quantity']+Quantity
                    js = json.dumps(record)

                    fd = open("record.json", 'w')
                    fd.write(js)
                    fd.close()
                    
                else:
                    Product = st.text_input("Enter Product Name:")
                    if Product:
                        Category = st.text_input("Enter Category of Product: ")
                        if Category:
                            Price = st.text_input("Enter Price of Product: ")
                            if Price:
                                Expiry = st.text_input("Enter Expiry date of Product: ")
                                if Expiry:
                                    record[uid] = {"Product": Product, "Category": Category, "Price": Price, "Quantity": Quantity, "Expiry Date": Expiry}

                                    js = json.dumps(record)

                                    fd = open("record.json", 'w')
                                    fd.write(js)
                                    fd.close()

        else:
            st.warning("Incorrect User Name/Password")
            
elif add_selectbox == "Data Analysis":
    df = pd.read_json (r'data.json')
    df_t = df.T
    df_t.to_csv (r'sales.csv', index = None)
    
    df1=pd.read_csv("sales.csv")
    
    fig = px.bar(df1, x = "Product", y = "Purchased",title = "Sales Analysis")
    st.plotly_chart(fig)
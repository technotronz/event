import gspread
from oauth2client.service_account import ServiceAccountCredentials
# from  pydrive.drive import GoogleDrive
# from  pydrive.auth import GoogleAuth
import smtplib
import streamlit as st
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
st.set_page_config(page_title="Technotronz Event Registration",page_icon="Untitled design.png")
hide_ststyle = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_ststyle, unsafe_allow_html=True)

creds = ServiceAccountCredentials.from_json_keyfile_name("final.json", scope)
client = gspread.authorize(creds)
sheet = client.open("registration").sheet1
data=sheet.get_all_values()

# creds2 = ServiceAccountCredentials.from_json_keyfile_name("final2.json", scope)
# client2 = gspread.authorize(creds2)
# sheet2 = client2.open("Techrival").sheet1
# data2=sheet2.get_all_values()

# creds4 = ServiceAccountCredentials.from_json_keyfile_name("final4.json", scope)
# client4 = gspread.authorize(creds4)
# sheet4 = client4.open("Hacklite").sheet1
# data4=sheet4.get_all_values()

# creds5 = ServiceAccountCredentials.from_json_keyfile_name("final5.json", scope)
# client5 = gspread.authorize(creds5)
# sheet5 = client5.open("Tacktile arena").sheet1
# data5=sheet5.get_all_values()

# creds6 = ServiceAccountCredentials.from_json_keyfile_name("final6.json", scope)
# client6 = gspread.authorize(creds6)
# sheet6 = client6.open("Trinifty").sheet1
# data6=sheet6.get_all_values()
# #
# creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
# client7 = gspread.authorize(creds7)
# sheet7 = client7.open("Workshop").sheet1
# data7=sheet7.get_all_values()

# creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
# client8 = gspread.authorize(creds8)
# sheet8 = client8.open("Generic run").sheet1
# data8=sheet8.get_all_values()
def fun(mail,event,reg):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
    text=f"Hello {reg}\nYou have successfully registered to {event}."
    message='Subject: {}\n\n{}'.format(event, text)
    server.sendmail("21i252@psgtech.ac.in",mail,message)
    server.quit()
def fun2(mail1,event,reg1,mail2,reg2):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
    text=f"Hello {reg1}\nYou and {reg2}have successfully registered to {event}."
    message='Subject: {}\n\n{}'.format(event, text)
    server.sendmail("21i252@psgtech.ac.in",mail1,message)

    text=f"Hello {reg2}\nYou and {reg1}have successffully registered to {event}."
    message='Subject: {}\n\n{}'.format(event, text)
    server.sendmail("21i252@psgtech.ac.in",mail2,message)
    server.quit()
st.title("Technotronz '23 Event Registration")
sb=st.selectbox("Select the number of participants",options=["--Choose--","One","Two"],index=0)
if sb=="One":
    # st.write
    st.header("Fill in the appropriate registered details ⬇️")
    reg=st.text_input('Register ID of participant:')
    name=st.text_input('Name of participant: [Case sensitive]')
    ph=st.text_input('Contact number of participant:')
    event=st.selectbox("Select the event: ",options=["--Choose--","Techrival","Hacklite","Tactile Arena", "triNiFTy","Workshop", "Generic - Run"],index=0)
    if st.button("Submit"):
        if reg[:5] =="IETE_":
            if event=="Techrival":
                # print("1")
                # for i in range(1,len(data)+1):
                #     if sheet.cell(i,1).value==reg:
                #         # print(2)
                #         sheet2.insert_row([reg,name,ph],len(data)+1)
                #         mail=sheet.cell(i,4).value
                #         reg_id=sheet.cell(i,1).value
                #         break
                # else:
                #     st.error("Invalid Register ID.")
                # st.success("Successfully registered to the Techrival! (Email is sent to registered Mail ID)")
                # fun(mail,"Techrival",reg_id)
                creds2 = ServiceAccountCredentials.from_json_keyfile_name("final2.json", scope)
                client2 = gspread.authorize(creds2)
                sheet2 = client2.open("Techrival").sheet1
                data2=sheet2.get_all_values()
                print(1)
                for i in range(1,len(data)):
                    if(data[i][0]==reg):
                        print(2)
                        if(data[i][1]==name):
                            if data[i][6]==ph:
                                sheet2.insert_row([reg,name,ph],len(data2)+1)
                                st.success("Successfully registered to the Techrival! (Email is sent to registered Mail ID)")
                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                fun(data[i][3],"Techrival",data[i][1])
                                break
                            else:
                                st.error("Invalid Register Contact Number")
                                break    
                        else:
                            st.error("Invalid Register Name")
                            break
                else:
                    st.error("Invalid Register ID.")

            elif event=="Hacklite":
                creds4 = ServiceAccountCredentials.from_json_keyfile_name("final4.json", scope)
                client4 = gspread.authorize(creds4)
                sheet4 = client4.open("Hacklite").sheet1
                data4=sheet4.get_all_values()
                for i in range(1,len(data)):
                    if(data[i][0]==reg):
                        print(2)
                        if(data[i][1]==name):
                            if data[i][6]==ph:
                                sheet4.insert_row([reg,name,ph],len(data4)+1)
                                st.success("Successfully registered to the Hacklite! (Email is sent to registered Mail ID)")
                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                fun(data[i][3],"Hacklite",data[i][1])
                                break
                            else:
                                st.error("Invalid Register Contact Number")
                                break    
                        else:
                            st.error("Invalid Register Name")
                            break
                else:
                    st.error("Invalid Register ID.")
            
            elif event=="Tactile Arena":
                creds5 = ServiceAccountCredentials.from_json_keyfile_name("final5.json", scope)
                client5 = gspread.authorize(creds5)
                sheet5 = client5.open("Tacktile Arena").sheet1
                data5=sheet5.get_all_values()
                for i in range(1,len(data)):
                    if(data[i][0]==reg):
                        print(2)
                        if(data[i][1]==name):
                            if data[i][6]==ph:
                                sheet5.insert_row([reg,name,ph],len(data5)+1)
                                st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                fun(data[i][3],event,data[i][1])
                                break
                            else:
                                st.error("Invalid Register Contact Number")
                                break    
                        else:
                            st.error("Invalid Register Name")
                            break
                else:
                    st.error("Invalid Register ID.")

            elif event=="triNiFTy":
                creds6 = ServiceAccountCredentials.from_json_keyfile_name("final6.json", scope)
                client6 = gspread.authorize(creds6)
                sheet6 = client6.open("Trinifty").sheet1
                data6=sheet6.get_all_values()
                for i in range(1,len(data)):
                    if(data[i][0]==reg):
                        print(2)
                        if(data[i][1]==name):
                            if data[i][6]==ph:
                                sheet6.insert_row([reg,name,ph],len(data6)+1)
                                st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                fun(data[i][3],event,data[i][1])
                                break
                            else:
                                st.error("Invalid Register Contact Number")
                                break    
                        else:
                            st.error("Invalid Register Name")
                            break
                else:
                    st.error("Invalid Register ID.")
            elif event=="Workshop":
                creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
                client7 = gspread.authorize(creds7)
                sheet7 = client7.open("Workshop").sheet1
                data7=sheet7.get_all_values()
                for i in range(1,len(data)):
                    if(data[i][0]==reg):
                        print(2)
                        if(data[i][1]==name):
                            if data[i][6]==ph:
                                sheet7.insert_row([reg,name,ph],len(data7)+1)
                                st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                fun(data[i][3],event,data[i][1])
                                break
                            else:
                                st.error("Invalid Register Contact Number")
                                break    
                        else:
                            st.error("Invalid Register Name")
                            break
                else:
                    st.error("Invalid Register ID.")
            elif event=="Generic - Run":
                creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
                client8 = gspread.authorize(creds8)
                sheet8 = client8.open("Generic run").sheet1
                data8=sheet8.get_all_values()
                for i in range(1,len(data)):
                    if(data[i][0]==reg):
                        print(2)
                        if(data[i][1]==name):
                            if data[i][6]==ph:
                                sheet8.insert_row([reg,name,ph],len(data8)+1)
                                st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                fun(data[i][3],event,data[i][1])
                                break
                            else:
                                st.error("Invalid Register Contact Number")
                                break    
                        else:
                            st.error("Invalid Register Name")
                            break
                else:
                    st.error("Invalid Register ID.")
            #     # print("1")
            #     for i in range(1,len(data)+1):
            #         if sheet.cell(i,1).value==reg:
            #             # print(2)
            #             sheet4.insert_row([reg,name,ph],len(data)+1)
            #             mail=sheet.cell(i,4).value
            #             reg_id=sheet.cell(i,1).value
            #             break
            #     else:
            #         st.error("Invalid Register ID.")
            #     st.success("Successfully registered to the Techrival! (Email is sent to registered Mail ID)")
            #     fun(mail,"Hacklite",reg_id)
            
            
        else:
            st.error("Invalid Register ID")
if sb=="Two":
    st.header("Fill in the appropriate registered details ⬇️")
    st.header("Participant 1: ")
    reg1=st.text_input('Register ID of participant 1:')
    name1=st.text_input('Name of participant 1: [Case sensitive]')
    ph1=st.text_input('Contact number of participant 1:')

    st.header("Participant 2: ")
    reg2=st.text_input('Register ID of participant 2:')
    name2=st.text_input('Name of participant 2: [Case sensitive]')
    ph2=st.text_input('Contact number of participant 2:')
    
    event=st.selectbox("Select the event: ",options=["--Choose--","Tactile Arena", "Generic - Run"],index=0)
    if st.button("Submit"):
        if reg1[:5] =="IETE_":
            if event=="Tactile Arena":
                creds5 = ServiceAccountCredentials.from_json_keyfile_name("final5.json", scope)
                client5 = gspread.authorize(creds5)
                sheet5 = client5.open("Tacktile Arena").sheet1
                data5=sheet5.get_all_values()
                for i in range(1,len(data)):
                    if(data[i][0]==reg1):
                        print(2)
                        if(data[i][1]==name1):
                            if data[i][6]==ph1:
                                for j in range(1,len(data)):
                                    if(data[j][0]==reg2):
                                        print(2)
                                        if(data[j][1]==name2):
                                            if data[j][6]==ph2:
                                                sheet5.insert_row([reg1,name1,ph1,"2nd Part.",reg2,name2,ph2],len(data5)+1)
                                                st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                                fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
                                                break
                                            else:
                                                st.error("Invalid Participant 2 Contact Number")
                                                break
                                        else:            
                                            st.error("Invalid Participant 2 Register Name")
                                            break
                                    
                            else:
                                st.error("Invalid Register 1 Contact Number")
                                break    
                        else:
                            st.error("Invalid Participant 1 Register Name")
                            break
        else:
            st.error("Invalid Participant 1 Register ID.")
        if reg1[:5] =="IETE_":
            if event=="Generic - Run":
                creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
                client8 = gspread.authorize(creds8)
                sheet8 = client8.open("Generic run").sheet1
                data8=sheet8.get_all_values()
                for i in range(1,len(data)):
                    if(data[i][0]==reg1):
                        print(2)
                        if(data[i][1]==name1):
                            if data[i][6]==ph1:
                                for j in range(1,len(data)):
                                    if(data[j][0]==reg2):
                                        print(2)
                                        if(data[j][1]==name2):
                                            if data[j][6]==ph2:
                                                sheet8.insert_row([reg1,name1,ph1,"2nd Part.",reg2,name2,ph2],len(data8)+1)
                                                st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                                st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                                fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
                                                break
                                            else:
                                                st.error("Invalid Participant 2 Contact Number")
                                                break
                                        else:            
                                            st.error("Invalid Participant 2 Register Name")
                                            break
                                    
                            else:
                                st.error("Invalid Register 1 Contact Number")
                                break    
                        else:
                            st.error("Invalid Participant 1 Register Name")
                            break
        else:
            st.error("Invalid Participant 1 Register ID.")
#IETE_              
# for i in range(1,len(data)+1):
#     if sheet2.cell(i,1).value =='5':
#         print('ss')
#         print(sheet2.cell(i,2).value)
# print(sheet2.cell(1,2).value)
# gauth=GoogleAuth()
# gauth.LocalWebserverAuth()
# server=smtplib.SMTP_SSL("smtp.gmail.com",465)
# server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
# message='Subject: {}\n\n{}'.format("ff", "TEXT")
# server.sendmail("21i252@psgtech.ac.in","sarvesh20123@gmail.com",message)
# server.quit()
# name="S"
# r="1"
# ph=90
# text=f"Hello {name}! You now can register for upcoming Technotonz events\nYour login credentials:\nRegistration ID: {r}\nName: {name}\nContact number: {ph}\n\nNote: You can use this mail as verification if the registration pdf went missing."
# print(text)
# drive=GoogleDrive(gauth)
# file1=drive.CreateFile({'title':'test.txt'})
# file1.SetContentString('ff')
# file1.Upload()
# contacts = ['YourAddress@gmail.com', 'test@example.com']
# msg = EmailMessage()
# msg['Subject'] = 'Check out Bronx as a puppy!'
# msg['From'] = 'sarvesh20123@gmail.com'
# msg['To'] = 'YourAddress@gmail.com'
# msg.set_content('This is a plain text email')
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login('sarvesh20123@gmail.com', 'A1.2.3.4.5.6')
#     smtp.send_message(msg)

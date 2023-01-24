import gspread
from oauth2client.service_account import ServiceAccountCredentials
# from  pydrive.drive import GoogleDrive
# from  pydrive.auth import GoogleAuth
import smtplib
import streamlit as st
from PIL import Image

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
st.set_page_config(page_title="Technotronz'23 Event Registration",page_icon="Untitled design.png")
hide_ststyle = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_ststyle, unsafe_allow_html=True)
img = Image.open('TZ_logo2.png')
st.image(img)

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
# col1,col2,col3=st.columns([2,1,2])
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(255, 255, 255);
    height:1.5em;
    width: 3em; 
    font-size: 29px;
    color: black;
}
</style>""", unsafe_allow_html=True)
# with col2:
#             d=st.button("Submit")
link="https://discord.gg/Pf4cqxZtQu"
def fun(mail,event,reg):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
    text=f"Hello {reg}!\nYou have successfully registered to {event}.\n\nBest regards,\nTeam Technotronz."
    text=f"Hello {reg}!\nWe are gratified to announce that you have successfully registered for {event}.\nMake sure you join our discord server to receive regular updates: {link}\nAll the very best!\n\nBest regards,\nTeam Technotronz."
    message='Subject: {}\n\n{}'.format("Registered in "+ event, text)
    server.sendmail("21i252@psgtech.ac.in",mail,message)
    server.quit()
def fun2(mail1,event,reg1,mail2,reg2):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
    text=f"Hello {reg1}!\nWe are gratified to announce that you and {reg2} have successfully registered for {event}.\nMake sure you join our discord server to receive regular updates: {link}\nAll the very best!\n\nBest regards,\nTeam Technotronz."
    message='Subject: {}\n\n{}'.format("Registered in "+ event, text)
    server.sendmail("21i252@psgtech.ac.in",mail1,message)

    text=f"Hello {reg2}!\nWe are gratified to announce that you and {reg1} have successfully registered for {event}.\nMake sure you join our discord server to receive regular updates: {link}\nAll the very best!\n\nBest regards,\nTeam Technotronz."
    message='Subject: {}\n\n{}'.format("Registered in "+event, text)
    server.sendmail("21i252@psgtech.ac.in",mail2,message)
    server.quit()
def fun3():
#             st.write(f'''<a target="_self" href="https://discord.gg/WgEDCtPN" target="_blank"><button>Click to join Technotronz'23 Discord server to follow regular updates</button></a>''',unsafe_allow_html=True)
              link = '[Make sure you join our discord server to receive regular updates](https://discord.gg/Pf4cqxZtQu)'
              st.markdown(link, unsafe_allow_html=True)
# def fun3(mail,event,)
one,two,thr=st.columns([0.1,1, 0.1])
with two:
            st.header("Technotronz'23 Event Registration")
# st.title("Technotronz'23 Event Registration")
note_er = 'Note: If you have not completed the general registration, **[click here](https://technotronz-general-registration-tkl0ww.streamlit.app/)** to register and get your registration ID.'
st.markdown(note_er, unsafe_allow_html=True)
event=st.selectbox("Select the event: ",options=["--Choose--","Techrival","Hacklite","Tactile Arena", "triNiFTy","Techverse - Workshop", "Generic - Run"],index=0)
# p=st.selectbox("Selelct the number of participants: ",options=["--Choose--","One","Two"])
# if p=="One":
#         st.header("Fill in the appropriate registered details ⬇️")
#         reg=st.text_input('Your register ID:')
#         name=st.text_input('Your name [Case sensitive]:')
#         ph=st.text_input('Your contact number:')
#         if st.button("Submit"):
if event=="Techrival":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
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
                                    sheet2.insert_row([reg,name,ph,data[i][3]],len(data2)+1)
                                    st.success("Successfully registered to the Techrival! (Email is sent to registered Mail ID)")
                                    fun3()
#                                     c1,c2,c3,c4=st.columns([1,1,1,1])
#                                     with c2:
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
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
            else:
                    st.error("Invalid Register ID.")
elif event=="Hacklite":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds4 = ServiceAccountCredentials.from_json_keyfile_name("final4.json", scope)
                    client4 = gspread.authorize(creds4)
                    sheet4 = client4.open("Hacklite").sheet1
                    data4=sheet4.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet4.insert_row([reg,name,ph,data[i][3]],len(data4)+1)
                                    st.success("Successfully registered to the Hacklite! (Email is sent to registered Mail ID)")
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                    fun(data[i][3],"Hacklite",data[i][1])
                                    fun3()
#                                     link = '[Make sure you join our discord server to receive regular updates](https://discord.gg/Pf4cqxZtQu)'
#                                     st.markdown(link, unsafe_allow_html=True)
                                    break
                                else:
                                    st.error("Invalid Register Contact Number")
                                    break    
                            else:
                                st.error("Invalid Register Name")
                                break
                    else:
                        st.error("Invalid Register ID.")
            else:
                    st.error("Invalid Register ID.")
elif event=="Tactile Arena":
    p=st.selectbox("Selelct the number of participants: ",options=["--Choose--","One","Two"])
    if p=="One":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds5 = ServiceAccountCredentials.from_json_keyfile_name("final5.json", scope)
                    client5 = gspread.authorize(creds5)
                    sheet5 = client5.open("Tacktile Arena").sheet1
                    data5=sheet5.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet5.insert_row([reg,name,ph,data[i][3]],len(data5)+1)
                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                    fun(data[i][3],event,data[i][1])
                                    fun3()
                                    break
                                else:
                                    st.error("Invalid Register Contact Number")
                                    break    
                            else:
                                st.error("Invalid Register Name")
                                break
                    else:
                        st.error("Invalid Register ID.")
            else:
                st.error("Invalid Register ID.")
    elif p=="Two":
        st.header("Fill in the appropriate details ⬇️")
        st.header("Participant 1: ")
        reg1=st.text_input('Register ID of participant 1:')
        name1=st.text_input('Name of participant 1: [Case sensitive]')
        ph1=st.text_input('Contact number of participant 1:')

        st.header("Participant 2: ")
        reg2=st.text_input('Register ID of participant 2:')
        name2=st.text_input('Name of participant 2: [Case sensitive]')
        ph2=st.text_input('Contact number of participant 2:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg1[:4] =="TZ23":
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
                                                    sheet5.insert_row([reg1,name1,ph1,data[i][3],"2nd Part.",reg2,name2,ph2,data[j][3]],len(data5)+1)
                                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                                    fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
                                                    fun3()
                                                    break
                                                else:
                                                    st.error("Invalid Participant 2 Contact Number")
                                                    break
                                            else:            
                                                st.error("Invalid Participant 2 Register Name")
                                                break
                                    else:
                                        st.error("Invalid Participant 2 Register ID")    
                                else:
                                    st.error("Invalid Register 1 Contact Number")
                                    break    
                            else:
                                st.error("Invalid Participant 1 Register Name")
                                break
                    # else:
                        # st.error("Invalid Participant 1 Register ID.")
            else:
                st.error("Invalid Participant 1 Register ID.")                 

elif event=="triNiFTy":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds6 = ServiceAccountCredentials.from_json_keyfile_name("final6.json", scope)
                    client6 = gspread.authorize(creds6)
                    sheet6 = client6.open("Trinifty").sheet1
                    data6=sheet6.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet6.insert_row([reg,name,ph,data[i][3]],len(data6)+1)
                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                    fun(data[i][3],event,data[i][1])
                                    fun3()
                                    break
                                else:
                                    st.error("Invalid Register Contact Number")
                                    break    
                            else:
                                st.error("Invalid Register Name")
                                break
                    else:
                        st.error("Invalid Register ID.")
            else:
                st.error("Invalid Register ID.")
elif event=="Techverse - Workshop":
    ch=st.selectbox("Click the credential: ",options=["--Choose--","Campus Ambassador","PSG Tech Student","IETE membership holder","None of the above"])
    if ch=="Campus Ambassador":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        adm=st.text_input('Your Campus ambassador ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
                    client7 = gspread.authorize(creds7)
                    sheet7 = client7.open("Workshop").sheet1
                    data7=sheet7.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet7.insert_row([reg,name,ph,data[i][3],ch,adm],len(data7)+1)
                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                    st.write("Check out mail regarding payment details and stay tuned for further updates!")
                                    fun3()
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                    # fun3(data[i][3],event,data[i][1],ch)
                                    break
                                else:
                                    st.error("Invalid Register Contact Number")
                                    break    
                            else:
                                st.error("Invalid Register Name")
                                break
                    else:
                        st.error("Invalid Register ID.")
            else:
                    st.error("Invalid Register ID.")
    if ch=="PSG Tech Student":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        rollno=st.text_input('Your roll number: ')
        # adm=st.text_input('Your Campus ambassador ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
                    client7 = gspread.authorize(creds7)
                    sheet7 = client7.open("Workshop").sheet1
                    data7=sheet7.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet7.insert_row([reg,name,ph,data[i][3],ch,rollno],len(data7)+1)
                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                    st.write("Check out mail regarding payment details and stay tuned for further updates!")
                                    fun3()
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                    # fun3(data[i][3],event,data[i][1],ch)
                                    break
                                else:
                                    st.error("Invalid Register Contact Number")
                                    break    
                            else:
                                st.error("Invalid Register Name")
                                break
                    else:
                        st.error("Invalid Register ID.")
            else:
                    st.error("Invalid Register ID.")
    if ch=="None of the above":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        rollno=st.text_input('Your roll number: ')
        # adm=st.text_input('Your Campus ambassador ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
                    client7 = gspread.authorize(creds7)
                    sheet7 = client7.open("Workshop").sheet1
                    data7=sheet7.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet7.insert_row([reg,name,ph,data[i][3],ch,rollno],len(data7)+1)
                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                    st.write("Check out mail regarding payment details and stay tuned for further updates!")
                                    fun3()
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                    # fun3(data[i][3],event,data[i][1],ch)
                                    break
                                else:
                                    st.error("Invalid Register Contact Number")
                                    break    
                            else:
                                st.error("Invalid Register Name")
                                break
                    else:
                        st.error("Invalid Register ID.")
            else:
                    st.error("Invalid Register ID.")
    if ch=="IETE membership holder":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        # rollno=st.text_input('Your roll number: ')
        sf=st.text_input('Your IETE SF membership number:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
                    client7 = gspread.authorize(creds7)
                    sheet7 = client7.open("Workshop").sheet1
                    data7=sheet7.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet7.insert_row([reg,name,ph,data[i][3],ch,sf],len(data7)+1)
                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                    st.write("Check out mail regarding payment details and stay tuned for further updates!")
                                    fun3()
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                    # fun3(data[i][3],event,data[i][1],ch)
                                    break
                                else:
                                    st.error("Invalid Register Contact Number")
                                    break    
                            else:
                                st.error("Invalid Register Name")
                                break
                    else:
                        st.error("Invalid Register ID.")
            else:
                    st.error("Invalid Register ID.")        
        # st.header("Fill in the appropriate details ⬇️")
        # reg=st.text_input('Your register ID:')
        # name=st.text_input('Your name [Case sensitive]:')
        # ph=st.text_input('Your contact number:')
        # col1,col2,col3=st.columns([2,1,2])
        # with col2:
        #     d=st.button("Submit")
        # if d:
        #     if reg[:4] =="TZ23":
        #             creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
        #             client7 = gspread.authorize(creds7)
        #             sheet7 = client7.open("Workshop").sheet1
        #             data7=sheet7.get_all_values()
        #             for i in range(1,len(data)):
        #                 if(data[i][0]==reg):
        #                     print(2)
        #                     if(data[i][1]==name):
        #                         if data[i][6]==ph:
        #                             sheet7.insert_row([reg,name,ph,data[i][3]],len(data7)+1)
        #                             st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
        #                             # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
        #                             fun(data[i][3],event,data[i][1])
        #                             break
        #                         else:
        #                             st.error("Invalid Register Contact Number")
        #                             break    
        #                     else:
        #                         st.error("Invalid Register Name")
        #                         break
        #             else:
        #                 st.error("Invalid Register ID.")
        #     else:
        #                 st.error("Invalid Register ID.")        
elif event=="Generic - Run":
    p=st.selectbox("Selelct the number of participants: ",options=["--Choose--","One","Two"])
    if p=="One":
        st.header("Fill in the appropriate details ⬇️")
        reg=st.text_input('Your register ID:')
        name=st.text_input('Your name [Case sensitive]:')
        ph=st.text_input('Your contact number:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg[:4] =="TZ23":
                    creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
                    client8 = gspread.authorize(creds8)
                    sheet8 = client8.open("Generic run").sheet1
                    data8=sheet8.get_all_values()
                    for i in range(1,len(data)):
                        if(data[i][0]==reg):
                            print(2)
                            if(data[i][1]==name):
                                if data[i][6]==ph:
                                    sheet8.insert_row([reg,name,ph,data[i][3]],len(data8)+1)
                                    st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                    fun3()
                                    # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
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
            else:
                st.error("Invalid Register ID")
    if p=="Two":
        st.header("Fill in the appropriate details ⬇️")
        st.header("Participant 1: ")
        reg1=st.text_input('Register ID of participant 1:')
        name1=st.text_input('Name of participant 1: [Case sensitive]')
        ph1=st.text_input('Contact number of participant 1:')

        st.header("Participant 2: ")
        reg2=st.text_input('Register ID of participant 2:')
        name2=st.text_input('Name of participant 2: [Case sensitive]')
        ph2=st.text_input('Contact number of participant 2:')
        col1,col2,col3=st.columns([2,1,2])
        with col2:
            d=st.button("Submit")
        if d:
            if reg1[:4] =="TZ23":
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
                                                sheet8.insert_row([reg1,name1,ph1,data[i][3],"2nd Part.",reg2,name2,ph2,data[i][3]],len(data8)+1)
                                                st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
                                                # st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                                                fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
                                                fun3()
                                                break
                                            else:
                                                st.error("Invalid Participant 2 Contact Number")
                                                break
                                        else:            
                                            st.error("Invalid Participant 2 Register Name")
                                            break
                                else:
                                        st.error("Invalid Participant 2 Register ID")    
                            else:
                                st.error("Invalid Register 1 Contact Number")
                                break    
                        else:
                            st.error("Invalid Participant 1 Register Name")
                            break
                # else:
                #     st.error("Invalid Participant 1 Register ID")
            else:
                st.error("Invalid Participant 1 Register ID")
# if p=="Two":
#     st.header("Fill in the appropriate registered details ⬇️")
#     st.header("Participant 1: ")
#     reg1=st.text_input('Register ID of participant 1:')
#     name1=st.text_input('Name of participant 1: [Case sensitive]')
#     ph1=st.text_input('Contact number of participant 1:')

#     st.header("Participant 2: ")
#     reg2=st.text_input('Register ID of participant 2:')
#     name2=st.text_input('Name of participant 2: [Case sensitive]')
#     ph2=st.text_input('Contact number of participant 2:')
#     if st.button("Submit"):
#         if reg1[:4] =="TZ23":
#             if event=="Tactile Arena":
#                 creds5 = ServiceAccountCredentials.from_json_keyfile_name("final5.json", scope)
#                 client5 = gspread.authorize(creds5)
#                 sheet5 = client5.open("Tacktile Arena").sheet1
#                 data5=sheet5.get_all_values()
#                 for i in range(1,len(data)):
#                     if(data[i][0]==reg1):
#                         print(2)
#                         if(data[i][1]==name1):
#                             if data[i][6]==ph1:
#                                 for j in range(1,len(data)):
#                                     if(data[j][0]==reg2):
#                                         print(2)
#                                         if(data[j][1]==name2):
#                                             if data[j][6]==ph2:
#                                                 sheet5.insert_row([reg1,name1,ph1,data[i][3],"2nd Part.",reg2,name2,ph2,data[j][3]],len(data5)+1)
#                                                 st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
#                                                 st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
#                                                 fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
#                                                 break
#                                             else:
#                                                 st.error("Invalid Participant 2 Contact Number")
#                                                 break
#                                         else:            
#                                             st.error("Invalid Participant 2 Register Name")
#                                             break
                                    
#                             else:
#                                 st.error("Invalid Register 1 Contact Number")
#                                 break    
#                         else:
#                             st.error("Invalid Participant 1 Register Name")
#                             break
#             elif event=="Generic - Run":
#                 creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
#                 client8 = gspread.authorize(creds8)
#                 sheet8 = client8.open("Generic run").sheet1
#                 data8=sheet8.get_all_values()
#                 for i in range(1,len(data)):
#                     if(data[i][0]==reg1):
#                         print(2)
#                         if(data[i][1]==name1):
#                             if data[i][6]==ph1:
#                                 for j in range(1,len(data)):
#                                     if(data[j][0]==reg2):
#                                         print(2)
#                                         if(data[j][1]==name2):
#                                             if data[j][6]==ph2:
#                                                 sheet8.insert_row([reg1,name1,ph1,data[i][3],"2nd Part.",reg2,name2,ph2,data[i][3]],len(data8)+1)
#                                                 st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
#                                                 st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
#                                                 fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
#                                                 break
#                                             else:
#                                                 st.error("Invalid Participant 2 Contact Number")
#                                                 break
#                                         else:            
#                                             st.error("Invalid Participant 2 Register Name")
#                                             break
                                    
#                             else:
#                                 st.error("Invalid Register 1 Contact Number")
#                                 break    
#                         else:
#                             st.error("Invalid Participant 1 Register Name")
#                             break
#         else:
#             st.error("Invalid Participant 1 Register ID.")
        # if reg1[:4] =="TZ23":
        #     if event=="Generic - Run":
        #         creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
        #         client8 = gspread.authorize(creds8)
        #         sheet8 = client8.open("Generic run").sheet1
        #         data8=sheet8.get_all_values()
        #         for i in range(1,len(data)):
        #             if(data[i][0]==reg1):
        #                 print(2)
        #                 if(data[i][1]==name1):
        #                     if data[i][6]==ph1:
        #                         for j in range(1,len(data)):
        #                             if(data[j][0]==reg2):
        #                                 print(2)
        #                                 if(data[j][1]==name2):
        #                                     if data[j][6]==ph2:
        #                                         sheet8.insert_row([reg1,name1,ph1,data[i][3],"2nd Part.",reg2,name2,ph2,data[i][3]],len(data8)+1)
        #                                         st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
        #                                         st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
        #                                         fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
        #                                         break
        #                                     else:
        #                                         st.error("Invalid Participant 2 Contact Number")
        #                                         break
        #                                 else:            
        #                                     st.error("Invalid Participant 2 Register Name")
        #                                     break
                                    
        #                     else:
        #                         st.error("Invalid Register 1 Contact Number")
        #                         break    
        #                 else:
        #                     st.error("Invalid Participant 1 Register Name")
        #                     break
        # else:
        #     st.error("Invalid Participant 1 Register ID.")
# sb=st.selectbox("Select the number of participants",options=["--Choose--","One","Two"],index=0)
# if sb=="One":
    # st.write
    # st.header("Fill in the appropriate registered details ⬇️")
    # reg=st.text_input('Register ID of participant:')
    # name=st.text_input('Name of participant: [Case sensitive]')
    # ph=st.text_input('Contact number of participant:')
    # event=st.selectbox("Select the event: ",options=["--Choose--","Techrival","Hacklite","Tactile Arena", "triNiFTy","Workshop", "Generic - Run"],index=0)
    # if st.button("Submit"):
        # if reg[:4] =="TZ23":
            # if event=="Techrival":
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
                # creds2 = ServiceAccountCredentials.from_json_keyfile_name("final2.json", scope)
                # client2 = gspread.authorize(creds2)
                # sheet2 = client2.open("Techrival").sheet1
                # data2=sheet2.get_all_values()
                # print(1)
                # for i in range(1,len(data)):
                #     if(data[i][0]==reg):
                #         print(2)
                #         if(data[i][1]==name):
                #             if data[i][6]==ph:
                #                 sheet2.insert_row([reg,name,ph,data[i][3]],len(data2)+1)
                #                 st.success("Successfully registered to the Techrival! (Email is sent to registered Mail ID)")
                #                 st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
                #                 fun(data[i][3],"Techrival",data[i][1])
                #                 break
                #             else:
                #                 st.error("Invalid Register Contact Number")
                #                 break    
                #         else:
                #             st.error("Invalid Register Name")
                #             break
                # else:
                #     st.error("Invalid Register ID.")

            # elif event=="Hacklite":
            #     creds4 = ServiceAccountCredentials.from_json_keyfile_name("final4.json", scope)
            #     client4 = gspread.authorize(creds4)
            #     sheet4 = client4.open("Hacklite").sheet1
            #     data4=sheet4.get_all_values()
            #     for i in range(1,len(data)):
            #         if(data[i][0]==reg):
            #             print(2)
            #             if(data[i][1]==name):
            #                 if data[i][6]==ph:
            #                     sheet4.insert_row([reg,name,ph,data[i][3]],len(data4)+1)
            #                     st.success("Successfully registered to the Hacklite! (Email is sent to registered Mail ID)")
            #                     st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
            #                     fun(data[i][3],"Hacklite",data[i][1])
            #                     break
            #                 else:
            #                     st.error("Invalid Register Contact Number")
            #                     break    
            #             else:
            #                 st.error("Invalid Register Name")
            #                 break
            #     else:
            #         st.error("Invalid Register ID.")
            
            # elif event=="Tactile Arena":
            #     creds5 = ServiceAccountCredentials.from_json_keyfile_name("final5.json", scope)
            #     client5 = gspread.authorize(creds5)
            #     sheet5 = client5.open("Tacktile Arena").sheet1
            #     data5=sheet5.get_all_values()
            #     for i in range(1,len(data)):
            #         if(data[i][0]==reg):
            #             print(2)
            #             if(data[i][1]==name):
            #                 if data[i][6]==ph:
            #                     sheet5.insert_row([reg,name,ph,data[i][3]],len(data5)+1)
            #                     st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
            #                     st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
            #                     fun(data[i][3],event,data[i][1])
            #                     break
            #                 else:
            #                     st.error("Invalid Register Contact Number")
            #                     break    
            #             else:
            #                 st.error("Invalid Register Name")
            #                 break
            #     else:
            #         st.error("Invalid Register ID.")

            # elif event=="triNiFTy":
            #     creds6 = ServiceAccountCredentials.from_json_keyfile_name("final6.json", scope)
            #     client6 = gspread.authorize(creds6)
            #     sheet6 = client6.open("Trinifty").sheet1
            #     data6=sheet6.get_all_values()
            #     for i in range(1,len(data)):
            #         if(data[i][0]==reg):
            #             print(2)
            #             if(data[i][1]==name):
            #                 if data[i][6]==ph:
            #                     sheet6.insert_row([reg,name,ph,data[i][3]],len(data6)+1)
            #                     st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
            #                     st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
            #                     fun(data[i][3],event,data[i][1])
            #                     break
            #                 else:
            #                     st.error("Invalid Register Contact Number")
            #                     break    
            #             else:
            #                 st.error("Invalid Register Name")
            #                 break
            #     else:
            #         st.error("Invalid Register ID.")
            # elif event=="Workshop":
            #     creds7 = ServiceAccountCredentials.from_json_keyfile_name("final7.json", scope)
            #     client7 = gspread.authorize(creds7)
            #     sheet7 = client7.open("Workshop").sheet1
            #     data7=sheet7.get_all_values()
            #     for i in range(1,len(data)):
            #         if(data[i][0]==reg):
            #             print(2)
            #             if(data[i][1]==name):
            #                 if data[i][6]==ph:
            #                     sheet7.insert_row([reg,name,ph,data[i][3]],len(data7)+1)
            #                     st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
            #                     st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
            #                     fun(data[i][3],event,data[i][1])
            #                     break
            #                 else:
            #                     st.error("Invalid Register Contact Number")
            #                     break    
            #             else:
            #                 st.error("Invalid Register Name")
            #                 break
            #     else:
            #         st.error("Invalid Register ID.")
            # elif event=="Generic - Run":
            #     creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
            #     client8 = gspread.authorize(creds8)
            #     sheet8 = client8.open("Generic run").sheet1
            #     data8=sheet8.get_all_values()
            #     for i in range(1,len(data)):
            #         if(data[i][0]==reg):
            #             print(2)
            #             if(data[i][1]==name):
            #                 if data[i][6]==ph:
            #                     sheet8.insert_row([reg,name,ph,data[i][3]],len(data8)+1)
            #                     st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
            #                     st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
            #                     fun(data[i][3],event,data[i][1])
            #                     break
            #                 else:
            #                     st.error("Invalid Register Contact Number")
            #                     break    
            #             else:
            #                 st.error("Invalid Register Name")
            #                 break
            #     else:
            #         st.error("Invalid Register ID.")
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
            
            
        # else:
        #     st.error("Invalid Register ID")
# if sb=="Two":
#     st.header("Fill in the appropriate registered details ⬇️")
#     st.header("Participant 1: ")
#     reg1=st.text_input('Register ID of participant 1:')
#     name1=st.text_input('Name of participant 1: [Case sensitive]')
#     ph1=st.text_input('Contact number of participant 1:')

#     st.header("Participant 2: ")
#     reg2=st.text_input('Register ID of participant 2:')
#     name2=st.text_input('Name of participant 2: [Case sensitive]')
#     ph2=st.text_input('Contact number of participant 2:')
    
#     event=st.selectbox("Select the event: ",options=["--Choose--","Tactile Arena", "Generic - Run"],index=0)
    # if st.button("Submit"):
    #     if reg1[:4] =="TZ23":
    #         if event=="Tactile Arena":
    #             creds5 = ServiceAccountCredentials.from_json_keyfile_name("final5.json", scope)
    #             client5 = gspread.authorize(creds5)
    #             sheet5 = client5.open("Tacktile Arena").sheet1
    #             data5=sheet5.get_all_values()
    #             for i in range(1,len(data)):
    #                 if(data[i][0]==reg1):
    #                     print(2)
    #                     if(data[i][1]==name1):
    #                         if data[i][6]==ph1:
    #                             for j in range(1,len(data)):
    #                                 if(data[j][0]==reg2):
    #                                     print(2)
    #                                     if(data[j][1]==name2):
    #                                         if data[j][6]==ph2:
    #                                             sheet5.insert_row([reg1,name1,ph1,data[i][3],"2nd Part.",reg2,name2,ph2,data[j][3]],len(data5)+1)
    #                                             st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
    #                                             st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
    #                                             fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
    #                                             break
    #                                         else:
    #                                             st.error("Invalid Participant 2 Contact Number")
    #                                             break
    #                                     else:            
    #                                         st.error("Invalid Participant 2 Register Name")
    #                                         break
                                    
    #                         else:
    #                             st.error("Invalid Register 1 Contact Number")
    #                             break    
    #                     else:
    #                         st.error("Invalid Participant 1 Register Name")
    #                         break
    #     else:
    #         st.error("Invalid Participant 1 Register ID.")
    #     if reg1[:4] =="TZ23":
    #         if event=="Generic - Run":
    #             creds8 = ServiceAccountCredentials.from_json_keyfile_name("final8.json", scope)
    #             client8 = gspread.authorize(creds8)
    #             sheet8 = client8.open("Generic run").sheet1
    #             data8=sheet8.get_all_values()
    #             for i in range(1,len(data)):
    #                 if(data[i][0]==reg1):
    #                     print(2)
    #                     if(data[i][1]==name1):
    #                         if data[i][6]==ph1:
    #                             for j in range(1,len(data)):
    #                                 if(data[j][0]==reg2):
    #                                     print(2)
    #                                     if(data[j][1]==name2):
    #                                         if data[j][6]==ph2:
    #                                             sheet8.insert_row([reg1,name1,ph1,data[i][3],"2nd Part.",reg2,name2,ph2,data[i][3]],len(data8)+1)
    #                                             st.success(f"Successfully registered to the {event}! (Email is sent to registered Mail ID)")
    #                                             st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
    #                                             fun2(data[i][3],event,data[i][1],data[j][3],data[j][1])
    #                                             break
    #                                         else:
    #                                             st.error("Invalid Participant 2 Contact Number")
    #                                             break
    #                                     else:            
    #                                         st.error("Invalid Participant 2 Register Name")
    #                                         break
                                    
    #                         else:
    #                             st.error("Invalid Register 1 Contact Number")
    #                             break    
    #                     else:
    #                         st.error("Invalid Participant 1 Register Name")
    #                         break
    #     else:
    #         st.error("Invalid Participant 1 Register ID.")
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

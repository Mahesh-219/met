import streamlit as st
st.chat_message("ai")
with st.sidebar:
        messages = st.container(height=300)
        if prompt := st.chat_input("Say something"):
                messages.chat_message("user").write(prompt)
                messages.chat_message("assistant").write(f"Echo: {prompt}")
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")
st.markdown( ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]")
st.header("Registration Form")

username = st.text_input("Enter username", placeholder = "your username")

password = st.text_input("Enter password ", placeholder = "your password")

confirm_password = st.text_input("password", placeholder="your password")

is_checked = st.checkbox("Agree to Terms and Conditions")

is_clicked = st.button("Register",type="primary" , use_container_width=True)



if  password == confirm_password :
        st.toast("Registration Successful")
else:
        st.toast("Registration unsuccessful")
        

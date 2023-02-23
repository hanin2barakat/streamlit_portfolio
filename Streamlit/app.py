from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage" , page_icon=":fire:", layout="wide")

def load_lottieurl(url):
 r=requests.get(url)
 if r.status_code !=200:
  return None
 return r.json()


#use local css
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#-- LOAD ASSETS --
lottie_coding = load_lottieurl ("https://assets6.lottiefiles.com/packages/lf20_rbgEm9En6D.json")
img_lha=Image.open("images/lha.jpg")
img_daviart=Image.open("images/Davi_art.jpg")



# -- HEADER --

with st.container():
 st.subheader("Hi, I am Hanin :wave:")
 st.title("A Fresh Graduated Software Engineer")
 st.write("I am passionate about finding ways to use Python and AI and Software Testing to be more efficient and effective")

with st.container():
    st.write("")
    left_column, right_column = st.columns(2)
    with left_column:
     st.header("What I do")
     st.write(
           """
            On my Behance I share my recent designs, most of them are Logo Designs,you can check them.
           
            My GitHub include all my projects, strating from this one "My Portfilio" wich I've had alot of fun building it,
            to my graduation project, another python projects and AI.
            """ 
            )
          
     st.write("[My Behance account](https://www.behance.net/haninbarakat?isa0=1)")
     st.write("[My GitHub account](https://github.com/hanin2barakat)")

     st.write("##")
    with right_column:
     st_lottie(lottie_coding, height=300, key="coding")

# -- Projects --
with st.container():
  st.header("My Projects")
  st.write("##")
  image_column, text_column = st.columns((1, 2))
  with image_column:
    st.image(img_lha)
with text_column: 
    st.header("##")

    st.subheader("Abaya Brand - LhA abaya")
    st.write(
          """
         That was my latest project, it's my own abaya brand, I've worked on it's social media designs and the abaya's too, you can order from my website, don't forget the discount code!  

     """
     )
    st.markdown("[View the project...](https://www.behance.net/gallery/159912155/Abaya-brand)")

    st.write("##")
with st.container():
  st.write("##")
  image_column, text_column = st.columns((1, 2))
with image_column:
 st.image(img_daviart)
  
with text_column: 
    st.header("##")

    st.subheader("AI predicting model- Davi Art")
    st.write(
          """
an AI model which is trained to predict the user mood based on chosen pictures the trained data is classified into 5 sets happy, very happy, neutral, sad and very sad, it's classified into this 5 sets based on the impact of the picture on the user mood.

     """
     )
    st.markdown("[View the project...](https://github.com/hanin2barakat/sent_pred)")


#-- CONTACT--
with st.container():
  st.header("Get In Touch With Me!")
  st.write("##")
   
  #Documentation: https://formsubmit.co/ 
  contact_form= """"
  <form action="https://formsubmit.co/hanin2barakat@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="False">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your Mesaage here!" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column= st.columns(2)
with left_column:
  st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
  st.empty()
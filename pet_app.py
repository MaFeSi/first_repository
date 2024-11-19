import streamlit as st
import requests

st.set_page_config(page_title="Pet App",
                   page_icon="🐱")

st.header("Welcome to the Pet App",
          divider="rainbow")

def get_cat_image():
    url = "https://cataas.com//cat/gif"
    contents = requests.get(url)
    #st.write(contents)

    return contents.content

def get_dog_image_url():
    url = "https://random.dog/woof.json"
    contents = requests.get(url).json()
    dog_image_url = contents["url"]

    return dog_image_url

c1, c2 = st.columns(2)

with c1:
    cat_button = st.button("Click here for a cat image")
    if cat_button:
        cat_image = get_cat_image()
        st.image(cat_image, width=300, caption="MY CAT IMAGE")

with c2:
    dog_button = st.button("Click here for a dog image")
    if dog_button:
        dog_image_url = get_dog_image_url()
        while dog_image_url[:-4] == ".mp4":
            dog_image_url = get_dog_image_url()


        st.image(dog_image_url, width=300, caption="MY DOG IMAGE")



import streamlit as st

st.set_page_config(page_title="MY OUTFIT GENERATOR",
                   page_icon="🪡")

def registration_page():
    st.title("Registration Page")

def main_page():
    st.title("Main Page")
    st.subheader("Welcome to My Outfit Generator!")
    st.write(
        "This app is your personal style guide. "
        "The quiz and outfit generator will not only help you to find out what your personal style is, but will also help you create cool new outfits from your own wardrobe!")

def quiz_page():
    st.title("Quiz")

    """Style-Quiz"""
    st.title("Style-Quiz: What is your style?")

    # Quiz-Fragen
    st.write("Beantworte die folgenden Fragen, um deinen Stil besser zu verstehen.")
    frage_1 = st.radio("Wie würdest du deinen Style beschreiben?",
                       ["Casual", "Elegant", "Sportlich", "Boho", "Vintage"])
    frage_2 = st.radio("Welche Farben trägst du gerne?",
                       ["Neutral (Schwarz, Weiß, Grau)", "Pastellfarben", "Knallige Farben", "Erdtöne"])
    frage_3 = st.radio("Welche Accessoires bevorzugst du?", ["Schmuck", "Sonnenbrillen", "Hüte", "Keine"])

    # Auswertung
    if st.button("Style entdecken!"):
        st.subheader("Dein Style-Ergebnis:")
        if frage_1 == "Casual":
            st.write("Dein Style ist **entspannt und alltagstauglich** – du magst es bequem und unkompliziert.")
        elif frage_1 == "Elegant":
            st.write("Dein Style ist **klassisch und schick** – du setzt auf zeitlose Mode und klare Linien.")
        elif frage_1 == "Sportlich":
            st.write("Dein Style ist **aktiv und dynamisch** – du bevorzugst funktionale Kleidung.")
        elif frage_1 == "Boho":
            st.write("Dein Style ist **kreativ und unkonventionell** – du liebst verspielte Details und Muster.")
        elif frage_1 == "Vintage":
            st.write("Dein Style ist **retro und einzigartig** – du magst nostalgische Kleidung.")

def upload_page():
    st.title("Upload your own photos here")
    """Outfit Generator"""
    st.title("Outfit Generator")

    # Initialisierung von Session State
    if "tops" not in st.session_state:
        st.session_state["tops"] = []
    if "bottoms" not in st.session_state:
        st.session_state["bottoms"] = []
    if "shoes" not in st.session_state:
        st.session_state["shoes"] = []
    if "accessories" not in st.session_state:
        st.session_state["accessories"] = []
    if "top_index" not in st.session_state:
        st.session_state["top_index"] = 0
    if "bottom_index" not in st.session_state:
        st.session_state["bottom_index"] = 0
    if "shoes_index" not in st.session_state:
        st.session_state["shoes_index"] = 0
    if "accessories_index" not in st.session_state:
        st.session_state["accessories_index"] = 0

    # Upload-Bereich für mehrere Bilder
    st.sidebar.header("Upload your own photos here")
    uploaded_tops = st.sidebar.file_uploader("Oberteile hochladen", type=["png", "jpg", "jpeg"],
                                             accept_multiple_files=True)
    uploaded_bottoms = st.sidebar.file_uploader("Unterteile hochladen", type=["png", "jpg", "jpeg"],
                                                accept_multiple_files=True)
    uploaded_shoes = st.sidebar.file_uploader("Schuhe hochladen", type=["png", "jpg", "jpeg"],
                                              accept_multiple_files=True)
    uploaded_accessories = st.sidebar.file_uploader("Accessoires hochladen", type=["png", "jpg", "jpeg"],
                                                    accept_multiple_files=True)

    # Bilder speichern
    if uploaded_tops:
        st.session_state["tops"].extend(uploaded_tops)
    if uploaded_bottoms:
        st.session_state["bottoms"].extend(uploaded_bottoms)
    if uploaded_shoes:
        st.session_state["shoes"].extend(uploaded_shoes)
    if uploaded_accessories:
        st.session_state["accessories"].extend(uploaded_accessories)

    # Outfit anzeigen
    st.header("Dein aktuelles Outfit (untereinander):")
    if st.session_state["tops"]:
        st.image(st.session_state["tops"][st.session_state["top_index"]], caption="Oberteil", width=200)
    else:
        st.write("👕 Keine Oberteile hochgeladen.")

    if st.button("Nächstes Oberteil"):
        st.session_state["top_index"] = (st.session_state["top_index"] + 1) % len(st.session_state["tops"])

    if st.session_state["bottoms"]:
        st.image(st.session_state["bottoms"][st.session_state["bottom_index"]], caption="Unterteil", width=200)
    else:
        st.write("👖 Keine Unterteile hochgeladen.")

    if st.button("Nächstes Unterteil"):
        st.session_state["bottom_index"] = (st.session_state["bottom_index"] + 1) % len(st.session_state["bottoms"])

    if st.session_state["shoes"]:
        st.image(st.session_state["shoes"][st.session_state["shoes_index"]], caption="Schuhe", width=200)
    else:
        st.write("👟 Keine Schuhe hochgeladen.")

    if st.button("Nächste Schuhe"):
        st.session_state["shoes_index"] = (st.session_state["shoes_index"] + 1) % len(st.session_state["shoes"])

    if st.session_state["accessories"]:
        st.image(st.session_state["accessories"][st.session_state["accessories_index"]], caption="Accessoire",
                 width=200)
    else:
        st.write("👜 Keine Accessoires hochgeladen.")

    if st.button("Nächstes Accessoire"):
        st.session_state["accessories_index"] = (st.session_state["accessories_index"] + 1) % len(
            st.session_state["accessories"])
# function for changing colors
def set_theme(theme_name):
    themes = {
        "Bright": {
            "primary_color": "#FFFFFF",
            "background_color": "#CBEDB1",
            "text_color": "#000000",
            "header_color": "#FFFFFF"
        },
        "Dark": {
            "primary_color": "#6C6C6C",
            "background_color": "#6C6C6C",
            "text_color": "#000000",
            "header_color": "#000000"
        },
        "Blue": {  # Blue-themed colors
            "primary_color": "#298897",
            "background_color": "#298897",
            "text_color": "#99F1FF",
            "header_color": "#99F1FF"
        },
        "Green": {  # Emerald-green inspired colors
            "primary_color": "#3F804E",
            "background_color": "#3F804E",
            "text_color": "#86CA96",
            "header_color": "#86CA96"
        },
        "Red": {  # Bordeaux-inspired deep reds
            "primary_color": "#BC6175",
            "background_color": "#F2CED1",
            "text_color": "#880924",
            "header_color": "#880924"
        },
        "Brown": {  # Warm brown tones
            "primary_color": "#8B4513",
            "background_color": "#F4E3D7",
            "text_color": "#4E342E",
            "header_color": "#6D4C41"
        }
    }

    if theme_name in themes:
        theme = themes[theme_name]
        custom_css = f"""
        <style>
            :root {{
                --primary-color: {theme['primary_color']};
                --background-color: {theme['background_color']};
                --text-color: {theme['text_color']};
                --header-color: {theme['header_color']};
            }}

            /* Apply background color and text color with higher specificity */
            html, body, div.stApp {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            h1, h2, h3, h4, h5, h6 {{
                color: var(--header-color) !important;
            }}

            /* Streamlit-specific class adjustments */
            .css-18e3th9 {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            .stButton > button {{
                background-color: var(--primary-color) !important;
                color: var(--text-color) !important;
            }}

            .stTextInput > div > div input {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            .css-1cpxqw2 {{
                background-color: var(--background-color) !important;
            }}
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)

# choosing the color in the menu
st.sidebar.header("")
theme_name = st.sidebar.selectbox("Which colour theme do you prefer", ["Bright", "Dark", "Blue", "Green", "Red", "Brown"], index=0)

set_theme(theme_name)

options = ['Registration Page','Main Page', 'Quiz', 'Your Outfit Generator']
page_selection = st.sidebar.selectbox("Menu", options)

if page_selection == "Registration Page":
    registration_page()
elif page_selection == "Main Page":
    main_page()
elif page_selection == "Quiz":
    quiz_page()
elif page_selection == "Your Outfit Generator":
    upload_page()


# Seiten im Dropdown-Menü
#menu_options = ["Startseite", "Style-Quiz", "Outfit-Generator", "Einstellungen"]
#selected_page = st.sidebar.selectbox("Navigiere zu", menu_options)


# Navigation zwischen den Seiten

import streamlit as st
import time

# 1. POSTAVKE I DETEKTIVSKI STIL
st.set_page_config(page_title="Snovi i Vizije 2", page_icon="🕵️")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', monospace; }
    
    /* BIJELA SLOVA ZA UNOS */
    input { 
        color: #FFFFFF !important; 
        background-color: #111111 !important; 
        border: 2px solid #00FF41 !important; 
        font-size: 1.2rem !important;
    }
    
    .stTextInput label { color: #00FF41 !important; font-weight: bold; }
    .stButton>button { background-color: #00FF41; color: #000; width: 100%; font-weight: bold; }
    
    /* Efekt bljeska munje */
    .bolt { color: #FFFFFF; text-shadow: 0 0 20px #FFFFFF; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 2. UVODNO ODBROJAVANJE (Munje i grmljavina)
if 'intro_done' not in st.session_state:
    placeholder = st.empty()
    for i in range(5, -1, -1):
        with placeholder.container():
            if i % 2 == 0:
                st.markdown(f"<h1 style='text-align: center; color: white; text-shadow: 0 0 30px white;'>⚡ {i} ⚡</h1>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center; color: white;'>BOOM! Grmljavina trese prozore...</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{i}</h1>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center;'>⛈️ Kiša udara o limeni krov...</p>", unsafe_allow_html=True)
            time.sleep(1)
    placeholder.empty()
    st.session_state.intro_done = True

# 3. NASLOV I DETEKTIV
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("<h1 style='font-size: 80px; margin-top: 0;'>🕵️</h1>", unsafe_allow_html=True)
with col2:
    st.title("Snovi i Vizije 2")
    st.subheader("Strah od tišine by Dominic Chant")
    st.markdown("**Datum:** 22.02.2026 | **Vizija ukupno:** 33")

# AUDIO (Za grmljavinu - korisnik mora kliknuti Play zbog pravila preglednika)
st.write("🎵 *Uključi zvuk za potpuni doživljaj tišine i grmljavine:*")
st.audio("https://www.soundjay.com")

# 4. BAZA VIZIJA (Samo prvih par radi primjera, ostalo ostaje isto u tvom kodu)
vizije = {
    "1": "Gledao sam korak čvrst kao stijena a hladan poput leda, prolazio je pored nasmijanog cvijeća koje je uvenulo.",
    "2": "Vidio sam strana bića koja su stigla i ljude koji tvrde znali smo da postojite. Nitko nije shvatio da su oni tek nedavno stvoreni i njihovim tijelom ne teče krv.",
    # ... Ovdje idu sve tvoje vizije do 33 ...
}

# 5. UNOS BROJA
if 'otkljucano2' not in st.session_state:
    st.session_state.otkljucano2 = set()

preostalo = 33 - len(st.session_state.otkljucano2)

if preostalo > 0:
    st.info(f"🔓 Otključano vizija: {len(st.session_state.otkljucano2)}/33")
    broj = st.text_input("Unesi broj vizije (1-33):", key="main_input")
    
    # Dodao sam provjeru da ispiše viziju samo ako postoji u bazi
    if broj in vizije:
        st.markdown(f"### 🔍 ISTRAGA: VIZIJA {broj}")
        st.success(vizije[broj])
        if st.button("Zabilježi u detektivski dnevnik"):
            st.session_state.otkljucano2.add(broj)
            st.rerun()
    elif broj != "":
        st.error("Taj trag ne vodi nikamo. Pokušaj s drugim brojem.")
else:
    # FINALNI DIO (Isti kao prije s tvojim linkovima)
    st.success("✅ SVIH 33 VIZIJA JE PRIKUPLJENO.")
    # ... tvoj finalni kod ...

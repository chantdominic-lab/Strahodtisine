import streamlit as st
import time

# 1. FINALNI STIL - PLAN B ZA ENTER
st.set_page_config(page_title="Snovi i Vizije 2", page_icon="🕵️")

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', monospace; }
    
    /* NASLOV I ZELENI TEKSTOVI */
    h1, .zeleni-tekst { color: #00FF41 !important; text-shadow: 0 0 5px #00FF41; }

    /* SAKRIVANJE SIVOG "PRESS ENTER" TEKSTA */
    div[data-testid="stInputInstructions"] { display: none !important; }

    /* LABEL IZNAD UNOSA - ZELENO */
    .stTextInput label {
        color: #00FF41 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }

    /* ŠTO KORISNIK TIPKA - BIJELO */
    input {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        background-color: #111111 !important;
        border: 2px solid #00FF41 !important;
    }

    /* VIZIJE I PORUKE - BIJELO */
    .stAlert p, .stMarkdown p, .stWrite, h3 { color: #FFFFFF !important; }

    /* GUMB */
    .stButton>button { 
        background-color: #008F11 !important; 
        color: #FFFFFF !important; 
        font-weight: bold !important; 
    }
</style>
""", unsafe_allow_html=True)

# 2. ODBROJAVANJE
if 'intro_v2' not in st.session_state:
    placeholder = st.empty()
    poruke = ["5... Tišina se širi", "4... Kiša natapa tlo", "3... Netko te promatra", "2... Tajne izlaze", "1... Strah od tišine", "0... Uđi"]
    for p in poruke:
        with placeholder.container():
            st.markdown(f"<h1 style='text-align: center; color:#00FF41;'>{p}</h1>", unsafe_allow_html=True)
            time.sleep(0.7)
    placeholder.empty()
    st.session_state.intro_v2 = True

# 3. NASLOV I PODACI (Sve u jednom redu)
st.markdown("<h1>🕵️ Snovi i Vizije 2</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='zeleni-tekst'>Strah od tišine by Dominic Chant</h3>", unsafe_allow_html=True)
st.markdown("<p style='color:#00FF41; font-size: 1.2rem;'>📖 22.02.2026 | 🗝️ 33</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. BAZA VIZIJA (1-33)
vizije = {
    "1": "Gledao sam korak čvrst kao stijena a hladan poput leda, prolazio je pored nasmijanog cvijeća koje je uvenulo.",
    "2": "Vidio sam strana bića koja su stigla i ljude koji tvrde znali smo da postojite. Nitko nije shvatio da su oni tek nedavno stvoreni i njihovim tijelom ne teče krv.",
    "3": "Vidio sam dvije osobe jedna pada u smrt zbog nečega što ulazi kroz nos a druga ostane u životu zbog razloga što živi bez potrebe za zrakom.",
    "4": "Vidim vrijeme u kojem ljudi na koljenu izgovaraju molitve ali ih šalju kao iz dubokog bezdana kroz tihi šapat i imaju osjećaj da im snagu molitve nešto priguši.",
    "5": "U ljudima će postojati nešto što može odrediti minute života i jedno vrijeme nitko neće puno obraćati pozornost na opasnosti koje su prihvatili.",
    "6": "Vidim dolazak vremena i ljude koji izbjegavaju ljude traže samoću da razgovaraju sami sa sobom.",
    "7": "Nebeske ptice sjede na granama i uživaju u hrani dok čudnim očima promatraju ptice koje ne traže ni vodu ni hranu a vješto krilima pobjeđuju vjetar.",
    "8": "Vidio sam prazne klupe i parkove, ulice puste. Vidio sam vrijeme u kojem je čovjek željan čovjeka kao da su na zemlji ostali samo kamen i drveće.",
    "9": "Iz zemlje i podzemlja bježe štakori zbog vatre i kaosa nije, bježe zbog stranca koji je živio na površini a sada se krije u podzemlje.",
    "10": "Doći će vrijeme kada će jezero u ljudima presušiti i ljudi neće znati kako čistit bol iz sebe.",
    "11": "Vidim ljude i broj ljudi koji ne raste nego naglo pada. Kroz velike gradove buknuo je vulkan u ljudima... gube svoj broj.",
    "12": "Pojavio se netko tko zna sve tajne i sve duhovnosti i može da priča s bilo kime na zemlji ili svemiru i pun sebe krenuo je da traži svoje mjesto na zemlji.",
    "13": "Vidio sam malo željezo koje će dobiti pravo kao čovjek ako usavrši znanje poput čovjeka od malog koraka do velikog.",
    "14": "Doći će dan kada će ljudi tražiti život u mislima a one će biti prazne nitko neće moći svojom voljom da lista prošlost u mislima.",
    "15": "Dolazi vrijeme kada na mrtva slova na papiru nitko neće obraćati pozornost.",
    "16": "Tajne u riječima i zagonetke kroz priče ostat će tamo gdje su upisane same za sebe jer nitko neće više upregnuti mozak.",
    "17": "Proći će puno godina ludog života prije nego svjetlost dođe i uzme svoje plodove probrane među trnjem.",
    "18": "U jednoj noći svijet više neće biti isti i pojavit će se many koji će pokušati kroz maglu ljudima objasniti da smo prevareni.",
    "19": "Sudbinu lopova više neće čistiti rešetke i zidovi zato što će doći dan kada sudbinu lopova budu odredili u jednoj ljudskoj sekundi.",
    "20": "Mnogi će pokušati iz početka daleko od svih ali neće znati da je cijeli svijet jedno oko.",
    "21": "Jednog dana će ljudi živjeti s ljudima koji kada legnu spavati iz istog položaja se ustanu i nikad ne pričaju o svojim snovima.",
    "22": "Vidio sam čovjeka koji se usred noći probudio... pored kreveta je stajalo nešto što hoda ali nije čovjek.",
    "23": "Prvi puta čovjek razmišlja o svojem psu koji je bio dobar čuvar... pas bježi pod gazdin krevet.",
    "24": "Gledam čovjeka koji promatra djecu dok šutaju loptu i u sebi razmišlja ova lopta je sada mala ali ih priprema za veću loptu.",
    "25": "Pojavit će se strah i vladat će velika tišina ljudi će pažljivo birati što će pričati na glas.",
    "26": "Rijeke svijeta će početi presušivati... netko će shvatiti da rijeku pije velika žedna zvijer.",
    "27": "Vidio sam žurbu čovjeka koji pokušava tajno znanje skriti s lica zemlje.",
    "28": "Pojavit će se živo željezo koje ima veliku ljepotu... ta ljepota će zaluditi many da krenu u smjeru koji nije život.",
    "29": "Doći će dan velike panike kada željezo svojom snagom bude pokušalo čovjeka osloboditi od zla.",
    "30": "Svijetom će letjeti uvjerenje da su ljudi postali prosvijetljeni kada su prihvatili da je tijelo samo prazna čahura.",
    "31": "Jedan čovjek će kroz grad jahati konja i reći niste me slušali kao čovjeka sada možda budete slušali mojeg konja.",
    "32": "Vidio sam pokušaj gdje za okruglim stolom pričaju da se sve može kroz jedan duži ciklus života.",
    "33": "Čovjek stane pred prozor i briše prašinu... u ovome prozoru je nešto živo."
}

# 5. LOGIKA UNOSA S PLANOM B ZA ENTER
if 'v2_count' not in st.session_state:
    st.session_state.v2_count = 1

if st.session_state.v2_count <= 33:
    st.markdown(f"<p style='color:#FFFFFF; font-size: 1.1rem;'>⚡ Ukupno vizija: 33 | Zabilježio si: {st.session_state.v2_count - 1}</p>", unsafe_allow_html=True)
    
    # PLAN B: Jasna uputa u zelenoj boji umjesto siva
    broj = st.text_input("Unesi broj vizije i klikni ENTER:", key="input_v2").strip()
    
    if broj != "":
        if not broj.isdigit():
            st.error("Unesi samo broj.")
        elif int(broj) > 33:
            st.error("Ovaj san ne postoji u arhivi.")
        elif int(broj) > st.session_state.v2_count:
            st.warning(f"Prvo moraš zabilježiti san broj {st.session_state.v2_count}.")
        elif int(broj) < st.session_state.v2_count:
            st.markdown(f"<p style='color:white;'>San {broj} je već zabilježen: {vizije[broj]}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"### VIZIJA {broj}")
            st.markdown(f"<p style='color:white; font-size:1.2rem; border:1px solid #00FF41; padding:10px;'>{vizije[broj]}</p>", unsafe_allow_html=True)
            if st.button("ZABILJEŽI SAN"):
                st.session_state.v2_count += 1
                st.rerun()
else:
    # FINALNI DIO
    st.success("✅ SVE VIZIJE SU ZABILJEŽENE.")
    st.subheader("Ispit tišine")
    
    q1 = st.text_input("Koji je broj za sveti dan?", key="f1").strip().lower()
    q2 = st.text_input("Što čisti bol iz ljudi?", key="f2").strip().lower()
    q3 = st.text_input("Tko je Anđeo Gabriel? (Luka 1, 26)", key="f3").strip().lower()
    
    if st.button("POTVRDI ODGOVORE"):
        c1 = ("7" in q1 or "sedam" in q1)
        c2 = ("suze" in q2)
        c3 = ("glasnik" in q3)
        
        if c1 and c2 and c3:
            st.balloons()
            st.session_state.final_win = True
        else:
            if not c1: st.error("Pogrešan broj svetog dana.")
            if not c2: st.error("Pogrešan odgovor o čišćenju boli.")
            if not c3: st.error("Pogrešan odgovor o Gabrielu.")

            if st.session_state.get('final_win'):
        st.markdown("---")
        st.markdown("<p style='color:white;'>Autor piše više od 25 godina mudrosti u bilježnice i ima ih preko 2000 i uskoro će biti u knjizi:</p>", unsafe_allow_html=True)
        st.markdown("<h3 class='zeleni-tekst'>Labave istine i čvrste sjene</h3>", unsafe_allow_html=True)
        
        if st.button("KLIKNI OVDJE ZA MUDROST"):
            st.warning("📜 'Ja nisam kriv što netko vidi samo mrtva slova na papiru.'")
            
        st.markdown("---")
        # Tri linka u jednom redu - pazite na uvlačenje svakog reda ispod!
        col_l1, col_l2, col_l3 = st.columns(3)
        with col_l1:
            st.markdown("[🔗 DOI Profil](https://doi.org)")
        with col_l2:
            st.markdown("[🔗 ORCID Profil](https://orcid.org)")
        with col_l3:
            st.markdown("[🎮 Igraj PRVI DIO](https://dominicchantigraapppy.streamlit.app)")

import streamlit as st
import time

# 1. POSTAVKE I DETEKTIVSKI STIL
st.set_page_config(page_title="Snovi i Vizije 2", page_icon="🕵️")

st.markdown("""
<style>
    /* Glavna pozadina i zelena slova */
    .stApp { background-color: #000000; color: #00FF41; font-family: 'Courier New', monospace; }
    
    /* PRISILNA BIJELA BOJA ZA UNOS - TESTIRANO */
    input[type="text"] { 
        color: #FFFFFF !important; 
        background-color: #111111 !important; 
        border: 2px solid #00FF41 !important; 
        -webkit-text-fill-color: #FFFFFF !important;
    }
    
    .stTextInput label { color: #00FF41 !important; }
    .stButton>button { background-color: #00FF41; color: #000; width: 100%; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 2. VIZUALNO ODBROJAVANJE
if 'intro_done' not in st.session_state:
    placeholder = st.empty()
    for i in range(5, -1, -1):
        with placeholder.container():
            st.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>⛈️ Grmljavina u daljini... Tišina nastupa...</p>", unsafe_allow_html=True)
            time.sleep(0.7)
    placeholder.empty()
    st.session_state.intro_done = True

# 3. NASLOV
st.markdown("<h1 style='font-size: 50px;'>🕵️ Snovi i Vizije 2</h1>", unsafe_allow_html=True)
st.subheader("Strah od tišine by Dominic Chant")
st.write("📅 22.02.2026 | 🌀 Vizija ukupno: 33")

# 4. BAZA SVIH 33 VIZIJA
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
    "11": "Vidim ljude i broj ljudi koji ne raste nego naglo pada. Kroz velike gradove buknuo je vulkan u ljudima... ljudi gube svoj broj.",
    "12": "Pojavio se netko tko zna sve tajne i sve duhovnosti i može da priča s bilo kime na zemlji ili svemiru i pun sebe krenuo je da traži svoje mjesto na zemlji.",
    "13": "Vidio sam malo željezo koje će dobiti pravo kao čovjek ako usavrši znanje poput čovjeka od malog koraka do velikog.",
    "14": "Doći će dan kada će ljudi tražiti život u mislima a one će biti prazne nitko neće moći svojom voljom da lista prošlost u mislima.",
    "15": "Dolazi vrijeme kada na mrtva slova na papiru nitko neće obraćati pozornost.",
    "16": "Tajne u riječima i zagonetke kroz priče ostat će tamo gdje su upisane same za sebe jer nitko neće više upregnuti mozak.",
    "17": "Proći će puno godina ludog života prije nego svjetlost dođe i uzme svoje plodove probrane među trnjem.",
    "18": "U jednoj noći svijet više neće biti isti i pojavit će se mnogi koji će pokušati kroz maglu objasniti da smo prevareni.",
    "19": "Sudbinu lopova više neće čistiti rešetke i zidovi zato što će doći dan kada sudbinu lopova budu odredili u jednoj ljudskoj sekundi.",
    "20": "Mnogi će pokušati iz početka daleko od svih ali neće znati da je cijeli svijet jedno oko.",
    "21": "Jednog dana će ljudi živjeti s ljudima koji kada legnu spavati iz istog položaja se ustanu i nikad ne pričaju o svojim snovima.",
    "22": "Vidio sam čovjeka koji se usred noći probudio... pored kreveta je stajalo nešto što hoda ali nije čovjek.",
    "23": "Prvi puta čovjek razmišlja o svojem psu koji je bio dobar čuvar... pas bježi pod gazdin krevet.",
    "24": "Gledao sam čovjeka koji promatra djecu dok šutaju loptu i u sebi razmišlja ova lopta je sada mala ali ih priprema za veću loptu.",
    "25": "Pojavit će se strah i vladat će velika tišina ljudi će pažljivo birati što će pričati na glas.",
    "26": "Rijeke svijeta će početi presušivati... netko će shvatiti da rijeku pije velika žedna zvijer.",
    "27": "Vidio sam žurbu čovjeka koji pokušava tajno znanje skriti s lica zemlje.",
    "28": "Pojavit će se živo željezo koje ima veliku ljepotu... ta ljepota će zaluditi mnoge da krenu u smjeru koji nije život.",
    "29": "Doći će dan velike panike kada željezo svojom snagom bude pokušalo čovjeka osloboditi od zla.",
    "30": "Svijetom će letjeti uvjerenje da su ljudi postali prosvijetljeni kada su prihvatili da je tijelo samo prazna čahura.",
    "31": "Jedan čovjek će kroz grad jahati konja i reći niste me slušali kao čovjeka sada možda budete slušali mojeg konja.",
    "32": "Vidio sam pokušaj gdje za okruglim stolom pričaju da se sve može kroz jedan duži ciklus života.",
    "33": "Čovjek stane pred prozor i briše prašinu... u ovome prozoru je nešto živo."
}

# 5. LOGIKA IGRE
if 'otkljucano2' not in st.session_state:
    st.session_state.otkljucano2 = set()

preostalo = 33 - len(st.session_state.otkljucano2)

if preostalo > 0:
    st.info(f"🔓 Otključano: {len(st.session_state.otkljucano2)}/33")
    broj = st.text_input("Unesi broj vizije (1-33):", key="v2_input")
    
    if broj in vizije:
        st.markdown(f"### VIZIJA {broj}")
        st.success(vizije[broj])
        if st.button("Zabilježi viziju"):
            st.session_state.otkljucano2.add(broj)
            st.rerun()
else:
    # 6. FINALNI DIO
    st.success("✅ SVIH 33 VIZIJA JE PRIKUPLJENO.")
    st.subheader("Finalni ispit")
    
    q1 = st.text_input("Koji je broj za sveti dan?", key="q1").strip().lower()
    q2 = st.text_input("Što čisti bol iz ljudi?", key="q2").strip().lower()
    q3 = st.text_input("Tko je Anđeo Gabriel?", key="q3").strip().lower()
    
    if st.button("ZAVRŠI"):
        if ("7" in q1 or "sedam" in q1) and "suze" in q2 and "glasnik" in q3:
            st.balloons()
            st.markdown("### Čestitamo! (Luka 1, 26)")
            st.write("Autor piše više od 25 godina mudrosti u bilježnice...")
            if st.button("PROČITAJ MUDROST"):
                st.info("📜 'Ja nisam kriv što netko vidi samo mrtva slova na papiru.'")
            st.markdown("---")
            st.markdown("[🔗 DOI Profil](https://doi.org)")
            st.markdown("[🔗 ORCID Profil](https://orcid.org)")
        else:
            st.error("Provjeri odgovore.")

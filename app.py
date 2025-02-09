import streamlit as st
import pandas as pd

# Definiamo le combinazioni della roulette
terzine = [set(range(i, i+3)) for i in range(1, 36, 3)]
quartine = [set([i, i+1, i+3, i+4]) for i in range(1, 33, 4)]
sestine = [set(range(i, i+6)) for i in range(1, 32, 6)]

# Memorizziamo i numeri estratti
if "numeri_estratti" not in st.session_state:
    st.session_state.numeri_estratti = []

# **Funzione per calcolare i ritardi**
def calcola_ritardi(numeri_estratti, gruppi):
    tutti_i_numeri = set(range(37))  # Roulette numeri 0-36
    ritardi = {}
    
    for gruppo in gruppi:
        if not gruppo.intersection(numeri_estratti):
            ritardi[f"{sorted(gruppo)}"] = "Mai uscito"
        else:
            ultimi_estratti = [i for i in numeri_estratti[::-1] if i in gruppo]
            ritardi[f"{sorted(gruppo)}"] = len(numeri_estratti) - numeri_estratti[::-1].index(ultimi_estratti[0])
    
    return ritardi

# **Interfaccia Streamlit**
st.title("🎰 Roulette Tracker - Analisi Ritardi")

# **Input dei numeri estratti**
nuovi_numeri = st.text_input("Inserisci i numeri estratti separati da virgola o spazio:", "")

if st.button("Aggiungi Numeri"):
    try:
        numeri = [int(n) for n in nuovi_numeri.replace(",", " ").split() if n.strip().isdigit()]
        st.session_state.numeri_estratti.extend(numeri)
        st.success(f"Aggiunti: {', '.join(map(str, numeri))}")
    except:
        st.error("Errore! Assicurati di inserire solo numeri validi.")

# **Mostra numeri estratti**
st.write("📊 Numeri estratti finora:", ", ".join(map(str, st.session_state.numeri_estratti)))

# **Calcola ritardi**
if st.button("Mostra Ritardi"):
    ritardi_numeri = calcola_ritardi(st.session_state.numeri_estratti, [{n} for n in range(37)])
    ritardi_terzine = calcola_ritardi(st.session_state.numeri_estratti, terzine)
    ritardi_quartine = calcola_ritardi(st.session_state.numeri_estratti, quartine)
    ritardi_sestine = calcola_ritardi(st.session_state.numeri_estratti, sestine)

    st.subheader("📌 Ritardi dei Numeri Singoli")
    st.write(ritardi_numeri)

    st.subheader("🔢 Ritardi delle Terzine")
    st.write(ritardi_terzine)

    st.subheader("🔳 Ritardi delle Quartine")
    st.write(ritardi_quartine)

    st.subheader("🎲 Ritardi delle Sestine")
    st.write(ritardi_sestine)

# **Pulsante per resettare**
if st.button("🔄 Resetta Dati"):
    st.session_state.numeri_estratti = []
    st.success("Dati resettati con successo!")

import streamlit as st

# Titolo dell'app
st.title("Roulette Game 🎰")

# Input per i numeri della roulette
numero = st.number_input("Inserisci il numero della roulette (0-36):", min_value=0, max_value=36)

# Bottone per confermare
if st.button("Gioca!"):
    import random
    risultato = random.randint(0, 36)
    st.write(f"📢 Numero uscito: {risultato}")

    if numero == risultato:
        st.success("🎉 Complimenti! Hai vinto!")
    else:
        st.error("😞 Riprova, la fortuna gira!")



import streamlit as st
import requests
import streamlit.components.v1 as components
#from streamlit_lottie import st_lottie
import sys, random, json

#def load_lottieurl(url:str):
 #   r = requests.get(url)
  #  if r.status_code != 200:
  #      return None
 #   return r.json()

def autocoids():
    answers = ['1st Gen H1-blockers','2nd Gen H1-blockers','Antagonist of H2-receptors','Mast cell stabilizers','5-HT1A (anxiolytic agonist)','5-HT1D/B (migraine headache)']
# Q1
    userAns2 = st.radio(':blue[Loratadine, Cetirizine]',answers)
    if st.button('Submit for Q1'):
        if userAns2 == '2nd Gen H1-blockers':
            st.write(':green[Correct]')
        else:
            st.write(':red[Wrong!]')
# Q2
    userAns5 = st.radio(':blue[Buspirone]',answers)
    if st.button('Submit for Q2'):
        if userAns5 == '5-HT1A (anxiolytic agonist)':
            st.write(':green[Correct]')
        else:
            st.write(':red[Wrong!]')
# Q3
    userAns4 = st.radio(':blue[Cromoglycate]',answers)
    if st.button('Submit for Q3'):
        if userAns4 == 'Mast cell stabilizers':
            st.write(':green[Correct]')
        else:
            st.write(':red[Wrong!]')
# Q4
    userAns1 = st.radio(':blue[Diphenhydramine, Chlorpheniramine, Triprolidine]',answers)
    if st.button('Submit for Q4'):
        if userAns1 == '1st Gen H1-blockers':
            st.write(':green[Correct]')
        else:
            st.write(':red[Wrong!]')
# Q5
    userAns6 = st.radio(':blue[Sumatriptan, Naratriptan, Almotriptan, Zolmitriptan, Nzatriptan, Eletriptan]',answers)
    if st.button('Submit for Q5'):
        if userAns6 == '5-HT1D/B (migraine headache)':
            st.write(':green[Correct]')
        else:
            st.write(':red[Wrong!]')
# Q6
    userAns3 = st.radio(':blue[Cimetidine, Famotidine, Nizatidine, Ranitidine, Roxatidine]',answers)
    if st.button('Submit for Q6'):
        if userAns3 == 'Antagonist of H2-receptors':
            st.write(':green[Correct]')
        else:
            st.write(':red[Wrong!]')
    #st.write('Your answer is' + userAns)
    #submitted = form.form_submit_button("Submit your answer")
    #if submitted:
        #st.write('Your answer is' + userAns)
    #st.write('\n1. 1st Gen H1-blockers\n2. 2nd Gen H1-blockers\n3. Antagonist of H2-receptors\n4. Mast cell stabilizers\n5. 5-HT1A (anxiolytic agonist)\n6. 5-HT1D/B (migraine headache)')
    #st.write('\nType your answer:')
    #st.button("asdfsadf")

st.set_page_config(page_title="My webpage", page_icon=":tada", layout="wide")

# Header section
#st.subheader(" created by Edwin")
st.title("This is a warm place for 藥理學地獄 QQ")
#lottie_pharmacy = load_lottieurl("https://lottie.host/7f2781e7-cab9-425c-8d63-dca7917a7fa9/TYjTbOOEvS.json") 
#st_lottie(lottie_pharmacy, key = "pharmacy")
menu = ["Notes", "Quiz"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Quiz":
    st.subheader("(現在只有更新autocoids的藥物)")
    autocoids()
elif choice == "Notes":
    st.subheader("筆記斟酌看看就好,然後ppt網路版會跑版,所以推薦下載下來")
    st.write('第12週 Autocoids link : https://1drv.ms/p/s!ApTEYroVO0GKgeADHlGt8HEXrwwyIw?e=9ym2jG')
    st.write('第12週 高血壓 link : https://1drv.ms/p/s!ApTEYroVO0GKgd99oU6lGhCM-3U7Rg?e=A35Kl6')
    st.write('第13週 心絞痛跟心律不整 link : https://1drv.ms/p/s!ApTEYroVO0GKgd9_TRR4Vb2HkIjmFw?e=RRmRz7')
    st.write('第13週 心衰竭 link : https://1drv.ms/p/s!ApTEYroVO0GKgd98DhkT2cyCuKgpnQ?e=h4qbhY')
    st.write('第14週 利尿劑 link : https://1drv.ms/p/s!ApTEYroVO0GKgeAA3StR8KUtfL_6NA?e=1cGr2C')
    st.write('第14週 呼吸系統藥物 link : https://1drv.ms/p/s!ApTEYroVO0GKgd97pUgreCJ59KvFJA?e=OdiJSu')
    st.write('第15週 抗癌藥物 link : https://1drv.ms/p/s!ApTEYroVO0GKgeAC7-e83imksTHD5w?e=8ja53a')
    st.write('第15週 抗細菌藥物 link : https://1drv.ms/p/s!ApTEYroVO0GKgd9--yBzxcPgZlUxFg?e=nF3tGL')
    st.write('第16週 抗病毒藥物 link : https://1drv.ms/p/s!ApTEYroVO0GKgeABqYMtg7nCgAC4HQ?e=n1hHhS')

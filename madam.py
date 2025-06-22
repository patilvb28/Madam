import streamlit as st
import random
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Hello, Bestie 💖", layout="centered")

def send_telegram(message):
	try:
		import requests
		TELEGRAM_BOT_TOKEN = "7918441115:AAHZG3-YaGgViGmMBnlHiMfqq8qI7AYB7Dc"
		TELEGRAM_CHAT_ID = "6808247170"
		url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
		data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
		requests.post(url, data=data)
	except Exception as e:
		print(f"❌ Failed to send Telegram alert: {e}")

# Title
st.title("🌸 How are you, Bestie 💖")
st.markdown("""<hr style="border: 1px solid #6d567d;">""", unsafe_allow_html=True)


happy = st.toggle("I am fine 🤗")

if happy:

    st.markdown("Chlo stress kum ho gya!! 😁 ")
    msg1 = "I am fine 🤗"
    send_telegram(msg1) 
    rain(
            emoji=" 🥳 ",
            font_size=60,
            falling_speed=3,
            animation_length=1,
        )

    st.info('Yaha pr mast tumhare pics dalta, memories dalta but tum bhejti kaha ho ?! Aur bhejte ho toh sirf shakal se neck tk ka bhejte ho jaise passport size photo mangwaya ho!! Isliye acche wale photo bheja kro aise surprises dene mein kaam aayenge!! Samjhe !! Next time dhyan rkhna!! ', icon="😑")
    st.divider()

    if st.button("Abse Bhejungi photo !!"):
        msg6 = ("Photo bhejegi")
        send_telegram(msg6)
        st.markdown("Good gurl !!🤗 ")
    
        st.markdown("Ab photo bhi bhejoge, health bhi badhiya hai, toh kuch krna chahiye cuz u are free now, phir baad mein padhne chale jaoge!?? 🧐🧐")

        search = st.toggle("Let's Search 🔎")
        # if st.button("Let's Search 🔎"):
        if search:
            st.markdown("Interest toh hai madam aapko, buss chat mein hi gayab ho jata hai usme bhi dikhaya kro !! 😑 ")
            st.divider()
            st.markdown("Sorry, yaar iss baar time kum tha aur jyada kuch bana nhi paya but next time pakka this is will be interesting, music, videos, photos, and many more animations sb kuch iss baar seh lo, thode se mein kuc ho jao madam plz 😭😭 ")

        st.markdown("upar toggle hai try krna kaam kr jaye toh kismat warna mere mein error aa rha tha aur solve krne mein bahut time lag jayega aur ho hi nhi rha!!")
        st.info('Sorry, yaar ye  toggle kaam nhi kr rha hai and kuch special nhi kr paya but giveme time, i will make it better next time 😭😭🤗🤗')
        rain(emoji=" 😭 ", font_size=60, falling_speed=3, animation_length=1,)

st.markdown("""<hr style="border: 1px solid #6d567d;">""", unsafe_allow_html=True)  

sad   = st.toggle("Not good 😔")

if sad:
    st.markdown("Phir toh mujhe chinta krni chahiye !! 😟 ")
    msg2 = "Not good 😔"
    send_telegram(msg2)
    # Display a comforting message
    messages = [
        "Sending virtual hugs 🤗, Reality mein toh mushkil nhi na-mumkin hai 😑",
        "You’re stronger than you think 💪, I told 1000s of time ⌚",
        "Pain is temporary, your smile is forever 😊",
        "Breathe in... breathe out... You got this 💫",
        "Even the moon 🌙 has to hesitate to flex in front of you 😍"
    ]

    if st.button("Click here for a Mood Boost ✨, Try krna new thoughts on every click!!"):
        st.success(random.choice(messages))

    if st.checkbox("Did you drink water, barabar se time se ??!! 💧"):
        st.info("chlo itna toh krte ho, thank you 💙")

    if st.checkbox("Did you khana khaya healthy wala ??!! 🍽"):
        st.info("Good Gurl!!! 💙")


    # Pain Tracker
    st.markdown("### 😖 How much pain are you feeling?")
    pain_level = st.slider("Kitna dard ho rha hai ??", 0, 10, 0)
    if pain_level >= 7:
        st.warning("Ouch! Take a rest and maybe a warm water bottle? 💦")
        msg3 = ("Dard 7 above hai!!")
        send_telegram(msg3)

    elif pain_level >= 4:
        st.info("Medium pain — deep breaths, maybe some tea? ☕")
        msg4 = ("Dard 4 above hai!! Ok hai")
        send_telegram(msg4)

    else:
        st.success("That's good! Stay comfortable 💗")
        msg5 = ("Dard nhi hai jyada chill!!")
        send_telegram(msg5)


    # Footer message
st.markdown("""<hr style="border: 1px solid #f08080;">""", unsafe_allow_html=True)
st.markdown("Upar 🙄 se ghumkr aana phir rate krna!!")

sentiment_mapping = ["You didn't love (me and this site)", "You didn't like", "thik thak laga tumhe (Badhiya ke liye pics bhejo acche wale)", "Badhiya laga (next wala star nhi dogi guaranteee se!!)", "YOU LOVE ME SO MUCH ❤❤"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"{sentiment_mapping[selected]}.")
    msg10 = (f"{sentiment_mapping[selected]}.")
    send_telegram(msg10)
    st.markdown("IG pr text krke batana kaisa laga ?? OK, Take Care Madam!!")
    st.badge("Dhyan rkhna Apna")

st.markdown("""<hr style="border: 1px solid #6c757d;">""", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:gray;'>😎 Prepared by <b>Patil</b> | Made with 💗 by your bestie.</div>", unsafe_allow_html=True)
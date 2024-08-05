import streamlit as st

def generate_referral_url(referral_name):
    base_url = "https://transcripts.lifetracklearning.com"
    utm_url = f"{base_url}?utm_source=referral&referral_name={referral_name.replace(' ', '_').lower()}"
    return utm_url

st.title("LifeTrack Learning")
st.subheader("Generate Referral URL")

# Input field for referral name
referral_name = st.text_input("Referral Partner's Name:")

# Generate URL button
if st.button("Generate URL"):
    if referral_name:
        generated_url = generate_referral_url(referral_name)
        st.write("Copy this link!")
        st.success(generated_url)
    else:
        st.warning("Please enter the Referral Name.")
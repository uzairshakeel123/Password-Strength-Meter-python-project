import streamlit as st
import re

def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Use at least 8 characters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔹 Add uppercase letters")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔹 Add lowercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔹 Include numbers")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("🔹 Include special characters")

    return score, feedback

def strength_label(score):
    if score <= 2:
        return "🔴 Weak", "danger"
    elif score == 3 or score == 4:
        return "🟡 Medium", "warning"
    else:
        return "🟢 Strong", "success"

# UI
st.set_page_config(page_title="Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = password_strength(password)
    label, level = strength_label(score)

    st.markdown(f"### Strength: {label}")
    st.progress(score / 5)

    if score < 5:
        st.subheader("Tips to improve:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("👆 Type a password above to check its strength.")

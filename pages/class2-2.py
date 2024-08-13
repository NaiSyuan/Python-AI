import streamlit as st

# st.number_input() can be used to get a number input from the user
number = st.number_input("Please input a number", step=1, min_value=0, max_value=100)

# st.write() can be used to display the markdown text
st.markdown(f"The number is ：{number}")


# user input the score
score = st.number_input("Please input the score", step=1, min_value=0, max_value=100)
# display the result of the score
# A :score>90
# B :score>80
# C :score>70
# D :score>60
# F :score<=60
if score > 90:
    st.markdown("A")
elif score > 80:
    st.markdown("B")
elif score > 70:
    st.markdown("C")
elif score > 60:
    st.markdown("D")
else:
    st.markdown("F")

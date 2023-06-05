import streamlit as st
from PIL import Image

#체질량 치수 구하는 랩
#몸무게, 키입력받기

st.write('#체질량 치수 계산기')

height = st.number_input('키를 입력하시오.(cm)', value = 181, step =5)
st.write(height,'cm')

weight = st.number_input('체중을 입력하시오.(kg)', value = 73, step =5)
st.write(weight,'kg')

bmi = weight/((height/100)**2)

def bmi_range(bmi):
    if bmi>=25:
        st.error("비만입니다!!!")
    elif bmi >=23:
        st.success("과체중입니다.")
    elif bmi >=18.5:
        st.info("당신은 정상입니다")
    else:
        st.warning("과체중입니다!")  

if st.button('계산'):
    st.balloons()
    st.write('당신의 체질량 지수는', round(bmi,2), '입니다.')
    bmi_range(bmi)
    
image = Image.open('porsche-1851246_960_720.jpg')

st.image(image, caption='i can buy this car')       
    

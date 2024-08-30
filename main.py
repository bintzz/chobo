import streamlit as st
from data_ loader import load_data

def main():
    st.title('안녕 세계야')
    st.title('이것도 깃허브에서 추가했다 멋지지~')

    df= load_data()
    
    st.write(df)

if __namer__ == '__main__':
        main()
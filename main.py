import streamlit as st
from data_ loader import load_data

def main():
    st.title('안녕 대시보드')
    
    start_date = st.date_input("Start date", df['Date'].min())
    end_date = st.date_input("End date", df['Date'].max())

    df= load_data()
    
    st.write(df)

if __name__ == '__main__':
        main()

'이게 뭐다냐 신기해'
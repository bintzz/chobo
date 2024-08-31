import pandas as pd

import streamlit as st
from data_loader import load_data

def main():
    st.title('안녕 대시보드')
    
    start_date = st.date_input("Start date", df['Date'].min())
    end_date = st.date_input("End date", df['Date'].max())

    df= load_data()
    
#특정 날짜 범위 선택
    df['Date'] = pd.to_datetime(df['Date'])
    with st.expander("범위를 선택하세요"):
          col1,col2 = st.columns(2)
            with col1 :
                start_date = st.date_input("Start date", df['Date'].min())
            with col2 :
                end_date = st.date_input("End date", df['Date'].max())

    ranged_df = df[(df['Date']>= pd.to_datetime(start_date))&(df['Date']>= pd.to_datetime(end_date))]
    ranged_df = ranged_df.reset_index(drop=True)
    st.table(ranged_df)

if __name__ == '__main__':
        main()

'이게 뭐다냐 신기해'
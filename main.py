import pandas as pd

import streamlit as st
from data_ loader import load_data

def main():
st.title('안녕 세계야')
st.title('이것도 깃허브에서 추가했다 멋지지~')

df= load_data()
    
#특정 날짜 범위 선택
st.subheader("Select Date Range")
df['Date'] = pd.to_datetime(df['Date'])
start_date = st.date_input("Start date", df['Date'].min())
end_date = st.date_input("End date", df['Date'].max())

ranged_df = df[(df['Date']>= pd.to_datetime(start_date))&(df['Date']>= pd.to_datetime(end_date))]
ranged_df = ranged_df.reset_index(drop=True)
st.table(ranged_df)

if __name__ == '__main__':
        main()

'이게 뭐다냐 신기해'
import streamlit as st
import pandas as pd

st.title('Data Kasus Covid-19 Februari 2023 di Indonesia')

data = {
    'Tanggal': ['1 Feb 2023', '2 Feb 2023', '3 Feb 2023', '4 Feb 2023', '5 Feb 2023', '6 Feb 2023', '7 Feb 2023', '8 Feb 2023', '9 Feb 2023', '10 Feb 2023', '11 Feb 2023', '12 Feb 2023', '13 Feb 2023', '14 Feb 2023', '15 Feb 2023', '16 Feb 2023', '17 Feb 2023', '18 Feb 2023', '19 Feb 2023', '20 Feb 2023', '21 Feb 2023', '22 Feb 2023', '23 Feb 2023', '24 Feb 2023', '25 Feb 2023', '26 Feb 2023', '27 Feb 2023', '28 Feb 2023'],
    'Jumlah Kasus': [212, 159, 204, 182, 157, 219, 176, 208, 187, 185, 169, 221, 185, 164, 164, 162, 235, 203, 166, 223, 150, 212, 180, 243, 208, 231, 166, 159]
}

df = pd.DataFrame(data)
df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d %b %Y')

if st.checkbox('Show Bar Chart'):
    tab1, tab2, tab3, tab4 = st.tabs(['1 Feb - 28 Feb', '1 Feb - 10 Feb', '11 Feb - 20 Feb', '21 Feb - 28 Feb'])

    df.set_index('Tanggal', inplace=True)
    df.sort_index(inplace=True) # sort by index to preserve original order

    with tab1:
        st.subheader('1 Feb - 28 Feb')
        st.bar_chart(df)

    with tab2:
        st.subheader('1 Feb - 10 Feb')
        st.bar_chart(df.head(10))
    
    with tab3:
        st.subheader('11 Feb - 20 Feb')
        st.bar_chart(df.iloc[10:20])

    with tab4:
        st.subheader('21 Feb - 28 Feb')
        st.bar_chart(df.tail(8))
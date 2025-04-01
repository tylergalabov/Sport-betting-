
import streamlit as st
import pandas as pd
import plotly.express as px

# Примерни данни
balances = pd.DataFrame(columns=['Дата', 'Букмейкър', 'Акаунт', 'Баланс'])
transactions = pd.DataFrame(columns=['Дата', 'Тип', 'Сума', 'Букмейкър', 'Акаунт'])
expenses = pd.DataFrame(columns=['Дата', 'Описание', 'Сума'])
bets = pd.DataFrame(columns=['Дата', 'Спорт', 'Първенство', 'Букмейкър', 'Акаунт', 'Залог', 'Сума', 'Коефициент', 'Резултат'])

# Интерфейс за добавяне на нови записи
st.title('Спортни Залози – Проследяване')
st.subheader('Добави нови данни')

# Въвеждане на данни за залози
st.write("Добави нов залог:")
date = st.date_input('Дата', pd.to_datetime('today'))
sport = st.text_input('Спорт')
league = st.text_input('Първенство')
bookmaker = st.text_input('Букмейкър')
account = st.text_input('Акаунт')
bet = st.text_input('Залог')
amount = st.number_input('Сума', min_value=0.0)
odds = st.number_input('Коефициент', min_value=0.0)
result = st.selectbox('Резултат', ['Печалба', 'Загуба'])

if st.button('Добави залог'):
    new_bet = {
        'Дата': date,
        'Спорт': sport,
        'Първенство': league,
        'Букмейкър': bookmaker,
        'Акаунт': account,
        'Залог': bet,
        'Сума': amount,
        'Коефициент': odds,
        'Резултат': result
    }
    bets = bets.append(new_bet, ignore_index=True)
    st.success('Залогът е добавен успешно!')

# Визуализация на данни (графики)
st.subheader('Графики на залозите')
fig = px.pie(bets, names='Спорт', values='Сума', title='Разпределение на залозите по спортове')
st.plotly_chart(fig)

# Филтриране на данни по спорт
sport_filter = st.selectbox('Избери спорт за филтриране', bets['Спорт'].unique())
filtered_bets = bets[bets['Спорт'] == sport_filter]
st.write(filtered_bets)

# Записване на данни в CSV
st.subheader('Изтегли данни')
if st.button('Изтегли всички данни'):
    bets.to_csv('bets_data.csv', index=False)
    st.success('Файлът е генериран: bets_data.csv')

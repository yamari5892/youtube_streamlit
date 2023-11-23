import streamlit as st
import time
st.title('stremlit 超入門')

#st.write('Dataframe')
#df = pd.DataFrame(
#   np.random.rand(100, 2)/ [50, 50] + [35.69, 139.70], 
#   columns=['lat', 'lon']
#)
#st.map(df)

st.write('プログレスバーの表示')
'START!!'

latest_iteraction = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteraction.text(f'Iteraction{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'DONE!'
st.write('Display Image')

text = st.sidebar.text_input(
    'あなたの趣味を教えてほしい'
)
'あなたの趣味は', text

condition = st.slider('あなたの調子は?', 0, 100, 50)

'condition', condition
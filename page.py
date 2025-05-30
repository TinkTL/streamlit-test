import streamlit as st
import pandas as pd

st.title("我的个人网站")

with st.sidebar:
    st.image("https://image.lainuoniao.cn/1748326713982919400_0.png",width=200)
    st.text_input("请输入你的名字")
    st.text_area("请输入你的自我介绍")
    st.radio("请选择你的性别",["男","女"])
    st.color_picker("请选择你的颜色")

st.divider()

tab1,tab2,tab3 = st.tabs(["城市","爱好","年龄"])

with tab1:
    st.selectbox("请选择你的城市",["北京","上海","广州","深圳"])

with tab2:
    st.multiselect("请选择你的爱好",["篮球","足球","羽毛球","乒乓球"])

with tab3:
    st.slider("请选择你的年龄",min_value=18,max_value=100,value=20,step=1)

st.divider()

col1,col2,col3 = st.columns([1,1,1])

with col1:
    st.number_input("请输入你的身高",min_value=100,max_value=200,value=170,step=1)

with col2:
    st.date_input("请选择你的生日")

with col3:
    st.time_input("请选择你的出生时间")

st.divider()

with st.expander("展开"):
    st.file_uploader("请上传你的文件",type=["py"])
    st.camera_input("请上传你的照片")

df = pd.DataFrame({
    "学号":["01","02","03"],
    "班级":["1班","2班","3班"],
    "成绩":[95,87,90]
})

st.table(df)

st.dataframe(df)

st.checkbox("我同意以上条款")

st.button("提交")
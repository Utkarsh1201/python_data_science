import streamlit as st 
import plotly.express as px

st.title("My web App")
numbers = st.text_input("Enter multiple number seperated by space")
num_list = list(map(int,numbers.split()))

#line graph
st.area_chart(num_list, use_container_width=True)
# bar chart
st.bar_chart(num_list, use_container_width=True)

x = st.text_input("enter numbers seperated by space for x")
y = st.text_input("enter numbers seperated by space for y")
x_list = list(map(int,x.split()))
y_list = list(map(int,x.split()))
if len(x_list) != len(y_list):
    st.error("Length of x and y must be same")
else:
    st.plotly_chart(px.scatter(x=x_list, y=y_list, title="scatter plot"))
    c1, c2 = st.columns(2)
    c1.plotly_chart(px.histogram(x=x_list, title="histogram x"), use_container_width=True)
    c2.plotly_chart(px.histogram(y=y_list, title="histogram y"), use_container_width=True)
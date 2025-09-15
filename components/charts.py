# components/charts.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def line_chart(data: pd.DataFrame, x: str, y: str, title: str = ""):
    """Render a simple line chart."""
    fig, ax = plt.subplots()
    ax.plot(data[x], data[y], marker="o")
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)

def bar_chart(data: pd.DataFrame, x: str, y: str, title: str = ""):
    """Render a simple bar chart."""
    fig, ax = plt.subplots()
    ax.bar(data[x], data[y])
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)

def scatter_chart(data: pd.DataFrame, x: str, y: str, title: str = ""):
    """Render a scatter plot."""
    fig, ax = plt.subplots()
    ax.scatter(data[x], data[y])
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)

def pie_chart(data: pd.Series, title: str = ""):
    """Render a pie chart from a Series."""
    fig, ax = plt.subplots()
    ax.pie(data.values, labels=data.index, autopct="%1.1f%%")
    ax.set_title(title)
    st.pyplot(fig)

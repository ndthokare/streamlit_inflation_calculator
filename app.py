import streamlit as sl
import pandas as pd

# sl.title("Hello World!")
# sl.subheader("This is a subheader.")
# sl.write("This is normal text.")
# sl.write("**This is bold text.**")
# sl.write("*This is italic text.*")

sl.title("B-LEAP: Simple Calculator")

form = sl.form("calculator_form")
cust_name = form.text_input("Enter your name")
initial_amount = form.number_input("Initial amount",value=10000)
inflation_rate = form.number_input("Annual inflation rate",value=7.0)
years = form.number_input("Number of years",value=10)
submit = form.form_submit_button('Calculate')

def calculate_inflation(initial_amount, inflation_rate, years):
    return initial_amount*(1+inflation_rate/100)**years

if submit:
    sl.write(f"Hello {cust_name}!")
    year_range = range(0,years+1)
    future_values = [calculate_inflation(initial_amount,inflation_rate,yr) for yr in year_range]

    df = pd.DataFrame({
        'Year': year_range,
        'Future Value': future_values
    })
    # print(df)

    # sl.line_chart(df, x='Year', y='Future Value')
    sl.line_chart(df.set_index('Year'))

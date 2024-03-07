import plotly.express as px
from shiny import reactive
from shiny.express import ui, input, render
from shinywidgets import render_plotly

ui.page_opts(title='Tips Dataset')

with ui.sidebar():
    ui.input_checkbox_group('time', 'Time', ['Lunch', 'Dinner'])

@render.text
def df_shape():
    return 'Shape: {} rows x {} cols'.format(*tips_df().shape)

@render_plotly
def scatter():
    return px.scatter(tips_df(), y='tip', x='total_bill', color='time')

@reactive.calc
def tips_df():
    df = px.data.tips()
    print(input.time())
    return df[df.time.isin(input.time())]
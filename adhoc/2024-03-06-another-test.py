from faicons import icon_svg as icon
import plotly.express as px
from shiny.express import input, ui, render
from shinywidgets import render_plotly

ui.page_opts(title='Another Test Dashboard')

ui.hr(class_='my-5')

df = px.data.tips()

with ui.card():
    ui.card_header('Icons and Value Boxes')
    with ui.layout_columns(col_widths=(4, 4, 4)):
        with ui.value_box(showcase=icon('dollar-sign')):
            'Total Sales'
            f'${df.total_bill.sum():,.0f}'
        with ui.value_box(showcase=icon('money-bill-wave')):
            'Total Tips'
            f'${df.tip.sum():,.0f}'
        with ui.value_box(showcase=icon('receipt')):
            'Total Checks'
            f'{df.shape[0]:,.0f}'
        with ui.value_box(showcase=icon('percent')):
            'Tip Percentage'
            f'{df.tip.sum() / df.total_bill.sum():.1%}'
        with ui.value_box(showcase=icon('sack-dollar')):
            'Avg Check'
            f'${df.total_bill.mean():.2f}'
        with ui.value_box(showcase=icon('gratipay')):
            'Avg Tip'
            f'${df.tip.mean():.2f}'

with ui.card():
    ui.card_header('Customize Figure')
    with ui.layout_sidebar():
        with ui.sidebar(open='desktop'):
            ui.input_text('title', 'Title')
            ui.input_text('subtitle', 'Subtitle')
            ui.input_numeric('font_size', 'Font Size', value=10, min=6, max=32, step=1)
            ui.input_switch('show_tip_avg', 'Show Avg Tip', value=False)
            ui.input_switch('show_total_bill_avg', 'Show Avg Bill', value=False)

        @render_plotly
        def plotly_fig():
            df = px.data.tips()
            fig = px.scatter(df, x='total_bill', y='tip')
            if input.show_tip_avg():
                fig.add_hline(df.tip.mean(), line_dash='dash', annotation_text=f'Avg: ${df.tip.mean():.2f}')
            if input.show_total_bill_avg():
                fig.add_vline(df.total_bill.mean(), line_dash='dash', annotation_text=f'Avg: ${df.total_bill.mean():.2f}')
            title = input.title()
            if input.subtitle():
                title += f'<br><sup>{input.subtitle()}</sup>'
            return fig.update_layout(
                title=title,
                font_size=input.font_size()
            )

with ui.card():
    ui.card_header('Card with Sidebar')
    with ui.layout_sidebar():
        with ui.sidebar(open='desktop'):
            ui.input_text('text', 'Write Something:')
        @render.text
        def text_output():
            return "You wrote: " + input.text()

with ui.card():
    ui.card_header('Checkboxes')
    ui.input_checkbox_group('opts', 'Options', list('ABCDE'), inline=True)
    @render.code
    def output():
        return 'Selected: ' + str(input.opts())
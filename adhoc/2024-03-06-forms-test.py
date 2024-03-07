from faicons import icon_svg as icon
from shiny import reactive
from shiny.express import ui, render, input

ui.page_opts(title='Form Demo')
ui.hr()
with ui.layout_columns():
    with ui.card():
        ui.card_header(icon('filter'), 'Type')
        ui.input_select('type', 'Type', list('ABCD'))
    with ui.card():
        ui.card_header(icon('pencil'), 'Your Name')
        ui.input_text('name', 'Full Name')

with ui.tooltip():
    with ui.card():
        ui.card_header('Test title')
        'Card Body'
    'Entire Card Tooltip?'

@reactive.effect
@reactive.event(input.submit)
def on_submit():
    print('Form Submitted!')
    print(f'{input.type()=}')
    print(f'{input.name()=}')
    ui.modal_show(ui.modal(
        ui.p('We are processing your request.'),
        ui.p('You will receive a response in 3-5 business months.'),
        title='Submitted!',
        size='l',
    ))
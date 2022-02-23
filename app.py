from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

from nltk.corpus import words
import re
import nltk 

# set nltk data path
nltk.data.path.append('nltk_data')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Wordle Helper'),
    html.Br(),
    html.P('use the letter positions for letters you know go in that place'),
    html.P('leave a-z if you do not know what letter is in that position'),
    html.P('replace a-z with desired letter'),
    html.Br(),
    html.Div([
    dcc.Textarea(
        id='letter_1',
        value='a-z',
        style={'width': 60, 'height': 40, 'padding-top': 20, 'font-size': 20, 'text-align': 'center', 'margin-right': 20},
    ),
    dcc.Textarea(
        id='letter_2',
        value='a-z',
        style={'width': 60, 'height': 40, 'padding-top': 20, 'font-size': 20, 'text-align': 'center', 'margin-right': 20},
    ),
    dcc.Textarea(
        id='letter_3',
        value='a-z',
        style={'width': 60, 'height': 40, 'padding-top': 20, 'font-size': 20, 'text-align': 'center', 'margin-right': 20},
    ),
    dcc.Textarea(
        id='letter_4',
        value='a-z',
        style={'width': 60, 'height': 40, 'padding-top': 20, 'font-size': 20, 'text-align': 'center', 'margin-right': 20},
    ),
    dcc.Textarea(
        id='letter_5',
        value='a-z',
        style={'width': 60, 'height': 40, 'padding-top': 20, 'font-size': 20, 'text-align': 'center', 'margin-right': 20},
    ),
    
    # Letters not used
    html.P('Letters Not Used', style={'margin-left': 10}),
    dcc.Textarea(
        id='letter_not',
        style={'width': 200, 'height': 40, 'padding-top': 20, 'font-size': 20, 'margin-left': 10},
    ),


    ]),
    # end text box div
    html.Br(),
    html.Button('check words', id='sub_button', n_clicks=0),
    html.Br(),
    html.Br(),
    html.H3('Optional Words'),
    html.Div(id='textarea_output', style={'whiteSpace': 'pre-line', 'overflow': 'scroll', 'width': '60%', 'height': 200}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('check out the source code'),
    html.A('github', href='https://github.com/chadless1/wordle-hlper'),
    html.Footer('CML Labs', style={'text-align': 'center', 'position': 'sticky'})
])

@app.callback(
    Output('textarea_output', 'children'),
    Input('sub_button', 'n_clicks'),
    State('letter_1', 'value'),
    State('letter_2', 'value'),
    State('letter_3', 'value'),
    State('letter_4', 'value'),
    State('letter_5', 'value'),
    State('letter_not', 'value'),
)

# update and display 
def update_output(n_clicks, letter_1, letter_2, letter_3, letter_4, letter_5, letter_not):
    
    if n_clicks > 0:

        # check for blanks
        ll = [letter_1, letter_2, letter_3, letter_4, letter_5]

        # word dictionary and regex
        word_list = words.words()

        # regex 
        r = re.compile('[{}][{}][{}][{}][{}]'.format(ll[0], ll[1], ll[2], ll[3], ll[4]))
        
        # filtered list 
        filtered_list = list(filter(r.match, word_list))
        
        # new list of 5 letter words
        new_list = []
        for i in filtered_list:
            if len(i) == 5:
                new_list.append(i)

        # not used list
        not_used_words = []
        
        for w in new_list:
            if not letter_not:
                pass
            else:
                for l in letter_not:
                    if l in w:
                        not_used_words.append(w)
    
        # remove words with not used letters
        for nuw in not_used_words:
            if nuw in new_list:
                new_list.remove(nuw)

        # display output
        return html.Ul([html.Li(x) for x in new_list], style={'columns': 2, 'column-count': 2})


app.config.suppress_callback_exceptions=True
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)

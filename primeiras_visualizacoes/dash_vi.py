import numpy as np
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from jupyter_dash import JupyterDash
import plotly.graph_objs as go


paises = pd.read_csv('/home/rafael/git/advanced_visualization/primeiros_testes/dados_paises.csv')


fig = go.Figure(data=go.Choropleth(locations=paises['Country Code'],
                                    z = np.log10(paises['1995'].loc[paises['Series Name']=='inflation']),
                                    hoverinfo = 'text',
                                    text= paises['1995'].loc[paises['Series Name']=='inflation'],
                                    colorscale='Reds',
                                    colorbar=dict(
                                        title='Inflação',
                                        dtick = [200, 400, 600, 800],
                                        xanchor = 'center'
                                    ),
                                    ))

fig.update_geos(
    visible=False, resolution=50, scope="europe",
    showcountries=True, countrycolor="Black"
)
fig.update_layout(
    title = "Inflação na Europa em 1995",
    #margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

fig1 = go.Figure(data=go.Choropleth(locations=paises['Country Code'],
                                    z = np.log10(paises['1995'].loc[paises['Series Name']=='life_expectancy']),
                                    hoverinfo = 'text',
                                    text= paises['1995'].loc[paises['Series Name']=='life_expectancy'],
                                    colorscale='Reds',
                                    colorbar=dict(
                                        title='Inflação',
                                        dtick = [200, 400, 600, 800],
                                        xanchor = 'center'
                                    ),
                                    
                                    ))

fig1.update_geos(
    visible=False, resolution=50, scope="europe",
    showcountries=True, countrycolor="Black"
)
fig1.update_layout(
    title = "Expectativa de Vida na Europa em 1995"
    #margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )


app = Dash()
app.layout = html.Div(
    [
    html.H1('Teste'),
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig1)
    ]
)

app.run_server(debug=True, port = 8049)
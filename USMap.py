import json
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

token = 'pk.eyJ1IjoiaGVpc2hhbm1hbyIsImEiOiJjazlveWkwdnowNHB1M2VuNzJ2dmp5c250In0.kk_ErS2msH2HPAhXOl2i8Q'

with open('.\gz_2010_us_040_00_20m.json') as response:
    geo = json.load(response)

df = pd.read_csv('.\Production_state_2018.csv', encoding= 'unicode_escape')

fig = go.Figure(go.Choropleth(
    locations = df.short_name,
    z = df.production,
    locationmode = 'USA-states',
    colorscale = 'mint',
    text = df.state, #hover text!!!
    marker_line_color = 'white',
    marker_line_width = 5
))

fig.update_layout(
    title_text = 'State',
    geo_scope='usa',
)

fig.show()
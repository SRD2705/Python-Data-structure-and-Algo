##################################  Live location of ISS(International Space Station) ########################
'''
In this python program we plot the live location of the ISS using an API
Detail explanation in in the program
'''

import pandas as pd
# import panda for data exploration and customization
import plotly.express as px
# import plotly for plotting in a map
url = 'http://api.open-notify.org/iss-now.json'
# We use this API for get the live location of the ISS
df = pd.read_json(url)
# print(df)
df['latitude'] = df.loc['latitude','iss_position']            # Making different data row
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace=True)
df = df.drop(['index','message'], axis = 1)   # We drop those which we do not need to plot
# print(df)
fig = px.scatter_geo(df,lat='latitude',lon='longitude')  # Plotting the location in the map
fig.show() #Showing the map
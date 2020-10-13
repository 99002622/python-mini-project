import folium
import pandas as pd
corona_df = pd.read_csv('covid-19.csv')
print(corona_df)
corona_df=corona_df.dropna()
print(corona_df)
m=folium.Map(location=[34.223334,-82.461707],
            tiles='Stamen toner',
            zoom_start=8)

def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2])*10,
                 color="red",
                 popup='{}\n confirmed cases:{}'.format(x[3],x[2])).add_to(m)
corona_df[['Lat','Long_','Confirmed']].apply(lambda x:circle_maker(x),axis=1)

html_map=m._repr_html_()
############# Projet-DSIA-2019/2020  ############# 


############ INTRODUCTION ############# 

# La mortalité enfantile (< 5 ans) a été étudiée dans ce projet.
# Dans un premier temps,nous avons visualiser le taux de mortalité en fonction des différents continents sous forme d'Histogramme et carte.
# Par la suite, nous allons étudier 2 causes de déces pour 50 pays sur 4 années.

        
        # 1 -  La mortalité enfantile par continent


# La première base de données traitée est issue du site de l'UNICEF. Nous avons télécharger le document lié à la Table 2 - Child mortality
# Lien internet: ('https://data.unicef.org/resources/dataset/sowc-2019-statistical-tables/')
# Document d'origine ': "Table-2-Child-Mortality-EN.xlsx"
# Seulement une partie des données a été utilisée pour réaliser l'Histogramme et la carte géographique.
# La nouvelle base de données se trouve dans le fichier "ContinentChildMortality.xlsx"
# La variable analysée est "Under-5 mortality rate deaths per 1,000 live births" pour l'année 2018.
# Cette variable corespond au nombre d'enfants décédés avant l'age de 5 ans sur un échantillon de 1000 enfants.

                # A- Histogramme
import pandas as pd
import plotly.express as plt
unicef = pd.read_excel("/Users/admin/Documents/Python/ProjetPython/ContinentChildMortality.xlsx")

fig_mortality = plt.histogram(unicef, x="Continent",y="Number", color="Continent",histfunc='avg')
fig_mortality .show()
# Observations: Il y a un taux de mortalité enfantile élevé dans le continent africain mais également dans l'Asie du sud. Ces zones correspondent aux pays du Tiers Monde             # Le taux de mortalité le plus faible est dans l'Europe de l'Ouest et l'Amérique du nord, ce qui correspond aux pays développés.

                # B- Histogramme
import folium
import branca

coords = (48.8398094,2.5840685) # Cela permet de centraliser la carte.

map = folium.Map(location=coords, zoom_start = 3)

# L'importation de donnée se fait manuellement car les continents à visualiser ne sont pas nombreux.
# Nous avons choisi des coordonées centrées pour chaque continent.
# Dans l'interprétation des données, il faut donc prendre en compte  l'appartenance a un continent et non l'espace délimité par le cercle.

CONTINENT = ['East Asia and Pacific', 'Europe and Central Asia', 'Latin America and Caribbean', 'Middle East and North Africa', 'North America'
            'South Asia', 'Sub-Saharan Africa']

LATS = [4.5352769, 49.725948, 4.624335, 26.8357675, 39.114053, 19.07283, -11.202692]

LONGS = [114.7276688, 5.982458, -74.063644, 30.7956597, -94.6274636, 72.88261, 17.873887]

MORTALITY = [57, 31, 55, 65, 11, 130, 180]

# Définition d'une bar de couleur (colorbar)
cm = branca.colormap.LinearColormap(['blue','yellow','red'],vmin=min(MORTALITY), vmax=max(MORTALITY))
map.add_child(cm) # ajouter la colorbar à l'affichage
print(cm.colors)

f = folium.map.FeatureGroup() # création d'un groupe

for lat,lng,size, color in zip(LATS,LONGS,MORTALITY,MORTALITY):
    print(lat,lng,size,color)
    f.add_child(
        folium.CircleMarker(
            location=[lat,lng],
            radius = size*1,
            color = None,
            fill=True,
            fill_color=cm(color),
            fill_opacity=0.6
        )
    )

map.add_child(f)

map.save(outfile='map3.html')


# Observation: L'analyse de la carte est plus approximative que l'Histogramme.


        # 2 -  Analyse de données

# Les continents où il y a un plus plus fort taux de  mortalité enfantile sont fortement touchés par les 2 maladies étudiées: le Paludisme et l'infection par le VIH.
# On s'est basé sur des données filtrées, issues du site de World Health Organization.
# Lien: http://apps.who.int/gho/data/node.main.ChildMortCTRY1002015?lang=en 
# Nous avons représenté le nombre de décès en 2000, 2005, 2010 et 2017 pour une cinquantaine de pays.
# La tranche d'âge choisis est de 0 à 4 ans.
# Les données se trouvent dans le document "ChildDeath.xlsx".

import pandas as pd
import plotly.express as plt

#Importation des données en utilisant Panda Frame
who = pd.read_excel("/Users/admin/Documents/Python/ProjetPython/ChildDeath.xlsx")

# Graphique : Nombre d'enfants (0-4 à ans) mort de la malaria par pays.
fig_malaria = plt.histogram(who, x="Country",y="Malaria", color="Year", histfunc='avg')
fig_malaria .show()
# Observations: Les régions d'Afrique Centrale et de l'Ouest sont largement concernées par la malaria. 
# Parmi les pays analysés, le Nigéria et le Congo sont les plus touchés.

# Graphique : Nombre d'enfants (0-4 à ans) mort de l'infection par le VIH par pays.
fig_hiv = plt.histogram(who, x="Country",y="HIV", color="Year", histfunc='avg')
fig_hiv.show()
# Observation: L'Afrique centrale, du Sud et l'Inde était très touchés par l'infectio, au VIH en 2000. 
# Au cours du temps la mortalité due à l'infection du VIH a fortement diminué pour l'ensebmle de ces pays. 
# Cette diminution été moindre en Nigéria, comparée aux autres pays.

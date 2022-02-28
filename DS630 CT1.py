#!/usr/bin/env python
# coding: utf-8

# # Critical Thinking 1
# 
# <br>
# Course Code: DS630 <br>
# Course Name: Artificial Intelligence for Data Science <br>
# CRN: 24543
# 
# Student ID: G200007615 <br>
# Student Name: Abdulaziz Alqumayzi
# 
# #### Requirements 
# - Colab or Jupyter notebook to run the code.
# - networkx, matplotlib, and datetime packages

# In[3]:


# networkx package was installed to draw the map and then finding the shortest path from my city Riyadh to other cities. 
# pip install networkx


# In[1]:


# import packages needed for this task
import networkx as nx
import matplotlib.pyplot as plt
import datetime as dt

# create an empty graph structure. land_G stand for land travel time. air_G (will be shown later) stand for air travel time.
land_G = nx.Graph()

''' add_edge method can build nodes, edges and weights in the same code. 
    This method build an edge and assign two nodes to that edge. 
    Weight is an optional parameter, you can change w to any text you want. For example, tt an abbreviation to travel time.
    w stands for weight, and the number indicates the travel time between nodes in hours and the minutes after the point.
'''

land_G.add_edge('Dammam','Riyadh', w= 4.43)
land_G.add_edge('Riyadh','Makkah',w= 11.28)
land_G.add_edge('Makkah','Jeddah', w = 1.01)
land_G.add_edge('Jeddah','Madinah',w= 4.38)
land_G.add_edge('Al Bahah','Abha', w= 1)
land_G.add_edge('Abha','Najran', w=5.08)
land_G.add_edge('Hayil', 'Buraydah', w= 3.09)
land_G.add_edge('Buraydah','Riyadh', w= 4.10)
land_G.add_edge('Tabuk', 'Sakaka', w=5.36)
land_G.add_edge('Sakaka' , 'Al Ar Ar', w=1.58)
land_G.add_edge('Sakaka' , 'Hayil', w= 4.55)
land_G.add_edge('Hayil' , 'Madinah',w= 6.27)
land_G.add_edge('Makkah' , 'Jizan', w= 8.44)
land_G.add_edge('Jeddah' ,'Jizan', w= 8.34)
land_G.add_edge('Jizan', 'Najran', w= 7.25)
land_G.add_edge('Dammam','Al Ar Ar', w= 11.53)
land_G.add_edge('Jizan','Abha',w= 2.24)
land_G.add_edge('Hayil','Riyadh',w= 7.16)
land_G.add_edge('Dammam','Hafoof', w= 1.47)
land_G.add_edge('Hafoof' ,'Riyadh', w= 3.49)
land_G.add_edge('Jeddah' ,'Yanbu', w= 3.41)
land_G.add_edge('Madinah' ,'Yanbu', w= 2.47)

# pos refer to the position of latitude and longitude. The dictionary is one of the ways that the method reads the locations. 
# note that: the first number is longitude and the second is latitude. That's how the method draw reads the positions.   
pos= {'Riyadh':(46.72185, 24.68773), 'Dammam':(50.10326, 26.43442), 'Makkah':(39.82563, 21.42664),
      'Jeddah':(39.19797, 21.54238 ),'Madinah':(39.61417, 24.46861), 'Al Bahah':(41.46767, 20.01288),
      'Abha':(42.50528, 18.21639),'Najran':(44.12766, 17.49326), 'Hayil':(41.690731, 27.521879),
      'Buraydah':(43.97497, 26.32599), 'Tabuk':(36.57151, 28.3998), 'Sakaka':(40.20641, 29.96974),
      'Al Ar Ar':(41.03808, 30.97531), 'Jizan':(42.55111, 16.88917), 'Hafoof':(49.56532, 25.36457),
      'Yanbu':(38.0618, 24.08954)}

# I made a big figure using figure() method from matplotlib and title() method for the figure
# draw method used to draw the nodes using land_G and pos. 
# here to draw the lables of the edges using also lang_G and pos. 
plt.figure(figsize=(15,12))
plt.title('The land map shows weighted edges for travel time spend between nodes',fontsize=18);
nx.draw(land_G,pos, with_labels=True, node_size=3500,alpha=0.8, node_color='g')
nx.draw_networkx_edge_labels(land_G,pos, edge_labels=nx.get_edge_attributes(land_G,'w'));

''' now printing the path length and which cities to take from the destination of my city to other cities
    using dijkstra_path_length and dijkstra_path functions. 
    The first function (dijkstra_path_length) returns the shortest weighted path length in land_G from source to target. 
    And show the travel time takes from my city Riyadh to reach the destination city. 
    The second function (dijkstra_path) returns the shortest weighted path from source to target in land_G.
    And show the name of cities takes to reach the destination including the destination city.
    timedelta function used to convert weights from integers to time.
''' 
print('The travel time from  Riyadh to Dammam is',
      dt.timedelta(hours= nx.dijkstra_path_length(land_G, 'Riyadh','Dammam', weight='w')),'hours')
print('The shortest way from the cities to reach Dammam is',nx.dijkstra_path(land_G, 'Riyadh','Dammam'),'\n')
print('The travel time from  Riyadh to Makkah is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Makkah', weight='w')),'hours')
print('The shortest way from the cities to reach Makkah is',nx.dijkstra_path(land_G, 'Riyadh','Makkah'),'\n')
print('The travel time from  Riyadh to Jeddah is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Jeddah',weight='w')),'hours')
print('The shortest way from the cities to reach Jeddah is',nx.dijkstra_path(land_G, 'Riyadh','Jeddah'),'\n')
print('The travel time from  Riyadh to Madinah is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Madinah', weight='w')),'hours')
print('The shortest way from the cities to reach Madinah is',nx.dijkstra_path(land_G, 'Riyadh','Madinah'),'\n')
print('The travel time from  Riyadh to Al Bahah is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Al Bahah', weight='w')),'hours')
print('The shortest way from the cities to reach Al Bahah is',nx.dijkstra_path(land_G, 'Riyadh','Al Bahah'),'\n')
print('The travel time from  Riyadh to Abha is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Abha', weight='w')),'hours')
print('The shortest way from the cities to reach Abha is',nx.dijkstra_path(land_G, 'Riyadh','Abha'),'\n')
print('The travel time from  Riyadh to Najran is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Najran', weight='w')),'hours')
print('The shortest way from the cities to reach Najran is',nx.dijkstra_path(land_G, 'Riyadh','Najran'),'\n')
print('The travel time from  Riyadh to Hayil is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Hayil', weight='w')),'hours')
print('The shortest way from the cities to reach Hayil is',nx.dijkstra_path(land_G, 'Riyadh','Hayil'),'\n')
print('The travel time from  Riyadh to Buraydah is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Buraydah', weight='w')),'hours')
print('The shortest way from the cities to reach Buraydah is',nx.dijkstra_path(land_G, 'Riyadh','Buraydah'),'\n')
print('The travel time from  Riyadh to Tabuk is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Tabuk', weight='w')),'hours')
print('The shortest way from the cities to reach Tabuk is',nx.dijkstra_path(land_G, 'Riyadh','Tabuk'),'\n')
print('The travel time from  Riyadh to Sakaka is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Sakaka', weight='w')),'hours')
print('The shortest way from the cities to reach Sakaka is',nx.dijkstra_path(land_G, 'Riyadh','Sakaka'),'\n')
print('The travel time from  Riyadh to Al Ar Ar is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Al Ar Ar', weight='w')),'hours')
print('The shortest way from the cities to reach Al Ar Ar is',nx.dijkstra_path(land_G, 'Riyadh','Al Ar Ar'),'\n')
print('The travel time from  Riyadh to Jizan is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Jizan', weight='w')),'hours')
print('The shortest way from the cities to reach Jizan is',nx.dijkstra_path(land_G, 'Riyadh','Jizan'),'\n')
print('The travel time from  Riyadh to Hafoof is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Hafoof', weight='w')),'hours')
print('The shortest way from the cities to reach Hafoof is',nx.dijkstra_path(land_G, 'Riyadh','Hafoof'),'\n')
print('The travel time from  Riyadh to Yanbu is',
      dt.timedelta(hours=nx.dijkstra_path_length(land_G, 'Riyadh','Yanbu', weight='w')),'hours')
print('The shortest way from the cities to reach Yanbu is',nx.dijkstra_path(land_G, 'Riyadh','Yanbu'),'\n')
plt.show()


# In[2]:


# Next, constructing the map of air travel time
# note:let's pretend that all cities have airports for simplicity. Because most of the cities don't have an airport. 
# same code but different weight, weight refers to the travel time in air  
air_G = nx.Graph()
air_G.add_edge('Dammam','Riyadh', w= 0.57)
air_G.add_edge('Riyadh','Makkah',w= 1.33)
air_G.add_edge('Makkah','Jeddah', w = 0.33)
air_G.add_edge('Jeddah','Madinah',w= 0.53)
air_G.add_edge('Al Bahah','Abha', w= 0.43)
air_G.add_edge('Abha','Najran', w= 0.41)
air_G.add_edge('Hayil', 'Buraydah', w= 0.46)
air_G.add_edge('Buraydah','Riyadh', w= 0.52)
air_G.add_edge('Tabuk', 'Sakaka', w= 0.57)
air_G.add_edge('Sakaka' , 'Al Ar Ar', w= 0.33)
air_G.add_edge('Sakaka' , 'Hayil', w= 0.51)
air_G.add_edge('Hayil' , 'Madinah',w= 0.58)
air_G.add_edge('Makkah' , 'Jizan', w= 1.14)
air_G.add_edge('Jeddah' ,'Jizan', w= 1.18)
air_G.add_edge('Jizan', 'Najran', w= 0.40)
air_G.add_edge('Dammam','Al Ar Ar', w= 1.36)
air_G.add_edge('Jizan','Abha',w= 0.37)
air_G.add_edge('Hayil','Riyadh',w= 1.15)
air_G.add_edge('Dammam','Hafoof', w= 0.34)
air_G.add_edge('Hafoof' ,'Riyadh', w= 0.50)
air_G.add_edge('Jeddah' ,'Yanbu', w= 0.50)
air_G.add_edge('Madinah' ,'Yanbu', w= 0.37)
plt.figure(figsize=(15,12))
plt.title('The air map shows weighted edges for travel time spend between nodes',fontsize=18)
nx.draw(air_G,pos, with_labels=True, node_size=3500,alpha=0.8, node_color='r')
nx.draw_networkx_edge_labels(air_G,pos, edge_labels=nx.get_edge_attributes(air_G,'w'));

print('The travel time from  Riyadh to Dammam is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Dammam', weight='w')),'minutes')
print('The shortest way from the cities to reach Dammam is',nx.dijkstra_path(air_G, 'Riyadh','Dammam'),'\n')
print('The travel time from  Riyadh to Makkah is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Makkah', weight='w')),'hours')
print('The shortest way from the cities to reach Makkah is',nx.dijkstra_path(air_G, 'Riyadh','Makkah'),'\n')
print('The travel time from  Riyadh to Jeddah is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Jeddah',weight='w')),'hours')
print('The shortest way from the cities to reach Jeddah is',nx.dijkstra_path(air_G, 'Riyadh','Jeddah'),'\n')
print('The travel time from  Riyadh to Madinah is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Madinah', weight='w')),'hours')
print('The shortest way from the cities to reach Madinah is',nx.dijkstra_path(air_G, 'Riyadh','Madinah'),'\n')
print('The travel time from  Riyadh to Al Bahah is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Al Bahah', weight='w')),'hours')
print('The shortest way from the cities to reach Al Bahah is',nx.dijkstra_path(air_G, 'Riyadh','Al Bahah'),'\n')
print('The travel time from  Riyadh to Abha is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Abha', weight='w')),'hours')
print('The shortest way from the cities to reach Abha is',nx.dijkstra_path(air_G, 'Riyadh','Abha'),'\n')
print('The travel time from  Riyadh to Najran is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Najran', weight='w')),'hours')
print('The shortest way from the cities to reach Najran is',nx.dijkstra_path(air_G, 'Riyadh','Najran'),'\n')
print('The travel time from  Riyadh to Hayil is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Hayil', weight='w')),'minutes')
print('The shortest way from the cities to reach Hayil is',nx.dijkstra_path(air_G, 'Riyadh','Hayil'),'\n')
print('The travel time from  Riyadh to Buraydah is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Buraydah', weight='w')),'minutes')
print('The shortest way from the cities to reach Buraydah is',nx.dijkstra_path(air_G, 'Riyadh','Buraydah'),'\n')
print('The travel time from  Riyadh to Tabuk is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Tabuk', weight='w')),'hours')
print('The shortest way from the cities to reach Tabuk is',nx.dijkstra_path(air_G, 'Riyadh','Tabuk'),'\n')
print('The travel time from  Riyadh to Sakaka is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Sakaka', weight='w')),'hours')
print('The shortest way from the cities to reach Sakaka is',nx.dijkstra_path(air_G, 'Riyadh','Sakaka'),'\n')
print('The travel time from  Riyadh to Al Ar Ar is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Al Ar Ar', weight='w')),'hours')
print('The shortest way from the cities to reach Al Ar Ar is',nx.dijkstra_path(air_G, 'Riyadh','Al Ar Ar'),'\n')
print('The travel time from  Riyadh to Jizan is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Jizan', weight='w')),'hours')
print('The shortest way from the cities to reach Jizan is',nx.dijkstra_path(air_G, 'Riyadh','Jizan'),'\n')
print('The travel time from  Riyadh to Hafoof is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Hafoof', weight='w')),'minutes')
print('The shortest way from the cities to reach Hafoof is',nx.dijkstra_path(air_G, 'Riyadh','Hafoof'),'\n')
print('The travel time from  Riyadh to Yanbu is',
      dt.timedelta(hours=nx.dijkstra_path_length(air_G, 'Riyadh','Yanbu', weight='w')),'hours')
print('The shortest way from the cities to reach Yanbu is',nx.dijkstra_path(air_G, 'Riyadh','Yanbu'),'\n')
plt.show()


# #### References: 
# - Distance and time calculator between cities for land travels, latitudes and longitudes locations of cities. [distance.to](https://www.distance.to/)
# - Shortest path algorithms. [networkx.org](https://networkx.org/documentation/stable//reference/algorithms/shortest_paths.html)
# - Distance and time calculator between cities for air travels. [flighttime-calculator.com](https://flighttime-calculator.com/)
# - How to create nodes, edges and postions. [datascience.stackexchange.com](https://datascience.stackexchange.com/questions/61248/create-nodes-edges-from-csv-latitude-and-longitude-for-graphs)
# - How to convert integer to time. [docs.python.org](https://docs.python.org/3/library/datetime.html)

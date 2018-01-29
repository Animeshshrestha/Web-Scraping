import csv
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('details.csv',delimiter = ',')
data1 = pd.DataFrame(data)
data1.set_index("Name",inplace = True) # instead of 0,1 it gives film name
#print(data1)

# Most Popular
popular = data1[0:11]
a = popular[['Seeders','Leechers']].plot(kind = 'bar')
plt.title("Seeders VS Leechers of Most popular Torrent")
plt.xlabel("Name of movie")
plt.ylabel("No of seeders and Leechers")
plt.show()

#Popular Movie
popular = data1[24:35]
b = popular[['Seeders','Leechers']].plot(kind = 'bar')
plt.title("Seeders VS Leechers of popular movies")
plt.xlabel("Name of movie")
plt.ylabel("No of seeders and Leechers")
plt.show()

#Popular Tv torrent
popular = data1[46:57]
c = popular[['Seeders','Leechers']].plot(kind = 'bar')
plt.title("Seeders VS Leechers of Popular TV Torrent")
plt.xlabel("Name of movie")
plt.ylabel("No of seeders and Leechers")
plt.show()

#Popular Application Torrent
popular = data1[70:81]
d = popular[['Seeders','Leechers']].plot(kind = 'bar')
plt.title("Seeders VS Leechers of Popular Application")
plt.xlabel("Name of movie")
plt.ylabel("No of seeders and Leechers")
plt.show()

#Popular Game torrent
popular = data1[82:93]
e = popular[['Seeders','Leechers']].plot(kind = 'bar')
plt.title("Seeders VS Leechers of Popular Game Torrent")
plt.xlabel("Name of movie")
plt.ylabel("No of seeders and Leechers")
plt.show()


#Overall Seeders vs Leechers
a = data[['Seeders','Leechers']].plot(kind = 'bar')
plt.title("Seeders VS Leechers of Overall Torrents")
plt.xlabel("Name of movie")
plt.ylabel("No of seeders and Leechers")
plt.show()
     

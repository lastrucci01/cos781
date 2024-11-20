import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

deep = "#304674"
blue = "#006f9e"
sea = "#0099ae"
turq = "#00c0a1"
green = "#88e184"
yellow = "#f9f871"
plt.rcParams['font.family'] =  'monospace'
plt.rcParams['font.size'] = 10 


def plot_large_heatmap(utility_matrix):
    plt.figure(figsize=(30, 18))  
    colors = [deep,sea,yellow]
    cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)
    sns.heatmap(
        utility_matrix, 
        annot=False,  
        cmap=cmap, 
        cbar_kws={'label': 'Value'}, 
        xticklabels=False, 
        yticklabels=False 
    )
    plt.show()

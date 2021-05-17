# Import packages
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from wordcloud import WordCloud# Generate word cloud
from nltk.corpus import stopwords

text = []

# Set Stopwords in spanish
nltk.download('stopwords')
stop_words_sp = set(stopwords.words('spanish'))


# Define a function to plot word cloud

def plot_cloud(wordcloud):
    # Set figure size
    fig = plt.figure(figsize=(40, 30))

    # Display image
    plt.imshow(wordcloud) 

    # No axis details
    plt.axis("off");

    # Save image
    fig.savefig('salida.png', dpi=fig.dpi)


# Read CSV
df = pd.read_csv(r"constituyentes_general.csv", encoding ="utf-8") 

# Iterate through the csv file
for val in df.texto: 
    
    # typecast each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split()  

    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
    text += " ".join(tokens)+" "

# Join words into one text
text = str(''.join(text))

# Clean some 'artifact-strings'
text = text.replace('xa0','')
text = text.replace("n'",'')

# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white', collocations=False, stopwords = stop_words_sp).generate(text)

# Plot
plot_cloud(wordcloud)
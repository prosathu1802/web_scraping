from bs4 import BeautifulSoup
import urllib.request

from wordcloud import WordCloud

import matplotlib.pyplot as plt

r = urllib.request.urlopen('https://www.lyrics.com/lyric/32168635/Charlie+Puth/One+Call+Away')
soup = BeautifulSoup(r.read(),'html.parser')
lyrics = soup.findAll("pre", {"id": "lyric-body-text"})[0].text
print(lyrics)

wordcloud = WordCloud().generate(lyrics)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(lyrics)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

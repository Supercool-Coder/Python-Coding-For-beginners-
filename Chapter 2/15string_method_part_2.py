# replace () method
# find () method

article = "What word is that to which if you add a syllable, it will make it shorter"
print(article.replace(" ","_"))
print(article.find("make"))

a_pos1 = article.find("it")
a_pos2 = article.find("it", a_pos1+1)
print(a_pos2)
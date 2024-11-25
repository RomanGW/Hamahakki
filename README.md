# Lukki
Lukki is the Finnish word for "harvestman", referring to a daddy long leg. Lukki is a webcrawling bot I made as a part of a separate project.

Requirements:
  - bs4
  - urllib
  - requests

In an effort to support my Finnish learning endeavors, I am in the process of developing a tool that reads Finnish news articles, tokenizes the words, and compiles lesson plans using *REAL* Finnish, rather than nonsense through things like Duolingo. In order to do the whole "reading news articles" thing, I had to develop something that pulls that text data as I am too lazy to pull it all manually. Plus, it pads out my portfolio and shows that I know about web scraping.

# How to use:

Lukki works by iterating through all websites entered in the 'source_list.txt' file that is included in the repository, it pulls the HTML data similarly to other web scraping tools. By adding websites to 'source_list.txt', you are adding additional websites (and by extension sub-websites) to be scraped. As it stands, when ran, it will only return a list of websites found from the websites entered in 'source_list.txt', however, if you want to modify the code, there is a spot within iterate_sources() that is saved to call additional functions. 
Of importance is the "depth_max" variable local to main(). It determines the "depth" of recursion that Lukki will scrape, finding an exponentially larger amount of websites for each website in 'source_list.txt'. It isn't hard to tell that increasing this will make it run longer, and it is currently set to '2' for everyone's safety. 

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import requests

def open_source_list():
    # Iterate through all websites in source file.
    try:
        with open("source_list.txt", "r") as file:
            file_content = file.read()
            return file_content.split("\n")
    except Exception as e:
        print(f"Error. Please make sure 'source_list.txt' is in the active directory. Error message: {e}. \nPlease notify me on Github!")
        return []

def find_new_sources(depth_max):
    links = []
    for source in open_source_list():
        links = iterate_sources(source, links, depth_max)
    return links

def iterate_sources(source, links, depth_max, visited = set(), depth = 0):
    # Iterate through sources up to a maximum depth
    if depth < depth_max:
        if source not in visited:
            try:
                visited.add(source)
                # Open page content.
                soup = get_soup(source)

                # -- ADD LOGIC HERE IF YOU WANT TO SCRAPE ADDITIONAL DATA OR MANIPULATE PAGE DATA. --
                # If not, this recursive function will just return a list of visited websites.

                # Pull new sources from page.
                new_sources = get_sources_from_page(source, soup)
                add_new_sources(new_sources, links)

                # Use recursion to return any new websites.
                for new_source in new_sources:
                    iterate_sources(new_source, links, depth_max, visited, depth + 1)
            except Exception as e: 
                # Catch-all for any errors.
                print(f"Error. Error message: {e}. \nPlease notify me on Github!")
    else:
        return visited, links

def add_new_sources(sources, links):
    # Iterate through sources provided, if that source is not currently in links, append to links.
    for source in sources:
        if source not in links:
            print(f"Link found: {source}")
            links.append(source)
    return links

def get_sources_from_page(source, soup):
    adj_links = []
    # Find all "href" tags in HTML on page.
    for div in soup.find_all("a", href = True):
        href = div["href"]
        full_url = urljoin(source, href)
        # IF YOU WANT ONLY LINKS THAT LEAD TO PLACES WITHIN THE SAME WEBSITE.
        if urlparse(source).netloc in urlparse(full_url).netloc:
            adj_links.append(full_url)
        # IF YOU WANT LINKS THAT CAN LEAD YOU AWAY FROM THE HOME WEBSITE.
        #adj_links.append(full_url)
    return adj_links

def get_soup(source):
    # Get content from website in div.
    response = requests.get(source)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def main():
    depth_max = 1
    links = find_new_sources(depth_max)
    print(links)

if __name__ == "__main__":
    main()
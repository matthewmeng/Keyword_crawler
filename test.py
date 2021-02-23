import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re   

ua = UserAgent()

lists = ["mortgage","homeloan","mortgage broker","Loan Calculator","Property Report","Car Loan","Home Solar"]
f = open('result.txt', 'w')
for keyword in lists:
    

    google_url = "https://www.google.com/search?q=" + keyword + "&num=20"
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")

    result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})

    links = []
    titles = []
    descriptions = []
    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href = True)
            print(link)
            title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
            description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
            
            # Check to make sure everything is present before appending
            if link != '': 
                url=links.append(link['href'])
                # print(url)
                titles.append(title)
                descriptions.append(description)
        # Next loop if one element is not present
        except:
            continue

    to_remove = []
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa',l)

        # Anything that doesn't fit the above pattern will be removed
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))

    # Remove the corresponding titles & descriptions
    for x in to_remove:
        del titles[x]
        del descriptions[x]
    
    # with open('%i.txt','w') as filehandle:
    #         for list in clean_links:
    #             filehandle.write('%s\n' % list)

    # f = open('%s.txt' % keyword, 'w')
    # for item in clean_links:
    #     f.write("%s\n" % item)
    
    for item in clean_links:
        f.write("%s\n" % item)
    
    print(clean_links)
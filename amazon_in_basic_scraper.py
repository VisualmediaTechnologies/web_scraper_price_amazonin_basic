import requests , bs4 ,os ,easygui

index =1 
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

#Get User input of file
filepath = easygui.enterbox('Where is the file stored ? Provide the full path.')

#correct the file extension in casse of not entered
if not filepath.endswith('.txt'):
    filepath = filepath+'.txt'

def getAmazoninPrice(url):
    #get the html page
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    #beautifulsoup part - search for price class
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elem = soup.select('#priceblock_ourprice')
    return(elem[0].text.strip())

#read the whole content first
with open(os.path.expanduser(filepath),mode='r+',encoding='utf-8') as f :
    contents = f.readlines()
    f.close()

#Now search for each individual line
with open(os.path.expanduser(filepath),mode='r+',encoding='utf-8') as fp:
    line = fp.readline()
    while line:
        price_link = getAmazoninPrice(line)
        contents.insert(index,price_link+'\n')
        line = fp.readline()
        index += 2
    fp.close()
    
#Save the file
dir_name =os.path.dirname(filepath)
output_file_path =os.path.join(dir_name , 'Price_Output'+'.txt')
with open(os.path.expanduser(output_file_path), "w",encoding='utf-8') as f:
    contents = "".join(contents)
    f.write(contents)
    f.close()


from bs4 import BeautifulSoup
import requests, openpyxl

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
URL='https://www.imdb.com/chart/top/?ref_=nv_mv_250'

excel=openpyxl.Workbook()
print(excel.sheetnames)
sheet=excel.active
sheet.title='Top Rated Movies'
print(excel.sheetnames)
sheet.append(['Movie Rank','Movie Name', 'Year Of Release', 'IMDB Rating'])
try:
    source=requests.get(URL,headers=headers)
    source.raise_for_status()

    soup=BeautifulSoup(source.text,'html.parser')

    movies=soup.find('tbody',class_='lister-list').find_all('tr')

    for movie in movies:
        name=movie.find('td',class_='titleColumn').a.text

        rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
        
        year=movie.find('td',class_='titleColumn').span.text.strip('()')
        
        rating=movie.find('td',class_='ratingColumn imdbRating').strong.text
 
        sheet.append([rank,name,year,rating])

        
except Exception as e:
    print(e)

excel.save('IMDB Movie Ratings.xlsx')


from gtts import gTTS
import os
import requests
from dotenv import load_dotenv
lang='en'

load_dotenv()
API_KEY=os.getenv("API_KEY")

def speech(mytext,language):
    myobj = gTTS(text=mytext, lang=language, slow=False)
    file='newsapi.mp3'
    myobj.save(file)
    os.system(f"mpg321 -q {file}")
    os.remove(file)

def gen():
    i=1
    while True:
        yield i
        i=i+1

def dis(choice):
        print(2*"\n")
        title=f"Please wait while we are fetching the latest {choice} news from the A.P.I"
        print(title.center(170))
        print("\n")
        # speech(title,lang)
        return


def cat(api_key):
    print("\n::Categories::\n") 
    catlist=['Business', 'Entertainment', 'Health', 'Nation', 'Science', 'Sports', 'Technology', 'Times of India']
    genz1=gen()
    for item in catlist:
        print(f'{next(genz1)}. {item}')
    genz1.close()
    while True:
        inn=input("\nEnter your choice: ")
        match inn:
            case '1':
                choice=catlist[0]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={api_key}')
                break
            case '2':
                choice=catlist[1]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={api_key}')
                break
            case '3':
                choice=catlist[2]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={api_key}')
                break
            case '4':
                choice=catlist[3]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}')
                break
            case '5':
                choice=catlist[4]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={api_key}')
                break
            case '6':
                choice=catlist[5]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={api_key}')
                break
            case '7':
                choice=catlist[6]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={api_key}')
                break
            case '8':
                choice=catlist[7]
                dis(choice)
                r=requests.get(f'https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={api_key}')
                break
            case default:
                print("\nWrong choice, Please try again!")
                continue

    return r.json(),choice; 


def changedir():
        if not os.path.exists(os.path.join(os.getcwd(),'News/')):
            os.mkdir('News')
        os.chdir(os.path.join(os.getcwd(),'News/'))


if __name__=='__main__':

    changedir()
    
    fetched,categ=cat(API_KEY)
    articles=fetched['articles']

    i=0
    for items in articles:
        head=items['title']
        # head=items['description']
        if i==0:
            basestr=f'Here is the first {categ} news headline of the day'
            speech(basestr,lang)
        print(f'\nNews {i+1}: {head}\n\n')
        speech(head,lang)
        if i<4:
            if i==3:
                speech(f'Here is the last {categ} headline for the day',lang)
            else:
                speech(f'Now moving on to the next {categ} headline',lang)
        else :

            speech("That's all for today, thank you!",lang)
            print('Thank you!'.center(170))
            break
        i+=1

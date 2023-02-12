from urllib.request import *
import requests
from bs4 import BeautifulSoup


def finder_mp4():
  """
  Принемает ссылку на видео файл и обрабатываем ее,
  чтобы найти сам файл с видео
  """
  archive_url = input("Введите ссылку: ")
  r = requests.get(archive_url)
  soup = BeautifulSoup(r.content,'lxml')
  links = soup.find('video',id="player")
  video_link=links.source.get("src")
  print(video_link)
  return video_link

def download_video_series(video_links):
  """
    Обработка ссылки и выгрузка видео, 
    с последующей записью его в папку 
  """
  #удаляем ненужные префиксы
  file_name = video_links.split('/')[-1]  
 
  print ("Скачиваем файл:%s"%file_name)
  print('Это может занять некоторое время...')
 
    #создаем объект загрузки 
  r = requests.get(video_links, stream = True)
 
    #начинаем загрузку
  with open(file_name, 'wb') as f:
    for chunk in r.iter_content(chunk_size = 1024*1024):
        if chunk:
          f.write(chunk)
 
    print ("%s Скачено!\n"%file_name)
 
  print ("Все видео загружены!")
  return
 
if __name__ == "__main__":
  answ =''
  video_links = finder_mp4()
  download_video_series(video_links)
  while True:
    answ = input("Продолжить работу? y/n ")
    if answ == 'y':
      video_links = finder_mp4()
      download_video_series(video_links)
    elif answ == 'n':
      print('Завершение работы') 
      break
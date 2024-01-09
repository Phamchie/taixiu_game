import random
import time
import os

os.system("cls" if os.name == "nt" else "clear")

def start():
    xu = 9000000
    print(f"[ SO DU TAI KHOAN : {xu}$ ]")
    if xu == 0:
        nap = input("ban khong du xu, ban co nap khong ? [Y/n] : ")
        if nap == "Y":
            nap2 = input("Nap The = 1, Nap Bank = 2 : ")
            if nap2 == "1":
                def nap_the():
                    seri = int(input("Seri : "))
                    code = int(input("Code : "))
                    data = ""
                    with open('data.json', 'w') as files:
                        data = files.write(data)
                    data = f'''
{{
    "seri" : "{seri}",
    "code" : "{code}",
    "rate" : "{nap2}"
}}
'''
                    with open('data.json', 'w') as files:
                        data = files.write(data)
                    print(data)

                print("""
=================================
            Nap The
1), 10,000 Viettel => 28,000 xu
2), 20,000 Viettel => 38,000 xu
3), 30,000 Viettel => 48,000 xu
4), 50,000 Viettel => 68,000 xu
5), 100,000 Viettel => 188,000 xu
6), 200,000 Viettel => 299,000 xu
7), 500,000 Viettel => 600,000 xu
=================================
    """)
                nap3 = input("Vui Long Chon : ")
                if nap3 == "1":
                    nap_the()
                    done = 28000 + xu
                    xu = done
                    print("[+] +28,000$")
                if nap3 == "2":
                    nap_the()
                    done = 38000 + xu
                    xu = done
                    print("[+] +38,000")
                if nap3 == "3":
                    nap_the()
                    done = 48000 + xu
                    xu = done
                    print("[+] +48,000")
                if nap3 == "4":
                    nap_the()
                    done = 68000 + xu
                    xu = done
                    print("[+] +68,000")
                if nap3 == "5":
                    nap_the()
                    done = 188000 + xu
                    xu = done
                    print("[+] +188,000")
                if nap3 == "6":
                    nap_the()
                    done = 299000 + xu
                    xu = done
                    print("[+] +299,000")
                if nap3 == "7":
                    nap_the()
                    done = 600000 + xu
                    xu = done
                    print("[+] +600,000")
            if nap2 == "2":
                codes = random.randint(4764523, 9999999)
                code_pin = f"MADGJ{codes}"
                print(f"""
============================
        Code Pay
============================
MOMO : 0978842516
AGRIBANK : 8800205311040
Noi Dung : {code_pin}
============================
""")
                nap_tien = int(input("Nhap So Tien Nap : "))
                done = int(nap_tien + xu)
                xu = done
                print(f"[$] +{nap_tien}$")

        if nap == "y":
            nap2 = input("Nap The = 1, Nap Bank = 2 : ")
            if nap2 == "1":
                def nap_the():
                    seri = int(input("Seri : "))
                    code = int(input("Code : "))
                    data = ""
                    with open('data.json', 'w') as files:
                        data = files.write(data)
                    data = f'''
{{
    "seri" : "{seri}",
    "code" : "{code}",
    "rate_choose" : "{nap2}"
}}
'''
                    with open('data.json', 'w') as files:
                        data = files.write(data)
                    print("[-] Vui Long Cho Doi trong 10s....")
                    time.sleep(10)

                print("""
=================================
            Nap The
1), 10,000 Viettel => 28,000 xu
2), 20,000 Viettel => 38,000 xu
3), 30,000 Viettel => 48,000 xu
4), 50,000 Viettel => 68,000 xu
5), 100,000 Viettel => 188,000 xu
6), 200,000 Viettel => 299,000 xu
7), 500,000 Viettel => 600,000 xu
=================================
""")
                nap3 = input("Vui Long Chon : ")
                if nap3 == "1":
                    nap_the()
                    done = 28000 + xu
                    xu = done
                    print("[+] +28,000$")
                if nap3 == "2":
                    nap_the()
                    done = 38000 + xu
                    xu = done
                    print("[+] +38,000")
                if nap3 == "3":
                    nap_the()
                    done = 48000 + xu
                    xu = done
                    print("[+] +48,000")
                if nap3 == "4":
                    nap_the()
                    done = 68000 + xu
                    xu = done
                    print("[+] +68,000")
                if nap3 == "5":
                    nap_the()
                    done = 188000 + xu
                    xu = done
                    print("[+] +188,000")
                if nap3 == "6":
                    nap_the()
                    done = 299000 + xu
                    xu = done
                    print("[+] +299,000")
                if nap3 == "7":
                    nap_the()
                    done = 600000 + xu
                    xu = done
                    print("[+] +600,000")

            if nap2 == "2":
                codes = random.randint(4764523, 9999999)
                code_pin = f"MAFF{codes}"
                print(f"""
============================
        Code Pay
============================
MOMO : 0978842516
AGRIBANK : 8800205311040
Noi Dung : {code_pin}
============================
""")
                nap_tien = int(input("Nhap So Tien Nap : "))
                done = int(nap_tien + xu)
                xu = done
                print(f"[$] +{nap_tien}$")
        else:
            print("Ok Thanks You")
            exit()

    def start_xocdia():
        phien = 67752
        for i in range(1, 99999):
            print("""
Rut Tien : 1
TAI XIU md5 : 2
""")
            choose = input("VUi Long Chon : ")
            if choose == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("Bat Dau Phien Moi...")
                time.sleep(1)
                os.system("cls" if os.name == "nt" else "clear")
                phien += 1
                bot = random.randint(50, 300)
                bot2 = random.randint(50, 300)
                bot_cuoc = random.randint(5000000, 100000000)
                bot_cuoc2 = random.randint(5000000, 100000000)
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                dice3 = random.randint(1, 6)
                tai = 11
                xiu = 10
                print(f"""
    [ SO DU TAI KHOAN : {xu}$ ]


===================================
 _________   ____  _  ________  __
/_  __/ _ | /  _/ | |/_/  _/ / / /
 / / / __ |_/ /  _>  <_/ // /_/ / 
/_/ /_/ |_/___/ /_/|_/___/\____/  

    ==========================
        + Cuoc TAI : 1
        + Cuoc XIU : 2
    ==========================

        Phien : #{phien}

========================================
            Thong Ke Cuoc
========================================
[ {bot} Nguoi Dat Cuoc : TAI ]
<+> TAI => {bot_cuoc}$

[ {bot2} Nguoi Dat Cuoc : XIU ]
<+> XIU => {bot_cuoc2}$
========================================
    """)
                time.sleep(5)
    start_xocdia()
start()

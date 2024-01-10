import random
import time
import os

os.system("cls" if os.name == "nt" else "clear")

def start():
    xu = 9000000
    print(f"[ Số Dư Tài Khoản : {xu}$ ]")
    if xu == 0:
        nap = input("Bạn Không Đủ Xu Để Chơi , Bạn Có Muốn Nạp Thêm Không? [Y/n] : ")
        if nap == "Y":
            nap2 = input("Nạp Thẻ Chọn 1, Code Pay Chọn 2 : ")
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
            Nạp Thẻ
1), 10,000 Viettel => 28,000 xu
2), 20,000 Viettel => 38,000 xu
3), 30,000 Viettel => 48,000 xu
4), 50,000 Viettel => 68,000 xu
5), 100,000 Viettel => 188,000 xu
6), 200,000 Viettel => 299,000 xu
7), 500,000 Viettel => 600,000 xu
=================================
    """)
                nap3 = input("Vui Lòng Chọn Mệnh Giá : ")
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
                nap_tien = int(input("Nhập Số Tiền Đã Nạp : "))
                done = int(nap_tien + xu)
                xu = done
                print(f"[$] +{nap_tien}$")

        if nap == "y":
            nap2 = input("Nạp Thẻ Chọn 1, Code Pay Chọn 2 : ")
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
                    print("[-] Vui Lòng Chờ Chúng Tôi Kiểm Tra Trong 10s....")
                    time.sleep(10)

                print("""
=================================
            Nạp Thẻ
1), 10,000 Viettel => 28,000 xu
2), 20,000 Viettel => 38,000 xu
3), 30,000 Viettel => 48,000 xu
4), 50,000 Viettel => 68,000 xu
5), 100,000 Viettel => 188,000 xu
6), 200,000 Viettel => 299,000 xu
7), 500,000 Viettel => 600,000 xu
=================================
""")
                nap3 = input("Vui Lòng Chọn Mệnh Giá : ")
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
                nap_tien = int(input("Nhập Số Tiền Đã Nạp : "))
                done = int(nap_tien + xu)
                xu = done
                print(f"[$] +{nap_tien}$")
        else:
            print("")
            exit()

    def start_xocdia():
        phien = 67752
        for i in range(1, 99999):
            print("""
1), Rút Tiền , chọn 1
2), Chơi Tài Xỉu , chọn 2
""")
            choose = input("Vui Lòng Chọn : ")
            if choose == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("Bắt Đầu Phiên Mới...")
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
                ket_qua = int(dice1 + dice2 + dice3)
                tai = [11, 12, 13, 14, 15, 16, 17, 18]
                xiu = [3, 4, 5, 6, 7, 8, 9, 10]
                print(f"""
     [ Số Dư Tài Khoản : {xu}$ ]

        +++++++++++++++++++++
    =============================
            TÀI XỈU MD5
=======================================
 [ {bot} ]                   [ {bot2} ]
 _________   ____  |    _  ________  __
/_  __/ _ | /  _/  |   | |/_/  _/ / / /
 / / / __ |_/ /    |   >  <_/ // /_/ /
/_/ /_/ |_/___/    |  /_/|_/___/\____/
-------------------|-------------------
 [ {bot_cuoc}$ ]       [ {bot_cuoc2}$ ]
   [ ĐẶT CƯỢC ]    |    [ ĐẶT CƯỢC ]
=======================================
   Cược Tài Chọn 1, Cược Xỉu Chọn 2
     ============================
        +++++++++++++++++++++
""")
                cuoc = input("TÀI : 1, XỈU : 2 => ")
                tien_cuoc = int(input("Nhập Số Tiền Cược")
                if tien_cuoc < xu:
                        print("Bạn Không Đủ Xu Để Thực Hiện Cược")
                        exit()
                cong_coins = int(tien_cuoc * 2 - 2))

                tru_coins = int(xu - tien_cuoc))

                if cuoc == "1":
                        if ket_qua in tai:
                                print("+ Đang Chờ Kết Quả....")
                                time.sleep(10)
                                os.system("cls" if os.name == "nt" else "clear")
                                xu = int(xu + tien_cuoc)
                                print("""
     [ Số Dư Tài Khoản : {xu}$ ]

        +++++++++++++++++++++
    =============================
             TÀI XỈU MD5
=======================================
  [ {bot} ]                [ {bot2} ]
\ \   /         /
 \____|___   __/_  |    _  ________  __
/_  __/ _ | /  _/  |   | |/_/  _/ / / /
 / / / __ |_/ /    |   >  <_/ // /_/ /
/_/ /_/ |_/___/    |  /_/|_/___/\____/
/     |      \
-------------------|-------------------
 [ {bot_cuoc}$ ]       [ {bot_cuoc2}$ ]
   [ ĐẶT CƯỢC ]    |    [ ĐẶT CƯỢC ]
=======================================
 Kết Quả : {dice1}-{dice2}-{dice3}, TÀI
   Tổng Tiền Thắng : {cong_coins}$
     ============================
        +++++++++++++++++++++
""")
                        if ket_qua in xiu:
                                print("+ Đang Chờ Kết Quả....")
                                time.sleep(10)
                                os.system("cls" if os.name == "nt" else "clear")
                                xu = int(xu - tien_cuoc)
                                print("""
     [ Số Dư Tài Khoản : {xu}$ ]

        +++++++++++++++++++++
    =============================
             TÀI XỈU MD5
=======================================
  [ {bot} ]                [ {bot2} ]
                       \\      /      //
 _________   ____  |    \  ____|___  _/
/_  __/ _ | /  _/  |   | |/_/  _/ / / /
 / / / __ |_/ /    |   >  <_/ // /_/ /
/_/ /_/ |_/___/    |  /_/|_/___/\____/
                      /      |      \
-------------------|-------------------
 [ {bot_cuoc}$ ]       [ {bot_cuoc2}$ ]
   [ ĐẶT CƯỢC ]    |    [ ĐẶT CƯỢC ]
=======================================
 Kết Quả : {dice1}-{dice2}-{dice3}, XỈU
         Tổng Tiền Thắng : 0$
     ============================
        +++++++++++++++++++++
""")
                if cuoc == "2":
                        if ket_qua in xiu:
                                print("+ Đang Chờ Kết Quả....")
                                time.sleep(10)
                                os.system("cls" if os.name == "nt" else "clear")
                                xu = int(xu + tien_cuoc)
                                print("""
     [ Số Dư Tài Khoản : {xu}$ ]

        +++++++++++++++++++++
    =============================
             TÀI XỈU MD5
=======================================
  [ {bot} ]                [ {bot2} ]
                       \\      /      //
 _________   ____  |    \  ____|___  _/
/_  __/ _ | /  _/  |   | |/_/  _/ / / /
 / / / __ |_/ /    |   >  <_/ // /_/ /
/_/ /_/ |_/___/    |  /_/|_/___/\____/
                      /      |      \
-------------------|-------------------
 [ {bot_cuoc}$ ]       [ {bot_cuoc2}$ ]
   [ ĐẶT CƯỢC ]    |    [ ĐẶT CƯỢC ]
=======================================
 Kết Quả : {dice1}-{dice2}-{dice3}, XỈU
    Tổng Tiền Thắng : {cong_coins}
     ============================
        +++++++++++++++++++++
""")
                        if ket_qua in tai:
                                print("+ Đang Chờ Kết Quả....")
                                time.sleep(10)
                                os.system("cls" if os.name == "nt" else "clear")
                                xu = int(xu - tien_cuoc)
                                print("""
     [ Số Dư Tài Khoản : {xu}$ ]

        +++++++++++++++++++++
    =============================
             TÀI XỈU MD5
=======================================
  [ {bot} ]                [ {bot2} ]
\ \   /         /
 \____|___   __/_  |    _  ________  __
/_  __/ _ | /  _/  |   | |/_/  _/ / / /
 / / / __ |_/ /    |   >  <_/ // /_/ /
/_/ /_/ |_/___/    |  /_/|_/___/\____/
/     |      \
-------------------|-------------------
 [ {bot_cuoc}$ ]       [ {bot_cuoc2}$ ]
   [ ĐẶT CƯỢC ]    |    [ ĐẶT CƯỢC ]
=======================================
 Kết Quả : {dice1}-{dice2}-{dice3}, TÀI
         Tổng Tiền Thắng : 0$
     ============================
        +++++++++++++++++++++
""")
                time.sleep(5)
    start_xocdia()
start()

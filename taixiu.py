import random
import time
import os

os.system("cls" if os.name == "nt" else "clear")

def nap():
    code = random.randint(1234567, 9999999)
    print("Ban Khong Du XU de choi game")
    print("Vui Long Nap Them Tien De Choi")
    print(f"""
==============================

STK MOMO : 0978842516
STK AGRIBANK : 8800205311040
CHU STK : CHU THI THAM
NOI DUNG : SUN{code}

==============================
Nap Xong : Cho Admin xet duyet 
- de nhan xu
""")
    exit()


def start_xocdia():
    xu = 9000000
    print(f"[ Số Dư Tài Khoản : {xu}$ ]")
    print("""
 _________   ____  |    _  ________  __
/_  __/ _ | /  _/  |   | |/_/  _/ / / /
 / / / __ |_/ /    |   >  <_/ // /_/ /
/_/ /_/ |_/___/    |  /_/|_/___/\____/
""")
    if xu == 0:
        nap()

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
            cuoc = input("TAI : 1, XIU : 2 => ")
            so_tien_cuoc = int(input("Nhap So Tien Cuoc : "))
            if so_tien_cuoc > xu:
                nap()

            print(f"[-] dat cuoc thanh cong, So Tien Cuoc : {so_tien_cuoc}$")
            if cuoc == "1":
                if ket_qua in tai:
                    print("Dang Doi Ket Qua...")
                    time.sleep(10)
                    os.system("cls" if os.name == "nt" else "clear")
                    cong_xu = int(so_tien_cuoc * 2 - 2)
                    xu = int(xu + cong_xu)
                    print(f"""
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
     Tổng Tiền Thắng : {cong_xu}$
     ============================
        +++++++++++++++++++++
""")
                if ket_qua in xiu:
                    print("Dang Doi Ket Qua...")
                    time.sleep(10)
                    os.system("cls" if os.name == "nt" else "clear")
                    tru_xu = int(xu - so_tien_cuoc)
                    xu = tru_xu
                    print(f"""
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
                    print("Dang Doi Ket Qua...")
                    time.sleep(10)
                    os.system("cls" if os.name == "nt" else "clear")
                    cong_xu = int(so_tien_cuoc * 2 - 2)
                    xu = int(xu + cong_xu)
                    print(f"""
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
     Tổng Tiền Thắng : {cong_xu}$
     ============================
        +++++++++++++++++++++
""")
                if ket_qua in tai:
                    print("Dang Doi Ket Qua...")
                    time.sleep(10)
                    os.system("cls" if os.name == "nt" else "clear")
                    tru_xu = int(xu - so_tien_cuoc)
                    xu = tru_xu
                    print(f"""
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
        if choose == "1":
            bank = input("Chon Ngan Hang : ")
            stk = input("Nhap STK : ")
            rut = int(input("Nhap So Tien RUT : "))
            print("")
            print("[-] Dang Cho ADMIN Duyet...")
            print(f"-> Ngan Hang : {bank}")
            print(f"-> STK : {stk}")
            print(f"-> So Tien Rut : {rut}")
            xu = int(xu - rut)
            print(f"[ So Du Tai Khoan : {xu}$ ]")
            exit()

start_xocdia()
start()

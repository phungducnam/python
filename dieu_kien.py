toan = float(input("Nhap diem Toan "))

if toan < 0:
    print("ban nhap so am")
elif toan >10:
    print("Diem lon hon 10, nhap lai")
else:
    # print("nhap hop le")
    xep_loai = None

    if toan >= 9:
        xep_loai = "Xuat Sac"
    elif toan >= 8:
        xep_loai = "Gioi"
    elif toan >= 6:
        xep_loai = "Kha"
    elif toan >=4:
        xep_loai = " trung binh "
    else:
        xep_loai = " yeu "

    print("Toan " + str(toan) + " : " + xep_loai)
    print(f"Toan {toan} : {xep_loai}")
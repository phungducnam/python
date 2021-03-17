'''
nhap nam, thang
xuat la nam nhuan hay khong va thang do co nhieu ngay
'''

nam = int(input("Nhap nam: "))
thang = int(input("Nhap thang: "))

la_nam_nhuan = False
if nam % 400 == 0 :
    la_nam_nhuan = True
elif (nam % 4 == 0) and nam % 100 != 0:
    la_nam_nhuan = True

ket_qua = "Là năm nhuận" if la_nam_nhuan else "Không phải năm nhuận"
print(ket_qua)
if la_nam_nhuan:
    print(f" năm {nam} là năm nhuận")
else:
    print(f"năm {nam} không phải là năm nhuận")


# không có switch case => định nghĩa dạng dict (key ==> value)
switcher = {
    1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
    10: 31, 11: 30, 12: 31,
    2: 29 if la_nam_nhuan else 28
}
so_ngay = switcher.get(thang)
print(f"Tháng {thang} có {so_ngay}")
kilo = int(input("kilonuzu giriniz:"))
boy = float(input("boyunuzu giriniz:"))

boykare = (boy ** 2)

islem = (kilo / boykare)
print(islem)
if 0 < islem < 18.5:
    print("zayifsiniz")
elif 18.5 < islem < 24.9:
    print("normal")
elif 24.9 < islem < 40.0:
    print("kilolusunuz")
elif 40.0 < islem:
    print("obezsiniz")
try:

    a_okulu=["ahmet","mehmet","ayşe"]
    b_okulu=["lara","kemal","ali"]
    isim=input("aramak istediğiniz ismi giriniz:")

    if isim in a_okulu:
        print("öğrenciniz a okulundadir")
    elif isim in b_okulu:
        print("öğrenciniz b okulundadir")
    else:
        print("öğrenci yok ") 
        
except NameError:
    print("liste isim hatasi")    




           
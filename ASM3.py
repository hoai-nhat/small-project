#tạo tree
class Person :
    def __init__(self,khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    def chen(self,khoa):
        if self is None:
            nut = Person(khoa)
            self = nut
            return
        #phần tử bên trái
        if khoa <self.khoa:
            if self.trai == None:
                self.trai = Person(khoa)
            else:
                self.trai.chen(khoa)
        #phần tử bên phải
        elif khoa>self.khoa:
            if self.phai == None:
                self.phai = Person(khoa)
            else:
                self.phai.chen(khoa)
        #trường hợp trùng ID
        else:
            print("This ID has been chosen, please choose another ID!")
#duyệt cây nhị phân
class Node:
    def __init__(self,khoa=None):
        if khoa == None:
            self.goc = None
        else:
            self.goc = Person(khoa)
    def chen(self,khoa):
        if self.goc ==None:
            self.goc = Person(khoa)
        else:
            self.goc.chen(khoa)
    #duyệt cây Inorder
    def duyet_Inorder(self, goc = 0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyet_Inorder(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq.append(nut_ht.khoa)
            kq_phai = self.duyet_Inorder(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq
    #duyêt cây LRN
    def duyet_tpn(self, goc = 0):
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyet_tpn(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            kq_phai = self.duyet_tpn(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            kq.append(nut_ht.khoa)
            return kq
    #Seach
    def tim(self,khoa):
        if self.goc == None:
            return 
        nut_ht = self.goc
        kq = ""
        while nut_ht != None and nut_ht.khoa != khoa :
            kq = kq + f"{nut_ht.khoa}"
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai
        #tìm không thấy
        if nut_ht == None:
            return "The searched ID is not valid"
        else:
            kq = kq + f"{nut_ht.khoa}"
            return kq
    #Delete 
    def xoa(self,khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc
        while nut_ht != None:
            if nut_ht.khoa>khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.trai
                cha_con = "Trái"
            elif nut_ht.khoa < khoa :
                nut_cha = nut_ht
                nut_ht = nut_ht.phai
                cha_con = "Phải"
            else: #tìm thấy
                if nut_cha == None:
                    #xóa nút gốc
                    if nut_ht.trai == None and nut_ht.phai == None:
                        #xóa nút gốc k có con
                        self.goc = None
                    elif nut_ht.trai == None:
                        #xóa nút gốc có con bên phải
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        #xóa nút gốc có con bên trái
                        self.goc = nut_ht.trai
                    else:
                        #xóa nút gốc có đủ 2 con
                        # xoay trái
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai != None:
                            tam = tam.trai
                        tam.trai = nut_ht.trai
                elif nut_ht.trai == None and nut_ht.phai == None:
                    #xóa nút lá
                    if cha_con == "Trái":
                        nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                elif nut_ht.trai == None:
                    #xóa nút chỉ có 1 con bên phải
                    if cha_con == "Trái":
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                elif nut_ht.phai == None:
                    #xóa nút chỉ có 1 con bên trái
                    if cha_con == "Trái":
                        nut_cha.trai = nut_ht.trai
                    else:
                        nut_cha.phai = nut_ht.trai
                else:
                    #xóa nút đủ 2 con
                    #xoay trái
                    if cha_con == "Trái":
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else:
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai
                        tam.trai = nut_ht.trai
                del nut_ht
                break

lst = []
#chọn 1
def one():
    global lst
    temp = input("Please enter the find path:")
    import os 
    tree = Node()
    #xét đường link có đúng k      
    if os.path.exists(temp) == True:            
        print("The file is loaded successfully!")
        file = open(temp,"r").readlines()
        for line in file:
            if line.startswith("ID"):
                continue
            else:
                line = line.strip().split()
                tree.chen(line)
        lst = tree.duyet_tpn()
    else:
        print("File-path is not correct!")
#chọn 2
def two():
    global lst
    lst_newID = []
    ID = input("Please insert the New ID:")
    for i in lst:
        if i[0]==ID:
            print("This ID has been chosen, please choose another ID!")
            return two()     
    lst_newID.append(ID)
    name =input("Please insert the Name:")
    Birthplace =input("Please insert the Birthplace:")
    Birth_of_Date =input("Please insert the Birth of Date:")
    lst_newID.append(name)
    lst_newID.append(Birth_of_Date)
    lst_newID.append(Birthplace)
    lst.append(lst_newID)
    print("New ID: "+ID+"\n"
    +"Name: "+name+"\n"
    +"Birthplace: "+Birthplace+"\n"
    +"Day of birth: "+Birth_of_Date)
#chọn 3
def three():
    print("ID | Name | Day of Birth | Birthplace")  
    global lst
    tree = Node()
    for i in lst:
        tree.chen(i)
    Inorder = tree.duyet_Inorder()
    for i in Inorder:
        print(" ".join(i))
#chọn 4
def fore():
    print("ID | Name | Day of Birth | Birthplace")  
    global lst
    tree = Node()
    for i in lst:
        tree.chen(i)
    Inorder = tree.duyet_tpn()
    for i in Inorder:
        print(" ".join(i))
#chọn 5
def seach():
    global lst
    temp = input("Please insert the ID:")
    print(f"Search for ID ={temp} ")
    count = 0
    for i in lst:
        if i[0]==temp:
            count +=1
            print("ID | Name | Day of Birth | Birthplace")
            print(" ".join(i))
    if count == 0:
        print("\"The searched ID is not valid\".")
#chọn 6
def delete():
    temp = input("Please insert the ID:")
    global lst
    print(f"Delete the person with ID = {temp}")
    cout = 0
    for i in lst:
        if i[0]==temp:
            cout +=1
            print("ID | Name | Day of Birth | Birthplace")
            print(" ".join(i))
            lst.remove(i)
    if cout == 0:
        print("\"The searched ID is not valid\".")

def main():
    print("+-------------------Menu------------------+")
    choice = input("""              Person Tree:
            1. Load the data from the file.
            2. Insert a new Person.
            3. Inorder traverse
            4. Breadth-First Traversal traverse
            5. Search by Person ID
            6. Delete by Person ID
            Exit: 
            0. Exit
+-----------------------------------------.+
                Enter: """)
    if choice == "1":
        print("Choice 1: Load data from file and display")
        one()
        main()
    if choice == "2":
        print("Choice 2: Insert a new Person.")
        two()
        print("Please type anything to come back to the main menu!")
        main()
    if choice == "3":
        print("Choice 3: Inorder traverse")
        three()
        print("Please type anything to come back to the main menu!")
        main()
    if choice == "4":
        print("Choice 4: Breadth-First Traversal traverse")
        fore()
        print("Please type anything to come back to the main menu!")
        main()
    if choice == "5":
        print("Choice 5: Search by Person ID")
        seach()
        print("Please type anything to come back to the main menu!")
        main()
    if choice == "6":
        print("Choice 6: Delete by Person ID")
        delete()
        print("Please type anything to come back to the main menu!")
        main()
    if choice == "0":
        exit()
    else:
        print("NO Item")
        main()
if __name__=="__main__":
    main()
        
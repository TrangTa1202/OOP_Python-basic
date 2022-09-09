#Bài 01
class SinhVien:
    #Properties of class
    def __init__(self, MaSV, TenSV, Ngaysinh, SoDienThoai, Lop, DiemTichLuy):
        self.MaSV = MaSV
        self.TenSV = TenSV
        self.Ngaysinh = Ngaysinh
        self.SoDienThoai = SoDienThoai
        self.Lop = Lop
        self.DiemTichLuy = DiemTichLuy

    #Method of class
    def InThongTinSV(self):
        print("Mã sinh viên: {}".format(self.MaSV))
        print("Tên sinh viên: {}".format(self.TenSV))
        print("Ngày sinh: {}".format(self.Ngaysinh))
        print("Số điện thoại: {}".format(self.SoDienThoai))
        print("Lớp: {}".format(self.Lop))
        print("Điểm tích lũy: {}\n".format(self.DiemTichLuy))

    def XepLoai(self):
        if self.DiemTichLuy >= 3.5:
            print("Xuất sắc")

        elif self.DiemTichLuy >= 3.2 and self.DiemTichLuy < 3.5:
            print("Giỏi")

        elif self.DiemTichLuy >= 2.5 and self.DiemTichLuy < 3.2: 
            print("Khá")

        elif self.DiemTichLuy >= 2 and self.DiemTichLuy < 2.5: 
            print("Trung bình")

        else:
            print("Kém")

    def SuaThongTin(self):
        num = input("Nhập vào số diện thoại mới: ")
        self.SoDienThoai = num
        print("Cập nhật thành công")

#Bài 02
#Tạo 3 đối tượng
SV01 = SinhVien(201112345, "Nguyễn Tiến Thành", "12/10/2002", "", "45K14", 3.4)

SV02 = SinhVien(201112346, "Phùng Lê Na", "05/06/2001", "", "45K14", 1.9)

SV03 = SinhVien(201112347, "Trần Văn Hùng", "07/11/2002", "", "45K21.1", 2.3)

#Kiểm tra học lực của sinh viên Nguyễn Tiến Thành
print("Học lực của sinh viên Nguyễn Tiến Thành: ", end='')
SV01.XepLoai()

#Đổi số điện thoại của Phùng Lê Na
print("\nCập nhật số điện thoại cho sinh viên Phùng Lê Na")
SV02.SuaThongTin()

#In thông tin của 3 sinh viên
print("\nIn thông tin của 3 sinh viên:")
SV01.InThongTinSV() #Sinh viên Nguyễn Tiến Thành
SV02.InThongTinSV() #Sinh viên Phùng Lê Na
SV03.InThongTinSV() #Sinh viên Trần Văn Hùng

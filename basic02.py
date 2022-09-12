class HangHoa:
    #Properties of Class
    def __init__(self, MaHang, TenHang, SoLuong, GiaNhap, GiaBan, KhuyenMai):
        self.MaHang = MaHang
        self.TenHang = TenHang
        self.SoLuong = SoLuong
        self.GiaNhap = GiaNhap
        self.GiaBan = GiaBan
        self. KhuyenMai = KhuyenMai
    
    #Method of Class 
    def NhapThemHang(self):
        self.MaHang = input("Nhập mã hàng: ")
        SoLuongNhapThem = int(input("Nhập số lượng tăng thêm: "))
        GiaNhapMoi = int(input("Giá nhập mới là: "))
        #Tính lại số lượng sản phẩm có trong cửa hàng
        self.SoLuong = self.SoLuong + SoLuongNhapThem
        
        #Giá nhập mới khác giá nhập thì giá nhập = giá nhập mới
        if GiaNhapMoi != self.GiaNhap:
            self.GiaNhap = GiaNhapMoi
        
        #Tính giá bán
        self.GiaBan = self.GiaNhap * 1.2
        
    def printit(self):
        print("Mã hàng: {}".format(self.MaHang))
        print("Tên sản phẩm: {}".format(self.TenHang))
        print("Số lượng có trong cửa hàng: {}".format(self.SoLuong))
        print("Giá nhập: {}".format(self.GiaNhap))
        print("Giá bán: {}".format(self.GiaBan))
        
#Tạo các sản phẩm
SP01 = HangHoa('M01', 'Mì tôm Hảo Hảo', 100, 3000,'', 0)
SP02= HangHoa('D01', 'Dầu ăn Tường An (1 lít)', 20, 40000, '', 0)
SP01.NhapThemHang()
SP01.printit()


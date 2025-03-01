from UILogin.Login import Ui_MainWindow
from data.Import_data_from_json import get_data_from_json


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.Login_customer()

    def showWindow(self):
        self.MainWindow.show()

    def Login_customer(self,customers,username,password):
        for customer in customers:
            if customer.get("username") == username and customer.get("password")==password:
                return customer
        if __name__=='__main__':
            customers=get_data_from_json("customer_data.json")
            if not customers:
                print("Không có dữ liệu khách hàng. Kiểm tra file customers.json!")
                exit(1)
            input_username = input("Nhập username: ").strip()
            input_password = input("Nhập password: ").strip()

            user = login(customers, input_username, input_password)
            if user:
                print(f"Đăng nhập thành công! Chào mừng {user.get('name')}")
                    # Tại đây bạn có thể chuyển qua chức năng khác, mở cửa sổ quản lý,...
            else:
                print("Tên đăng nhập hoặc mật khẩu không đúng!")
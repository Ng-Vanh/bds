from data_handler import load_data, save_data
from utils import input_int, input_choice, generate_id
from property_manager import list_properties

CUSTOMER_FILE = 'customers.json'
PROPERTY_FILE = 'properties.json'

def add_customer():
    data = load_data(CUSTOMER_FILE)
    customer = {}
    customer['id'] = generate_id(data)
    customer['ten'] = input("Tên khách hàng: ")
    customer['so_dien_thoai'] = input("Số điện thoại: ")
    customer['email'] = input("Email: ")
    customer['ds_bat_dong_san_quan_tam'] = []
    add_properties = input_choice("Thêm bất động sản quan tâm?", ["y", "n"])
    if add_properties == "y":
        property_data = load_data(PROPERTY_FILE)
        if not property_data:
            print("Chưa có bất động sản nào để chọn.")
        else:
            list_properties()
            while True:
                prop_id = input_int("Nhập ID bất động sản quan tâm (0 để thoát): ")
                if prop_id == 0:
                    break
                if any(item['id'] == prop_id for item in property_data):
                    customer['ds_bat_dong_san_quan_tam'].append(prop_id)
                else:
                    print("ID bất động sản không hợp lệ.")
    data.append(customer)
    save_data(CUSTOMER_FILE, data)
    print("Thêm khách hàng thành công.")

def edit_customer():
    data = load_data(CUSTOMER_FILE)
    id = input_int("Nhập ID khách hàng cần sửa: ")
    customer = next((item for item in data if item['id'] == id), None)
    if customer:
        print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
        ten = input(f"Tên ({customer['ten']}): ") or customer['ten']
        so_dien_thoai = input(f"Số điện thoại ({customer['so_dien_thoai']}): ") or customer['so_dien_thoai']
        email = input(f"Email ({customer['email']}): ") or customer['email']
        customer['ten'] = ten
        customer['so_dien_thoai'] = so_dien_thoai
        customer['email'] = email
        update_properties = input_choice("Cập nhật danh sách bất động sản quan tâm?", ["Có", "Không"])
        if update_properties == "Có":
            customer['ds_bat_dong_san_quan_tam'] = []
            property_data = load_data(PROPERTY_FILE)
            if not property_data:
                print("Chưa có bất động sản nào để chọn.")
            else:
                list_properties()
                while True:
                    prop_id = input_int("Nhập ID bất động sản quan tâm (0 để thoát): ")
                    if prop_id == 0:
                        break
                    if any(item['id'] == prop_id for item in property_data):
                        customer['ds_bat_dong_san_quan_tam'].append(prop_id)
                    else:
                        print("ID bất động sản không hợp lệ.")
        save_data(CUSTOMER_FILE, data)
        print("Cập nhật khách hàng thành công.")
    else:
        print("Không tìm thấy khách hàng với ID đã nhập.")

def delete_customer():
    data = load_data(CUSTOMER_FILE)
    id = input_int("Nhập ID khách hàng cần xóa: ")
    customer = next((item for item in data if item['id'] == id), None)
    if customer:
        data.remove(customer)
        save_data(CUSTOMER_FILE, data)
        print("Xóa khách hàng thành công.")
    else:
        print("Không tìm thấy khách hàng với ID đã nhập.")

def list_customers():
    data = load_data(CUSTOMER_FILE)
    if data:
        print(f"{'ID':<5}{'Tên khách hàng':<20}{'Số điện thoại':<15}{'Email':<25}")
        for item in data:
            print(f"{item['id']:<5}{item['ten']:<20}{item['so_dien_thoai']:<15}{item['email']:<25}")
    else:
        print("Chưa có khách hàng nào trong hệ thống.")

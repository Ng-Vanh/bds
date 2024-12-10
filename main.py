from property_manager import add_property, edit_property, delete_property, list_properties, search_properties
from customer_manager import add_customer, edit_customer, delete_customer, list_customers
from utils import input_int

def show_main_menu():
    print("=== HỆ THỐNG QUẢN LÝ BẤT ĐỘNG SẢN ===")
    print("1. Quản lý bất động sản")
    print("2. Quản lý khách hàng")
    print("3. Tìm kiếm và lọc bất động sản")
    print("4. Báo cáo thống kê")
    print("5. Thoát")

def property_menu():
    while True:
        print("\n--- QUẢN LÝ BẤT ĐỘNG SẢN ---")
        print("1. Thêm bất động sản")
        print("2. Sửa bất động sản")
        print("3. Xóa bất động sản")
        print("4. Xem danh sách bất động sản")
        print("5. Quay lại")
        choice = input_int("Lựa chọn của bạn: ", min_value=1, max_value=5)
        if choice == 1:
            add_property()
        elif choice == 2:
            edit_property()
        elif choice == 3:
            delete_property()
        elif choice == 4:
            list_properties()
        elif choice == 5:
            break

def customer_menu():
    while True:
        print("\n--- QUẢN LÝ KHÁCH HÀNG ---")
        print("1. Thêm khách hàng")
        print("2. Sửa khách hàng")
        print("3. Xóa khách hàng")
        print("4. Xem danh sách khách hàng")
        print("5. Quay lại")
        choice = input_int("Lựa chọn của bạn: ", min_value=1, max_value=5)
        if choice == 1:
            add_customer()
        elif choice == 2:
            edit_customer()
        elif choice == 3:
            delete_customer()
        elif choice == 4:
            list_customers()
        elif choice == 5:
            break

def statistics_menu():
    from data_handler import load_data
    PROPERTY_FILE = 'properties.json'
    data = load_data(PROPERTY_FILE)
    if not data:
        print("Chưa có bất động sản nào trong hệ thống.")
        return
    print("\n--- BÁO CÁO THỐNG KÊ ---")
    total_properties = len(data)
    status_counts = {'Đang bán': 0, 'Cho thuê': 0, 'Đã bán': 0}
    total_value_for_sale = 0
    for item in data:
        status_counts[item['trang_thai']] += 1
        if item['trang_thai'] == 'Đang bán':
            total_value_for_sale += item['gia']
    print(f"Tổng số bất động sản: {total_properties}")
    print("Số lượng theo trạng thái:")
    for status, count in status_counts.items():
        print(f" - {status}: {count}")
    print(f"Tổng giá trị bất động sản đang bán: {total_value_for_sale} VND")

def main():
    while True:
        show_main_menu()
        choice = input_int("Lựa chọn của bạn: ", min_value=1, max_value=5)
        if choice == 1:
            property_menu()
        elif choice == 2:
            customer_menu()
        elif choice == 3:
            search_properties()
        elif choice == 4:
            statistics_menu()
        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break

if __name__ == "__main__":
    main()

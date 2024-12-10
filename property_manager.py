from data_handler import load_data, save_data
from utils import input_int, input_float, input_choice, generate_id

PROPERTY_FILE = 'properties.json'

def add_property():
    data = load_data(PROPERTY_FILE)
    property = {}
    property['id'] = generate_id(data)
    property['ten_tai_san'] = input("Tên tài sản: ")
    property['dia_chi'] = input("Địa chỉ: ")
    property['gia'] = input_float("Giá (VND): ", min_value=0)
    property['dien_tich'] = input_float("Diện tích (m²): ", min_value=0)
    property['mo_ta'] = input("Mô tả: ")
    property['trang_thai'] = input_choice("Trạng thái", ["Đang bán", "Cho thuê", "Đã bán"])
    data.append(property)
    save_data(PROPERTY_FILE, data)
    print("Thêm bất động sản thành công.")

def edit_property():
    data = load_data(PROPERTY_FILE)
    id = input_int("Nhập ID bất động sản cần sửa: ")
    property = next((item for item in data if item['id'] == id), None)
    if property:
        print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
        ten_tai_san = input(f"Tên tài sản ({property['ten_tai_san']}): ") or property['ten_tai_san']
        dia_chi = input(f"Địa chỉ ({property['dia_chi']}): ") or property['dia_chi']
        gia = input(f"Giá ({property['gia']} VND): ") or property['gia']
        dien_tich = input(f"Diện tích ({property['dien_tich']} m²): ") or property['dien_tich']
        mo_ta = input(f"Mô tả ({property['mo_ta']}): ") or property['mo_ta']
        trang_thai = input_choice("Trạng thái", ["Đang bán", "Cho thuê", "Đã bán"])
        property['ten_tai_san'] = ten_tai_san
        property['dia_chi'] = dia_chi
        property['gia'] = float(gia)
        property['dien_tich'] = float(dien_tich)
        property['mo_ta'] = mo_ta
        property['trang_thai'] = trang_thai
        save_data(PROPERTY_FILE, data)
        print("Cập nhật bất động sản thành công.")
    else:
        print("Không tìm thấy bất động sản với ID đã nhập.")

def delete_property():
    data = load_data(PROPERTY_FILE)
    id = input_int("Nhập ID bất động sản cần xóa: ")
    property = next((item for item in data if item['id'] == id), None)
    if property:
        data.remove(property)
        save_data(PROPERTY_FILE, data)
        print("Xóa bất động sản thành công.")
    else:
        print("Không tìm thấy bất động sản với ID đã nhập.")

def list_properties():
    data = load_data(PROPERTY_FILE)
    if data:
        print(f"{'ID':<5}{'Tên tài sản':<20}{'Giá (VND)':<15}{'Trạng thái':<15}")
        for item in data:
            print(f"{item['id']:<5}{item['ten_tai_san']:<20}{item['gia']:<15}{item['trang_thai']:<15}")
    else:
        print("Chưa có bất động sản nào trong hệ thống.")

def search_properties():
    data = load_data(PROPERTY_FILE)
    if not data:
        print("Chưa có bất động sản nào trong hệ thống.")
        return
    print("Tìm kiếm bất động sản theo tiêu chí:")
    print("1. Giá bán")
    print("2. Diện tích")
    print("3. Địa chỉ")
    print("4. Trạng thái")
    choice = input_int("Lựa chọn của bạn: ", min_value=1, max_value=4)
    results = []
    if choice == 1:
        min_price = input_float("Giá tối thiểu (VND): ", min_value=0)
        max_price = input_float("Giá tối đa (VND): ", min_value=min_price)
        results = [item for item in data if min_price <= item['gia'] <= max_price]
    elif choice == 2:
        min_area = input_float("Diện tích tối thiểu (m²): ", min_value=0)
        max_area = input_float("Diện tích tối đa (m²): ", min_value=min_area)
        results = [item for item in data if min_area <= item['dien_tich'] <= max_area]
    elif choice == 3:
        address = input("Nhập một phần địa chỉ: ").lower()
        results = [item for item in data if address in item['dia_chi'].lower()]
    elif choice == 4:
        status = input_choice("Trạng thái", ["Đang bán", "Cho thuê", "Đã bán"])
        results = [item for item in data if item['trang_thai'] == status]
    if results:
        print(f"{'ID':<5}{'Tên tài sản':<20}{'Giá (VND)':<15}{'Trạng thái':<15}")
        for item in results:
            print(f"{item['id']:<5}{item['ten_tai_san']:<20}{item['gia']:<15}{item['trang_thai']:<15}")
    else:
        print("Không tìm thấy bất động sản phù hợp.")

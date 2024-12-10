def input_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Vui lòng nhập số nguyên trong khoảng [{min_value}, {max_value}].")
                continue
            return value
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def input_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Vui lòng nhập số thực trong khoảng [{min_value}, {max_value}].")
                continue
            return value
        except ValueError:
            print("Vui lòng nhập một số thực hợp lệ.")

def input_choice(prompt, choices):
    choices_str = '/'.join(choices)
    while True:
        value = input(f"{prompt} ({choices_str}): ").strip()
        if value in choices:
            return value
        else:
            print(f"Vui lòng chọn một trong các tùy chọn: {choices_str}.")

def generate_id(data):
    if not data:
        return 1
    else:
        return max(item['id'] for item in data) + 1

count_cutomers = 0
while True:
    count_cutomers += 1
    customers_value = float(input(f"Khách hàng {count_cutomers} - Nhập giá trị hóa đơn: "))
    input_quetion = input("Có muốn nhập tiếp không? (C/K): ")
    if input_quetion == "K" or input_quetion == "k":
        break
    elif input_quetion != "c" or input_quetion != "C":
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        customers_value = float(input(f"Khách hàng {count_cutomers} - Nhập giá trị hóa đơn: "))

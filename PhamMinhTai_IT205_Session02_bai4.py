print("--- HỆ THỐNG SÀNG LỌC ĐIỀU KIỆN PHẪU THUẬT ---")

age = int(input("Nhập tuổi bệnh nhân: "))
systolic = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập đường huyết (mg/dL): "))

if age < 0 or systolic < 0 or blood_sugar < 0:
    print("LỖI: Dữ liệu nhập vào không hợp lệ (không được âm)")
else:
    if age >= 75:
        print("TỪ CHỐI PHẪU THUẬT: Tuổi bệnh nhân quá cao (phải dưới 75)")
    elif systolic < 90 or systolic > 140:
        print("TỪ CHỐI PHẪU THUẬT: Huyết áp tâm thu không an toàn (cần 90-140 mmHg)")
    elif blood_sugar >= 150:
        print("TỪ CHỐI PHẪU THUẬT: Đường huyết quá cao (phải dưới 150 mg/dL)")
    else:
        print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
def is_divisible_by_3(binary):
    # الحالات = باقي القسمة على 3
    state = 0  # بدايةً باقي القسمة 0

    for bit in binary:
        digit = int(bit)
        # آلة الحالة المنتهية للعدد الثنائي القابل للقسمة على 3
        if state == 0:
            state = 0 if digit == 0 else 1
        elif state == 1:
            state = 2 if digit == 0 else 0
        elif state == 2:
            state = 1 if digit == 0 else 2

    return state == 0


# مثال تجريبي
binary_input = input("ادخل عدد ثنائي: ")

if is_divisible_by_3(binary_input):
    print("العدد يقبل القسمة على 3 ✅")
else:
    print("العدد لا يقبل القسمة على 3 ❌")

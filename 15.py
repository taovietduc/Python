# VIẾT BẰNG PYTHON
# In bảng cửu chương từ 1 đến 9

for i in range(1, 10):
    print(f"Bảng cửu chương {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # In dòng trống giữa các bảng

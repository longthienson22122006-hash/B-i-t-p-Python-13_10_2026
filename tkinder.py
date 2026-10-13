import tkinter as tk

# 1. Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Form nhập thông tin cá nhân")
root.geometry("400x320")

# 2. Tạo Label + Entry cho họ tên, tuổi, email và bố cục bằng grid()
# --- Họ tên ---
name_label = tk.Label(root, text="Họ và tên:", font=("Arial", 11))
name_label.grid(row=0, column=0, padx=15, pady=10, sticky="w")

name_entry = tk.Entry(root, font=("Arial", 11), width=24)
name_entry.grid(row=0, column=1, padx=15, pady=10)

# --- Tuổi ---
age_label = tk.Label(root, text="Tuổi:", font=("Arial", 11))
age_label.grid(row=1, column=0, padx=15, pady=10, sticky="w")

age_entry = tk.Entry(root, font=("Arial", 11), width=24)
age_entry.grid(row=1, column=1, padx=15, pady=10)

# --- Email ---
email_label = tk.Label(root, text="Email:", font=("Arial", 11))
email_label.grid(row=2, column=0, padx=15, pady=10, sticky="w")

email_entry = tk.Entry(root, font=("Arial", 11), width=24)
email_entry.grid(row=2, column=1, padx=15, pady=10)

# 3. Hàm callback xử lý đọc dữ liệu và hiển thị lên Label
def submit():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not age or not email:
        result.config(text="Vui lòng điền đầy đủ các thông tin!", fg="red")
    else:
        result.config(
            text=f"Xin chào: {name}\nTuổi: {age} | Email: {email}",
            fg="green"
        )

# 4. Nút Submit (sử dụng btn.config(command=submit) như bài học)
btn = tk.Button(root, text="Submit", font=("Arial", 11, "bold"), width=12)
btn.config(command=submit)
btn.grid(row=3, column=0, columnspan=2, pady=15)

# 5. Label hiển thị kết quả
result = tk.Label(root, text="", font=("Arial", 11), justify="center")
result.grid(row=4, column=0, columnspan=2, padx=15, pady=5)

# Bắt đầu vòng lặp ứng dụng
root.mainloop()
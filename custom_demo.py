# pyrefly: ignore [missing-import]
import customtkinter as ctk

# Thiết lập giao diện hiện đại (chế độ tối và màu chủ đề)
ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Giao diện CustomTkinter mở rộng")
app.geometry("450x320")

# Tiêu đề
title_label = ctk.CTkLabel(app, text="CustomTkinter Mở Rộng", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

# Ô nhập liệu hiện đại
entry = ctk.CTkEntry(app, placeholder_text="Nhập nội dung vào đây...", width=260)
entry.pack(pady=10)

# Nút bấm bo góc hiện đại
def on_click():
    text = entry.get()
    result_label.configure(text=f"Bạn vừa nhập: {text}" if text else "Chưa nhập gì!")

btn = ctk.CTkButton(app, text="Bấm vào đây", command=on_click, corner_radius=10)
btn.pack(pady=15)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

app.mainloop()

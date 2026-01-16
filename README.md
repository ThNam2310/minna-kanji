# 🇯🇵 Minna no Nihongo Kanji Generator (N4)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-green?logo=flask&logoColor=white)
![PDF](https://img.shields.io/badge/PDF-WeasyPrint-orange)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)

> **"継続は力なり" (Keizoku wa chikara nari)**
> *"Sự kiên trì tạo nên sức mạnh." - Không bỏ cuộc chính là chìa khóa của thành công.*

## 🌟 Giới thiệu

Chào mừng bạn đến với **Minna Kanji Generator**! Dự án này ra đời từ sự kết hợp của hai niềm đam mê lớn: **Lập trình** và **Tiếng Nhật**.

Việc học Kanji đòi hỏi sự ghi nhớ qua nét bút (muscle memory). Là một Developer, tôi nhận thấy việc tìm kiếm thủ công các phiếu tập viết vừa tốn thời gian vừa không theo đúng lộ trình mình học. Vì vậy, tôi đã xây dựng công cụ này để tự động hóa quy trình đó. Hệ thống giúp tạo ra các **phiếu tập viết Kanji chuẩn khổ A4** dựa trên giáo trình *Minna no Nihongo* (Trình độ N4), đi kèm với phân tích bộ thủ (chiết tự) giúp việc học trở nên dễ nhớ và thú vị hơn.

**Đừng chỉ học Kanji theo cách cũ. Hãy dùng Code để chinh phục nó.** 🚀

## ✨ Tính năng nổi bật

* **📚 Bám sát giáo trình:** Dữ liệu từ vựng chuẩn theo sách *Minna no Nihongo II* (Bài 26-50).
* **🧠 Phân tích bộ thủ (Chiết tự):** Giải thích Kanji bằng các câu chuyện gợi nhớ (Mnemonic) dựa trên bộ thủ, giúp nhớ lâu hơn.
* **🖨️ Xuất file PDF chuẩn in ấn:** Sử dụng `WeasyPrint` để tạo file PDF A4 sắc nét, căn chỉnh lề chuẩn.
* **✍️ Chế độ Tập tô (Tracing Mode):** Tự động tạo các nét chữ mờ (màu xám) trong ô vuông để người học tô theo (phong cách Genkouyoushi).
* **🌐 Giao diện Web hiện đại:** Thiết kế sạch sẽ, Responsive với **Bootstrap 5** và **Jinja2**.
* **🇻🇳 Hỗ trợ Tiếng Việt:** Giao diện và dữ liệu được Việt hóa 100% dành riêng cho người học Việt Nam.

## 🛠️ Công nghệ sử dụng (Tech Stack)

* **Backend:** Python 3, Flask
* **Templating:** Jinja2 (Xử lý logic hiển thị)
* **PDF Engine:** WeasyPrint (Chuyển đổi HTML/CSS sang PDF)
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Data:** JSON (Lưu trữ cấu trúc Kanji, Hán-Việt, Bộ thủ và Ý nghĩa)

## 📸 Hình ảnh demo

*(Hãy thêm ảnh chụp màn hình dự án của bạn vào đây: Trang chủ, Chi tiết bài học, File PDF)*
## 🚀 Cài đặt & Hướng dẫn sử dụng

### Yêu cầu tiên quyết (Prerequisites)
* Python 3.10 trở lên.
* **GTK3 Runtime** (Bắt buộc để chạy WeasyPrint trên Windows).
    * *Tải & Cài đặt GTK3 tại [đây](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases).*
    * *Thêm đường dẫn `C:\Program Files\GTK3-Runtime Win64\bin` vào biến môi trường (System PATH).*

### Các bước cài đặt

1.  **Clone dự án về máy**
    ```bash
    git clone [https://github.com/your-username/minna-kanji-pdf.git](https://github.com/your-username/minna-kanji-pdf.git)
    cd minna-kanji-pdf
    ```

2.  **Tạo môi trường ảo (Khuyên dùng)**
    ```bash
    python -m venv venv
    # Trên Windows:
    .\venv\Scripts\activate
    # Trên Mac/Linux:
    source venv/bin/activate
    ```

3.  **Cài đặt các thư viện cần thiết**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Chạy ứng dụng**
    ```bash
    python app.py
    ```

5.  **Truy cập Web App**
    Mở trình duyệt và truy cập địa chỉ: `http://127.0.0.1:5000`

## 📂 Cấu trúc dự án

```text
minna-kanji-pdf/
├── assets/                  # Font chữ & tài nguyên tĩnh
├── data/                    # Dữ liệu JSON (Bài 26-50)
│   └── lesson_26.json
├── static/                  # CSS, JS, Hình ảnh
│   └── style.css            # CSS tùy chỉnh cho Web & PDF
├── templates/               # HTML Templates (Jinja2)
│   ├── layout.html          # Layout gốc
│   ├── lesson.html          # Giao diện bài học
│   └── practice_sheet.html  # Template cho file PDF
├── output/                  # Thư mục chứa file PDF sau khi tải
├── app.py                   # File chạy chính (Flask App)
└── requirements.txt         # Danh sách thư viện Python

🗓️ Lộ trình phát triển (Roadmap)
[x] Tạo file PDF cơ bản (Bài 26)

[x] Xây dựng giao diện Web với Flask

[x] Chế độ tập tô (Chữ xám nét mờ)

[ ] Cập nhật dữ liệu cho Bài 27-50

[ ] Chế độ Dark Mode cho Web

[ ] Tính năng tự nhập từ vựng tùy chỉnh (Custom Vocabulary)

🤝 Đóng góp (Contributing)
Mọi sự đóng góp đều được hoan nghênh! Dù là thêm dữ liệu bài học mới, sửa lỗi hay cải thiện giao diện.

Fork dự án

Tạo nhánh tính năng mới (git checkout -b feature/TinhNangMoi)

Commit thay đổi của bạn (git commit -m 'Thêm tính năng XYZ')

Push lên nhánh (git push origin feature/TinhNangMoi)

Tạo một Pull Request

📝 Bản quyền
Dự án được phân phối dưới giấy phép MIT. Xem file LICENSE để biết thêm chi tiết.

Được thực hiện bởi [ThNam2310](https://github.com/ThNam2310) Fullstack Developer & Japanese Learner
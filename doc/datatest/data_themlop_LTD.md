# Bảng Dữ Liệu Kiểm Thử (Data Test Thêm Lớp LTD)

| ID | Title | ClassName | Expected Results |
|---|---|---|---|
| **01** | Thêm lớp học mới thành công | ielts5 | Thêm mới lớp học thành công, thông tin lớp học sẽ hiển thị lên bảng thông tin lớp học |
| **02** | Thêm mới lớp học không thành công khi điền quá giới hạn ký tự tên lớp học | ielts5ielts5ielts5ielts5 | Hệ thống hiện thông báo lỗi cụ thể, yêu cầu nhập lại |
| **03** | Thêm mới lớp học không thành công khi nhập ký tự đặc biệt vào trường class | ielts5!0# | Hệ thống hiện thông báo lỗi cụ thể, yêu cầu nhập lại |
| **04** | Thêm mới lớp học không thành công khi nhập khoảng trắng vào trường class | ielts  5.0 | Hệ thống hiện thông báo lỗi cụ thể, yêu cầu nhập lại |
| **05** | Bỏ trống trường ClassName | (Trống) | Hệ thống hiện thông báo lỗi cụ thể, yêu cầu nhập tên |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Giáo viên đăng nhập thành công vào hệ thống.
2. **Bước 2:** Chọn mục **Dashboard/Classes** (Quản lý lớp học).
3. **Bước 3:** Nhấn nút **Create Class** (Tạo lớp).
4. **Bước 4:** Nhập dữ liệu vào trường **[ClassName]** (Tham khảo giá trị theo từng Test Case ở bảng trên). Các trường Code, Description, Status điền mặc định nếu cần.
5. **Bước 5:** Click nút **“Save”** hoặc **“Create”**.
6. **Bước 6:** So sánh kết quả hiển thị thực tế với **Expected Results**.

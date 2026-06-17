# Bảng Dữ Liệu Kiểm Thử (Data Test Thêm Mới Tên Bài Tập LTD)

| ID | Title | Assignments name | Question type | Question count | Open time | Close time | Checkbox | Expected Results |
|---|---|---|---|---|---|---|---|---|
| **01** | Thêm mới tên bài tập thành công | bai tap | Single choice | 5 | 26/04/2026 | 30/04/2026 | Show result | Hệ thống lưu và hiển thị tên bài tập trong bảng Bài tập |
| **02** | Thêm mới tên bài tập không thành công khi nhập > 20 ký tự vào trường Assignments name | bai tap trac nghiem tieng anh tong hop | Fill blank | 2 | 26/04/2026 | 30/04/2026 | Show explanation | Hệ thống hiện thông báo lỗi cụ thể |
| **03** | Thêm mới tên bài tập không thành công khi để trống trường Assignments name | (Trống) | Single choice | 1 | 26/04/2026 | 30/04/2026 | (Trống) | Hệ thống hiện popup thông báo lỗi cụ thể |
| **04** | Thêm mới tên bài tập không thành công khi nhập ký tự #@$ | @#$ | Fill blank | 2 | 26/04/2026 | 30/04/2026 | (Trống) | Hệ thống hiện popup thông báo lỗi cụ thể |
| **05** | Thêm mới tên bài tập không thành công khi để trống trường Question count | bai tap ve nha | Fill blank | (Trống) | (Trống) | (Trống) | (Trống) | Hệ thống hiện popup thông báo lỗi Question count must be > 0 |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Đăng nhập vào hệ thống thành công.
2. **Bước 2:** Click vào menu **Assignments** ở thanh điều hướng (sidebar).
3. **Bước 3:** Nhấn nút **Create**.
4. **Bước 4:** Điền thông tin vào form (Assignments name, Question type, Question count, Open time, Close time, Show result...) theo từng test case.
5. **Bước 5:** Click nút **Create** để lưu bài tập.
6. **Bước 6:** So sánh kết quả hiển thị thực tế với **Expected Results**.

# Bảng Dữ Liệu Kiểm Thử (Data Test Fill Blank)

| ID | Title | Question content | Correct answer | Explanation | Expected Results |
|---|---|---|---|---|---|
| **01** | Thêm mới câu hỏi thành công | hom nay la thu may | chu nhat | hom nay là chu nhat | Hệ thống thêm mới câu hỏi thành công, đồng thời hiển thị câu hỏi xuống phía dưới dưới dạng List |
| **02** | Thêm mới câu hỏi không thành công khi để trống Question content | (Trống) | chu nhat | hom nay là chu nhat | Hệ thống hiện lỗi Content required |
| **03** | Thêm mới câu hỏi không thành công khi nhập ký tự $#@ vào trường Question content | hom nay la thu may ? #@$ | chu nhat | hom nay là chu nhat | Hệ thống hiện lỗi Create failed |
| **04** | Thêm mới câu hỏi không thành công khi nhập ký tự $#@ vào trường Correct answer | hom nay la thu may | chu nhat !#@$ | hom nay là chu nhat | Hệ thống hiện lỗi (Dự kiến: Create failed hoặc thông báo lỗi) |
| **05** | Thêm mới câu hỏi không thành công khi để trống Correct answer | hom nay la thu may | (Trống) | hom nay là chu nhat | Hệ thống hiện lỗi Content required |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Đăng nhập vào hệ thống thành công (Sử dụng Hoangtrungmanh24@gmail.com).
2. **Bước 2:** Click vào menu **Assignments** ở thanh điều hướng.
3. **Bước 3:** Nhấn nút **Q (Thêm câu hỏi)** của bài tập loại Fill blank.
4. **Bước 4:** Điền nội dung câu hỏi vào trường **Question content**.
5. **Bước 5:** Điền đáp án vào trường **Correct answer**.
6. **Bước 6:** Nhập giải thích vào trường **Explanation**.
7. **Bước 7:** Click **Create Question**.
8. **Bước 8:** Đánh giá kết quả hiển thị so với **Expected Results**.

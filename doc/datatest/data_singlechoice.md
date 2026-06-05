# Bảng Dữ Liệu Kiểm Thử (Data Test Single Choice)

| ID | Title | Question content | Option A | Option B | Option C | Option D | Correct Answer | Explanation | Expected Results |
|---|---|---|---|---|---|---|---|---|---|
| **01** | Thêm mới câu hỏi thành công | Hom nay la thu may? | thuhai | thu ba | thu tu | thubay | D | hom nay la thu bay | Hệ thống thêm mới câu hỏi thành công, đồng thời hiển thị câu hỏi xuống phía dưới dưới dạng List |
| **02** | Thêm mới câu hỏi không thành công khi để trống 1 trong 4 Option | Hom nay la thu may? | thuhai | (Trống) | (Trống) | (Trống) | A | hom nay la thu hai | Hệ thống hiện popup lỗi All options A B C D are required |
| **03** | Thêm mới câu hỏi không thành công khi để trống cả 4 Option | Hom nay la thu may? | (Trống) | (Trống) | (Trống) | (Trống) | A | hom nay la thu hai | Hệ thống hiện lỗi, không thể thêm mới câu hỏi |
| **04** | Thêm mới câu hỏi không thành công khi để trống Question content | (Trống) | thuhai | thu ba | thu tu | thubay | D | hom nay la thu bay | Hệ thống hiện lỗi, không thể thêm mới câu hỏi |

---

### Chi tiết các bước thực hiện chung
1. **Bước 1:** Đăng nhập vào hệ thống thành công (Sử dụng Hoangtrungmanh24@gmail.com).
2. **Bước 2:** Click vào menu **Assignments** ở thanh điều hướng.
3. **Bước 3:** Nhấn nút **Q (Thêm câu hỏi)** của bài tập tương ứng.
4. **Bước 4:** Điền nội dung câu hỏi vào trường **Question content**.
5. **Bước 5:** Điền các phương án A, B, C, D.
6. **Bước 6:** Chọn đáp án đúng từ dropdown.
7. **Bước 7:** Nhập Explanation (Giải thích).
8. **Bước 8:** Click **Create Question**.
9. **Bước 9:** Đánh giá kết quả hiển thị so với **Expected Results**.

# Bảng Dữ Liệu Kiểm Thử (Data Test Profile - Updated)

| ID | Title | Name (input) | Phone (input) | Expected Results |
|---|---|---|---|---|
| **01** | Cập nhật thông tin thành công | nguyenthuhang | 9876543210 | Hệ thống lưu và cập nhật thông tin mới thành công |
| **02** | Trống Name | (Trống) | 9876543210 | Hệ thống hiện thông báo lỗi “ Update failed” |
| **03** | Name > 25 ký tự | nguyenthuhangnguyenthuhangg | 9876543210 | Hệ thống hiện thông báo lỗi “ Update failed” |
| **04** | Name có dấu space | ng uye nthuhang | 9876543210 | Hệ thống hiện thông báo lỗi “ Update failed” |
| **05** | Trống Phone | nguyenthuhang | (Trống) | Hệ thống hiện thông báo lỗi “ Update failed” |
| **06** | Sai định dạng Phone | nguyenthuhang | mothai | Hệ thống hiện thông báo lỗi “ Update failed” |
| **07** | Phone có dấu space | nguyenthuhang | 98 765 43210 | Hệ thống hiện thông báo lỗi “ Update failed” |
| **08** | Trùng Phone CSDL | nguyenthuhang | 9876543210 | Hệ thống hiện thông báo lỗi “ Update failed” |
| **09** | Phone > 11 ký tự | nguyenthuhang | 987654321023 | Hệ thống hiện thông báo lỗi “ Update failed” |
| **10** | Cập nhật liên tiếp | Nhiều giá trị | Nhiều giá trị | Sau mỗi lần cập nhật, hệ thống đều cập nhật thành công |

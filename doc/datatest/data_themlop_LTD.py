TEST_CASES_THEMLOP_LTD = [
    {
        "id": "01",
        "name": "Thêm lớp học mới thành công",
        "classname": "ielts5",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Thêm mới lớp học không thành công khi điền quá giới hạn ký tự tên lớp học",
        "classname": "ielts5ielts5ielts5ielts5",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Thêm mới lớp học không thành công khi nhập ký tự đặc biệt vào trường class",
        "classname": "ielts5!0#",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Thêm mới lớp học không thành công khi nhập khoảng trắng vào trường class",
        "classname": "ielts  5.0",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Bỏ trống trường ClassName",
        "classname": "",
        "expect_success": False
    }
]

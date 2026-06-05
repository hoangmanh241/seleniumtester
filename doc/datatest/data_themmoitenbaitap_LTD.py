TEST_CASES_THEMMOITENBAITAP_LTD = [
    {
        "id": "01",
        "name": "Thêm mới tên bài tập thành công",
        "assignment_name": "bai tap",
        "question_type": "Single choice",
        "question_count": "5",
        "open_time": "04262026",
        "close_time": "04302026",
        "checkbox": "Show result",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Thêm mới tên bài tập không thành công khi nhập > 20 ký tự vào trường Assignments name",
        "assignment_name": "bai tap trac nghiem tieng anh tong hop",
        "question_type": "Fill blank",
        "question_count": "2",
        "open_time": "04262026",
        "close_time": "04302026",
        "checkbox": "Show explanation",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Thêm mới tên bài tập không thành công khi để trống trường Assignments name",
        "assignment_name": "",
        "question_type": "Single choice",
        "question_count": "1",
        "open_time": "04262026",
        "close_time": "04302026",
        "checkbox": "",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Thêm mới tên bài tập không thành công khi nhập ký tự #@$",
        "assignment_name": "@#$",
        "question_type": "Fill blank",
        "question_count": "2",
        "open_time": "04262026",
        "close_time": "04302026",
        "checkbox": "",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Thêm mới tên bài tập không thành công khi để trống trường Question count",
        "assignment_name": "bai tap ve nha",
        "question_type": "Fill blank",
        "question_count": "",
        "open_time": "",
        "close_time": "",
        "checkbox": "",
        "expect_success": False
    }
]

TEST_CASES_FILLBLANK = [
    {
        "id": "01",
        "name": "Thêm mới câu hỏi thành công",
        "content": "hom nay la thu may",
        "correct_answer": "chu nhat",
        "explanation": "hom nay là chu nhat",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Thêm mới câu hỏi không thành công khi để trống Question content",
        "content": "",
        "correct_answer": "chu nhat",
        "explanation": "hom nay là chu nhat",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Thêm mới câu hỏi không thành công khi nhập ký tự $#@ vào trường Question content",
        "content": "hom nay la thu may ? #@$",
        "correct_answer": "chu nhat",
        "explanation": "hom nay là chu nhat",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Thêm mới câu hỏi không thành công khi nhập ký tự $#@ vào trường Correct answer",
        "content": "hom nay la thu may",
        "correct_answer": "chu nhat !#@$",
        "explanation": "hom nay là chu nhat",
        "expect_success": False
    },
    {
        "id": "05",
        "name": "Thêm mới câu hỏi không thành công khi để trống Correct answer",
        "content": "hom nay la thu may",
        "correct_answer": "",
        "explanation": "hom nay là chu nhat",
        "expect_success": False
    }
]

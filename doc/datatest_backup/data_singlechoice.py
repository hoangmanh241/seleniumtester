TEST_CASES_SINGLECHOICE = [
    {
        "id": "01",
        "name": "Thêm mới câu hỏi thành công",
        "content": "Hom nay la thu may?",
        "opt_a": "thuhai",
        "opt_b": "thu ba",
        "opt_c": "thu tu",
        "opt_d": "thubay",
        "correct": "D",
        "explanation": "hom nay la thu bay",
        "expect_success": True
    },
    {
        "id": "02",
        "name": "Thêm mới câu hỏi không thành công khi để trống 1 trong 4 Option",
        "content": "Hom nay la thu may?",
        "opt_a": "thuhai",
        "opt_b": "",
        "opt_c": "",
        "opt_d": "",
        "correct": "A",
        "explanation": "hom nay la thu hai",
        "expect_success": False
    },
    {
        "id": "03",
        "name": "Thêm mới câu hỏi không thành công khi để trống cả 4 Option",
        "content": "Hom nay la thu may?",
        "opt_a": "",
        "opt_b": "",
        "opt_c": "",
        "opt_d": "",
        "correct": "A",
        "explanation": "hom nay la thu hai",
        "expect_success": False
    },
    {
        "id": "04",
        "name": "Thêm mới câu hỏi không thành công khi để trống Question content",
        "content": "",
        "opt_a": "thuhai",
        "opt_b": "thu ba",
        "opt_c": "thu tu",
        "opt_d": "thubay",
        "correct": "D",
        "explanation": "hom nay la thu bay",
        "expect_success": False
    }
]

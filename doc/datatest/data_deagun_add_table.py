TEST_CASES_ADD_TABLE = [
    {
        "id": "TC_TB01",
        "name": "(TH1) Thêm bàn thành công",
        "table_name": "Bàn 01",
        "area": "Tầng 1",
        "capacity": "4",
        "expect_success": True
    },
    {
        "id": "TC_TB02",
        "name": "(TH6) Để trống Tên bàn (B)",
        "table_name": "",
        "area": "Tầng 1",
        "capacity": "4",
        "expect_success": False
    },
    {
        "id": "TC_TB03",
        "name": "(TH5) Tên bàn > 50 kí tự (F)",
        "table_name": "a"*51,
        "area": "Tầng 1",
        "capacity": "4",
        "expect_success": False
    },
    {
        "id": "TC_TB04",
        "name": "(TH5) Tên bàn đã tồn tại (F)",
        "table_name": "Bàn 01",
        "area": "Tầng 1",
        "capacity": "4",
        "expect_success": False
    },
    {
        "id": "TC_TB05",
        "name": "(TH3) Để trống Sức chứa (B)",
        "table_name": "Bàn 02",
        "area": "Tầng 1",
        "capacity": "",
        "expect_success": False
    },
    {
        "id": "TC_TB06",
        "name": "(TH2) Sức chứa < mức tối thiểu (F)",
        "table_name": "Bàn 02",
        "area": "Tầng 1",
        "capacity": "0",
        "expect_success": False
    }
]

TEST_CASES_CREATE_ORDER = [
    {
        "id": "TC_DH01",
        "name": "(TH1) Tạo đơn thành công",
        "customer_name": "Bàn 05",
        "total_amount": "150000",
        "expect_success": True
    },
    {
        "id": "TC_DH02",
        "name": "(TH6) Để trống Tên KH/Số bàn (B)",
        "customer_name": "",
        "total_amount": "150000",
        "expect_success": False
    },
    {
        "id": "TC_DH03",
        "name": "(TH5) Tên KH/Số bàn < 2 kí tự (F)",
        "customer_name": "A",
        "total_amount": "150000",
        "expect_success": False
    },
    {
        "id": "TC_DH04",
        "name": "(TH5) Tên KH/Số bàn > 100 kí tự (F)",
        "customer_name": "a"*101,
        "total_amount": "150000",
        "expect_success": False
    },
    {
        "id": "TC_DH05",
        "name": "(TH4) Để trống Tổng tiền (B)",
        "customer_name": "Bàn 05",
        "total_amount": "",
        "expect_success": False
    },
    {
        "id": "TC_DH06",
        "name": "(TH3) Tổng tiền <= 0 (F)",
        "customer_name": "Bàn 05",
        "total_amount": "-50",
        "expect_success": False
    }
]

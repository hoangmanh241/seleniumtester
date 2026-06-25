TEST_CASES_ADD_MENU_ITEM = [
    {
        "id": "TC_TM01",
        "name": "(TH1) Thêm món thành công (Hợp lệ)",
        "item_name": "Gà rán",
        "price": "50000",
        "expect_success": True
    },
    {
        "id": "TC_TM02",
        "name": "(TH5) Để trống Tên món (B)",
        "item_name": "",
        "price": "50000",
        "expect_success": False
    },
    {
        "id": "TC_TM03",
        "name": "(TH4) Tên món < 2 kí tự (F)",
        "item_name": "A",
        "price": "50000",
        "expect_success": False
    },
    {
        "id": "TC_TM04",
        "name": "(TH3) Để trống Giá bán (B)",
        "item_name": "Pizza",
        "price": "",
        "expect_success": False
    },
    {
        "id": "TC_TM05",
        "name": "(TH2) Giá bán < mức tối thiểu (F)",
        "item_name": "Pizza",
        "price": "-5",
        "expect_success": False
    }
]

import os
import json
import webbrowser

def generate_html_report(report_title, results, output_file_path):
    """
    Tạo báo cáo dạng HTML (Allure Style) từ danh sách kết quả test.
    results: list of dictionaries, ví dụ: [{"ID": "01", "Testcase": "Tên test", "Pass/Fail": "Pass/Fail"}]
    """
    passed = sum(1 for r in results if str(r.get('Pass/Fail', '')).lower() == 'pass')
    failed = sum(1 for r in results if str(r.get('Pass/Fail', '')).lower() == 'fail')
    broken = 0
    skipped = 0
    unknown = 0
    
    total = passed + failed + broken + skipped + unknown
    pass_percent = round((passed / total * 100), 2) if total > 0 else 0
    
    # Render test cases list
    test_items_html = ""
    for r in results:
        status = str(r.get('Pass/Fail', '')).lower()
        if status == 'pass':
            color = "#97cc64"
            icon = "P" # P for pass, or a checkmark
            bg_color = "#e8f5e9"
        else:
            color = "#fd5a3e"
            icon = "F" # F for fail
            bg_color = "#ffebee"
            
        test_name = r.get('Testcase', 'Unknown test')
        test_id = r.get('ID', '')
        display_name = f"{test_id}_{test_name}" if test_id else test_name
        
        test_items_html += f"""
        <div class="test-item">
            <div class="test-name">
                <span class="chevron">></span> {display_name}
            </div>
            <div class="test-status" style="background-color: {color};">
                {"✓" if status == 'pass' else "✗"}
            </div>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{report_title}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #ffffff;
            color: #333;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .report-container {{
            width: 100%;
            max-width: 800px;
        }}
        h2.status-title {{
            text-align: left;
            font-size: 18px;
            font-weight: normal;
            margin-bottom: 20px;
            color: #333;
        }}
        .chart-section {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 30px;
            gap: 50px;
        }}
        .chart-container {{
            position: relative;
            width: 250px;
            height: 250px;
        }}
        .chart-center-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 32px;
            color: #333;
        }}
        .legend {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            font-size: 14px;
        }}
        .legend-color {{
            width: 16px;
            height: 16px;
            border-radius: 3px;
            margin-right: 10px;
        }}
        
        .image-caption {{
            text-align: center;
            font-size: 16px;
            margin: 20px 0;
        }}
        
        .execution-list-title {{
            font-weight: bold;
            font-size: 18px;
            margin-top: 20px;
            margin-bottom: 15px;
        }}
        
        .test-list-card {{
            border: 1px solid #f0f0f0;
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            background: #fff;
            padding: 10px;
            margin-bottom: 20px;
        }}
        
        .test-item {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 10px;
            border-bottom: 1px dashed #eee;
        }}
        .test-item:last-child {{
            border-bottom: none;
        }}
        .test-name {{
            font-size: 13px;
            color: #666;
            display: flex;
            align-items: center;
        }}
        .chevron {{
            color: #ccc;
            margin-right: 8px;
            font-size: 12px;
        }}
        .test-status {{
            color: white;
            font-size: 12px;
            font-weight: bold;
            width: 18px;
            height: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 3px;
        }}
        
    </style>
</head>
<body>

<div class="report-container">
    <h2 class="status-title">STATUS</h2>
    
    <div class="chart-section">
        <div class="chart-container">
            <canvas id="statusChart"></canvas>
            <div class="chart-center-text">{pass_percent}%</div>
        </div>
        
        <div class="legend">
            <div class="legend-item"><div class="legend-color" style="background: #fd5a3e;"></div> Failed</div>
            <div class="legend-item"><div class="legend-color" style="background: #ffd050;"></div> Broken</div>
            <div class="legend-item"><div class="legend-color" style="background: #97cc64;"></div> Passed</div>
            <div class="legend-item"><div class="legend-color" style="background: #aaaaaa;"></div> Skipped</div>
            <div class="legend-item"><div class="legend-color" style="background: #d35ebe;"></div> Unknown</div>
        </div>
    </div>
    
    <div class="image-caption">
        Tỷ lệ pass/fail kiểm thử: {report_title}
    </div>
    
    <div class="execution-list-title">
        * Danh sách thực thi:
    </div>
    
    <div class="test-list-card">
        {test_items_html}
    </div>
    
    <div class="image-caption" style="font-size: 13px; color: #666;">
        Kết quả kiểm thử thực tế ({total} tests)
    </div>
    
</div>

<script>
    const ctx = document.getElementById('statusChart').getContext('2d');
    
    // Values
    const dataValues = [{failed}, {broken}, {passed}, {skipped}, {unknown}];
    
    // To prevent empty chart if all are 0
    let chartData = dataValues;
    let chartColors = ['#fd5a3e', '#ffd050', '#97cc64', '#aaaaaa', '#d35ebe'];
    
    if ({total} === 0) {{
        chartData = [0, 0, 0, 0, 1];
        chartColors = ['#fd5a3e', '#ffd050', '#97cc64', '#aaaaaa', '#e0e0e0']; // show empty ring
    }}

    new Chart(ctx, {{
        type: 'doughnut',
        data: {{
            labels: ['Failed', 'Broken', 'Passed', 'Skipped', 'Unknown'],
            datasets: [{{
                data: chartData,
                backgroundColor: chartColors,
                borderWidth: 0,
                hoverOffset: 4
            }}]
        }},
        options: {{
            responsive: true,
            maintainAspectRatio: false,
            cutout: '75%',
            plugins: {{
                legend: {{
                    display: false // We use custom HTML legend
                }},
                tooltip: {{
                    callbacks: {{
                        label: function(context) {{
                            let label = context.label || '';
                            if (label) {{
                                label += ': ';
                            }}
                            if (context.parsed !== null) {{
                                label += context.parsed;
                            }}
                            return label;
                        }}
                    }}
                }}
            }},
            animation: {{
                animateScale: true,
                animateRotate: true
            }}
        }}
    }});
</script>

</body>
</html>
"""

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Bao cao HTML da duoc tao tai: {output_file_path}")
    
    # Tự động mở file HTML bằng trình duyệt mặc định
    try:
        abs_path = os.path.abspath(output_file_path)
        # webbrowser.open hỗ trợ truyền đường dẫn file tuyệt đối
        webbrowser.open(f"file:///{abs_path.replace(os.sep, '/')}")
    except Exception as e:
        print(f"Khong the tu dong mo trinh duyet: {e}")

if __name__ == "__main__":
    # Test thử chức năng
    sample_data = [
        {"ID": "QD_DN_03", "Testcase": "InvalidEmailFormat_ValidPassword_ShouldFail", "Pass/Fail": "Pass"},
        {"ID": "QD_DN_06", "Testcase": "EmptyEmail_EmptyPassword_ShouldFail", "Pass/Fail": "Pass"},
        {"ID": "QD_DN_01", "Testcase": "ValidEmail_ValidPassword_ShouldSucceed", "Pass/Fail": "Fail"}
    ]
    generate_html_report("Chức năng Đăng nhập", sample_data, "sample_report.html")

import os
import glob
import re

def patch_files():
    files = glob.glob('test_*.py')
    for f in files:
        if f == 'test_login_BQD.py':
            continue # Already done
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Add import
        if 'from html_reporter import generate_html_report' not in content:
            content = content.replace('import os\n', 'import os\nfrom html_reporter import generate_html_report\n')
            
        # Add HTML report generation
        if 'generate_html_report(' not in content:
            # Find the title from print statement
            title_match = re.search(r'print\(f"Hoàn thành! Báo cáo (.*?) đã được', content)
            if not title_match:
                title_match = re.search(r'print\(f"Hoàn thành! (.*?) đã được', content)
                
            title = title_match.group(1) if title_match else "Kiểm thử tự động"
            
            replacement = f"""    wb.save(report_file)
    
    # XUẤT FILE HTML
    html_report_file = report_file.replace('.xlsx', '.html')
    generate_html_report("{title}", results, html_report_file)"""
            
            content = content.replace('    wb.save(report_file)', replacement)
            
            # Update print statement
            content = re.sub(r'(print\(f"Hoàn thành!.*?)\{report_file\}"\)', r'\1{report_file} và {html_report_file}")', content)

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"Patched {f}")

if __name__ == '__main__':
    patch_files()

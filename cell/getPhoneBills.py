import sys
import subprocess
from datetime import datetime, timedelta

def call_download_script(month_string):
    subprocess.run(['./download_att.sh', month_string], check=True)

def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("Usage: python getPhoneBills.py <startMonth_yyyymm> ?<endMonth_yyyymm>")
        sys.exit(1)

    start_month = datetime.strptime(sys.argv[1], '%Y%m')

    if len(sys.argv) == 2:
        end_month = datetime.now()
    else:
        end_month = datetime.strptime(sys.argv[2], '%Y%m')

    months = list()
    curr_month = start_month
    while curr_month <= end_month:
        months.append(curr_month.strftime('%Y%m'))
        curr_month += timedelta(days=31)

    for month in months:
        subprocess.run(['./download_att.sh', month], check=True)


if __name__ == "__main__":
    main()

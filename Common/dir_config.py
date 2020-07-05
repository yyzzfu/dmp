import os

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
screenshot_dir = os.path.join(base_dir, "Outputs/screenshots")
log_dir = os.path.join(base_dir, "Outputs/logs")
report_dir = os.path.join(base_dir, "Outputs/reports")
code_picture_dir = os.path.join(base_dir, "Outputs/code_pictures")

if __name__ == '__main__':

    print(base_dir)
    print(screenshot_dir)
    print(log_dir)
    print(report_dir)
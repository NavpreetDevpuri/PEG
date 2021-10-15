__all__ = ["Peg"]

import pyautogui
import os


class Peg:
    def __init__(self, project_dir):
        self.screenshots_dir = os.path.join(project_dir, "screenshots")
        self.tasks_config = os.path.join(project_dir, "tasks.json")
        screenshot_names = os.listdir(self.screenshots_dir)
        self.screenshot_name_to_path_map = self.get_screenshot_name_to_path_map(screenshot_names)

    def get_screenshot_name_to_path_map(self, screenshot_names):
        screenshot_name_to_path_map = {}
        for screenshot_name in screenshot_names:
            screenshot_path = os.path.join(self.screenshots_dir, screenshot_name)
            screenshot_name_to_path_map[screenshot_name] = screenshot_path
        return screenshot_name_to_path_map

    def open_run_command_window(self):
        0

    def open_file_or_folder_from_run_command_window(self, file_path):
        0

    def open_file_from_file_explorer_using_keyword(self, file_path):
        0

    def download_file_from_url_using_chrome(self, file_url):
        0


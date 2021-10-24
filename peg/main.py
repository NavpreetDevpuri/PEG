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
        pyautogui.hotkey('win', 'r')

    def open_file_or_folder_from_run_command_window(self,file_or_folder_path):
        # open run window
        pyautogui.hotkey('win', 'r')
        # write path in run window
        pyautogui.write(file_or_folder_path)
        # press enter so that we go to that  path
        pyautogui.hotkey('enter')

    def download_file_from_url_using_chrome(self,file_url):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('chrome')
        # open chrome
        pyautogui.hotkey('enter', interval=3)
        # We got to enter url section
        pyautogui.hotkey('alt', 'd')
        # paste the given file url so that we can download the file
        pyautogui.write(file_url)
        # let file load first then we download
        pyautogui.hotkey('enter', interval=3)
        pyautogui.hotkey('ctrl', 's', interval=1)
        # if window is there then we have to press enter button to download file
        pyautogui.hotkey('enter')
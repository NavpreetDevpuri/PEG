__all__ = ["Peg"]

import pyautogui
import os

from constants import MouseButtons

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

    def open_chrome(self):
        self.open_run_command_window()
        pyautogui.write('chrome')
        pyautogui.hotkey('enter', interval=3)

    def open_file_or_folder_from_run_command_window(self, file_or_folder_path):
        # open run window
        self.open_run_command_window()
        # write path in run window
        pyautogui.write(file_or_folder_path)
        # press enter so that we go to that  path
        pyautogui.hotkey('enter')

    def download_file_from_url_using_chrome(self, file_url):
        self.open_chrome()
        # We got to enter url section
        pyautogui.hotkey('alt', 'd')
        # paste the given file url so that we can download the file
        pyautogui.write(file_url)
        # let file load first then we download
        pyautogui.hotkey('enter', interval=3)
        pyautogui.hotkey('ctrl', 's', interval=1)
        # if window is there then we have to press enter button to download file
        pyautogui.hotkey('enter')


    def click_at(
        self,
        image_file_path,
        click_coordinates=(50, 50),
        mouse_button_click_action=pyautogui.leftClick,
        **kwargs,
    ):
        available_click_actions = {
            pyautogui.leftClick,
            pyautogui.middleClick,
            pyautogui.rightClick,
        }

        # Not a 'MouseButtons' constant
        if mouse_button_click_action not in available_click_actions:
            raise ValueError(
                f'Invalid "mouse_button_click_action": {mouse_button_click_action}'
            )

        x, y = click_coordinates

        image_location = pyautogui.locateOnScreen(image_file_path, **kwargs)

        # Could not find the image
        if not image_location:
            raise Exception(f"Unable to locate given image: {image_file_path}")

        left, top = image_location.left, image_location.top

        x += top
        y += left

        mouse_button_click_action(x, y)

    def change_power_options(self,screen_off_on_battery, screen_off_when_plugged, sleep_on_battery,
                             sleep_when_plugged):
        self.open_run_command_window()
        pyautogui.write('powershell')
        pyautogui.hotkey('enter', interval=1)
        pyautogui.write(f'powercfg /change monitor-timeout-dc {screen_off_on_battery}')
        pyautogui.hotkey('enter', interval=1)
        pyautogui.write(f'powercfg /change monitor-timeout-ac {screen_off_when_plugged}')
        pyautogui.hotkey('enter', interval=1)
        pyautogui.write(f'powercfg /change standby-timeout-dc {sleep_on_battery}')
        pyautogui.hotkey('enter', interval=1)
        pyautogui.write(f'powercfg /change standby-timeout-ac {sleep_when_plugged}')
        pyautogui.hotkey('enter', interval=1)
        # close the window
        pyautogui.write('exit')
        pyautogui.hotkey('enter')

import os
import shutil
import telebot
import time



TELEGIRAM_BOT_TOKEN = '6503938650:AAGDWE_8RnqSRftHT-HH7aUBEu3f12FvoU4'
bot = telebot.Telebot(TELEGIRAM_BOT_TOKEN)

def copy_folder(source_data, destination_folder, dirs_exist_ok):
    try:
        start_time = time.time()
        shutil.copytree(source_data, destination_folder, dirs_exist_ok=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Folder copied from {source_data} to {destination_folder}, in {elapsed_time:.2f} seconds ")
        return True
    except:
        print(f"error: {e}")
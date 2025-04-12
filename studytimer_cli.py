import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def init():
    try:
        work_hours = int(input("Çalışma süresini saat cinsinden girin: "))
        work_minutes = int(input("Çalışma süresini dakika cinsinden girin: "))
        work_seconds = int(input("Çalışma süresini saniye cinsinden girin: "))
    except ValueError:
        print("Geçersiz giriş! Lütfen geçerli bir sayı girin.")
        exit()

    work_time = (work_hours * 3600) + (work_minutes * 60) + work_seconds
    
    return work_time

def update(work_time):
    for remaining_time in range(work_time, 0, -1):
        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        seconds = remaining_time % 60

        clear_screen()
        print_colored(f"Çalışma süresi: {hours:02}:{minutes:02}:{seconds:02}", "32")  # Yeşil
        time.sleep(1)

    clear_screen()
    print_colored("Çalışma süresi bitti!", "31")

def mainloop():
    running = True
    while running:
        work_time = init()
        clear_screen()
        update(work_time)
        
        user_input = input("Yine çalışmak ister misiniz? (Evet/Hayır): ").strip().lower()
        if user_input != "evet":
            running = False

if __name__ == "__main__":
    mainloop()

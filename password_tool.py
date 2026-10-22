import random
import string
import base64

def generate_password(length=12, use_digits=True, use_special=True):
    """Генерирует случайный надежный пароль."""
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special = "!@#$%^&*()_+-=" if use_special else ""
    
    all_chars = letters + digits + special
    if not all_chars:
        return ""
    
    # Гарантируем, что в пароле будет хотя бы одна буква
    password = [random.choice(letters)]
    
    # Заполняем остальную длину
    for _ in range(length - 1):
        password.append(random.choice(all_chars))
        
    # Перемешиваем символы, чтобы первая буква не всегда была в начале
    random.shuffle(password)
    return "".join(password)

def save_password(service, password, filename="vault.txt"):
    """Кодирует пароль в Base64 и сохраняет в файл."""
    # Кодируем, чтобы скрыть пароль от случайных глаз при открытии файла
    encoded_bytes = base64.b64encode(password.encode("utf-8"))
    encoded_password = encoded_bytes.decode("utf-8")
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{service}:{encoded_password}\n")
    print(f"💾 Пароль для '{service}' успешно зашифрован и сохранен в {filename}!")

def show_vault(filename="vault.txt"):
    """Читает и расшифровывает сохраненные пароли."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("\n--- СОХРАНЕННЫЕ ПАРОЛИ ---")
            for line in f:
                if ":" in line:
                    service, encoded_password = line.strip().split(":", 1)
                    # Декодируем обратно в текст
                    decoded_bytes = base64.b64decode(encoded_password.encode("utf-8"))
                    decoded_password = decoded_bytes.decode("utf-8")
                    print(f"Сервис: {service} | Пароль: {decoded_password}")
            print("---------------------------")
    except FileNotFoundError:
        print("📭 Хранилище паролей пока пусто.")

def main():
    while True:
        print("\n=== SMART PASSWORD TOOL ===")
        print("1. Сгенерировать новый пароль")
        print("2. Сгенерировать и сохранить в хранилище")
        print("3. Посмотреть сохраненные пароли")
        print("4. Выйти")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice in ("1", "2"):
            try:
                length = int(input("Введите длину пароля (рекомендуется от 12): "))
                pwd = generate_password(length)
                print(f"🔑 Ваш новый надежный пароль: {pwd}")
                
                if choice == "2":
                    service = input("Для какого сервиса этот пароль? (например, Google, Discord): ")
                    if service.strip():
                        save_password(service, pwd)
            except ValueError:
                print("⚠️ Ошибка: Длина должна быть числом.")
                
        elif choice == "3":
            show_vault()
        elif choice == "4":
            print("👋 Безопасного вам интернета! Пока!")
            break
        else:
            print("⚠️ Неверный выбор.")

if __name__ == "__main__":
    main()

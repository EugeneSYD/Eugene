import json
import os
from datetime import datetime

class TodoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Загружает задачи из JSON файла."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        """Сохраняет текущие задачи в JSON файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    def add_task(self, title):
        """Добавляет новую задачу в список."""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✔️ Задача '{title}' успешно добавлена!")

    def list_tasks(self):
        """Выводит список всех задач."""
        if not self.tasks:
            print("📭 Ваш список задач пока пуст.")
            return
        
        print("\n--- ВАШ СПИСОК ЗАДАЧ ---")
        for task in self.tasks:
            status = "✅" if task["completed"] else "❌"
            print(f"[{task['id']}] {status} {task['title']} (Создано: {task['created_at']})")
        print("------------------------")

    def complete_task(self, task_id):
        """Отмечает задачу как выполненную."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"🎉 Задача [{task_id}] выполнена!")
                return
        print("⚠️ Задача с таким ID не найдена.")

def main():
    manager = TodoManager()
    
    while True:
        print("\n=== МЕНЕДЖЕР ЗАДАЧ ===")
        print("1. Посмотреть список дел")
        print("2. Добавить новую задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Выйти из программы")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == "1":
            manager.list_tasks()
        elif choice == "2":
            title = input("Введите название задачи: ")
            if title.strip():
                manager.add_task(title)
            else:
                print("⚠️ Название задачи не может быть пустым.")
        elif choice == "3":
            manager.list_tasks()
            try:
                task_id = int(input("Введите ID выполненной задачи: "))
                manager.complete_task(task_id)
            except ValueError:
                print("⚠️ Пожалуйста, введите корректное число.")
        elif choice == "4":
            print("👋 До свидания! Хорошего дня!")
            break
        else:
            print("⚠️ Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()

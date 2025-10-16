import bluetooth

def main():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        # Привязываемся к локальному адаптеру и каналу 1
        server_sock.bind(("", 1))
        server_sock.listen(1)
        print("Ожидание соединения на RFCOMM-канале 1...")

        client_sock, client_info = server_sock.accept()
        print(f"Соединение с {client_info}")

        while True:
            data = client_sock.recv(1024)
            if not data:
                print("Клиент закрыл соединение.")
                break
            msg = data.decode(errors="replace")
            print(f"Получено: {msg}")
            # здесь ваша обработка "сигнала"
            # при необходимости отправьте ответ:
            # client_sock.send(b"ok")
    except KeyboardInterrupt:
        print("\nОстановка по Ctrl+C")
    finally:
        try:
            client_sock.close()
        except Exception:
            pass
        server_sock.close()
        print("Сокеты закрыты.")

if __name__ == "__main__":
    main()
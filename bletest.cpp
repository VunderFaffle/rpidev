#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>

int main(int argc, char **argv)
{
    struct sockaddr_rc loc_addr = { 0 }, rem_addr = { 0 };
    char buf[1024] = { 0 };
    int s, client, bytes_read;
    socklen_t opt = sizeof(rem_addr);

    // создание RFCOMM сокета
    s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);

    // связывание сокета с локальным Bluetooth-адаптером и каналом 1
    loc_addr.rc_family = AF_BLUETOOTH;
    loc_addr.rc_bdaddr = *BDADDR_ANY;
    loc_addr.rc_channel = (uint8_t) 1;
    bind(s, (struct sockaddr *)&loc_addr, sizeof(loc_addr));

    // прослушивание входящих соединений
    listen(s, 1);

    // ожидание соединения
    client = accept(s, (struct sockaddr *)&rem_addr, &opt);

    ba2str(&rem_addr.rc_bdaddr, buf);
    printf("Соединение с %s\n", buf);
    memset(buf, 0, sizeof(buf));

    // чтение данных
    bytes_read = read(client, buf, sizeof(buf));
    if( bytes_read > 0 ) {
        printf("Получено [%s]\n", buf);
        // здесь ваша обработка сигнала
    }

    // закрытие соединения
    close(client);
    close(s);
    return 0;
}
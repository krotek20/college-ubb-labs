#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#define MSG_LEN (1 << 10)

int receive_int(int serverfd, struct sockaddr_in *server, unsigned int *sock_len) {
        int nr = 0;
        recvfrom(serverfd, &nr, sizeof(nr), MSG_WAITALL, (struct sockaddr *) server, sock_len);
        return ntohl(nr);
}

void send_int(int serverfd, struct sockaddr_in *server, int nr) {
        int to_send = htonl(nr);
        sendto(serverfd, &to_send, sizeof(to_send), 0, (struct sockaddr *) server, sizeof(*server));
}

void receive_string(int serverfd, struct sockaddr_in *server, unsigned int *sock_len, char mesaj[MSG_LEN]) {
        int nr = receive_int(serverfd, server, sock_len);
        memset(mesaj, 0, MSG_LEN * sizeof(char));
        recvfrom(serverfd, mesaj, nr, MSG_WAITALL, (struct sockaddr *) server, sock_len);
}

void send_string(int serverfd, struct sockaddr_in *server, char mesaj[MSG_LEN]) {
        unsigned int len = strlen(mesaj);
        send_int(serverfd, server, len);
        sendto(serverfd, mesaj, len, 0, (struct sockaddr *) server, sizeof(*server));
}

int main() {
        struct sockaddr_in server;
        int s = socket(AF_INET, SOCK_DGRAM, 0);
        if (s < 0) {
                perror("Socket error: ");
                return 1;
        }

        memset(&server, 0, sizeof(server));
        server.sin_port = htons(1234);
        server.sin_family = AF_INET;
        server.sin_addr.s_addr = inet_addr("127.0.0.1");

        unsigned int l = sizeof(server);

        send_string(s, &server, "hello there");
        char msg[MSG_LEN];
        receive_string(s, &server, &l, msg);
        printf("%s\n", msg);
}
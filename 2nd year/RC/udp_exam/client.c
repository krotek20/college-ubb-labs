#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#define MSG_LEN (1 << 10)

unsigned receive_int(int serverfd, struct sockaddr_in *server, unsigned int *sock_len) {
        unsigned int nr = 0;
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

void generate_magic_square(int magic_square[101][101], int n) {
        // initial position
        int i = n / 2, j = n / 2 + 1;
        for(int k = 1; k <= n*n;) {
                if(i == -1 && j == n) {
                        j = n - 2;
                        i = 0;
                }
                else {
                        if(j == n) {
                                j = 0;
                        }
                        if(i == -1) {
                                i = n - 1;
                        }
                }
                if(magic_square[i][j] != 0) {
                        j -= 2;
                        i++;
                        continue;
                }
                else {
                        magic_square[i][j] = k;
                        k++;
                }
                j++;
                i--;
        }
}

void print_magic_square(int magic_square[101][101], int n) {
        for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                        printf("%d ", magic_square[i][j]);
                }
                printf("\n");
        }
}

void send_magic_square(int magic_square[101][101], int n, int serverfd, struct sockaddr_in *server) {
        for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                        int to_send_position = htonl(magic_square[i][j]);
                        sendto(serverfd, &to_send_position, sizeof(to_send_position), 0, (struct sockaddr *) server, sizeof(*server));
                }
        }
}

void exchange_info(int serverfd, struct sockaddr_in *server, int *server_len) {
        sendto(serverfd, 0, sizeof(int), 0, (struct sockaddr *) server, sizeof(*server));

        char connected_message[MSG_LEN];
        int message_len = 0;
        recvfrom(serverfd, &message_len, sizeof(message_len), MSG_WAITALL, (struct sockaddr *) server, server_len);
        message_len = ntohl(message_len);
        memset(connected_message, 0, MSG_LEN * sizeof(char));
        recvfrom(serverfd, connected_message, message_len, MSG_WAITALL, (struct sockaddr *) server, server_len);
        printf("%s\n", connected_message);

        int n = 0;
        recvfrom(serverfd, &n, sizeof(n), MSG_WAITALL, (struct sockaddr *) server, server_len);
        int n = ntohl(n);
        printf("Magic square should have %d rows and columns\n", n);

        int a = 0, b = 0;
        int magic_square[101][101];
        for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                        magic_square[i][j] = 0;
                }
        }

        generate_magic_square(magic_square, n);
        print_magic_square(magic_square, n);
        send_magic_square(magic_square, n, serverfd, server);

        while(1) {
                int L, C;
                while(1) {
                        scanf("%d", &L);
                        scanf("%d", &C);
                        if(L >= 0 && L < n && C >= 0 && C < n) {
                                break;
                        }
                }
                int to_send_L = htonl(L);
                sendto(serverfd, &to_send_L, sizeof(to_send_L), 0, (struct sockaddr *) server, sizeof(*server));
                int to_send_C = htonl(C);
                sendto(serverfd, &to_send_C, sizeof(to_send_C), 0, (struct sockaddr *) server, sizeof(*server));

                int value = 0;
                recvfrom(serverfd, &value, sizeof(value), MSG_WAITALL, (struct sockaddr *) server, server_len);
                value = ntohl(value);
                printf("value: %d\n", value)
        }
}

int main(int argc, char* argv[]) {
        if (argc != 3) {
                printf("Usage: %s ip port\n", argv[0]);
                return 1;
        }
        struct sockaddr_in server;
        int s = socket(AF_INET, SOCK_DGRAM, 0);
        if (s < 0) {
                perror("Socket error: ");
                return 2;
        }
        memset(&server, 0, sizeof(server));
        server.sin_port = htons(atoi(argv[2]));
        server.sin_family = AF_INET;
        server.sin_addr.s_addr = inet_addr(argv[1]);
        int l = sizeof(server);

        exchange_info(s, &server, &l);
}

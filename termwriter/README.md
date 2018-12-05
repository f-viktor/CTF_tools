
sudo ./termwriter -n /dev/pts/1 $(echo -en "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc")

find the pts edb is running on (1 or 2 or 3 etc)
give the above command
your input should appear in edb terminal and actually work
python echos will not work well with non-ascii chars

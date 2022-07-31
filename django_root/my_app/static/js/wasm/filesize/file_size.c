#include <stdio.h>
#include <stdlib.h>

#define TMP_FILE_NAME "dir_size.txt"

int main(int argc, char *argv[])
{
    system("touch dir_size.txt");
    system("du -sh /usr/src/app/ > dir_size.txt");

    FILE *fdir = fopen("dir_size.txt", "r");
    char buff[100];
    if (fdir)
    {
        while (1)
        {
            if (fgets(buff, 100, fdir) == NULL)
                break;
            printf("%s", buff);
        }
    }
    fclose(fdir);
    remove("dir_size.txt");
    return 0;
}
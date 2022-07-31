#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include "ftw.h"
#include <sys/types.h>
#include <sys/stat.h>

static unsigned int total = 0;

int sum(const char *fpath, const struct stat *sb, int typeflag)
{
    total += sb->st_size;
    return 0;
}

int main()
{

    char *DJANGO_ROOT = "/usr/src/app";
    printf("Getting size of %s\n", DJANGO_ROOT);
    // if (!DJANGO_ROOT || access(DJANGO_ROOT, R_OK))
    // {
    //     printf("Cannot access %s\n", DJANGO_ROOT);
    //     return 1;
    // }
    if (ftw(DJANGO_ROOT, &sum, 1))
    {
        printf("Error occured when accessing %s\n", DJANGO_ROOT);
        perror("ftw");
        return 2;
    }
    printf("Got size of %s\n", DJANGO_ROOT);
    printf("%s: %u\n", DJANGO_ROOT, total);
    return 0;
}
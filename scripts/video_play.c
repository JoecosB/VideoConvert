#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void display(int n);
int read_format();
void fk();

int main()
{   
    int con, frame_ct;
    float percentage;

    frame_ct = read_format();
    printf("\n");
    
    for(int i=0; i<frame_ct; i++)
    {
        fk();
        system("clear");
        percentage = 100.0 * (i+1)/frame_ct;
        display(i);
        printf("%.2f%%\n", percentage);
    }

    system("sh ../run.sh");
    return 0;
}

void display(int n)
/*在命令行中播放第n帧*/
{
    FILE *fp=NULL;                                                                                   
    int c, ptr=10;
    char p[80]="../frames/", p_1[10]="", p_2[7]=".frames";
    sprintf(p_1, "%d", n);
    for(int i=0; i<strlen(p_1); i++)
    {
        p[ptr] = p_1[i];
        ptr++;
    }
    for(int i=0; i<6; i++)
    {
        p[ptr] = p_2[i];
        ptr++;
    }
    p[ptr] = '\0';

    fp = fopen(p,"r");                                                                              //  打开文件

    while(1)                                                                                        //  逐行读取文件，并用printf()输出到命令行。
    {                                                                                               //
        c = fgetc(fp);                                                                              //
        if( feof(fp) )                                                                              //
        {                                                                                           //
             break ;                                                                                //
        }                                                                                           //
        printf("%c", c);                                                                            //
    }                                                                                               //
    fclose(fp);									   		                                            //
    printf("\f");												                                    //
}

void fk()
/*等待*/
{
    for(int i=0; i<100000; i++)
    {
        for(int ii=0; ii<300; ii++);

    }
}

int read_format()
{
    FILE *fp;
    char c[10];
    int r;
    
    fp = fopen("../frames/disp.format", "r");
    fscanf(fp, "%[^\n]", c);
    r = atoi(c);
    fclose(fp);

    return r;
}
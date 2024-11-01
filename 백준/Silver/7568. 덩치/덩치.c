#include <stdio.h>

int main(){
    int N,i;
    scanf("%d",&N);
    int x[50]={0,};
    int y[50]={0,};
    for(i=0;i<N;i++){
        scanf("%d %d\n",&x[i],&y[i]);
    }
    
    for(i=0;i<N;i++){
        int k=0;
        for (int j=0; j<N;j++){
            if(x[i]<x[j] && y[i]<y[j])
                k++;
        }
        printf("%d\n",k+1);
    }
}
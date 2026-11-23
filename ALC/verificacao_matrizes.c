#include <stdio.h>

int verifica_diagonal(int matriz[][10], int li, int co);

int main (){
  
    int linhas, colunas;

    printf("Quantas linhas?\n");
    scanf("%d" ,&linhas);

    printf("Quantas colunas?\n");
    scanf("%d", &colunas);

    int matriz[linhas][colunas];

    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            scanf("%d", &matriz[i][j]);
        }
    }

    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    int teste_matriz = verifica_diagonal(matriz, linhas, colunas);

    if(teste_matriz == 1){
        printf("Haduken");
    }

    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
}


int verifica_diagonal(int matriz[][10], int li, int co){
    for(int i = 0; i < li; i++){
        for(int j = 0; j < co; j++){
           if(i < j && matriz[i][j] != 0){
            return 1;
           }
        }
    }
        return 0;
}
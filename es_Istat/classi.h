#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;
typedef struct{
    char carattere[1024];
}Stringa;

class Gestione_Files {
    // Variabili di Classe)
private:
    char NomeFIle_[255];
    char Path[255];
    char CarSeparatore;

public:
     Gestione_Files(); // costruttore
     void SetNomeFile(char nomefile[255]); //SET -> assegna un valore x = 3
     void GetNomeFile(char *nome); // GET -> return x
     void SetCarSeparatore(char sep);
     char GetCarSeparatore();
     void newFile(char nomeFile[255]);
     void concatena(char str1[255], char str2[255]);
     int AggiungiRiga(char riga[255]);
     int LeggiPrimaRiga(char *Riga);
     int LeggiRigaN(char *Riga, int pos);
     int ContaRigheFile();
     int leggiTuttoFile(Stringa *strl, int nRighe);
     int split(char *s,Stringa *strl);
     int CancellaFile();
     int LeggiPrimaRigaGets(char *Riga);
};

Gestione_Files::Gestione_Files()
{
    strcpy(NomeFIle_, " ");
    CarSeparatore = ',';
}

int Gestione_Files::CancellaFile()
{
    FILE* Fp;
    int err = -1;

    Fp = fopen(NomeFIle_, "w"); // "w" cancella e riscrive

    if(Fp != NULL){
        err = 0;
        fclose(Fp);
    }
    return err;
}

void Gestione_Files::SetCarSeparatore(char sep)
{
    CarSeparatore = sep;
}

char Gestione_Files::GetCarSeparatore()
{
    return CarSeparatore;
}

void Gestione_Files::SetNomeFile(char nomefile[255])
{
    strcpy(NomeFIle_, nomefile);
}

void Gestione_Files::GetNomeFile(char *nome)
{
    strcpy(nome, NomeFIle_);
}

int Gestione_Files::LeggiPrimaRiga(char *riga)
{
    FILE* Fp;
    int err = -1;
    char st1[255];
    int nCaratteri = 0;

    Fp = fopen(NomeFIle_, "r"); // "a" scrive sul file gia esistente al fondo, mentre "w" cancella e riscrive

    if(Fp != NULL){
        err = 0;
        nCaratteri = fscanf(Fp, "%s", st1);
        if(nCaratteri < 0)
            {
                err = -2;
            }
        else
            {
                err = strlen(st1);
                strcpy(riga, st1);
            }
        fclose(Fp);
    }
    return err;
}

int Gestione_Files::LeggiPrimaRigaGets(char *riga)
{
    FILE* Fp;
    int err = -1;
    char st1[255];
    int nCaratteri = 0;

    Fp = fopen(NomeFIle_, "r"); // "a" scrive sul file gia esistente al fondo, mentre "w" cancella e riscrive

    if(Fp != NULL){
        err = 0;
        fgets(st1,255,Fp);
        nCaratteri = strlen(st1);
        if(nCaratteri < 0)
            {
                err = -2;
            }
        else
            {
                err = strlen(st1);
                strcpy(riga, st1);
            }
        fclose(Fp);
    }
    return err;
}

int Gestione_Files::AggiungiRiga(char riga[255])
{
    FILE* Fp;
    int err = -1;

    Fp = fopen(NomeFIle_, "a"); // "a" scrive sul file gia esistente al fondo, mentre "w" cancella e riscrive

    if(Fp != NULL){
        err = 0;
        fprintf(Fp, "%s\n", riga);
        fclose(Fp);
    }

    return err;
}

int Gestione_Files::LeggiRigaN(char Riga[255], int pos)
{
    FILE* Fp;
    int err = -1;
    int Nriga=0;
    char st1[255];
    int nCaratteri = 0;

    Fp = fopen(NomeFIle_, "r"); // "a" scrive sul file gia esistente al fondo, mentre "w" cancella e riscrive

    if(Fp != NULL){
        err = 0;
        nCaratteri = fscanf(Fp, "%s", st1);
        while((Nriga!=pos) && (nCaratteri>0)){
            nCaratteri = fscanf(Fp, "%s", st1);
            //printf("%s\n", st1);
            Nriga++;
        }
        if(nCaratteri < 0)
            {
                err = -2;
            }
        else
            {
                err = strlen(st1);
                strcpy(Riga, st1);
            }
        fclose(Fp);
    }
    return err;
}

int Gestione_Files::ContaRigheFile(){
    FILE* Fp;
    int err = -1;
    int Nriga=0;
    char st1[255];
    int nCaratteri=0;

    Fp = fopen(NomeFIle_, "r"); // "a" scrive sul file gia esistente al fondo, mentre "w" cancella e riscrive

    if(Fp != NULL){
        err = 0;
        nCaratteri = fscanf(Fp, "%s", st1);
        while(nCaratteri>0){
            Nriga++;
            nCaratteri = fscanf(Fp, "%s", st1);
        }
        err =Nriga;
        fclose(Fp);
    }
    return err;
}

int Gestione_Files::leggiTuttoFile(Stringa *strl, int nRighe){
    FILE* Fp;
    int err = -1;
    int Nriga=0;
    char st1[255];
    int nCaratteri=0;

    Fp = fopen(NomeFIle_, "r"); // "a" scrive sul file gia esistente al fondo, mentre "w" cancella e riscrive

    if(Fp != NULL){
        err = 0;
        nCaratteri = fscanf(Fp, "%s", st1);
        while(nCaratteri>0){
            strcpy(strl[Nriga].carattere,st1);
            printf("%d %s\n",Nriga,st1);
            Nriga++;
            nCaratteri = fscanf(Fp, "%s", st1);
        }
        err =Nriga;
        fclose(Fp);
    }
    return err;
}

int Gestione_Files::split(char *s, Stringa *strl){
    int lun, i = 0, nc = 0, j, c = 0;
    char campo[255], copia[255];

    lun = strlen(s);

    if(s[lun - 1] != CarSeparatore){
        s[lun] = CarSeparatore;
        s[lun + 1] = '\0';
    }

    while(strlen(s) > 0){
        // printf("split %s\n", s);
        i=0;
        while(s[i] != CarSeparatore){
            campo[i] = s[i];
            i++;
        }

        campo[i] = '\0';
        strcpy(strl[nc].carattere, campo);
        nc++;
        c = 0;
        for(j = i + 1; j < strlen(s); j++){
            copia[c] = s[j];
            c++;
        }
        copia[c] = '\0';
        // printf("split copia : %s\n", copia);
        strcpy(s, copia);
    }
}

void Gestione_Files::newFile(char nomeFile[255])
{
    FILE *filePTR;
    filePTR = fopen(nomeFile, "w");
    fclose(filePTR);
}

void Gestione_Files::concatena(char str1[255], char str2[255]){
    strcat(str1, ";");
    strcat(str1, str2);
}

#include <iostream>
#include <stdio.h>
#include "classi.h"
#include "Istat.h"

using namespace std;

int main()
{
    //CREO UN OGGETTO DI CLASSE FILE
    Gestione_Files files;

    //SETTO IL NOME DEL FILE
    //E IL CARATTERE SEPARATORE
    char nFile[255] = "istat.csv";
    files.SetNomeFile(nFile);
    files.SetCarSeparatore(';');

    //CONTO LE RIGHE DEL FILE E STAMPO LE RIGHE TOTALI
    int nRighe = 0;
    nRighe = files.ContaRigheFile();
    printf("%d\n", nRighe);

    //CREO LE VARIABILI
    //DI CONTROLLO
    int conta = 0;
    char riga[255];
    Stringa campi[7];
    printf("Variabili Create\n");


    //NE CARICO 1000 PER VOLTA
    istat Registro[1000];
    printf("Istat creato\n");

    printf("\n");

    for(conta = 1; conta <= 1000; conta++)
    {
        files.LeggiRigaN(riga, conta);
        files.split(riga, campi);
        printf("Comune %d:\nRiga: %d\n", conta, conta+1);
        Registro[conta - 1].setId(campi[0].carattere);
        Registro[conta - 1].setYear(campi[1].carattere);
        Registro[conta - 1].setDayMonth(campi[2].carattere);
        Registro[conta - 1].setIsComune(campi[3].carattere);
        Registro[conta - 1].setMan(campi[4].carattere);
        Registro[conta - 1].setWoman(campi[5].carattere);
        Registro[conta - 1].setTotal(campi[6].carattere);
        printf("\n");
    }

    strcpy(nFile, "Uomini.csv");
    files.newFile(nFile);

    strcpy(nFile, "Donne.csv");
    files.newFile(nFile);

    int cUomini = 0;
    int cDonne = 0;

    int i = 0;
    char nU[255];
    char nD[255];
    char id[255];
    char year[255];
    char dM[255];
    char ist[255];
    char tot[255];
    char r[255];
    while((cUomini <= 10-1 || cDonne <= 10-1) && i < 1000)
    {
        Registro[i].getMan(nU);
        Registro[i].getWoman(nD);
        printf("%d confronto: uomini: %s Donne: %s\n", i+1, nU, nD);
        strcpy(r," ");
        if(strcmp(nU, nD)>0)
        {
            if(cUomini <= 10-1)
            {
                cUomini++;
                printf("cUomini: %d\n", cUomini);
                Registro[i].getId(id);
                strcpy(r, id);
                Registro[i].getYear(year);
                files.concatena(r, year);
                Registro[i].getDayMonth(dM);
                files.concatena(r, dM);
                Registro[i].getisComune(ist);
                files.concatena(r, ist);
                files.concatena(r, nU);
                files.concatena(r, nD);
                Registro[i].getTotal(tot);
                files.concatena(r, tot);
                printf("%s\n\n", r);
                files.SetNomeFile("Uomini.csv");
                files.AggiungiRiga(r);
            }
        }
        else
        {
            if(cDonne <= 10-1)
            {
                files.SetNomeFile("Donne.csv");
                cDonne++;
                printf("cDonne: %d\n", cDonne);
                Registro[i].getId(id);
                strcpy(r, id);
                Registro[i].getYear(year);
                files.concatena(r, year);
                Registro[i].getDayMonth(dM);
                files.concatena(r, dM);
                Registro[i].getisComune(ist);
                files.concatena(r, ist);
                files.concatena(r, nU);
                files.concatena(r, nD);
                Registro[i].getTotal(tot);
                files.concatena(r, tot);
                printf("%s\n\n", r);
                files.AggiungiRiga(r);
            }

        }
        i++;
    }

    strcpy(nFile, "Maggiore.csv");
    files.newFile(nFile);

    int contatore = 0;
}

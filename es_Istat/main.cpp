#include <iostream>
#include <string.h>
#include <stdio.h>
#include "classi.h"
#include "Istat.h"

using namespace std;

void bubbleSort(istat classe[], int n)
{
    Stringa nU[2];
    int controllo;

    istat temp;
    for(int i=0; i<n-1; i++)
    {
        for(int j=0; j<n-1-i; j++)
        {
            classe[j].getMan(nU[0].carattere);
            classe[j+1].getMan(nU[1].carattere);
            controllo = strcmp(nU[1].carattere, nU[0].carattere);
            if(controllo < 0)
            {
                temp = classe[j];
                classe[j] = classe[j+1];
                classe[j+1] = temp;
            }
        }
    }
}

void stampa(istat classe[], int dim)
{
    char nU[255];
    for(int i = 0; i <= dim - 1; i++)
    {
        classe[i].getMan(nU);
        printf("pop maschile: %s\n", nU);
    }
}

int main()
{
    //CREO UN OGGETTO DI CLASSE FILE
    Gestione_Files files;
    system("PAUSE");

    //SETTO IL NOME DEL FILE
    //E IL CARATTERE SEPARATORE
    char nFile[255] = "istat.csv";
    files.SetNomeFile(nFile);
    files.SetCarSeparatore(';');
    char anno[255];
    scanf("%s", anno);

    //CONTO LE RIGHE DEL FILE E STAMPO LE RIGHE TOTALI
    int nRighe = 0;
    nRighe = files.ContaRigheFilePerAnno(1, anno);
    printf("%d\n", nRighe);
    system("PAUSE");

    //CREO LE VARIABILI
    //DI CONTROLLO
    int conta = 1;
    char riga[255];
    Stringa campi[7];
    system("PAUSE");

    //NE CARICO 1000 PER VOLTA
    istat Registro[1000];
    system("PAUSE");

    char nU[255];
    char nD[255];

    istat RegistroUomini[1000];
    istat RegistroDonne[1000];

    for(int i = 1; i <= nRighe - 1; conta++)
    {
        files.LeggiRigaN(riga, conta);
        files.split(riga, campi);
        if(strcmp(campi[1].carattere, anno) == 0)
        {
            Registro[conta - 1].setMan(campi[4].carattere);
            Registro[conta - 1].setWoman(campi[5].carattere);
            Registro[i].getMan(nU);
            Registro[i].getWoman(nD);
            if(strcmp(nU, nD)>0)
            {
                RegistroUomini[conta - 1].setId(campi[0].carattere);
                RegistroUomini[conta - 1].setYear(campi[1].carattere);
                RegistroUomini[conta - 1].setDayMonth(campi[2].carattere);
                RegistroUomini[conta - 1].setIsComune(campi[3].carattere);
                RegistroUomini[conta - 1].setMan(campi[4].carattere);
                RegistroUomini[conta - 1].setWoman(campi[5].carattere);
                RegistroUomini[conta - 1].setTotal(campi[6].carattere);
                conta++;
                bubbleSort(RegistroUomini, conta);
                //BUBBLE SORT UOMINI + SCRITTURA
            }
            /*else
            {
                //BUBBLE SORT DONNE + SCRITTURA
            }*/
            printf("\n");
        }
        stampa(RegistroUomini, conta);


/*
        int cUomini = 0;
        int cDonne = 0;



                char id[255];
                char year[255];
                char dM[255];
                char ist[255];
                char tot[255];
                char r[255];
                if(strcmp(nU, nD)>0)
                {
                    if(cUomini <= 10-1)
                    {
                        cUomini++;
                        printf("cUomini: %d\n", cUomini);

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
                i++;*/
    }
}

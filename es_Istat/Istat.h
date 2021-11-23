#include <iostream>
#include <string.h>

class istat
{
private:
    char id_[255];
    char year_[255];
    char dayMonth_[255];
    char isComune_[255];
    char man_[255];
    char woman_[255];
    char total_[255];

public:
    istat();
    void getId(char id[255])
    {
        strcpy(id, id_);
    };
    void getYear(char y[255])
    {
        strcpy(y, year_);
    };
    void getDayMonth(char dM[255])
    {
        strcpy(dM, dayMonth_);
    };
    void getisComune(char ist[255])
    {
        strcpy(ist, isComune_);
    };
    void getMan(char mn[255])
    {
        strcpy(mn, man_);
    };
    void getWoman(char wmn[255])
    {
        strcpy(wmn, woman_);
    };
    void getTotal(char tot[255])
    {
        strcpy(tot, total_);
    };
    void setId(char id[255]);
    void setYear(char y[255]);
    void setDayMonth(char dM[255]);
    void setIsComune(char ist[255]);
    void setMan(char mn[255]);
    void setWoman(char wmn[255]);
    void setTotal(char tot[255]);
};

istat::istat()
{
    strcpy(id_, " ");
    strcpy(year_, " ");
    strcpy(dayMonth_, " ");
    strcpy(isComune_, " ");
    strcpy(man_, " ");
    strcpy(woman_, " ");
}

void istat::setId(char id[255])
{
    strcpy(id_, id);
    printf("id: ");
    printf("%s\n", id_);
}

void istat::setYear(char y[255])
{
    strcpy(year_, y);
    printf("anno: ");
    printf("%s\n", year_);
}

void istat::setDayMonth(char dM[255])
{
    strcpy(dayMonth_, dM);
    printf("data aggiornamento: ");
    printf("%s\n", dayMonth_);
}

void istat::setIsComune(char ist[255])
{
    strcpy(isComune_, ist);
    printf("istat comune: ");
    printf("%s\n", isComune_);
}

void istat::setMan(char mn[255])
{
    strcpy(man_, mn);
    printf("uomini: ");
    printf("%s\n", man_);
}

void istat::setWoman(char wmn[255])
{
    strcpy(woman_, wmn);
    printf("donne: ");
    printf("%s\n", woman_);
}

void istat::setTotal(char tot[255])
{
    strcpy(total_, tot);
    printf("Popolazione totale: ");
    printf("%s\n", total_);
}

#include <iostream>
#include <fstream>
#include<cmath>

using namespace std;

int main()
{
    //parametry materialowe

    double
    //wzor Varshniego
    Eg0_GaAs{1.519}, //eV
    Eg0_AlSb{2.386},
    Eg0_GaSb{0.812},
    Eg0_AlAs{3.099},
    Eg_GaAs{}, //eV
    Eg_AlSb{},
    Eg_GaSb{},
    Eg_AlAs{};
    double
    alpha_GaAs{0.5405*pow(10,-3)}, //eV/K
    alpha_AlSb{0.42*pow(10,-3)},
    alpha_GaSb{0.417*pow(10,-3)},
    alpha_AlAs{0.885*pow(10,-3)},
    beta_GaAs{204}, //K
    beta_AlSb{140},
    beta_GaSb{140},
    beta_AlAs{530},
    VBO_GaAs{-0.8}, //eV
    VBO_AlAs{-1.33},
    VBO_GaSb{-0.03},
    VBO_AlSb{-0.41},
    //zmiana parametru sieci
    alc300_GaAs{5.65325},   //Angstr
    alc300_AlSb{6.1355},
    alc300_GaSb{6.0959},
    alc300_AlAs{5.6611},
    alcT_GaAs{3.88*pow(10,-5)},  //Angstr/K
    alcT_AlSb{2.6*pow(10,-5)},
    alcT_GaSb{4.72*pow(10,-5)},
    alcT_AlAs{2.90*pow(10,-3)},
    alc_GaAs{},  //Angstr
    alc_AlSb{},
    alc_GaSb{},
    alc_AlAs{},
     //spin-orgita
    so_GaAs{0.341},
    so_AlAs{0.28},
    so_GaSb{0.76},
    so_AlSb{0.676},
    //bonding dla spin-orbity
    b_so_AlGaAs{0},
    b_so_AlGaSb{0.3},
    b_so_GaAsSb{0.6},
    b_so_AlAsSb{0.15};


    double
    //zmienne
    x,
    y,
    T,

    //wyniki dla trojskladnikowych
    Eg_AlGaAs{}, //eV
    Eg_AlGaSb{},
    Eg_GaAsSb{},
    Eg_AlAsSb{},
    alc_AlGaAs{},  //Angstr
    alc_AlGaSb{},
    alc_GaAsSb{},
    alc_AlAsSb{},
    VBO_AlGaAs{}, //eV
    VBO_AlGaSb{},
    VBO_GaAsSb{},
    VBO_AlAsSb{},
    a_c_AlGaAs{}, //eV
    a_c_AlGaSb{},
    a_c_GaAsSb{},
    a_c_AlAsSb{},
    a_v_AlGaAs{},  //Angstr
    a_v_AlGaSb{},
    a_v_GaAsSb{},
    a_v_AlAsSb{},
    b_AlGaAs{}, //eV
    b_AlGaSb{},
    b_GaAsSb{},
    b_AlAsSb{},
    c11_AlGaAs{},  //Angstr
    c11_AlGaSb{},
    c11_GaAsSb{},
    c11_AlAsSb{},
    c12_AlGaAs{}, //eV
    c12_AlGaSb{},
    c12_GaAsSb{},
    c12_AlAsSb{},
    so_AlGaAs{},
    so_AlGaSb{},
    so_GaAsSb{},
    so_AlAsSb{};


    double
    //bonding dla energii
    b_Eg_AlGaAs{-0.127+1.31*x},
    b_Eg_AlGaSb{-0.044+1.22*x},
    b_Eg_GaAsSb{1.43},
    b_Eg_AlAsSb{0.8},
    //bonding dla VBO
    b_VBO_AlGaAs{0},
    b_VBO_AlGaSb{0},
    b_VBO_GaAsSb{-1.06},
    b_VBO_AlAsSb{-1.71},

    //wynik dla czteroskladnikowych
    Eg_AlGaAsSb{},
    alc_AlGaAsSb{},
    VBO_AlGaAsSb{},
    a_c_AlGaAsSb{},
    a_v_AlGaAsSb{},
    b_AlGaAsSb{},
    c11_AlGaAsSb{},
    c12_AlGaAsSb{},
    so_AlGaAsSb{},


    //odksztalcenia
    exx{},
    ezz{},
    c11_GaAs{1221}, //GPa
    c12_GaAs{566},
    a_c_GaAs{-7.17},
    a_v_GaAs{-1.16},
    b_GaAs{-2.0},
    a_c_AlAs{-5.64},
    a_v_AlAs{-2.47},
    b_AlAs{-2.3},
    c11_AlAs{1250},
    c12_AlAs{534},
    a_c_GaSb{-7.5},
    a_v_GaSb{-0.8},
    b_GaSb{-2.0},
    c11_GaSb{884.2},
    c12_GaSb{402.6},
    a_c_AlSb{-4.5},
    a_v_AlSb{-1.4},
    b_AlSb{-1.35},
    c11_AlSb{876.9},
    c12_AlSb{434.1},
    E_chydro{},
    E_vhydro{},
    E_vbias{},
    E_vbiasp{},
    E_vbiasm{},

    //wierzcholki pasm
    E_c{},
    E_v_hh{},
    E_v_lh{},
    E_v_sh{};


    ofstream plik0;
    plik0.open("y0.dat");
    ofstream plik1;
    plik1.open("y2.dat");
    ofstream plik2;
    plik2.open("y4.dat");
    ofstream plik3;
    plik3.open("y6.dat");
    ofstream plik4;
    plik4.open("y8.dat");
    ofstream plik5;
    plik5.open("y10.dat");




x=1;

for (int T=0; T<=500; T++)
    {

        plik0<<T<<'\t';
        plik1<<T<<'\t';
        plik2<<T<<'\t';
        plik3<<T<<'\t';
        plik4<<T<<'\t';
        plik5<<T<<'\t';

         for(y=0.2; y<1; y=y+0.2)
         {
       //zmiany temperaturowe energii
       Eg_GaAs=Eg0_GaAs-alpha_GaAs*T*T/(beta_GaAs+T);
       Eg_AlAs=Eg0_AlAs-alpha_AlAs*T*T/(beta_AlAs+T);
       Eg_GaSb=Eg0_GaSb-alpha_GaSb*T*T/(beta_GaSb+T);
       Eg_AlSb=Eg0_AlSb-alpha_AlSb*T*T/(beta_AlSb+T);


       //zmiany temperaturowe stalej sieci
       alc_GaAs=alc300_GaAs-alcT_GaAs*(T-300);
       alc_AlAs=alc300_AlAs-alcT_AlAs*(T-300);
       alc_AlSb=alc300_AlSb-alcT_AlSb*(T-300);
       alc_GaSb=alc300_GaSb-alcT_GaSb*(T-300);

        //AlGaAs
        Eg_AlGaAs = Eg_GaAs*(1-x)+Eg_AlAs*x-x*(1-x)*(-0.127+1.31*x);
        alc_AlGaAs=alc_GaAs*(1-x)+alc_AlAs*x;
        VBO_AlGaAs = VBO_GaAs*(1-x)+VBO_AlAs*x-x*(1-x)*b_VBO_AlGaAs;
        a_c_AlGaAs=a_c_GaAs*(1-x)+a_c_AlAs*x;
        a_v_AlGaAs=a_v_GaAs*(1-x)+a_v_AlAs*x;
        b_AlGaAs=b_GaAs*(1-x)+b_AlAs*x;
        c11_AlGaAs=c11_GaAs*(1-x)+c11_AlAs*x;
        c12_AlGaAs=c12_GaAs*(1-x)+c12_AlAs*x;
        so_AlGaAs = so_GaAs*(1-x)+so_AlAs*x-x*(1-x)*b_so_AlGaAs;

        //AlGaSb
        Eg_AlGaSb = Eg_GaSb*(1-x)+Eg_AlSb*x-x*(1-x)*(-0.044+1.22*x);
        alc_AlGaSb=alc_GaSb*(1-x)+alc_AlSb*x;
        VBO_AlGaSb = VBO_GaSb*(1-x)+VBO_AlSb*x-x*(1-x)*b_VBO_AlGaSb;
        a_c_AlGaSb=a_c_GaSb*(1-x)+a_c_AlSb*x;
        a_v_AlGaSb=a_v_GaSb*(1-x)+a_v_AlSb*x;
        b_AlGaSb=b_GaSb*(1-x)+b_AlSb*x;
        c11_AlGaSb=c11_GaSb*(1-x)+c11_AlSb*x;
        c12_AlGaSb=c12_GaSb*(1-x)+c12_AlSb*x;
        so_AlGaSb = 
        
        //GaAsSb
        Eg_GaAsSb = Eg_GaAs*y+Eg_GaSb*(1-y)-y*(1-y)*b_Eg_GaAsSb;
        alc_GaAsSb=alc_GaAs*y+alc_GaSb*(1-y);
        VBO_GaAsSb = VBO_GaAs*y+VBO_GaSb*(1-y)-y*(1-y)*b_VBO_GaAsSb;
        a_c_GaAsSb = a_c_GaAs*y+a_c_GaSb*(1-y);
        a_v_GaAsSb=a_v_GaAs*y+a_v_GaSb*(1-y);
        b_GaAsSb = b_GaAs*y+b_GaSb*(1-y);
        c11_GaAsSb = c11_GaAs*y+c11_GaSb*(1-y);
        c12_GaAsSb=c12_GaAs*y+c12_GaSb*(1-y);
        so_GaAsSb = so_GaAs*y+so_GaSb*(1-y)-y*(1-y)*b_so_GaAsSb;

        //AlAsSb
        Eg_AlAsSb = Eg_AlAs*y+Eg_AlSb*(1-y)-y*(1-y)*b_Eg_AlAsSb;
        alc_AlAsSb=alc_AlAs*y+alc_AlSb*(1-y);
        VBO_AlAsSb = VBO_AlAs*y+VBO_AlSb*(1-y)-y*(1-y)*b_VBO_AlAsSb;
        a_c_AlAsSb = a_c_AlAs*y+a_c_AlSb*(1-y);
        a_v_AlAsSb=a_v_AlAs*y+a_v_AlSb*(1-y);
        b_AlAsSb = b_AlAs*y+b_AlSb*(1-y);
        c11_AlAsSb = c11_AlAs*y+c11_AlSb*(1-y);
        c12_AlAsSb=c12_AlAs*y+c12_AlSb*(1-y);
        so_AlAsSb = so_AlAs*y+so_AlSb*(1-y)-y*(1-y)*b_so_AlAsSb;

        //GaAlAsSb
        Eg_AlGaAsSb=(x*(1-x)*(y*Eg_AlGaAs+(1-y)*Eg_AlGaSb)+y*(1-y)*(x*Eg_AlAsSb+(1-x)*Eg_GaAsSb))/(x*(1-x)+y*(1-y));
        alc_AlGaAsSb=(x*(1-x)*(y*alc_AlGaAs+(1-y)*alc_AlGaSb)+y*(1-y)*(x*alc_AlAsSb+(1-x)*alc_GaAsSb))/(x*(1-x)+y*(1-y));
        VBO_AlGaAsSb=(x*(1-x)*(y*VBO_AlGaAs+(1-y)*VBO_AlGaSb)+y*(1-y)*(x*VBO_AlAsSb+(1-x)*VBO_GaAsSb))/(x*(1-x)+y*(1-y));
        a_c_AlGaAsSb=(x*(1-x)*(y*a_c_AlGaAs+(1-y)*a_c_AlGaSb)+y*(1-y)*(x*a_c_AlAsSb+(1-x)*a_c_GaAsSb))/(x*(1-x)+y*(1-y));
        a_v_AlGaAsSb=(x*(1-x)*(y*a_v_AlGaAs+(1-y)*a_v_AlGaSb)+y*(1-y)*(x*a_v_AlAsSb+(1-x)*a_v_GaAsSb))/(x*(1-x)+y*(1-y));
        b_AlGaAsSb=(x*(1-x)*(y*b_AlGaAs+(1-y)*b_AlGaSb)+y*(1-y)*(x*b_AlAsSb+(1-x)*b_GaAsSb))/(x*(1-x)+y*(1-y));
        c11_AlGaAsSb=(x*(1-x)*(y*c11_AlGaAs+(1-y)*c11_AlGaSb)+y*(1-y)*(x*c11_AlAsSb+(1-x)*c11_GaAsSb))/(x*(1-x)+y*(1-y));
        c12_AlGaAsSb=(x*(1-x)*(y*c12_AlGaAs+(1-y)*c12_AlGaSb)+y*(1-y)*(x*c12_AlAsSb+(1-x)*c12_GaAsSb))/(x*(1-x)+y*(1-y));
        so_AlGaAsSb=(x*(1-x)*(y*so_AlGaAs+(1-y)*so_AlGaSb)+y*(1-y)*(x*so_AlAsSb+(1-x)*so_GaAsSb))/(x*(1-x)+y*(1-y));

        //liczenie tensora odkszta�cen
        exx=(alc_GaAs-alc_AlGaAsSb)/alc_AlGaAsSb; //pod�oze-stala po interpolacji
        ezz=-2*c12_AlGaAsSb*exx/c11_AlGaAsSb;
        E_chydro=a_c_AlGaAsSb*(ezz+2*exx);
        E_vhydro=a_v_AlGaAsSb*(exx+2*exx);
        E_vbias=b_AlGaAsSb*(ezz-exx);
        E_vbiasp=(E_vbias-so_AlGaAsSb+sqrt(9*pow(E_vbias,2)+2*E_vbias*so_AlGaAsSb+pow(so_AlGaAsSb,2)))/2;
        E_vbiasm=(E_vbias-so_AlGaAsSb-sqrt(9*pow(E_vbias,2)+2*E_vbias*so_AlGaAsSb+pow(so_AlGaAsSb,2)))/2;

        //wierzcholki pasm
        E_c=VBO_AlGaAsSb+Eg_AlGaAsSb+E_chydro;
        E_v_hh=VBO_AlGaAsSb+E_vhydro-E_vbias;
        E_v_lh=VBO_AlGaAsSb+E_vhydro+E_vbiasp;
        E_v_sh=VBO_AlGaAsSb+E_vhydro+E_vbiasm;

        //wypisanie do plikow
        if(y==0.0)
        plik0<<exx<<'\t'<<ezz<<'\t'<<E_c<<'\t'<<E_v_hh<<'\t'<<E_v_lh<<'\t'<<E_v_sh<<endl;

        if(y==0.2)
        plik1<<exx<<'\t'<<ezz<<'\t'<<E_c<<'\t'<<E_v_hh<<'\t'<<E_v_lh<<'\t'<<E_v_sh<<endl;

        if(y==0.4)
        plik2<<exx<<'\t'<<ezz<<'\t'<<E_c<<'\t'<<E_v_hh<<'\t'<<E_v_lh<<'\t'<<E_v_sh<<endl;

        if(y>0.6-0.00001&&y<0.6+0.000001)
        plik3<<exx<<'\t'<<ezz<<'\t'<<E_c<<'\t'<<E_v_hh<<'\t'<<E_v_lh<<'\t'<<E_v_sh<<endl;

        if(y==0.8)
        plik4<<exx<<'\t'<<ezz<<'\t'<<E_c<<'\t'<<E_v_hh<<'\t'<<E_v_lh<<'\t'<<E_v_sh<<endl;

        if(y==1.0)
        plik5<<exx<<'\t'<<ezz<<'\t'<<E_c<<'\t'<<E_v_hh<<'\t'<<E_v_lh<<'\t'<<E_v_sh<<endl;

         }
    }
    plik0.close();
    plik1.close();
    plik2.close();
    plik3.close();
    plik4.close();
    plik5.close();

return 0;
}

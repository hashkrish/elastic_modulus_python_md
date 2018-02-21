#include<stdio.h>
#include<stdlib.h>
double SIGMA=0.3;
#define EPSILON 1.5;
double esp=24*EPSILON;
double LENGTH=10;
int DIM=3;
double min_dist(double x1, double x2)
{
	if(x1-x2>LENGTH/2.0)
		return x1-x2-LENGTH;
	else if(x1-x2<-LENGTH/2.0)
		return x1-x2+LENGTH;
	else
		return x1-x2;
}

double distance(double x1[DIM], double x2[DIM])
{
	int k;
	double foo,dist;
	dist=0;
	for(k=0;k<DIM;k++)
	{
		foo=min_dist(x1[k],x2[k]);
		dist+=foo*foo;		
	}
	return dist;
}

//Calculates LJ force and Potential
double force_LJ(double x1[DIM], double x2[DIM],double *potential)
{
	double dr2,s_r2,s2,s,s_r6,val;
	s2=SIGMA*SIGMA;
	dr2=distance(x1,x2);
	s_r2=s2/dr2;
	s_r6=s_r2*s_r2*s_r2;
	*potential+=s_r6*(s_r6-1);
	val=esp*s_r6*(2*s_r6-1)/dr2;
	return val;
}

int main()
{
	double x[2][3]={{0.1,0.1,0.1},{0.3,0.1,0.1}};
	double potential;
	potential=0;
	printf("%f %f %f %f\n",min_dist(x[0][0],x[1][0]),min_dist(x[0][1],x[1][1]),min_dist(x[0][2],x[1][2]),sqrt(distance(x[0],x[1])));
	printf("%f\n",force_LJ(x[0],x[1],&potential)*(x[0][0]-x[1][0]));
	printf("%f\n",potential);
	return 0;
}






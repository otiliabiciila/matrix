#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream f ("fisier.in");
	ofstream g ("fisier.out");
	int A[10][10], B[10][10], C[10][10], i, j, k, s, n;
	
	// citire dimensiune matrice 
	f>>n;
	
	// citirea primei matrice 
	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
			f>>A[i][j];
			
	// citirea celei de a doua matrice
	for (i=0; i<n; i++)
		for (j=0; j<n; j++)
			f>>B[i][j];
			
	// inmultirea acestora
	for (i=0; i<n; i++)
	{
		for (j=0; j<n; j++)
		{
			s=0;
			for (k=0; k<n; k++)
				s=s+A[i][k]*B[k][j];
			C[i][j]=s;
		}
	}
	
	// afisare rezultat in fisier
	for (i=0; i<n; i++)
	{
		for (j=0; j<n; j++)
			g<<C[i][j]<<" ";
		g<<endl;
	}
	return 0;
}

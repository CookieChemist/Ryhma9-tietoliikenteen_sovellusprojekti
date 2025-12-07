#include <zephyr/kernel.h>
#include <math.h>
#include "confusion.h"
#include "adc.h"
#include <stdlib.h> // Just for debugging, delete later to save space
#include "center_points.h"
/* 
  K-means algorithm should provide 6 center points with
  3 values x,y,z. Let's test measurement system with known
  center points. I.e. x,y,z are supposed to have only values
  1 = down and 2 = up
  
  CP matrix is thus the 6 center points got from K-means algoritm
  teaching process. This should actually come from include file like
  #include "KmeansCenterPoints.h"
  
  And measurements matrix is just fake matrix for testing purpose
  actual measurements are taken from ADC when accelerator is connected.
*/ 

/*
int CP[6][3]={
	                     {1,0,0},
						 {2,0,0},
						 {0,1,0},
						 {0,2,0},
						 {0,0,1},
						 {0,0,2}
};
*/
int measurements[6][3]={
	                     {1,0,0},
						 {2,0,0},
						 {0,1,0},
						 {0,2,0},
						 {0,0,1},
						 {0,0,2}
};

int CM[6][6]= {0};



void printConfusionMatrix(void)
{
	printk("Confusion matrix = \n");
	printk("   cp1 cp2 cp3 cp4 cp5 cp6\n");
	for(int i = 0;i<6;i++)
	{
		printk("cp%d %d   %d   %d   %d   %d   %d\n",i+1,CM[i][0],CM[i][1],CM[i][2],CM[i][3],CM[i][4],CM[i][5]);
	}
}

void makeHundredFakeClassifications(void)
{
  for (int d = 0; d<6; d++){
   for (int i = 0; i<100; i++){
   //int r = (rand() % (5 + 1 - 0)) + 0;
   int x = measurements[d][0];
   int y = measurements[d][1];
   int z = measurements[d][2];
   
   makeOneClassificationAndUpdateConfusionMatrix(d, x, y, z);
  }
  }
   printk("makeOneHundredFakeClassifications triggered\n");
}

void makeOneClassificationAndUpdateConfusionMatrix(int direction, int x, int y, int z)
{
  int prediction = calculateDistanceToAllCentrePointsAndSelectWinner(x, y, z);
  CM[direction][prediction]++;
   printk("makeOneClassification triggered\n");
}

int calculateDistanceToAllCentrePointsAndSelectWinner(int x,int y,int z)
{
  int distances[6];

  for (int i = 0; i<6; i++){
   int d = sqrt(pow(CP[i][0] - x, 2) +  pow(CP[i][1] - y, 2) +  pow(CP[i][2] - z, 2));
   //printk("Distance is %d", d);
   distances[i]=d;
   };
   int min = distances[0];
   int minIndex=0;
    for (int i = 1; i < 6; i++) {
      
      
        if (distances[i] < min) {
            min = distances[i]; 
            minIndex=i;

        }
    }
   printk("Calculate distance triggered. Shortest distance was to center: %d \n", minIndex);
   return minIndex;
}

void resetConfusionMatrix(void)
{
	for(int i=0;i<6;i++)
	{ 
		for(int j = 0;j<6;j++)
		{
			CM[i][j]=0;
		}
	}
}


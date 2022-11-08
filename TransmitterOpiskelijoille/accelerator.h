#ifndef ACCELERATOR_H
#define ACCELERATOR_H

#include "messaging.h"

struct Measurement
{
  int x;
  int y;
  int z;
};

class Accelerator
{
public:
  Accelerator();
  ~Accelerator();
  void makeMeasurement();
  void tulostus();
  Measurement getMeasurement();

  const int xPin   = A1;   // x-kanavan mittaus
  const int yPin   = A2;   // y-kanava
  const int zPin   = A3;   // z-kanava


private:
  Measurement m;
 
};

#endif // ACCELERATOR_H

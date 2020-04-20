#include <Wire.h>

#include <VL53L0X.h>

#include "RumiCar.h"

VL53L0X sensor0;
VL53L0X sensor1;
VL53L0X sensor2;

void setup()
{
  RC_setup();
}

void loop()
{

int ibound =250;
int s0, s1, s2;
s0=sensor0.readRangeSingleMillimeters();
s1=sensor1.readRangeSingleMillimeters();
s2=sensor2.readRangeSingleMillimeters();

if(s1<100){
  RC_drive(REVERSE,150);
}else if (s1<150){
  RC_drive(FORWARD,150);
}else if (s1<250){
  RC_drive(FORWARD,200);
}else{
  RC_drive(FORWARD,255);
}
 if(s0>s2){
  RC_steer(LEFT);
  }else{
    RC_steer(RIGHT);
  }
}

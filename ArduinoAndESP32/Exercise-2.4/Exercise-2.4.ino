#include <RumiCar.h>

void setup()
{
  RC_setup();
}

void loop()
{
  RC_drive(FORWARD,255);
  RC_steer(RIGHT);
  delay(500);
  RC_steer(LEFT);
  delay(500);
}

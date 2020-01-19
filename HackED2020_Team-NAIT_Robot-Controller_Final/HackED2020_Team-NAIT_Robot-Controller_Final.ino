***********************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)


uint8_t servonum = 0;

int recycleButton = 2;
int compostButton = 3;
int garbageButton = 4;


void setup() {
  Serial.begin(9600);
  Serial.println("TrashBot9000!!!");

  pwm.begin();
  
  pwm.setPWMFreq(60);

  yield();

  pinMode(recycleButton, INPUT_PULLUP);

  pinMode(compostButton, INPUT_PULLUP);

  pinMode(garbageButton, INPUT_PULLUP);
}

void setServoPulse(uint8_t n, double pulse) {
  double pulselength;
  
  pulselength = 1000000;   // 1,000,000 us per second
  pulselength /= 60;   // 60 Hz
  Serial.print(pulselength); Serial.println(" us per period"); 
  pulselength /= 4096;  // 12 bits of resolution
  Serial.print(pulselength); Serial.println(" us per bit"); 
  pulse *= 1000;
  pulse /= pulselength;
  Serial.println(pulse);
  pwm.setPWM(n, 0, pulse);
}

void setServoAngle(int servonum, int servoDegree) {
    uint16_t pulselength = map(servoDegree, 0, 180, SERVOMIN, SERVOMAX);
    pwm.setPWM(servonum, 0, pulselength);
    Serial.println(servoDegree);
}


void recycling()  {
  Serial.println(" This can be recycled");
  setServoAngle(0, 90);
  delay(500);
  setServoAngle(1, 150);
  delay(2000);
  setServoAngle(1, 10);
  delay(500);
  setServoAngle(0, 90);
}


void compost()  {
  Serial.println(" This is compost");
  for(int i = 90; i <= 170; i+= 4)  {
    setServoAngle(0, i);
    delay(200);
  }
  delay(500);
  setServoAngle(1, 150);
  delay(2000);
  setServoAngle(1, 10);
  delay(500);
  setServoAngle(0, 90);
  for(int i = 170; i > 90; i-= 4)  {
    setServoAngle(0, i);
    delay(200);
  }
  setServoAngle(0, 90);
}


void garbage()  {
  Serial.println(" This is garbage");
  for(int i = 90; i >= 10; i-= 4)  {
    setServoAngle(0, i);
    delay(200);
  }
  delay(500);
  setServoAngle(1, 150);
  delay(2000);
  setServoAngle(1, 10);
  delay(500);
  for(int i = 10; i < 90; i+= 4)  {
    setServoAngle(0, i);
    delay(200);
  }
  setServoAngle(0, 90);
}


void loop() {


  if(!digitalRead(recycleButton))  {
    recycling();
  }

  else if(!digitalRead(compostButton)) {
    compost();
  }

  else if(!digitalRead(garbageButton)) {
    garbage();
  }

}

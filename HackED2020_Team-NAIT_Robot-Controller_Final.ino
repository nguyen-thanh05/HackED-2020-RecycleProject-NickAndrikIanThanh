//***********************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)

int incomingByte = 0;

uint8_t servonum = 0;

int recycleButton = 2;
int compostButton = 3;
int garbageButton = 4;

#define RED_LED 5
#define GREEN_LED 6
#define BLUE_LED 9

int gBright = 0; 
int rBright = 0;
int bBright = 0;


void setup() {
  Serial.begin(9600);
  Serial.println("TrashBot9000!!!");

  pwm.begin();
  
  pwm.setPWMFreq(60);

  yield();

  pinMode(recycleButton, INPUT_PULLUP);

  pinMode(compostButton, INPUT_PULLUP);

  pinMode(garbageButton, INPUT_PULLUP);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  
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
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 255);
  Serial.println(" This can be recycled");
  setServoAngle(0, 90);
  delay(500);
  setServoAngle(1, 150);
  delay(2000);
  setServoAngle(1, 10);
  delay(500);
  setServoAngle(0, 90);
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 0);
}


void compost()  {
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 255);
  analogWrite(BLUE_LED, 0);
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
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 0);
}


void garbage()  {
  analogWrite(RED_LED, 255);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 0);
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
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 0);
}


void randomColors() {
  for(int i = 0; i < 20; i++) {
    setServoAngle(1, 60);
    analogWrite(RED_LED, random(255));
    analogWrite(GREEN_LED, random(255));
    analogWrite(BLUE_LED, random(255));
    delay(250);
    setServoAngle(1, 10);
    delay(100);
  }
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 0);
}


void colorFade()  {
  for(int x = 0; x < 1; x++)  {
    for(int i = 0; i < 255; i++)  {
      analogWrite(RED_LED, 255 - i);
      analogWrite(GREEN_LED, i);
      analogWrite(BLUE_LED, 0);
      delay(25);
    }
    for(int i = 0; i < 255; i++)  {
      analogWrite(RED_LED, 0);
      analogWrite(GREEN_LED, 255 - i);
      analogWrite(BLUE_LED, i);
      delay(25);
    }
    for(int i = 0; i < 255; i++)  {
      analogWrite(RED_LED, i);
      analogWrite(GREEN_LED, 0);
      analogWrite(BLUE_LED, 255-i);
      delay(25);
    }
  }
  for(int i = 0; i < 255; i++)  {
    analogWrite(RED_LED, 255-i);
    analogWrite(GREEN_LED, 0);
    analogWrite(BLUE_LED, 0);
    delay(10);
  }
}


void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte);
  

    if(incomingByte == 114) {
      recycling();
    }
  
    else if(incomingByte == 99) {
      compost();
    }
  
    else if(incomingByte == 103) {
      garbage();
    }

    else if(incomingByte == 112) {
      randomColors();
    }

    else if(incomingByte == 102) {
      colorFade();
    }
  }


}

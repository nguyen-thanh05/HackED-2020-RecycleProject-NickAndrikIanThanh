

#define RED_LED 5
#define GREEN_LED 6
#define BLUE_LED 9

int gBright = 0; 
int rBright = 0;
int bBright = 0;

void setup() {
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
}

void loop() {
  analogWrite(RED_LED, 255);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 0);
  delay(1000);
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 255);
  analogWrite(BLUE_LED, 0);
  delay(1000);
  analogWrite(RED_LED, 0);
  analogWrite(GREEN_LED, 0);
  analogWrite(BLUE_LED, 255);
  delay(1000);
}

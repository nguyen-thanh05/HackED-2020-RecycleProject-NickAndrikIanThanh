

int incomingByte = 0;

int recyclePin = 2;
int compostPin = 3;
int garbagePin = 4;


void setup() {
  Serial.begin(9600);
  pinMode(recyclePin, OUTPUT);
  pinMode(compostPin, OUTPUT);
  pinMode(garbagePin, OUTPUT);

  digitalWrite(recyclePin, LOW);
  digitalWrite(compostPin, LOW);
  digitalWrite(garbagePin, LOW);
  

}

void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte);
  

  if(incomingByte == 114) {
    digitalWrite(recyclePin, HIGH);
    delay(500);
    digitalWrite(recyclePin, LOW);
  }

  else if(incomingByte == 99) {
    digitalWrite(compostPin, HIGH);
    delay(500);
    digitalWrite(compostPin, LOW);
  }

  else if(incomingByte == 103) {
    digitalWrite(garbagePin, HIGH);
    delay(500);
    digitalWrite(garbagePin, LOW);
  }
  }
}

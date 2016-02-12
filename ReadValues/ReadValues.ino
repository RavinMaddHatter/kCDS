/*
  Button

 Turns on and off a light emitting diode(LED) connected to digital
 pin 13, when pressing a pushbutton attached to pin 2.


 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground

 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.


 created 2005
 by DojoDave <http://www.0j0.org>
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Button
 */

// constants won't change. They're used here to
// set pin numbers:
const int startPin = 2;     // the number of the pushbutton pin
const int noPins =  13;      // the number of the LED pin
int an0;
int an1;
int an2;
int an3;
int an4;
int an5;
int an6;
int an7;
int an8;
int an9;
//bool light= 1;
//int count;
// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  for (int pin = startPin;pin<=noPins;pin++){
    pinMode(pin,OUTPUT);
  }
  //pinMode(13,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  for (int pin=0;pin<startPin;pin++){
    Serial.print(0,BIN);
    Serial.print(',');
  }
  for (int pin = startPin;pin<=noPins;pin++){
    buttonState = digitalRead(pin);
    Serial.print(buttonState,BIN);
    Serial.print(',');
  }
  an0 = analogRead(A0);
  an1 = analogRead(A1);
  an2 = analogRead(A2);
  an3 = analogRead(A3);
  an4 = analogRead(A4);
  an5 = analogRead(A5);
  an6 = analogRead(A6);
  an7 = analogRead(A7);
  an8 = analogRead(A8);
  an9 = analogRead(A9);
  Serial.print("Yaw:");
  Serial.print(an0,DEC);
  Serial.print(',');
  Serial.print("Pitch:");
  Serial.print(an1,DEC);
  Serial.print(',');
  Serial.print("Roll:");
  Serial.print(an2,DEC);
  Serial.print(",");
  Serial.print("Up:");
  Serial.print(an3,DEC);
  Serial.print(',');
  Serial.print("Forward:");
  Serial.print(an4,DEC);
  Serial.print(',');
  Serial.print("Right:");
  Serial.print(an5,DEC);
  Serial.print(',');
  Serial.print("Throttle:");
  Serial.print(an6,DEC);
  Serial.print(',');
  Serial.print("WheelThrottle:");
  Serial.print(an7,DEC);
  Serial.print(',');
  Serial.print("Wheel:");
  Serial.print(an8,DEC);
  Serial.print(',');
  Serial.print("Extra1:");
  Serial.print(an8,DEC);
  Serial.print(',');
  Serial.print("Extra2:");
  Serial.println(an9,DEC);
//  Serial.print(',');
//  Serial.print(count);
//  count++;
//  Serial.print("\n");
  Serial.flush();
  Serial.send_now();
  //digitalWrite(13,light);
  //light=!light;
  delay(100);
 
}

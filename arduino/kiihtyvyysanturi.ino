/*
  Analog input, analog output, serial output

  Reads an analog input pin, maps the result to a range from 0 to 255 and uses
  the result to set the pulse width modulation (PWM) of an output pin.
  Also prints the results to the Serial Monitor.

  The circuit:
  - potentiometer connected to analog pin 0.
    Center pin of the potentiometer goes to the analog pin.
    side pins of the potentiometer go to +5V and ground
  - LED connected from digital pin 9 to ground through 220 ohm resistor

  created 29 Dec. 2008
  modified 9 Apr 2012
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/AnalogInOutSerial
*/

// These constants won't change. They're used to give names to the pins used:
const int analogInPinX = A0;
const int analogInPinY = A1;
const int analogInPinZ = A2;

int SensorValueX = 0;        // value read from the pot
int SensorValueY = 0;
int SensorValueZ = 0;
int sisaanmeno = 0;
unsigned long aika = 0;

  float Ax = 0.0;
  float Ay = 0.0;
  float Az = 0.0;
  float A = 0.0;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
 if (sisaanmeno == 0)
 {

 
  Serial.print("\t A x");
  Serial.print("\t A x");
  Serial.print("\t A y");
  Serial.println("\t A");
  sisaanmeno =1;
 }

 SensorValueX = analogRead(analogInPinX);
 SensorValueY = analogRead(analogInPinY);
 SensorValueZ = analogRead(analogInPinZ);
 aika = millis();

 Ax = 0.1507*SensorValueX-49.34;
 Ay = 0.1486*SensorValueY-48.604;
 Az = 0.1489*SensorValueZ-49.749;
 A = sqrt(Ax*Ax+Ay*Ay+Az*Az);

  Serial.print(aika);      
  Serial.print("\t ; ");
  Serial.print(Ax);           
  Serial.print("\t ; ");  
  Serial.print(Ay);      
  Serial.print("\t ; ");  
  Serial.print(Az);  
  Serial.print("\t ; ");
  Serial.println(A);     


  delay(100);
}

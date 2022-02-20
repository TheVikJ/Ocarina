#include <SoftwareSerial.h>

// Arduino pin numbers
const int SW_pin = 8; // digital pin connected to switch output
const int X_pin = 0; // analog pin connected to X output
const int Y_pin = 1; // analog pin connected to Y output

SoftwareSerial hc06(2,3);

// Initializing values of pins
int X_value = 512;
int Y_value = 512;
int SW_value = 1;

// Initialization
void setup() {
  pinMode(SW_pin, INPUT);
  digitalWrite(SW_pin, HIGH);
  Serial.begin(9600);
  hc06.begin(9600);
}

void loop() {
  // Read pins
  SW_value = digitalRead(SW_pin);
  X_value = analogRead(X_pin);
  Y_value = analogRead(Y_pin);

  // Do something if joystick is pressed or moved L, R, U or D
  if (SW_value == 0) 
  {
    hc06.write('A');
  }
  else if (abs(512-X_value) > 450) 
  {
    if (X_value > 0)
    {
      hc06.write('U');
    }
    else 
    {
      hc06.write('D');
    }
  }
  else if (abs(512-Y_value) > 450)
  {
    if (Y_value > 0)
    {
      hc06.write('R');
    }
    else 
    {
      hc06.write('L');
    }
  }
  delay(100); 
}
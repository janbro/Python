int vMotor = 13;
byte incomingByte = 0;

void setup() {                
  // initialize the digital pin as an output.
  pinMode(vMotor, OUTPUT); 
  Serial.begin(9600);  
}

// the loop routine runs over and over again forever:
void loop() {
  if(Serial.available()>0){
    incomingByte = Serial.read();
    Serial.println(incomingByte);
    if(incomingByte == 2){
      digitalWrite(vMotor, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);               // wait for a second
      digitalWrite(vMotor, LOW);    // turn the LED off by making the voltage LOW
    }
  }
}

int vMotor = 13;
int button = 2;
byte incomingByte = 0;
int buttonState = 0;
byte message = 0;
byte lastMessage = 0;

void setup() {                
  // initialize the digital pin as an output.
  pinMode(vMotor, OUTPUT); 
  pinMode(button, INPUT);
  Serial.begin(9600);  
    Serial.println(digitalRead(button));
}

// the loop routine runs over and over again forever:
void loop() {
   //Serial.println(digitalRead(button));
  if(Serial.available()>0){
    incomingByte = Serial.read();
    if(incomingByte == 97){
      digitalWrite(vMotor, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(100);               // wait for a second
      digitalWrite(vMotor, LOW);    // turn the LED off by making the voltage LOW
      delay(50);               // wait for a second
      digitalWrite(vMotor, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(100);               // wait for a second
      digitalWrite(vMotor, LOW);    // turn the LED off by making the voltage LOW
    }
  }
  buttonState = digitalRead(button);
  
  message = buttonState;
  
  if(lastMessage!=message)
    Serial.println(message);
    
  lastMessage = message;
}

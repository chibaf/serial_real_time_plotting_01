const int PIN_ANALOG_INPUT = 5;

void setup() {
  Serial.begin( 9600 );
}

void loop() {
  int i = analogRead( PIN_ANALOG_INPUT );
  Serial.println( i ); // 0 <= i =< 1023
  delay( 100 ); 
}

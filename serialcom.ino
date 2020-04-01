int analog_pin=3;
int data = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  data = analogRead(analog_pin);
  Serial.println(data);
  delay(1000);
}

int deger = 0;

void setup() {
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  deger = analogRead(A0);
  deger = map(deger, 0, 1024, 0, 180);
  Serial.println(deger);
  delay(300);
}

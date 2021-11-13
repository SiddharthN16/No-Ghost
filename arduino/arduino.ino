int onBtn = 5;
int onLed = 6;
int onState;

void setup()
{
    Serial.begin(9600);
    pinMode(onLed, OUTPUT);
}

void loop()
{
    if (digitalRead(onBtn) == LOW)
    {
        onState = (onState) ? false : true;
        digitalWrite(onLed, (onState) ? HIGH : LOW);
    }
    Serial.println(onState);
    delay(1000);
}
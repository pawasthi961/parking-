

#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <SoftwareSerial.h>
#include <FirebaseArduino.h>

#include <ESP8266HTTPClient.h>
 
// Set these to run example.
#define FIREBASE_HOST "https://park-arduino-3451d.firebaseio.com/"
#define FIREBASE_AUTH "secret"
#define WIFI_SSID "<wifi-ssid>"
#define WIFI_PASSWORD "<password>"
 
String myString_1,myString_2,myString_3,myString_4;
const int trigPin_1 = 2; //D4
const int echoPin_1 = 0; //D3

const int trigPin_2 = 14;//D5
const int echoPin_2 = 12;//D6

const int trigPin_3 = 13; //D7
const int echoPin_3 = 15; //D8

const int trigPin_4 = 16; //D0
const int echoPin_4 = 5; //D1


int distance_1,distance_2,distance_3,distance_4;
 
void setup()
{
  // Debug console
  Serial.begin(9600);
  
  pinMode(trigPin_1,OUTPUT);
  pinMode(echoPin_1,INPUT);

  pinMode(trigPin_2,OUTPUT);
  pinMode(echoPin_2,INPUT);

  pinMode(trigPin_3,OUTPUT);
  pinMode(echoPin_3,INPUT);

  pinMode(trigPin_4,OUTPUT);
  pinMode(echoPin_4,INPUT);
  // connect to wifi.
  
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED)
      {
    Serial.print(".");
    delay(500);
      }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
 
  Firebase.setString("sensors/sensor_01/Value","");
}
//creating a fucntion for reading ultasonic reading and returning distance 
long readUltrasonicDistance(int pin1,int pin2){
//clears the trigPin
digitalWrite(pin1 ,LOW);
delayMicroseconds(2);
//sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(pin1,HIGH);
delayMicroseconds(10);
digitalWrite(pin1,LOW);
//reads the echoPin, returns the sound wave travel time in microseconds
return pulseIn(pin2,HIGH);
}

void loop()
{
  //measure the ping time in cm
distance_1 =  0.01723*readUltrasonicDistance(trigPin_1,echoPin_1);
distance_2 =  0.01723*readUltrasonicDistance(trigPin_2,echoPin_2);
distance_3 =  0.01723*readUltrasonicDistance(trigPin_3,echoPin_3);
distance_4 =  0.01723*readUltrasonicDistance(trigPin_4,echoPin_4);


myString_1 = String(distance_1);
myString_2 = String(distance_2);
myString_3 = String(distance_3);
myString_4 = String(distance_4);
 
Serial.println(myString_1);
Serial.println(myString_2);
Serial.println(myString_3);
Serial.println(myString_4); 
Firebase.setString("sensors/sensor_01/Value",myString_1);
Firebase.setString("sensors/sensor_02/Value",myString_2);
Firebase.setString("sensors/sensor_03/Value",myString_3);
Firebase.setString("sensors/sensor_04/Value",myString_4);
delay(1000);            
}

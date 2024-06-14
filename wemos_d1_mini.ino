#include <ESP8266WiFi.h>
#include<Wire.h>
#include<Adafruit_Sensor.h>
#include<Adafruit_ADXL345_U.h>

const char* ssid = "realme5s";
const char* password = "00012345";
const char* serverIP = "192.168.43.236";

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified();


WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(10);
  if(!accel.begin()){
    Serial.println("ADXL345 not detected");
    while(true);
  }
  // Initialize Wi-Fi connection
  initWiFi();
}

void loop() {
  // Read sensor data
  float sensorData = readSensor();
  
  // Send data to server
  if (client.connect(serverIP, 80)) {
    Serial.println("Connected to server");
    client.print("POST /sensor_data HTTP/1.1\r\n");
    client.print("Host: ");
    client.print(serverIP);
    client.print("\r\n");
    client.print("Content-Type: application/x-www-form-urlencoded\r\n");
    client.print("Content-Length: ");
    client.print(String(sensorData).length());
    client.print("\r\n\r\n");
    client.print(sensorData);
  } else {
    Serial.println("Connection failed");
  }
  
  delay(2000); // Send data every 5 seconds
}

void initWiFi() {
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
}

float readSensor() {
  sensors_event_t event;
  accel.getEvent(&event);
  Serial.print("x-axis:");
  Serial.print(event.acceleration.x);
  Serial.print("");
  Serial.print("y-axis:");
  Serial.print(event.acceleration.y);
  Serial.print("");
  Serial.print("z-axis:");
  Serial.print(event.acceleration.z);
  Serial.print("");
  Serial.println("m/s^2");
  delay(500);
  return event.acceleration.x,event.acceleration.y,event.acceleration.z;
}

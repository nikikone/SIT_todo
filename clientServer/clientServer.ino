// Load Wi-Fi library
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <WiFiUdp.h>
#include "ESP8266WebServer.h"
#include <ESP8266HTTPClient.h>

// Replace with your network credentials
const char* ssid     = "free";
const char* password = "123456789000";

int counter = 0;

unsigned long currentTime;
unsigned long previousTime = 0;
int interval = 5000;

// Set web server port number to 80
ESP8266WebServer server(80);

HTTPClient http;  //Declare an object of class HTTPClient
WiFiClient _client;

void setup() {
    Serial.begin(115200);
    // Initialize the output variables as outputs
    pinMode(A0, INPUT);
    // Connect to Wi-Fi network with SSID and password
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    // Print local IP address and start web server
    Serial.println("");
    Serial.println("WiFi connected.");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
    server.on("/", openmain);
    server.on("", openmain);
    server.begin();
    
    Serial.println("Booting");
    Serial.println("Ready");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void req(){
    if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
        String geturl =  "http://strekalev.pythonanywhere.com/getdata?data="+String(counter);
        Serial.println(geturl);
        http.begin(_client, geturl);  //Specify request destination
        int httpCode = http.GET();                                  //Send the request
        
        if (httpCode > 0) { //Check the returning code
            String payload = http.getString();   //Get the request response payload
            Serial.println(payload);             //Print the response payload
        }
        http.end();   //Close connection
    }
}

void openmain() {
    String msg = "";
    String aRead = String(analogRead(A0));
    
    msg += aRead;
    server.send(200, "text/html", msg);
}

void loop() {
    server.handleClient();
    currentTime = millis();
    
    if(currentTime - previousTime > interval){
        previousTime = currentTime;
        counter += 1;
        req();
    }
}

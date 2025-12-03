#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "Familia Cruz";
const char* password = "Alfalfa01";

#define ENA 18
#define IN1 19
#define IN2 21

WebServer server(80);

void handleRoot() {
  String html = R"(
  <html>
  <head>
      <meta name='viewport' content='width=device-width, initial-scale=1.0'>
      <style>
          body { background:#111; color:white; font-family:Arial; text-align:center; }
          .btn {
              padding:20px;
              width:200px;
              margin:15px;
              font-size:22px;
              font-weight:bold;
              border-radius:12px;
              border:none;
              cursor:pointer;
          }
          .right { background:#007bff; }
          .left { background:#28a745; }
          .stop { background:#dc3545; }
      </style>
  </head>
  <body>
      <h1>Control Motor L298N</h1>
      <button class='btn right' onclick="location.href='/right'">Derecha</button><br>
      <button class='btn left' onclick="location.href='/left'">Izquierda</button><br>
      <button class='btn stop' onclick="location.href='/stop'">Detener</button>
  </body>
  </html>
  )";
  
  server.send(200, "text/html", html);
}

void girarDerecha() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(ENA, HIGH);  // Motor ON

  server.sendHeader("Location", "/");
  server.send(303);
}

void girarIzquierda() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(ENA, HIGH);  // Motor ON

  server.sendHeader("Location", "/");
  server.send(303);
}

void detener() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(ENA, LOW);  // Motor OFF

  server.sendHeader("Location", "/");
  server.send(303);
}

void setup() {
  Serial.begin(115200);

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
    Serial.print(".");
  }
  Serial.println("\nConectado!");
  Serial.print("IP del servidor: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/right", girarDerecha);
  server.on("/left", girarIzquierda);
  server.on("/stop", detener);

  server.begin();
}

void loop() {
  server.handleClient();
}
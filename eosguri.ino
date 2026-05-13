#include <SPI.h>
#include <SD.h>

int sck = 18;
int miso = 19;
int mosi = 23;
int cs = 5;

void setup() {
  Serial.begin(115200);

  SPI.begin(sck, miso, mosi, cs);

  if (!SD.begin(cs)) {
    Serial.println("SD falhou");
    while (1);
  }

  Serial.println("SD inicializado");

  // Abre/cria arquivo para escrita
  File file = SD.open("/bigode.txt", FILE_WRITE);

  if (!file) {
    Serial.println("Erro ao abrir arquivo");
    return;
  }

  // Escreve no SD
  file.println("Ola mundo!");
  file.println("Escrevendo no cartao SD");
  file.println("ESP32 funcionando");

  file.close();

  Serial.println("Texto escrito com sucesso");
}

void loop() {

}

#include <SPI.h>
#include <SD.h>

const int chipSelect = 10;

File arquivo;

void setup() {

  // Inicializa SD Card
  if (!SD.begin(chipSelect)) {
    while (1); // trava se falhar
  }

  // Abre/cria arquivo
  arquivo = SD.open("notas.txt", FILE_WRITE);

  if (arquivo) {

    arquivo.println("Arduino funcionando!");
    arquivo.println("Texto salvo no SD Card.");
    arquivo.println("----------------------");

    arquivo.close();
  }
}

void loop() {

}
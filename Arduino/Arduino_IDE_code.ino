#include <Wire.h>
#include <SparkFun_VL53L5CX_Library.h>

SparkFun_VL53L5CX myImager;

void setup() {
  Serial.begin(115200);
  delay(5000);  // allow stable power

  Serial.println("BOOT OK");

  Wire.begin(21, 22);

  Serial.println("Initializing sensor...");

  if (!myImager.begin()) {
    Serial.println("Sensor NOT detected");
    return;
  }

  Serial.println("Sensor detected");

  myImager.setResolution(4 * 4);   // stable mode
  delay(100);

  myImager.setRangingFrequency(10);  // important for stable output
  delay(100);

  myImager.startRanging();
  delay(200);

  Serial.println("Ranging started");
}

void loop() {
  VL53L5CX_ResultsData data;

  if (myImager.isDataReady()) {
    myImager.getRangingData(&data);

    for (int i = 0; i < 16; i++) {
      Serial.print(data.distance_mm[i]);
      if (i < 15) Serial.print(",");
    }
    Serial.println();
  }

  delay(100);
}
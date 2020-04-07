#!/usr/bin/env python

from Adafruit_BME280 import BME280
from time import sleep

DELAY_BETWEEN_SENSORS = 0.5
SPI_BUS = 0
for i in [1,2,3,4,5]:
	bme280SensorInstance = BME280(spi_bus=SPI_BUS,spi_dev=i)
	if bme280SensorInstance.sample_ok:
		print(f'sensor {SPI_BUS}.{i}')
		print(f't = {round(bme280SensorInstance.temperature,1)}')
		print(f'h = {round(bme280SensorInstance.humidity,1)}')
		print(f'p = {round(bme280SensorInstance.pressure,1)}')
	sleep(DELAY_BETWEEN_SENSORS)
print('-'*30)
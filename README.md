![welcome](https://i.ibb.co/5FjKB7x/welcome-to-the-jungle2.png)

# Cetgarden

Software para monitorización de cultivo hidropónico de uno o más trenes, mediante una [Raspberry PI 4B](https://www.amazon.es/gp/product/B07TC2BK1X/ref=ppx_yo_dt_b_asin_title_o06_s01?ie=UTF8&psc=1), sensor de temperatura y humedad ([DHT22](shorturl.at/hkuE7)), cámara infrarroja ([NoIR](shorturl.at/bpFJS)) y [celdas de carga](https://www.amazon.es/gp/product/B0888DXP3K/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1).

## El cultivo hidropónico

La hidroponía o agricultura hidropónica es un método utilizado para cultivar plantas usando disoluciones minerales en vez de suelo agrícola. Las raíces reciben una solución nutritiva y equilibrada disuelta en agua con los elementos químicos esenciales para el desarrollo de las plantas, que pueden crecer en una solución acuosa únicamente, o bien en un medio inerte, como arena lavada, grava o perlita, entre muchas otras.

![welcome](https://i.ibb.co/YQgBDqn/hydroponics-setup-guide.jpg)

## Montaje del sistema

Al sistema hidropónico convencional se añadirán los sensores necesarios. El sensor de temperatura y humedad [DHT22](shorturl.at/hkuE7) se colocará en un punto cualquiera, lo más cercano posible al cultivo. La camará [NoIR](shorturl.at/bpFJS) se colocará en un punto elevado, apuntando al cultivo y desde la posición más cenital posible. Las [celdas de carga](https://www.amazon.es/gp/product/B0888DXP3K/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1) se colocarán una en cada tren, siguiendo la disposición de la siguiente figura.

![esquemacelda](https://i.ibb.co/1ZRS9SX/esquema-Apoyos.png)


# Dependencias
**Schedule:** 

```
pip3 install schedule
```

**Base de datos mongo:** 

```
pip3 install pymongo
```

**DHT22:** 

```
pip3 install adafruit-circuitpython-dht (libreria de python)

sudo apt-get install libgpiod2
```

**PiCamera:**

```
sudo apt-get install python3-picamera
```

# Conexion DHT22 en Rpi 4B
Con el comando pinout desde la terminal de la rpi obtenemos un mapa de los GPIO
- Conectar positivo a alimentación 5V de la rpi
- Conectar salido del sensor (patilla central marcada como "out") al GPIO4
- Conectar negativo a tierra 

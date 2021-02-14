# Peludna prognoza
---
Aplikacija za prikupljanje i grafički prikaz podataka peludne prognoze. Podaci se prikupljanju scrapeanjem sa stranice https://stampar.hr/hr/peludna-prognoza-za-hrvatsku.

### Pokretanje aplikacije
---

Koraci:
1. Klonirati projekt
    ```bash
    git clone https://github.com/asarabok/pelpro.git
    ```
2. Pozicionarati se u root projekta
    ```bash
    cd pelpro
    ```
3. Buildati Docker container
    ```bash
    docker-compose build
    ```
4. Kreirati tablice u bazi i zapisati inicijalne podatke (gradove, biljke i mjerenja)
    ```
    docker exec flask python manage.py db upgrade
    docker exec flask python manage.py load_fixture -m City
    docker exec flask python manage.py load_fixture -m Plant
    docker exec flask python manage.py load_fixture -m Measurement
    ```
5. Pokrenuti aplikaciju iz containera
    ```bash
    docker-compose up
    ```

6. GUI i API endpointima se može pristupiti pod
    ```
    http://localhost:5000
    ```
    GUI: `/`
    API: `/api/measurements`

### API endpointi
---

 - Sva mjerenja
    ```
    /api/measurements
    ```
 - Mjerenja za grad
    ```
    /api/measurements/city/{grad_id}
    ```
 - Mjerenja za biljku
    ```
    /api/measurements/plant/{biljka_id}
    ```
 - Mjerenja za određenu biljku u gradu
    ```
    /api/measurements/city/{grad_id}}/{biljka_id}
    ```

##### API filtri
 - Broj posljednjih dana za prikaz (int)  `?days_delta={broj_dana}`

##### Primjer:
Prikaz mjerenja za lijesku za Zagreb za posljednjih 30 dana:
```
http://localhost:5000/api/measurements/city/1/lijeska-corylus-sp?days_delta=30
```

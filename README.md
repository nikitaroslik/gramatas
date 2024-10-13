
# Projekta Dokumentācija: Grāmatu Bibliotēka

## Projekta Apraksts

Šis projekts ir vienkārša tīmekļa lietotne, kas ļauj lietotājiem pārvaldīt savu grāmatu bibliotēku. Lietotne nodrošina funkcionalitāti, lai apskatītu, pievienotu, atjauninātu un dzēstu grāmatas. Projekts sastāv no divām daļām:
1. **Frontend** - HTML, CSS un JavaScript kods, kas tiek izpildīts pārlūkā.
2. **Backend** - Flask serveris Python valodā, kas nodrošina datu apstrādi un grāmatu saglabāšanu JSON failā.

## Lietotāja Rokasgrāmata

### Kā izmantot grāmatu bibliotēku:

1. **Grāmatu saraksta apskate**:
   - Kad atverat tīmekļa lapu, grāmatu saraksts automātiski tiks ielādēts un parādīts. Katrs sarakstā esošais ieraksts satur grāmatas nosaukumu, autoru un divas pogas: **Dzēst** un **Atjaunināt**.
  
2. **Pievienot jaunu grāmatu**:
   - Lai pievienotu jaunu grāmatu, aizpildiet laukus **Grāmatas nosaukums** un **Autors**, un nospiediet pogu **Pievienot grāmatu**.
   - Ja kāds no laukiem ir tukšs, sistēma jūs brīdinās, ka jāaizpilda visi lauki.

3. **Dzēst grāmatu**:
   - Lai dzēstu kādu no grāmatām, nospiediet pogu **Dzēst** pie attiecīgās grāmatas.
   - Pēc dzēšanas, grāmatu saraksts automātiski atjaunosies.

4. **Atjaunināt grāmatu**:
   - Lai atjauninātu grāmatas nosaukumu vai autoru, nospiediet pogu **Atjaunināt** pie attiecīgās grāmatas.
   - Parādīsies divi uzvednes, kur jāievada jaunais nosaukums un autors. Ja jūs nenorādīsiet kādu no šīm vērtībām, sistēma jūs brīdinās.

### Instalācijas Instrukcija:

1. **Nepieciešamās Prasības**:
   - Python 3.x
   - Flask bibliotēka (`pip install Flask`)
   - `flask_cors` bibliotēka (`pip install flask-cors`)

2. **Projekta uzstādīšana**:
   1. Lejupielādējiet projekta failus.
   2. Izveidojiet `books.json` failu ar tukšu masīvu:
      ```json
      []
      ```
   3. Sāciet Flask serveri, izpildot komandu:
      ```bash
      python app.py
      ```
   4. Atveriet tīmekļa pārlūku un apmeklējiet `http://127.0.0.1:5000`, lai piekļūtu lietotnei.

## Backend API Dokumentācija

### `GET /books`
- **Apraksts**: Atgriež visu grāmatu sarakstu.
- **Atgriež**: JSON saraksts ar grāmatām.
  
### `POST /books`
- **Apraksts**: Pievieno jaunu grāmatu.
- **Pieprasījuma dati**: 
  ```json
  {
    "title": "Grāmatas nosaukums",
    "author": "Grāmatas autors"
  }
  ```
- **Atgriež**: Jaunizveidoto grāmatu JSON formātā.
  
### `PUT /books/<id>`
- **Apraksts**: Atjaunina grāmatu ar noteikto ID.
- **Pieprasījuma dati**:
  ```json
  {
    "title": "Jauns nosaukums",
    "author": "Jauns autors"
  }
  ```
- **Atgriež**: Atjaunināto grāmatu JSON formātā vai kļūdas ziņojumu, ja grāmata nav atrasta.

### `DELETE /books/<id>`
- **Apraksts**: Dzēš grāmatu ar norādīto ID.
- **Atgriež**: Nav satura (statuss 204).

## Frontend Kods

Frontend ir uzrakstīts HTML, CSS un JavaScript valodās. Tas izmanto `fetch` funkciju, lai veiktu API pieprasījumus uz Flask serveri.

## Secinājumi

Šis projekts nodrošina vienkāršu veidu, kā pārvaldīt grāmatu kolekciju. Lietotāji var pievienot, atjaunināt un dzēst grāmatas, kā arī apskatīt esošo grāmatu sarakstu. Projekta struktūra ir modulāra, tāpēc to var paplašināt un pielāgot atbilstoši jūsu vajadzībām.

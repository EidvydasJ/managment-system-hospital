# Paprasta ligoninės valdymo sistema

## Apžvalga
Ši ligoninės valdymo sistema yra „Python“ programa, skirta padėti tvarkyti pacientų ir gydytojų sąrašą, tvarkyti vizitus ir inventorių ligoninės aplinkoje. Joje sutinkamos funkcijos, skirtos planuoti vizitus, tvarkyti informaciją apie pacientus bei gydytojus ir tvarkyti medicinos įrankių, priemonių inventorių.

## Funkcijos
- **Registracija pas gydytoją:** Planuoti vizitų datas ir laikus.
- **Gydytojų ir pacientų tvarkymas:** Pridėti gydytoją ir pacientą su Factory dizaino modelio pagalba; peržiūrėti esamą pacientų ir gydytojų sąrašą; peržiūrėti gydytojų ir pacientų informaciją.
- **Inventoriaus valdymas:** Ieškoti įrankio tarp esamų inventoriuje; pridėti naujų įrankių; atnaujinti jau esamą priemonių kiekį.

## Objektinio programavimo pagrindiniai ramsčiai
1. Enkapsuliacija
2. Paveldėjimas
3. Abstrakcija
4. Polimorfizmas

## Dizaino modeliai
1. „Factory metodas“
2. „Observer modelis“

## Kodėl būtent tokie dizaino modeliai?
- **„Factory metodas“:** Kuomet reikia kurti/pridėti žmogų, tai yra pacientą, gydytoją, labai paprasta tai įvykdyti, pasinaudojant Factory metodu. Šis metodas man patinko ir yra nuostabus, kadangi, kuriant žmogų, nėra būtina atitinkamai klasei kurti objekto ir priskirti visą informaciją - viskas daug paprasčiau. Pagal žmogaus tipą (pacientas tai, ar gydytojas), Factory sukuria žmogų su jam priskirta informacija.
- **„Observer modelis“:** Modelis, kuris, labiausiai tikėtina, nebuvo parodytas paskaitų metu, tačiau puikiai tiko įgyvendinant mano idėją - pranešti apie kažkokius pasikeitimus. Būtų tai naujo vizito registracija, būtų tai naujų priemonių „atvežimas“, būtų tai meginimas surasti objektą inventoriuje ar atnaujinti sandėlio turinį.


# Mondeling-trainer Grotius O&A

Oefentool voor het mondeling examen van de Grotius-specialisatie Onderneming & Aansprakelijkheid. Onofficieel: niet van of namens de Stichting Grotius Academie.

## Wat het doet
1. Je krijgt een casus en hebt 15 minuten om je voor te bereiden met je eigen lesstof.
2. Je beantwoordt de vraag 5 minuten mondeling. De app zet je antwoord om in tekst (Chrome of Edge op een computer).
3. Je antwoord wordt beoordeeld naast een antwoordmodel: per onderdeel een oordeel en een score op 100.

## Beoordeling
- **Zonder API-sleutel:** de app maakt een opdracht die je in claude.ai plakt; het antwoord plak je terug in de app.
- **Met een eigen Anthropic API-sleutel** (Instellingen): automatisch. De sleutel blijft in je eigen browser; de kosten zijn voor je eigen API-account.

## Privacy
- Sessies en instellingen staan alleen in je eigen browser (localStorage). Via Instellingen kun je ze exporteren en importeren.
- De spraakherkenning van Chrome stuurt audio naar de spraakdienst van Google. Wil je dat niet, typ je antwoord dan.

## Casussen toevoegen
1. Zet een nieuw bestand in `casussen/` (een lijst met casussen in hetzelfde formaat als `batch1.json`) en voeg de naam toe aan `casussen/index.json`.
2. Draai `python bouw_casussen.py`. Dat maakt `casussen.js` opnieuw aan.
3. Commit en push. Gebruikers zien de nieuwe casussen na het herladen van de pagina.

## Let op
De antwoordmodellen staan in `casussen.js` en zijn dus voor iedereen leesbaar die de broncode bekijkt.
Ze zijn oefenmateriaal en geen officiële uitwerkingen.

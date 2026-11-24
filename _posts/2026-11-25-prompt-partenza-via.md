---
layout: post
title: "Automatizzare senza complicarsi la vita"
subtitle: "Prima di chiedere a un agente AI di lavorare al posto nostro, vale la pena capire quali attività possono già essere affidate a un'automazione molto più semplice."
date: 2026-11-25 08:30:00 +0100
image: /images/14-Percorso di un prompt sulla scrivania.png
substack: "https://pianopianoai.substack.com/p/prompt-partenza-via-che-cosa-succede"
---

🎧 **Prima di iniziare**  
Niccolò Fabi — *Un passo alla volta*

Scrivi una domanda a ChatGPT.

Magari una cosa molto semplice:

> Perché il cielo è blu?

Poi premi Invio.

Per qualche istante non succede apparentemente nulla. Quindi iniziano ad apparire le prime parole della risposta.

Siamo talmente abituati a questo meccanismo che è facile immaginare ciò che avviene nel mezzo più o meno così: ChatGPT legge la domanda, la capisce, cerca tra quello che sa e formula una risposta.

È una descrizione comoda. Ma è anche abbastanza lontana da quello che succede davvero.

Proviamo allora a rallentare quei pochi secondi.

## Prima fermata: le parole spariscono

La prima cosa curiosa è che il modello non riceve esattamente le parole così come le vediamo noi.

Prima di poterle elaborare, il testo viene diviso in piccole unità chiamate **token**.

Un token può coincidere con una parola intera, con una parte di una parola, con un segno di punteggiatura o, in alcuni casi, con pochi caratteri. La divisione cambia a seconda del modello e della lingua.

“Cielo”, per esempio, potrebbe essere rappresentato da un solo token oppure essere suddiviso. Una parola poco comune o molto lunga ha maggiori probabilità di essere spezzata in più parti.

Questa operazione si chiama **tokenizzazione**.

È il primo passaggio importante perché ci ricorda una cosa: quando scriviamo a un modello linguistico, dall'altra parte non c'è qualcuno che vede una frase nello stesso modo in cui la vediamo noi. Il sistema riceve una sequenza di elementi codificati numericamente.

Ma siamo ancora soltanto all'ingresso.

## Dai token ai numeri

Un token, da solo, dice poco.

Pensiamo alla parola “banca”.

Può indicare il posto dove teniamo i soldi, ma dentro “banca dati” significa qualcosa di diverso. Se scriviamo “mi sono seduto sulla banca”, probabilmente abbiamo commesso un errore o stiamo usando la parola in un contesto insolito.

Per capire quale ruolo abbia una parola, quindi, bisogna guardare ciò che le sta intorno.

I token vengono trasformati in rappresentazioni numeriche composte da molti valori. In questo modo il modello può lavorare matematicamente sulle relazioni tra gli elementi della frase.

Qui comincia la parte più interessante.

## Ogni parola guarda le altre

Nel 2017 un gruppo di ricercatori presentò un'architettura chiamata **Transformer**, che è alla base della famiglia di modelli da cui sono nati molti degli attuali LLM.

Uno dei suoi elementi fondamentali è un meccanismo chiamato **attention**, attenzione.

Il nome, per una volta, aiuta.

Quando il modello elabora un token, può attribuire importanza diversa agli altri token presenti nel contesto.

Se scrivo:

> Il gatto è salito sul tavolo perché **era** affamato.

per interpretare “era” è utile mettere in relazione quella parola soprattutto con “gatto”.

In una frase diversa le relazioni cambiano.

Il modello esegue enormi quantità di questi calcoli attraverso molti strati successivi. Non sta consultando un dizionario per trovare il significato della frase. Sta modificando progressivamente le rappresentazioni numeriche dei token in base alle relazioni che ha imparato durante l'addestramento.

Ed è qui che il contesto comincia ad avere un peso enorme.

Se prima della domanda sul cielo abbiamo parlato per venti messaggi di astronomia, la situazione è diversa rispetto a una conversazione appena iniziata. Il sistema può elaborare insieme alla nostra domanda anche parte della conversazione e altre informazioni che gli vengono fornite.

Il prompt, quindi, non vive necessariamente da solo.

## Adesso bisogna scegliere una parola

Arriviamo al momento in cui il modello deve iniziare a rispondere.

Prendiamo ancora:

> Perché il cielo è blu?

Dopo aver elaborato l'input, il modello calcola quali token potrebbero essere buoni candidati per iniziare la risposta.

Potrebbero esserci token corrispondenti a parole come “La”, “Il”, “Perché”, “Durante” e moltissime altre possibilità.

A ciascuna viene associata una probabilità.

Il modello sceglie un token secondo il sistema di generazione utilizzato. Non significa necessariamente prendere ogni volta quello con la probabilità più alta: può esserci una certa variabilità.

Supponiamo che il primo token generato corrisponda a:

> La

A questo punto succede qualcosa di fondamentale.

Il modello prende tutto ciò che aveva prima, aggiunge **La** e calcola il token successivo.

Poi ricomincia.

> La luce

Ancora.

> La luce del

Ancora.

> La luce del Sole…

La risposta che leggiamo viene costruita così: **un token dopo l'altro**.

Non esiste necessariamente, da qualche parte dentro il modello, il paragrafo completo che viene recuperato e poi mostrato sullo schermo. La frase prende forma durante la generazione.

È anche per questo che vediamo spesso il testo apparire progressivamente.

## Ma allora sta solo indovinando la parola successiva?

Sì, ma quel “solo” rischia di trarci in inganno.

Dire che un grande modello linguistico predice il token successivo è corretto. Potrebbe però sembrare qualcosa di simile al completamento automatico della tastiera dello smartphone.

La differenza sta in tutto il lavoro che precede quella previsione.

Durante l'addestramento, modelli con un numero enorme di parametri imparano regolarità presenti nei testi: relazioni tra parole, strutture grammaticali, modi di argomentare, associazioni tra concetti e molti altri schemi.

Per prevedere bene quale elemento dovrebbe venire dopo, il modello finisce per costruire rappresentazioni molto sofisticate del testo che sta elaborando.

Questo gli permette di continuare una frase, ma anche di tradurre un brano, riassumere un documento, spiegare un concetto o modificare del codice.

Sempre attraverso lo stesso meccanismo di fondo: prevedere che cosa dovrebbe venire dopo.

## E dove sono conservate tutte le cose che “sa”?

Qui c'è un altro equivoco frequente.

Un modello linguistico non funziona normalmente come Google e nemmeno come un enorme archivio nel quale viene cercata la frase più simile alla nostra domanda.

Durante l'addestramento vengono modificati miliardi di valori numerici, i **parametri** del modello. È lì che rimangono codificate le regolarità apprese.

Quando facciamo una domanda, il modello utilizza quei parametri per calcolare una risposta.

Naturalmente un'applicazione come ChatGPT può fare anche altro. Può cercare informazioni sul Web, consultare documenti, utilizzare strumenti o recuperare dati da fonti esterne. Abbiamo già incontrato qualcosa di simile parlando di RAG.

Ma è utile separare le due cose.

**Il modello genera. Gli strumenti esterni possono fornirgli informazioni da utilizzare mentre genera.**

La distinzione diventerà ancora più importante quando parleremo della differenza tra chiedere qualcosa a ChatGPT e cercarla su Google.

## Ecco perché può inventare

A questo punto diventa anche più facile capire un argomento che avevamo affrontato nei primi articoli di PianopianoAI: le [allucinazioni](https://pianopianoai.it/articoli/Perche-ChatGPT-qualche-volta-inventa/).

Il compito fondamentale di un modello linguistico è produrre una continuazione plausibile del testo.

Non possiede un piccolo controllore interno che, prima di mostrare ogni frase, apre un'enciclopedia e verifica che sia vera.

Se le relazioni apprese portano verso una risposta molto convincente ma sbagliata, il meccanismo di generazione può continuare tranquillamente.

Una data plausibile. Un titolo che sembra esistere. Una citazione perfettamente credibile.

Token dopo token.

Sapere come nasce la risposta non elimina il problema, ma ci aiuta a capire perché esiste.

## Torniamo al pulsante Invio

Possiamo allora tornare al punto di partenza.

Hai scritto:

> Perché il cielo è blu?

e hai premuto Invio.

In quei pochi istanti il testo è stato suddiviso in token. I token sono stati trasformati in rappresentazioni numeriche. Il modello ha elaborato le relazioni tra loro utilizzando i parametri appresi durante l'addestramento. Poi ha calcolato un possibile primo token della risposta, lo ha aggiunto al contesto e ha ripetuto il calcolo.

Una volta.

Poi un'altra.

E un'altra ancora.

Sul nostro schermo, intanto, è comparsa una frase perfettamente leggibile.

È forse questo il passaggio più strano da tenere a mente quando usiamo un modello linguistico: **noi gli affidiamo parole e riceviamo parole, ma quasi tutto ciò che succede nel mezzo non assomiglia affatto al modo in cui noi leggiamo e scriviamo.**

La prossima volta che premi Invio, quei pochi secondi potrebbero sembrarti un po' meno vuoti.

### Fonti e approfondimenti

- OpenAI, [Understanding and counting tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them): una spiegazione introduttiva della tokenizzazione e dei token di input e output.
- Ashish Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017), il paper che ha introdotto l'architettura Transformer.

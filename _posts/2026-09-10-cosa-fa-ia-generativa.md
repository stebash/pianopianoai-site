---
layout: post
title: Che cosa fa davvero un’IA generativa?
subtitle: Cosa succede davvero quando fai una domanda all’IA?
date: 2026-09-10
image: /images/2-buon-compleanno.png
substack: https://pianopianoai.substack.com/p/che-cosa-fa-davvero-unia-generativa
---
[Stefano Basso](https://substack.com/@stefanobasso)  
set 10, 2026  
🎧 **Prima di iniziare**  
Elisa — *Eppure sentire*

Un amico compie cinquant’anni e vorresti scrivergli qualcosa di meno prevedibile del solito «tanti auguri». Chiedi a ChatGPT un messaggio affettuoso, magari con una battuta sulla sua abitudine di perdere le chiavi.

Dopo pochi secondi compare qualcosa del genere:

Cinquant’anni e ancora tante porte da aprire. Appena ritrovi le chiavi.


Battute a parte la domanda interessante è un’altra: **da dove arriva quella frase?**

È facile immaginare che ChatGPT abbia cercato da qualche parte un messaggio di auguri adatto e te l’abbia restituito. In fondo è quello che siamo abituati a fare con Google: scriviamo qualcosa e il motore di ricerca prova a trovare una pagina che contenga ciò che cerchiamo.

Qui succede qualcosa di diverso.

La frase sugli auguri non deve necessariamente esistere già da qualche parte. Il sistema può costruirla in quel momento.

Ed è proprio questo il significato più importante della parola **generativa**.

## **Una risposta che prende forma mentre la leggi**

Facciamo una prova molto semplice.

Se scrivo:

Tanti auguri di buon…

probabilmente penserai a *compleanno*.

Ma potrebbe anche arrivare *Natale*, *anno*, *onomastico*. Dipende da quello che è stato scritto prima.

Se poco sopra ti ho raccontato che oggi un amico compie cinquant’anni, “compleanno” diventa una continuazione molto più plausibile.

Un modello linguistico lavora, semplificando molto, proprio così: prende ciò che ha davanti e valuta quali continuazioni potrebbero avere senso. Ne produce una, poi ripete il procedimento tenendo conto anche di ciò che ha appena scritto.

La risposta nasce quindi un pezzo alla volta.

Questi piccoli pezzi vengono chiamati **token**. A volte corrispondono a una parola intera, altre volte a una parte di parola o a un segno di punteggiatura. Non è necessario conoscere i token per usare ChatGPT, ma sapere che esistono ci aiuta a capire che il testo non compare tutto insieme: viene costruito progressivamente.

Da una continuazione nasce la successiva, fino a formare la risposta che leggiamo sullo schermo.

## **Ma come fa a sapere che cosa viene dopo?**

Naturalmente non basta indovinare che dopo «buon» potrebbe arrivare «compleanno».

Durante l’addestramento, un grande modello linguistico viene esposto a enormi quantità di testo e impara moltissime regolarità: come sono costruite le frasi, quali parole tendono a comparire insieme, come si sviluppa una spiegazione, che differenza c’è tra il tono di una lettera formale e quello di un messaggio tra amici.

Impara anche relazioni tra concetti.

Se gli chiedi di spiegare la fotosintesi a un bambino, non ha bisogno che qualcuno abbia scritto in precedenza esattamente la risposta alla tua domanda. Può utilizzare ciò che ha appreso sulla fotosintesi, sul modo in cui si spiega qualcosa a un bambino e sulla lingua che stai utilizzando per costruire una risposta adatta alla richiesta.

Questo non significa che dentro il modello ci sia una gigantesca biblioteca da consultare.

Ci sono invece moltissimi valori numerici che, durante l’addestramento, sono stati modificati fino a rappresentare regolarità e relazioni presenti nei dati.

Il termine tecnico è **parametri**.

Per ora possiamo fermarci qui. Ci basta l’idea: il modello non deve recuperare una frase già pronta per poterla produrre.

## **Allora è solo un completamento automatico molto grande?**

Il paragone viene spontaneo.

Quando scrivi un messaggio sul telefono e compare la parola successiva suggerita dalla tastiera, anche quel sistema sta cercando di prevedere come potrebbe continuare la frase.

Il principio ha qualche somiglianza. Ma nei grandi modelli linguistici la quantità di relazioni apprese e il contesto che può essere preso in considerazione rendono il risultato molto più complesso.

Torniamo al nostro amico.

Non hai chiesto semplicemente «scrivi degli auguri». Hai detto che compie cinquant’anni, che vuoi un tono affettuoso e che perde continuamente le chiavi.

Queste informazioni orientano la risposta.

Se invece gli raccontassi che da qualche mese coltiva pomodori sul balcone, potrebbe comparire una battuta sul raccolto. Il modello non aveva bisogno di conoscere prima né il tuo amico né i suoi pomodori: sei stato tu a fornire quelle informazioni nella conversazione.

Ed eccoci a un’altra parola che incontreremo spesso parlando di intelligenza artificiale: **contesto**.

Il modello porta con sé ciò che ha imparato durante l’addestramento. Poi, quando gli scrivi, usa anche ciò che trova nella conversazione per decidere come continuare.

Le due cose sono diverse.

Ed è una distinzione importante, perché spiega buona parte di quello che succede quando utilizziamo questi strumenti.

## **Perché sembra che abbia capito?**

Prova a chiedere:

Riscrivi questa frase in modo più gentile.

Per farlo bene, il modello deve tenere conto del significato della frase e capire quale formulazione potrebbe risultare meno brusca.

Oppure puoi chiedergli di spiegare lo stesso concetto prima a un bambino e poi a uno studente universitario. Le informazioni di base possono rimanere simili, mentre cambiano parole, esempi e livello di dettaglio.

È questa capacità di adattare il testo al contesto che rende la conversazione con un’IA generativa così diversa dall’uso di molti programmi tradizionali.

Con un software siamo abituati a cercare il comando previsto da chi lo ha progettato. Qui possiamo descrivere con parole normali ciò che vorremmo ottenere e lasciare che il modello costruisca la risposta.

Ma proprio qui conviene ricordare una cosa.

**Costruire una risposta plausibile e scritta bene non significa automaticamente costruire una risposta vera.**

Il meccanismo che abbiamo appena visto serve a generare testo coerente. Questo spiega sia molte delle capacità di questi sistemi sia alcuni dei loro limiti.

Su questi ultimi torneremo presto. Meritano un articolo tutto loro.

Per ora possiamo tornare al nostro messaggio di compleanno.

La battuta sulle chiavi è nata dall’incontro tra ciò che il modello aveva imparato e le informazioni che gli hai dato sul tuo amico.

Se avessi cambiato quelle informazioni, sarebbe cambiata anche la risposta.

Ed è proprio da qui che possiamo fare il passo successivo: **che cosa conviene dire a un’IA quando vogliamo ottenere qualcosa di utile?**

Nel prossimo articolo parleremo di prompt. Non di formule magiche da imparare a memoria, ma delle istruzioni che diamo a questi sistemi e di come possono cambiare ciò che riceviamo in risposta.

**Per approfondire**  
Se vuoi vedere più da vicino come vengono addestrati i modelli che stanno dietro a ChatGPT, OpenAI ne propone una spiegazione semplice, che parla anche di token, parametri e previsione del testo.  
[Come vengono sviluppati ChatGPT e i modelli di OpenAI](https://help.openai.com/it-it/articles/7842364-come-vengono-sviluppati-chatgpt-e-i-nostri-modelli-foundation?utm_source=chatgpt.com)

Se questo articolo ti è stato utile e vuoi continuare il percorso, puoi iscriverti a PianopianoAI per ricevere i prossimi articoli direttamente via email.

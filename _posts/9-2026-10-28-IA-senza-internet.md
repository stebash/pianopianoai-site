---
layout: post
title: "L’intelligenza artificiale può funzionare anche senza Internet?"
subtitle: "Che cosa cambia tra usare ChatGPT e far girare un modello di IA sul proprio computer?"
date: 2026-10-28 08:30:00 +0200
image: /images/10-ia-locale.png
substack: https://pianopianoai.substack.com/p/lintelligenza-artificiale-puo-funzionare
---

🎧 Prima di iniziare
Subsonica — Liberi tutti



Grazie per aver letto PianopianoAI! Iscriviti gratuitamente per ricevere nuovi post e supportare il mio lavoro.

Sei in treno, stai lavorando a un documento e vuoi chiedere a ChatGPT di aiutarti a sistemare un paragrafo.

Scrivi la richiesta, premi Invio e aspetti.

Niente.

La connessione è sparita, probabilmente perché il treno è entrato in una galleria. Il documento è ancora sul tuo computer, ma l’intelligenza artificiale che stavi utilizzando non riesce più a risponderti.

È una situazione abbastanza normale. Quando usiamo ChatGPT, Claude o Gemini, nella maggior parte dei casi il lavoro viene svolto da computer che si trovano altrove, nei centri di calcolo delle aziende che offrono questi servizi.

Tu scrivi la domanda, questa viene inviata attraverso Internet, il modello elabora una risposta e il risultato torna sul tuo schermo.

È quello che chiamiamo cloud.

Ma esiste anche un’altra possibilità: scaricare un modello di intelligenza artificiale e farlo funzionare direttamente sul proprio computer.

Senza una connessione continua a Internet e senza dover inviare ogni domanda a un servizio esterno.

Sembra interessante. Ma è davvero una soluzione alla portata di tutti?

Un modello da portare a casa

In un (articolo precedente)[https://pianopianoai.it/articoli/lintelligenza-artificiale-migliore/] abbiamo distinto i servizi di intelligenza artificiale dai modelli che utilizzano.

ChatGPT, per esempio, è un servizio che mette a disposizione diversi modelli, insieme a strumenti e funzionalità aggiuntive.

Questa distinzione diventa importante quando parliamo di intelligenza artificiale locale.

Per utilizzare un modello sul tuo computer devi avere accesso ai file che contengono i suoi parametri, cioè i valori numerici che il modello ha acquisito durante l’addestramento. Sono, in un certo senso, ciò che gli permette di svolgere il proprio lavoro.

Alcune aziende e organizzazioni rendono disponibili questi file, chiamati pesi del modello.

Si parla spesso di modelli open-weight, cioè modelli i cui pesi possono essere scaricati e utilizzati secondo le condizioni stabilite dalla relativa licenza.

Non significa necessariamente che siano completamente open source: il codice di addestramento, i dati utilizzati e altre informazioni potrebbero non essere pubblici.

Tra le famiglie di modelli distribuite con pesi accessibili troviamo, per esempio, Llama, Qwen, Gemma e alcuni modelli di OpenAI.

Una volta scaricati i file, serve un programma capace di eseguire il modello. Strumenti come LM Studio e Ollama permettono di farlo senza dover costruire da zero un sistema di intelligenza artificiale.

Con LM Studio, per esempio, puoi scegliere un modello compatibile, scaricarlo e utilizzarlo attraverso un’interfaccia di chat.

A quel punto, se tutto è configurato per funzionare localmente, puoi anche scollegarti da Internet.

Naturalmente rimane un problema: il tuo computer deve essere abbastanza potente da eseguire il modello che hai scelto.

Una cucina per capire come funziona

Immagina di voler preparare una cena.

Quando utilizzi un servizio cloud è un po’ come andare al ristorante: scegli quello che desideri e qualcun altro mette a disposizione la cucina, il personale e le attrezzature.

Quando invece vuoi cucinare a casa, devi avere tutto il necessario.

Con i modelli di intelligenza artificiale possiamo usare un paragone simile.

Il modello è la ricetta. Contiene ciò che serve per preparare il risultato, anche se naturalmente è molto più complesso di una ricetta tradizionale.

La GPU, cioè il processore grafico, è il cuoco. È particolarmente efficace nello svolgere molti calcoli contemporaneamente, proprio quelli richiesti dai modelli linguistici.

La VRAM, la memoria dedicata alla GPU, è il piano di lavoro della cucina. È lo spazio veloce nel quale il cuoco tiene ciò che gli serve mentre prepara il piatto.

Infine c’è la RAM, la memoria principale del computer, che possiamo immaginare come il magazzino.

Il paragone è semplificato, ma aiuta a capire perché la potenza del processore non sia l’unico elemento importante.

Se il modello è troppo grande per lo spazio disponibile sulla GPU, il computer potrebbe dover utilizzare anche la RAM, con un possibile rallentamento.

È come cercare di preparare una cena complicata su un piano di lavoro troppo piccolo. Il cuoco deve continuamente spostare gli ingredienti dal magazzino al bancone.

Alcuni computer, come i Mac con chip Apple Silicon, utilizzano una memoria unificata, condivisa tra CPU e GPU. L’organizzazione è diversa, ma il problema dello spazio disponibile rimane.

E non basta avere tanta memoria per andare veloci.

Un modello può occupare poca memoria ed essere rapido, oppure richiedere risorse considerevoli e rispondere lentamente. Dipende anche dalla sua architettura, dall’hardware e da come viene eseguito.

Esistono tecniche per ridurre le dimensioni dei modelli, come la quantizzazione, che utilizza rappresentazioni numeriche meno precise per occupare meno memoria.

È un compromesso utile, anche se può comportare una perdita di qualità nelle risposte.

Perché dovrei complicarmi la vita?

A questo punto potresti chiederti perché installare un modello sul computer, quando ChatGPT funziona già piuttosto bene.

In effetti, per molte persone non ce n’è bisogno.

Un servizio cloud offre normalmente accesso a modelli molto capaci, senza richiedere hardware particolare. Non devi preoccuparti di scaricare file di grandi dimensioni, gestire la memoria del computer o aggiornare manualmente i modelli.

Apri il servizio e cominci a lavorare.

Ci sono però situazioni in cui un modello locale può avere senso.

La prima riguarda i dati.

Se utilizzi un modello interamente sul tuo computer, i testi che gli fornisci possono essere elaborati senza essere inviati a un server esterno.

Può essere interessante quando lavori su documenti personali o informazioni che preferisci non condividere con un servizio cloud.

Attenzione, però: avere un modello locale non significa automaticamente avere un sistema sicuro. I file rimangono sul computer e devono comunque essere protetti. Inoltre bisogna verificare che il programma e gli eventuali strumenti collegati non inviino informazioni all’esterno.

Un secondo vantaggio è la possibilità di lavorare senza connessione.

Una volta scaricato e configurato il modello, puoi continuare a utilizzarlo anche offline, almeno per le attività che non richiedono servizi esterni.

Infine c’è il controllo.

Puoi scegliere il modello, mantenerne una determinata versione, sperimentare configurazioni differenti e decidere quando aggiornarlo.

In cambio, però, ti assumi una parte del lavoro che nel cloud svolge il fornitore.

E anche i costi cambiano: magari non paghi un abbonamento per ogni utilizzo, ma hai bisogno di un computer adeguato, consumi energia e devi dedicare tempo alla gestione.

Un modello locale è bravo quanto ChatGPT?

Dipende dal modello, dal computer e da quello che gli chiedi.

Alcuni modelli scaricabili sono molto capaci e possono dare buoni risultati nella scrittura, nei riassunti, nella programmazione e in altri compiti.

Ma un modello sufficientemente piccolo da funzionare comodamente su un portatile non offre necessariamente le stesse prestazioni dei modelli più avanzati disponibili attraverso i servizi cloud.

Potresti accorgerti che scrive risposte meno articolate, fatica a seguire istruzioni complesse oppure impiega più tempo per generare un testo.

In altri casi la differenza potrebbe essere poco importante.

Se devi correggere una mail, classificare alcune informazioni o riorganizzare appunti, un modello più piccolo potrebbe essere del tutto adeguato.

Se invece stai affrontando un problema complesso, potresti preferire un servizio che mette a disposizione modelli più potenti.

È una distinzione che abbiamo già incontrato parlando di quale sia l’intelligenza artificiale migliore: la risposta dipende soprattutto dal lavoro che vogliamo svolgere.

Come provarne uno senza acquistare un nuovo computer

Se sei curioso, non serve cominciare comprando una scheda grafica.

Puoi verificare se il tuo computer è compatibile con LM Studio, un programma disponibile per diversi sistemi operativi che permette di scaricare e utilizzare modelli linguistici in locale.

Una volta installato, puoi scegliere un modello di dimensioni contenute, seguendo le indicazioni sulle risorse necessarie.

Per cominciare non cercherei il modello più grande che il computer riesce a caricare. Ne sceglierei uno piccolo, per capire come funziona il programma e valutare la velocità delle risposte.

Potresti chiedergli di riscrivere un paragrafo, spiegare un concetto oppure riassumere un breve testo.

Poi prova a disattivare il Wi-Fi.

Se il modello è stato scaricato e viene eseguito interamente in locale, dovrebbe continuare a risponderti.

Questa piccola prova permette di vedere concretamente la differenza tra utilizzare un modello sul proprio computer e collegarsi a uno che lavora altrove.

Non aspettarti necessariamente la stessa esperienza di ChatGPT. Potrebbero esserci differenze nella qualità delle risposte, nella velocità e nelle funzionalità disponibili.

Ed è proprio questo che rende interessante l’esperimento.

E allora, cloud o locale?

Torniamo al treno.

La connessione continua a funzionare a intermittenza. Sul computer hai un modello locale, magari meno capace di quello che utilizzi abitualmente online, ma sufficiente per sistemare il paragrafo che stavi scrivendo.

Puoi continuare a lavorare.

Quando tornerà la connessione, magari userai nuovamente ChatGPT per un compito più impegnativo.

Non c’è nessuna ragione per scegliere definitivamente un sistema e rinunciare all’altro.

Per molte attività il cloud continuerà probabilmente a essere la soluzione più semplice. Per altre potrebbe essere utile avere un modello sul proprio computer, soprattutto quando contano la riservatezza dei dati, l’indipendenza dalla connessione o la possibilità di controllare direttamente lo strumento.

C’è anche un aspetto che trovo interessante.

Siamo abituati a pensare all’intelligenza artificiale come a qualcosa che appartiene necessariamente a grandi aziende, con enormi centri di calcolo.

Eppure oggi possiamo scaricare un modello e farlo funzionare su un computer che abbiamo in casa.

Non sarà necessariamente il più potente. Magari risponderà con qualche esitazione e impiegherà diversi secondi per scrivere una frase.

Ma quel piccolo esperimento può aiutarci a capire qualcosa di importante: l’intelligenza artificiale non deve per forza essere un servizio a cui ci colleghiamo. Può essere anche uno strumento che possediamo e gestiamo direttamente.

La domanda, a quel punto, diventa molto concreta: per quali attività vale la pena avere una piccola cucina tutta nostra?



Fonti e approfondimenti





LM Studio – Guida introduttiva. Come scaricare ed eseguire un modello sul proprio computer.



LM Studio – Funzionamento offline. Quali attività possono essere svolte senza connessione e quali richiedono Internet.



Ollama. Un altro strumento per utilizzare modelli di intelligenza artificiale in locale.
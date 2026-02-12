# ISTRUZIONI TECNICHE PER CONFIGURAZIONE SITO HUGO BLOX

## 1. Obiettivo
Risolvere gli errori di rendering (layout missing) e popolare il contenuto del sito estraendo i dati ESCLUSIVAMENTE dal file sorgente `CVGsteccaEuropass2026_it.tex`.

## 2. Risoluzione Errori di Layout
- **Root Pages**: Configurare `content/en/_index.md` e `content/it/_index.md` con il parametro `type: widget_page` nel front matter.
- **Dependency Sync**: Eseguire `hugo mod tidy` in ambiente WSL per assicurarsi che i moduli di Hugo Blox (blox-bootstrap/v5) siano montati correttamente.

## 3. Protocollo di Popolamento Contenuti (MOLTO IMPORTANTE)
NON utilizzare informazioni riassunte precedentemente. Il tool deve:
1. Aprire il file `CVGsteccaEuropass2026_it.tex`.
2. Estrarre la sezione `\ecvsection{Istruzione e formazione}`.
3. Mappare i titoli di studio rispettando fedelmente le date e le istituzioni indicate (es. Dottorato di Ricerca in Ingegneria Economico Gestionale presso Tor Vergata, 2002-2004).
4. Tradurre i termini tecnici in inglese per la cartella `content/en/` e mantenerli originali per `content/it/`.

## 4. Gestione Pubblicazioni (No Single Pages)
- **Disabilitare Importazione Massiva**: Non utilizzare il comando `academic import`.
- **Static Asset**: Copiare il file `scopus2025.bib` nella cartella `static/files/`.
- **Widget Widget**: Creare un widget `publications.md` che contenga esclusivamente un link per il download del file `.bib` originale.
- **Menu**: Aggiungere nel file `hugo.yaml` una voce di menu "Bibliography" (EN) / "Bibliografia" (IT) che punti direttamente a `files/scopus2025.bib`.

## 5. Verifica Finale
- Verificare che il sito giri su `localhost:1313` senza avvisi di "layout not found".
- Controllare che l'elenco dei titoli di studio corrisponda al 100% al testo contenuto nel file LaTeX originale.
# Notiz für ein Upstream-Issue: pattern5.ttl

`docs/patterns/pattern5.ttl` deklariert `@prefix hat_Teil: <> .` mit leerer IRI, obwohl der
Block `hat_Teil:` tatsächlich verwendet (`Sekundarbereich_II: hat_Teil: G8_Einführungsphase:, …`).
Alle anderen Patterns (z. B. pattern6.ttl) schreiben dafür
`@prefix hat_Teil: <http://purl.obolibrary.org/obo/BFO_0000051> .` — die IRI fehlt hier
vermutlich nur versehentlich. Wörtlich kopiert bleibt das gültiges Turtle — `hat_Teil:`
löst sich dann aber gegen die Basis-IRI des Dokuments auf, nicht gegen `obo:BFO_0000051`.

Fix: die Zeile auf `@prefix hat_Teil: <http://purl.obolibrary.org/obo/BFO_0000051> .` ändern.

Noch nicht eingereicht — Entwurf für ein Issue bei FWU-DE/lehrplan-ontologie.

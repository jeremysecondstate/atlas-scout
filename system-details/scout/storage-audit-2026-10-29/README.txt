SCOUT DATASTORE AUDIT — OCTOBER 29, 2026

Actor: Scout
Purpose: Jeremy-requested storage comparison for Atlas's 15-minute-only cleanup.
Scope: Completed metadata-only report and source references, explicitly authorized
for publication to jeremysecondstate/atlas-scout. This is a report export, not an
application source change, installation, runtime deployment or cleanup action.

Files in this directory:
- Scout-DATASTORE-read-only-report.txt: full report, all folder sizes/counts,
  every SQLite database/sidecar, consumers, representation analysis and limits.
- folder-tree.csv: 57,548 folders, recursive and direct logical size/file counts.
- sqlite-inventory.csv: 90 SQLite databases, allocation/sidecars and source map.

The original scan ran October 29, 2026, approximately 20:56-21:05 Pacific.
Measured total: 288,338,549,866 bytes (268.54 GiB), 214,605 files.
The original report's statement that it had not been published describes its
audit-time state. These exact report bytes were subsequently published at
Jeremy's explicit request. Local source paths refer to Scout's inspected files.

Atlas should fetch these files from this Git repository and use them as dated
comparison evidence alongside its own actual consumers and installed sources.
Scout's absence/smallness of a path does not establish Atlas deletion safety.
All OPRA history remains protected. Current sizes are not three-day growth.
Gameplan retirement is the October 29 human direction; historical repository
prose does not restore retired operations.

The report contains no database row exports, raw market records, fitted models,
credential values or account values. Only these three requested deliverables
and this index are included. Local scripts and underlying inventory intermediates
are not part of the export.

Verification: exact reviewed SHA-256 identities, CSV coverage, an independent
metadata/privacy review, and the pinned local private-value scanner passed.
No tests involving providers, models, trading or running applications were run.

SHA-256 / bytes:
Scout-DATASTORE-read-only-report.txt
  c13aba39b52d48c602791988e57d33e30121b839f8f788c77ac3d3c2eef786e4  5386506 bytes
folder-tree.csv
  bcf4f2ff9b3b5d2caaa54ce4dd728cd1a639356a48a223be6e14bb7fd5a8aae7  6867835 bytes
sqlite-inventory.csv
  8a09d5c8876478215e4c1b978c488528ca3d973c7e2755c6e09ac187f44114de  29333 bytes

Completion-ID: 20261030T044411Z-scout-storage-audit-dcecb15a
Reviewed base: 8238b4af8e535f93c8c780465c2111f1320372be

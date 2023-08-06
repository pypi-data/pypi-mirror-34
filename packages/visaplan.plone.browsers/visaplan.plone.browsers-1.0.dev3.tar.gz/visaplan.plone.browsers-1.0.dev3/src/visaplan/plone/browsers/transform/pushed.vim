"  Korrektur für Python-Dateien, die aus dem Sandkasten zurückgekommen sind
%s,^\(from\) \(tools_\)\?\(classes\|spoons\|misc\|debug\|html\|misc\) \(import\)\>,\1 ...tools.\3 \4,e
%s,^\(from\) \(transform_\)\?\(sniff\|forks\|utils\|config\|dispatcher\|tocspecs\) \(import\)\>,\1 .\3 \4,e
%s,^\(from\) \(PDFreactor\) \(import\)\>,\1 ..export.\2 \3,e
%s,^\(from\) \(export\)_\(utils\) \(import\)\>,\1 ..\2.\3 \4,e

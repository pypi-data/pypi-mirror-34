" Transformationen für Module aus transform-Browser
%s,^\(from\) \.\.\.\(tools\)\.\(html\|misc\|debug\|csvfiles\) \(import\),\1 \2_\3 \4,e
" prominentere Module:
%s,^\(from\) \.\.\.\(tools\)\.\(spoons\|classes\) \(import\),\1 \3 \4,e
" Allgemeines:
%s,^\(from\) \.\.\.\(tools\)\.\(cfg\) \(import\),\1 mock_\3 \4,e
%s,^\(from\) \.\.\.\(browser\)\.\(versioninformation\)\.\2 \(import\),\1 mock_\3 \4,e
" eigener (transform-) Browser:
%s,^\(from\) \.\(sniff\|utils\|config\|kitchen\|dispatcher\|tocspecs\) \(import\),\1 transform_\2 \3,e
%s,^\(from\) \.\(forks\) \(import\),\1 \2 \3,e

%s,^\(from\) \.\.export\.\(PDFreactor\) \(import\),\1 \2 \3,e
%s,^\(from\) \.\.\(export\)\.\(utils\) \(import\),\1 \2_\3 \4,e

#requires -version 5.1
[CmdletBinding()]
param(
  [string]$RootPath = ".",
  [string]$OutDir   = ".",
  [string[]]$ExcludeDirs = @(
    ".git",".github",".vscode",".idea",".vs",
    "node_modules","dist","build","out",".next",".svelte-kit",
    "target","bin","obj","coverage","logs",
    ".venv","venv","__pycache__",".terraform",".gradle",".mvn"
  ),
  [string[]]$ExcludeExtensions = @(".log",".tmp",".lock",".DS_Store",".class",".pyc",".pyo"),
  [int]$MaxDepth = 0
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Ścieżki
$rootFull = (Resolve-Path -LiteralPath $RootPath).Path
if (-not (Test-Path -LiteralPath $OutDir)) { $null = New-Item -ItemType Directory -Path $OutDir -Force }
$outFull  = (Resolve-Path -LiteralPath $OutDir).Path
$filesTxt = Join-Path $outFull 'project-files.txt'
$treeMd   = Join-Path $outFull 'project-tree.md'

function Get-ProjectFiles {
  param(
    [string]$StartPath,
    [string[]]$ExcludeDirs,
    [string[]]$ExcludeExts,
    [int]$MaxDepth
  )
  Push-Location -LiteralPath $StartPath
  try {
    $q = New-Object System.Collections.Generic.Queue[object]
    $q.Enqueue([pscustomobject]@{ Path = (Resolve-Path ".\").Path; Depth = 0 })
    $list = New-Object System.Collections.Generic.List[string]

    while ($q.Count -gt 0) {
      $cur = $q.Dequeue()
      $curName = Split-Path -Leaf $cur.Path
      if ($ExcludeDirs -contains $curName) { continue }

      $children = Get-ChildItem -LiteralPath $cur.Path -Force -ErrorAction SilentlyContinue
      foreach ($child in $children) {
        if ($child.PSIsContainer) {
          if ($MaxDepth -eq 0 -or $cur.Depth + 1 -le $MaxDepth) {
            if (-not ($ExcludeDirs -contains $child.Name)) {
              $q.Enqueue([pscustomobject]@{ Path = $child.FullName; Depth = $cur.Depth + 1 })
            }
          }
        } else {
          if ($ExcludeExts -contains $child.Extension) { continue }
          $rel = Resolve-Path -LiteralPath $child.FullName -Relative
          $list.Add(($rel -replace '\\','/'))
        }
      }
    }
    ($list | Sort-Object -Unique)
  }
  finally { Pop-Location }
}

$files = Get-ProjectFiles -StartPath $rootFull -ExcludeDirs $ExcludeDirs -ExcludeExts $ExcludeExtensions -MaxDepth $MaxDepth

# TXT
$files | Set-Content -Path $filesTxt -Encoding UTF8

# Drzewo (ASCII) do MD
function New-TreeLines {
  param([string[]]$Paths, [string]$RootLabel)

  $tree = @{}
  foreach ($p in $Paths) {
    $segs = $p -split '/'
    $node = $tree
    for ($i=0; $i -lt $segs.Length; $i++) {
      $seg = $segs[$i]
      $isFile = ($i -eq $segs.Length - 1)
      if (-not $node.ContainsKey($seg)) { $node[$seg] = @{ __children = @{}; __isFile = $isFile } }
      else { if ($isFile) { $node[$seg].__isFile = $true } }
      $node = $node[$seg].__children
    }
  }

  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add($RootLabel)

  function Render([hashtable]$n, [string]$prefix) {
    $keys  = $n.Keys | Sort-Object
    $dirs  = @(); $files = @()
    foreach ($k in $keys) {
      $isFile = $n[$k].__isFile -and ($n[$k].__children.Count -eq 0)
      if ($isFile) { $files += $k } else { $dirs += $k }
    }
    $ordered = @($dirs + $files)
    for ($i=0; $i -lt $ordered.Count; $i++) {
      $k = $ordered[$i]; $entry = $n[$k]
      $isLast = ($i -eq $ordered.Count - 1)
      $branch = if ($isLast) { "+-- " } else { "|-- " }
      $lines.Add($prefix + $branch + $k)
      $childPrefix = if ($isLast) { $prefix + "    " } else { $prefix + "|   " }
      if ($entry.__children.Count -gt 0) { Render $entry.__children $childPrefix }
    }
  }

  Render $tree ""
  return $lines
}

$rootLabel = Split-Path -Leaf $rootFull
$treeLines = New-TreeLines -Paths $files -RootLabel $rootLabel

@(
  "# Struktura projektu: $rootLabel"
  ""
  '```text'
  $treeLines
  '```'
) | Set-Content -Path $treeMd -Encoding UTF8

Write-Host "Zapisano:" -ForegroundColor Green
Write-Host " - $filesTxt"
Write-Host " - $treeMd"

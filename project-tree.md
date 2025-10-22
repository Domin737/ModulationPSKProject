﻿# Struktura projektu: ModulationPSKProject

```text
ModulationPSKProject
|-- .
|   |-- docs
|   |   |-- ANALIZA_BLEDOW.md
|   |   |-- CODE_REVIEW.md
|   |   |-- COMPLETE_PROJECT_SUMMARY.md
|   |   |-- FILE_INDEX.md
|   |   |-- FILES_TO_DELETE.md
|   |   |-- INDEX.md
|   |   |-- INSTALLATION.md
|   |   |-- INSTRUKCJA_UZYCIA.md
|   |   |-- PODSUMOWANIE.md
|   |   |-- PROJECT_ARCHITECTURE.md
|   |   |-- QUICK_START.md
|   |   |-- QUICKSTART.md
|   |   |-- setup.bat
|   |   |-- setup.sh
|   |   |-- test_environment.py
|   |   +-- WYJASNIENIE_KODU.md
|   |-- results
|   |   |-- .gitkeep
|   |   +-- README.md
|   |-- src
|   |   |-- __pycache__
|   |   |   |-- AddAWGNNoise.cpython-313.pyc
|   |   |   |-- Demodulator.cpython-313.pyc
|   |   |   |-- GetBytes.cpython-313.pyc
|   |   |   |-- Modulator.cpython-313.pyc
|   |   |   +-- TransmissionChannel.cpython-313.pyc
|   |   |-- AddAWGNNoise.py
|   |   |-- Demodulator.py
|   |   |-- GetBytes.py
|   |   |-- main.py
|   |   |-- Modulator.py
|   |   +-- TransmissionChannel.py
|   |-- venv
|   |   |-- Lib
|   |   |   +-- site-packages
|   |   |       |-- __pycache__
|   |   |       |   |-- pylab.cpython-313.pyc
|   |   |       |   +-- six.cpython-313.pyc
|   |   |       |-- contourpy
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- _version.cpython-313.pyc
|   |   |       |   |   |-- array.cpython-313.pyc
|   |   |       |   |   |-- chunk.cpython-313.pyc
|   |   |       |   |   |-- convert.cpython-313.pyc
|   |   |       |   |   |-- dechunk.cpython-313.pyc
|   |   |       |   |   |-- enum_util.cpython-313.pyc
|   |   |       |   |   |-- typecheck.cpython-313.pyc
|   |   |       |   |   +-- types.cpython-313.pyc
|   |   |       |   |-- util
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _build_config.cpython-313.pyc
|   |   |       |   |   |   |-- bokeh_renderer.cpython-313.pyc
|   |   |       |   |   |   |-- bokeh_util.cpython-313.pyc
|   |   |       |   |   |   |-- data.cpython-313.pyc
|   |   |       |   |   |   |-- mpl_renderer.cpython-313.pyc
|   |   |       |   |   |   |-- mpl_util.cpython-313.pyc
|   |   |       |   |   |   +-- renderer.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _build_config.py
|   |   |       |   |   |-- bokeh_renderer.py
|   |   |       |   |   |-- bokeh_util.py
|   |   |       |   |   |-- data.py
|   |   |       |   |   |-- mpl_renderer.py
|   |   |       |   |   |-- mpl_util.py
|   |   |       |   |   +-- renderer.py
|   |   |       |   |-- __init__.py
|   |   |       |   |-- _contourpy.cp313-win_amd64.lib
|   |   |       |   |-- _contourpy.cp313-win_amd64.pyd
|   |   |       |   |-- _contourpy.pyi
|   |   |       |   |-- _version.py
|   |   |       |   |-- array.py
|   |   |       |   |-- chunk.py
|   |   |       |   |-- convert.py
|   |   |       |   |-- dechunk.py
|   |   |       |   |-- enum_util.py
|   |   |       |   |-- py.typed
|   |   |       |   |-- typecheck.py
|   |   |       |   +-- types.py
|   |   |       |-- contourpy-1.3.3.dist-info
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- LICENSE
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   +-- WHEEL
|   |   |       |-- cycler
|   |   |       |   |-- __pycache__
|   |   |       |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |-- __init__.py
|   |   |       |   +-- py.typed
|   |   |       |-- cycler-0.12.1.dist-info
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- LICENSE
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- top_level.txt
|   |   |       |   +-- WHEEL
|   |   |       |-- dateutil
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- _common.cpython-313.pyc
|   |   |       |   |   |-- _version.cpython-313.pyc
|   |   |       |   |   |-- easter.cpython-313.pyc
|   |   |       |   |   |-- relativedelta.cpython-313.pyc
|   |   |       |   |   |-- rrule.cpython-313.pyc
|   |   |       |   |   |-- tzwin.cpython-313.pyc
|   |   |       |   |   +-- utils.cpython-313.pyc
|   |   |       |   |-- parser
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _parser.cpython-313.pyc
|   |   |       |   |   |   +-- isoparser.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _parser.py
|   |   |       |   |   +-- isoparser.py
|   |   |       |   |-- tz
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _common.cpython-313.pyc
|   |   |       |   |   |   |-- _factories.cpython-313.pyc
|   |   |       |   |   |   |-- tz.cpython-313.pyc
|   |   |       |   |   |   +-- win.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _common.py
|   |   |       |   |   |-- _factories.py
|   |   |       |   |   |-- tz.py
|   |   |       |   |   +-- win.py
|   |   |       |   |-- zoneinfo
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- rebuild.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- dateutil-zoneinfo.tar.gz
|   |   |       |   |   +-- rebuild.py
|   |   |       |   |-- __init__.py
|   |   |       |   |-- _common.py
|   |   |       |   |-- _version.py
|   |   |       |   |-- easter.py
|   |   |       |   |-- relativedelta.py
|   |   |       |   |-- rrule.py
|   |   |       |   |-- tzwin.py
|   |   |       |   +-- utils.py
|   |   |       |-- fontTools
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |-- afmLib.cpython-313.pyc
|   |   |       |   |   |-- agl.cpython-313.pyc
|   |   |       |   |   |-- annotations.cpython-313.pyc
|   |   |       |   |   |-- fontBuilder.cpython-313.pyc
|   |   |       |   |   |-- help.cpython-313.pyc
|   |   |       |   |   |-- tfmLib.cpython-313.pyc
|   |   |       |   |   |-- ttx.cpython-313.pyc
|   |   |       |   |   +-- unicode.cpython-313.pyc
|   |   |       |   |-- cffLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- CFF2ToCFF.cpython-313.pyc
|   |   |       |   |   |   |-- CFFToCFF2.cpython-313.pyc
|   |   |       |   |   |   |-- specializer.cpython-313.pyc
|   |   |       |   |   |   |-- transforms.cpython-313.pyc
|   |   |       |   |   |   +-- width.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- CFF2ToCFF.py
|   |   |       |   |   |-- CFFToCFF2.py
|   |   |       |   |   |-- specializer.py
|   |   |       |   |   |-- transforms.py
|   |   |       |   |   +-- width.py
|   |   |       |   |-- colorLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- builder.cpython-313.pyc
|   |   |       |   |   |   |-- errors.cpython-313.pyc
|   |   |       |   |   |   |-- geometry.cpython-313.pyc
|   |   |       |   |   |   |-- table_builder.cpython-313.pyc
|   |   |       |   |   |   +-- unbuilder.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- builder.py
|   |   |       |   |   |-- errors.py
|   |   |       |   |   |-- geometry.py
|   |   |       |   |   |-- table_builder.py
|   |   |       |   |   +-- unbuilder.py
|   |   |       |   |-- config
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   +-- __init__.py
|   |   |       |   |-- cu2qu
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- benchmark.cpython-313.pyc
|   |   |       |   |   |   |-- cli.cpython-313.pyc
|   |   |       |   |   |   |-- cu2qu.cpython-313.pyc
|   |   |       |   |   |   |-- errors.cpython-313.pyc
|   |   |       |   |   |   +-- ufo.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- benchmark.py
|   |   |       |   |   |-- cli.py
|   |   |       |   |   |-- cu2qu.c
|   |   |       |   |   |-- cu2qu.cp313-win_amd64.pyd
|   |   |       |   |   |-- cu2qu.py
|   |   |       |   |   |-- errors.py
|   |   |       |   |   +-- ufo.py
|   |   |       |   |-- designspaceLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- split.cpython-313.pyc
|   |   |       |   |   |   |-- statNames.cpython-313.pyc
|   |   |       |   |   |   +-- types.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- split.py
|   |   |       |   |   |-- statNames.py
|   |   |       |   |   +-- types.py
|   |   |       |   |-- encodings
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- codecs.cpython-313.pyc
|   |   |       |   |   |   |-- MacRoman.cpython-313.pyc
|   |   |       |   |   |   +-- StandardEncoding.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- codecs.py
|   |   |       |   |   |-- MacRoman.py
|   |   |       |   |   +-- StandardEncoding.py
|   |   |       |   |-- feaLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- ast.cpython-313.pyc
|   |   |       |   |   |   |-- builder.cpython-313.pyc
|   |   |       |   |   |   |-- error.cpython-313.pyc
|   |   |       |   |   |   |-- lexer.cpython-313.pyc
|   |   |       |   |   |   |-- location.cpython-313.pyc
|   |   |       |   |   |   |-- lookupDebugInfo.cpython-313.pyc
|   |   |       |   |   |   |-- parser.cpython-313.pyc
|   |   |       |   |   |   +-- variableScalar.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- ast.py
|   |   |       |   |   |-- builder.py
|   |   |       |   |   |-- error.py
|   |   |       |   |   |-- lexer.c
|   |   |       |   |   |-- lexer.cp313-win_amd64.pyd
|   |   |       |   |   |-- lexer.py
|   |   |       |   |   |-- location.py
|   |   |       |   |   |-- lookupDebugInfo.py
|   |   |       |   |   |-- parser.py
|   |   |       |   |   +-- variableScalar.py
|   |   |       |   |-- merge
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- base.cpython-313.pyc
|   |   |       |   |   |   |-- cmap.cpython-313.pyc
|   |   |       |   |   |   |-- layout.cpython-313.pyc
|   |   |       |   |   |   |-- options.cpython-313.pyc
|   |   |       |   |   |   |-- tables.cpython-313.pyc
|   |   |       |   |   |   |-- unicode.cpython-313.pyc
|   |   |       |   |   |   +-- util.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- base.py
|   |   |       |   |   |-- cmap.py
|   |   |       |   |   |-- layout.py
|   |   |       |   |   |-- options.py
|   |   |       |   |   |-- tables.py
|   |   |       |   |   |-- unicode.py
|   |   |       |   |   +-- util.py
|   |   |       |   |-- misc
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- arrayTools.cpython-313.pyc
|   |   |       |   |   |   |-- bezierTools.cpython-313.pyc
|   |   |       |   |   |   |-- classifyTools.cpython-313.pyc
|   |   |       |   |   |   |-- cliTools.cpython-313.pyc
|   |   |       |   |   |   |-- configTools.cpython-313.pyc
|   |   |       |   |   |   |-- cython.cpython-313.pyc
|   |   |       |   |   |   |-- dictTools.cpython-313.pyc
|   |   |       |   |   |   |-- eexec.cpython-313.pyc
|   |   |       |   |   |   |-- encodingTools.cpython-313.pyc
|   |   |       |   |   |   |-- enumTools.cpython-313.pyc
|   |   |       |   |   |   |-- etree.cpython-313.pyc
|   |   |       |   |   |   |-- filenames.cpython-313.pyc
|   |   |       |   |   |   |-- fixedTools.cpython-313.pyc
|   |   |       |   |   |   |-- intTools.cpython-313.pyc
|   |   |       |   |   |   |-- iterTools.cpython-313.pyc
|   |   |       |   |   |   |-- lazyTools.cpython-313.pyc
|   |   |       |   |   |   |-- loggingTools.cpython-313.pyc
|   |   |       |   |   |   |-- macCreatorType.cpython-313.pyc
|   |   |       |   |   |   |-- macRes.cpython-313.pyc
|   |   |       |   |   |   |-- psCharStrings.cpython-313.pyc
|   |   |       |   |   |   |-- psLib.cpython-313.pyc
|   |   |       |   |   |   |-- psOperators.cpython-313.pyc
|   |   |       |   |   |   |-- py23.cpython-313.pyc
|   |   |       |   |   |   |-- roundTools.cpython-313.pyc
|   |   |       |   |   |   |-- sstruct.cpython-313.pyc
|   |   |       |   |   |   |-- symfont.cpython-313.pyc
|   |   |       |   |   |   |-- testTools.cpython-313.pyc
|   |   |       |   |   |   |-- textTools.cpython-313.pyc
|   |   |       |   |   |   |-- timeTools.cpython-313.pyc
|   |   |       |   |   |   |-- transform.cpython-313.pyc
|   |   |       |   |   |   |-- treeTools.cpython-313.pyc
|   |   |       |   |   |   |-- vector.cpython-313.pyc
|   |   |       |   |   |   |-- visitor.cpython-313.pyc
|   |   |       |   |   |   |-- xmlReader.cpython-313.pyc
|   |   |       |   |   |   +-- xmlWriter.cpython-313.pyc
|   |   |       |   |   |-- filesystem
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _base.cpython-313.pyc
|   |   |       |   |   |   |   |-- _copy.cpython-313.pyc
|   |   |       |   |   |   |   |-- _errors.cpython-313.pyc
|   |   |       |   |   |   |   |-- _info.cpython-313.pyc
|   |   |       |   |   |   |   |-- _osfs.cpython-313.pyc
|   |   |       |   |   |   |   |-- _path.cpython-313.pyc
|   |   |       |   |   |   |   |-- _subfs.cpython-313.pyc
|   |   |       |   |   |   |   |-- _tempfs.cpython-313.pyc
|   |   |       |   |   |   |   |-- _tools.cpython-313.pyc
|   |   |       |   |   |   |   |-- _walk.cpython-313.pyc
|   |   |       |   |   |   |   +-- _zipfs.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _base.py
|   |   |       |   |   |   |-- _copy.py
|   |   |       |   |   |   |-- _errors.py
|   |   |       |   |   |   |-- _info.py
|   |   |       |   |   |   |-- _osfs.py
|   |   |       |   |   |   |-- _path.py
|   |   |       |   |   |   |-- _subfs.py
|   |   |       |   |   |   |-- _tempfs.py
|   |   |       |   |   |   |-- _tools.py
|   |   |       |   |   |   |-- _walk.py
|   |   |       |   |   |   +-- _zipfs.py
|   |   |       |   |   |-- plistlib
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- arrayTools.py
|   |   |       |   |   |-- bezierTools.c
|   |   |       |   |   |-- bezierTools.cp313-win_amd64.pyd
|   |   |       |   |   |-- bezierTools.py
|   |   |       |   |   |-- classifyTools.py
|   |   |       |   |   |-- cliTools.py
|   |   |       |   |   |-- configTools.py
|   |   |       |   |   |-- cython.py
|   |   |       |   |   |-- dictTools.py
|   |   |       |   |   |-- eexec.py
|   |   |       |   |   |-- encodingTools.py
|   |   |       |   |   |-- enumTools.py
|   |   |       |   |   |-- etree.py
|   |   |       |   |   |-- filenames.py
|   |   |       |   |   |-- fixedTools.py
|   |   |       |   |   |-- intTools.py
|   |   |       |   |   |-- iterTools.py
|   |   |       |   |   |-- lazyTools.py
|   |   |       |   |   |-- loggingTools.py
|   |   |       |   |   |-- macCreatorType.py
|   |   |       |   |   |-- macRes.py
|   |   |       |   |   |-- psCharStrings.py
|   |   |       |   |   |-- psLib.py
|   |   |       |   |   |-- psOperators.py
|   |   |       |   |   |-- py23.py
|   |   |       |   |   |-- roundTools.py
|   |   |       |   |   |-- sstruct.py
|   |   |       |   |   |-- symfont.py
|   |   |       |   |   |-- testTools.py
|   |   |       |   |   |-- textTools.py
|   |   |       |   |   |-- timeTools.py
|   |   |       |   |   |-- transform.py
|   |   |       |   |   |-- treeTools.py
|   |   |       |   |   |-- vector.py
|   |   |       |   |   |-- visitor.py
|   |   |       |   |   |-- xmlReader.py
|   |   |       |   |   +-- xmlWriter.py
|   |   |       |   |-- mtiLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- __main__.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- __main__.py
|   |   |       |   |-- otlLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- builder.cpython-313.pyc
|   |   |       |   |   |   |-- error.cpython-313.pyc
|   |   |       |   |   |   +-- maxContextCalc.cpython-313.pyc
|   |   |       |   |   |-- optimize
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   +-- gpos.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   +-- gpos.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- builder.py
|   |   |       |   |   |-- error.py
|   |   |       |   |   +-- maxContextCalc.py
|   |   |       |   |-- pens
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- areaPen.cpython-313.pyc
|   |   |       |   |   |   |-- basePen.cpython-313.pyc
|   |   |       |   |   |   |-- boundsPen.cpython-313.pyc
|   |   |       |   |   |   |-- cairoPen.cpython-313.pyc
|   |   |       |   |   |   |-- cocoaPen.cpython-313.pyc
|   |   |       |   |   |   |-- cu2quPen.cpython-313.pyc
|   |   |       |   |   |   |-- explicitClosingLinePen.cpython-313.pyc
|   |   |       |   |   |   |-- filterPen.cpython-313.pyc
|   |   |       |   |   |   |-- freetypePen.cpython-313.pyc
|   |   |       |   |   |   |-- hashPointPen.cpython-313.pyc
|   |   |       |   |   |   |-- momentsPen.cpython-313.pyc
|   |   |       |   |   |   |-- perimeterPen.cpython-313.pyc
|   |   |       |   |   |   |-- pointInsidePen.cpython-313.pyc
|   |   |       |   |   |   |-- pointPen.cpython-313.pyc
|   |   |       |   |   |   |-- qtPen.cpython-313.pyc
|   |   |       |   |   |   |-- qu2cuPen.cpython-313.pyc
|   |   |       |   |   |   |-- quartzPen.cpython-313.pyc
|   |   |       |   |   |   |-- recordingPen.cpython-313.pyc
|   |   |       |   |   |   |-- reportLabPen.cpython-313.pyc
|   |   |       |   |   |   |-- reverseContourPen.cpython-313.pyc
|   |   |       |   |   |   |-- roundingPen.cpython-313.pyc
|   |   |       |   |   |   |-- statisticsPen.cpython-313.pyc
|   |   |       |   |   |   |-- svgPathPen.cpython-313.pyc
|   |   |       |   |   |   |-- t2CharStringPen.cpython-313.pyc
|   |   |       |   |   |   |-- teePen.cpython-313.pyc
|   |   |       |   |   |   |-- transformPen.cpython-313.pyc
|   |   |       |   |   |   |-- ttGlyphPen.cpython-313.pyc
|   |   |       |   |   |   +-- wxPen.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- areaPen.py
|   |   |       |   |   |-- basePen.py
|   |   |       |   |   |-- boundsPen.py
|   |   |       |   |   |-- cairoPen.py
|   |   |       |   |   |-- cocoaPen.py
|   |   |       |   |   |-- cu2quPen.py
|   |   |       |   |   |-- explicitClosingLinePen.py
|   |   |       |   |   |-- filterPen.py
|   |   |       |   |   |-- freetypePen.py
|   |   |       |   |   |-- hashPointPen.py
|   |   |       |   |   |-- momentsPen.c
|   |   |       |   |   |-- momentsPen.cp313-win_amd64.pyd
|   |   |       |   |   |-- momentsPen.py
|   |   |       |   |   |-- perimeterPen.py
|   |   |       |   |   |-- pointInsidePen.py
|   |   |       |   |   |-- pointPen.py
|   |   |       |   |   |-- qtPen.py
|   |   |       |   |   |-- qu2cuPen.py
|   |   |       |   |   |-- quartzPen.py
|   |   |       |   |   |-- recordingPen.py
|   |   |       |   |   |-- reportLabPen.py
|   |   |       |   |   |-- reverseContourPen.py
|   |   |       |   |   |-- roundingPen.py
|   |   |       |   |   |-- statisticsPen.py
|   |   |       |   |   |-- svgPathPen.py
|   |   |       |   |   |-- t2CharStringPen.py
|   |   |       |   |   |-- teePen.py
|   |   |       |   |   |-- transformPen.py
|   |   |       |   |   |-- ttGlyphPen.py
|   |   |       |   |   +-- wxPen.py
|   |   |       |   |-- qu2cu
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- benchmark.cpython-313.pyc
|   |   |       |   |   |   |-- cli.cpython-313.pyc
|   |   |       |   |   |   +-- qu2cu.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- benchmark.py
|   |   |       |   |   |-- cli.py
|   |   |       |   |   |-- qu2cu.c
|   |   |       |   |   |-- qu2cu.cp313-win_amd64.pyd
|   |   |       |   |   +-- qu2cu.py
|   |   |       |   |-- subset
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- cff.cpython-313.pyc
|   |   |       |   |   |   |-- svg.cpython-313.pyc
|   |   |       |   |   |   +-- util.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- cff.py
|   |   |       |   |   |-- svg.py
|   |   |       |   |   +-- util.py
|   |   |       |   |-- svgLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |-- path
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- arc.cpython-313.pyc
|   |   |       |   |   |   |   |-- parser.cpython-313.pyc
|   |   |       |   |   |   |   +-- shapes.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- arc.py
|   |   |       |   |   |   |-- parser.py
|   |   |       |   |   |   +-- shapes.py
|   |   |       |   |   +-- __init__.py
|   |   |       |   |-- t1Lib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   +-- __init__.py
|   |   |       |   |-- ttLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- macUtils.cpython-313.pyc
|   |   |       |   |   |   |-- removeOverlaps.cpython-313.pyc
|   |   |       |   |   |   |-- reorderGlyphs.cpython-313.pyc
|   |   |       |   |   |   |-- scaleUpem.cpython-313.pyc
|   |   |       |   |   |   |-- sfnt.cpython-313.pyc
|   |   |       |   |   |   |-- standardGlyphOrder.cpython-313.pyc
|   |   |       |   |   |   |-- ttCollection.cpython-313.pyc
|   |   |       |   |   |   |-- ttFont.cpython-313.pyc
|   |   |       |   |   |   |-- ttGlyphSet.cpython-313.pyc
|   |   |       |   |   |   |-- ttVisitor.cpython-313.pyc
|   |   |       |   |   |   +-- woff2.cpython-313.pyc
|   |   |       |   |   |-- tables
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _a_n_k_r.cpython-313.pyc
|   |   |       |   |   |   |   |-- _a_v_a_r.cpython-313.pyc
|   |   |       |   |   |   |   |-- _b_s_l_n.cpython-313.pyc
|   |   |       |   |   |   |   |-- _c_i_d_g.cpython-313.pyc
|   |   |       |   |   |   |   |-- _c_m_a_p.cpython-313.pyc
|   |   |       |   |   |   |   |-- _c_v_a_r.cpython-313.pyc
|   |   |       |   |   |   |   |-- _c_v_t.cpython-313.pyc
|   |   |       |   |   |   |   |-- _f_e_a_t.cpython-313.pyc
|   |   |       |   |   |   |   |-- _f_p_g_m.cpython-313.pyc
|   |   |       |   |   |   |   |-- _f_v_a_r.cpython-313.pyc
|   |   |       |   |   |   |   |-- _g_a_s_p.cpython-313.pyc
|   |   |       |   |   |   |   |-- _g_c_i_d.cpython-313.pyc
|   |   |       |   |   |   |   |-- _g_l_y_f.cpython-313.pyc
|   |   |       |   |   |   |   |-- _g_v_a_r.cpython-313.pyc
|   |   |       |   |   |   |   |-- _h_d_m_x.cpython-313.pyc
|   |   |       |   |   |   |   |-- _h_e_a_d.cpython-313.pyc
|   |   |       |   |   |   |   |-- _h_h_e_a.cpython-313.pyc
|   |   |       |   |   |   |   |-- _h_m_t_x.cpython-313.pyc
|   |   |       |   |   |   |   |-- _k_e_r_n.cpython-313.pyc
|   |   |       |   |   |   |   |-- _l_c_a_r.cpython-313.pyc
|   |   |       |   |   |   |   |-- _l_o_c_a.cpython-313.pyc
|   |   |       |   |   |   |   |-- _l_t_a_g.cpython-313.pyc
|   |   |       |   |   |   |   |-- _m_a_x_p.cpython-313.pyc
|   |   |       |   |   |   |   |-- _m_e_t_a.cpython-313.pyc
|   |   |       |   |   |   |   |-- _m_o_r_t.cpython-313.pyc
|   |   |       |   |   |   |   |-- _m_o_r_x.cpython-313.pyc
|   |   |       |   |   |   |   |-- _n_a_m_e.cpython-313.pyc
|   |   |       |   |   |   |   |-- _o_p_b_d.cpython-313.pyc
|   |   |       |   |   |   |   |-- _p_o_s_t.cpython-313.pyc
|   |   |       |   |   |   |   |-- _p_r_e_p.cpython-313.pyc
|   |   |       |   |   |   |   |-- _p_r_o_p.cpython-313.pyc
|   |   |       |   |   |   |   |-- _s_b_i_x.cpython-313.pyc
|   |   |       |   |   |   |   |-- _t_r_a_k.cpython-313.pyc
|   |   |       |   |   |   |   |-- _v_h_e_a.cpython-313.pyc
|   |   |       |   |   |   |   |-- _v_m_t_x.cpython-313.pyc
|   |   |       |   |   |   |   |-- asciiTable.cpython-313.pyc
|   |   |       |   |   |   |   |-- B_A_S_E_.cpython-313.pyc
|   |   |       |   |   |   |   |-- BitmapGlyphMetrics.cpython-313.pyc
|   |   |       |   |   |   |   |-- C_B_D_T_.cpython-313.pyc
|   |   |       |   |   |   |   |-- C_B_L_C_.cpython-313.pyc
|   |   |       |   |   |   |   |-- C_F_F_.cpython-313.pyc
|   |   |       |   |   |   |   |-- C_F_F__2.cpython-313.pyc
|   |   |       |   |   |   |   |-- C_O_L_R_.cpython-313.pyc
|   |   |       |   |   |   |   |-- C_P_A_L_.cpython-313.pyc
|   |   |       |   |   |   |   |-- D__e_b_g.cpython-313.pyc
|   |   |       |   |   |   |   |-- D_S_I_G_.cpython-313.pyc
|   |   |       |   |   |   |   |-- DefaultTable.cpython-313.pyc
|   |   |       |   |   |   |   |-- E_B_D_T_.cpython-313.pyc
|   |   |       |   |   |   |   |-- E_B_L_C_.cpython-313.pyc
|   |   |       |   |   |   |   |-- F__e_a_t.cpython-313.pyc
|   |   |       |   |   |   |   |-- F_F_T_M_.cpython-313.pyc
|   |   |       |   |   |   |   |-- G__l_a_t.cpython-313.pyc
|   |   |       |   |   |   |   |-- G__l_o_c.cpython-313.pyc
|   |   |       |   |   |   |   |-- G_D_E_F_.cpython-313.pyc
|   |   |       |   |   |   |   |-- G_M_A_P_.cpython-313.pyc
|   |   |       |   |   |   |   |-- G_P_K_G_.cpython-313.pyc
|   |   |       |   |   |   |   |-- G_P_O_S_.cpython-313.pyc
|   |   |       |   |   |   |   |-- G_S_U_B_.cpython-313.pyc
|   |   |       |   |   |   |   |-- G_V_A_R_.cpython-313.pyc
|   |   |       |   |   |   |   |-- grUtils.cpython-313.pyc
|   |   |       |   |   |   |   |-- H_V_A_R_.cpython-313.pyc
|   |   |       |   |   |   |   |-- J_S_T_F_.cpython-313.pyc
|   |   |       |   |   |   |   |-- L_T_S_H_.cpython-313.pyc
|   |   |       |   |   |   |   |-- M_A_T_H_.cpython-313.pyc
|   |   |       |   |   |   |   |-- M_E_T_A_.cpython-313.pyc
|   |   |       |   |   |   |   |-- M_V_A_R_.cpython-313.pyc
|   |   |       |   |   |   |   |-- O_S_2f_2.cpython-313.pyc
|   |   |       |   |   |   |   |-- otBase.cpython-313.pyc
|   |   |       |   |   |   |   |-- otConverters.cpython-313.pyc
|   |   |       |   |   |   |   |-- otData.cpython-313.pyc
|   |   |       |   |   |   |   |-- otTables.cpython-313.pyc
|   |   |       |   |   |   |   |-- otTraverse.cpython-313.pyc
|   |   |       |   |   |   |   |-- S__i_l_f.cpython-313.pyc
|   |   |       |   |   |   |   |-- S__i_l_l.cpython-313.pyc
|   |   |       |   |   |   |   |-- S_I_N_G_.cpython-313.pyc
|   |   |       |   |   |   |   |-- S_T_A_T_.cpython-313.pyc
|   |   |       |   |   |   |   |-- S_V_G_.cpython-313.pyc
|   |   |       |   |   |   |   |-- sbixGlyph.cpython-313.pyc
|   |   |       |   |   |   |   |-- sbixStrike.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I__0.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I__1.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I__2.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I__3.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I__5.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I_B_.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I_C_.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I_D_.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I_J_.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I_P_.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I_S_.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_S_I_V_.cpython-313.pyc
|   |   |       |   |   |   |   |-- T_T_F_A_.cpython-313.pyc
|   |   |       |   |   |   |   |-- ttProgram.cpython-313.pyc
|   |   |       |   |   |   |   |-- TupleVariation.cpython-313.pyc
|   |   |       |   |   |   |   |-- V_A_R_C_.cpython-313.pyc
|   |   |       |   |   |   |   |-- V_D_M_X_.cpython-313.pyc
|   |   |       |   |   |   |   |-- V_O_R_G_.cpython-313.pyc
|   |   |       |   |   |   |   +-- V_V_A_R_.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _a_n_k_r.py
|   |   |       |   |   |   |-- _a_v_a_r.py
|   |   |       |   |   |   |-- _b_s_l_n.py
|   |   |       |   |   |   |-- _c_i_d_g.py
|   |   |       |   |   |   |-- _c_m_a_p.py
|   |   |       |   |   |   |-- _c_v_a_r.py
|   |   |       |   |   |   |-- _c_v_t.py
|   |   |       |   |   |   |-- _f_e_a_t.py
|   |   |       |   |   |   |-- _f_p_g_m.py
|   |   |       |   |   |   |-- _f_v_a_r.py
|   |   |       |   |   |   |-- _g_a_s_p.py
|   |   |       |   |   |   |-- _g_c_i_d.py
|   |   |       |   |   |   |-- _g_l_y_f.py
|   |   |       |   |   |   |-- _g_v_a_r.py
|   |   |       |   |   |   |-- _h_d_m_x.py
|   |   |       |   |   |   |-- _h_e_a_d.py
|   |   |       |   |   |   |-- _h_h_e_a.py
|   |   |       |   |   |   |-- _h_m_t_x.py
|   |   |       |   |   |   |-- _k_e_r_n.py
|   |   |       |   |   |   |-- _l_c_a_r.py
|   |   |       |   |   |   |-- _l_o_c_a.py
|   |   |       |   |   |   |-- _l_t_a_g.py
|   |   |       |   |   |   |-- _m_a_x_p.py
|   |   |       |   |   |   |-- _m_e_t_a.py
|   |   |       |   |   |   |-- _m_o_r_t.py
|   |   |       |   |   |   |-- _m_o_r_x.py
|   |   |       |   |   |   |-- _n_a_m_e.py
|   |   |       |   |   |   |-- _o_p_b_d.py
|   |   |       |   |   |   |-- _p_o_s_t.py
|   |   |       |   |   |   |-- _p_r_e_p.py
|   |   |       |   |   |   |-- _p_r_o_p.py
|   |   |       |   |   |   |-- _s_b_i_x.py
|   |   |       |   |   |   |-- _t_r_a_k.py
|   |   |       |   |   |   |-- _v_h_e_a.py
|   |   |       |   |   |   |-- _v_m_t_x.py
|   |   |       |   |   |   |-- asciiTable.py
|   |   |       |   |   |   |-- B_A_S_E_.py
|   |   |       |   |   |   |-- BitmapGlyphMetrics.py
|   |   |       |   |   |   |-- C_B_D_T_.py
|   |   |       |   |   |   |-- C_B_L_C_.py
|   |   |       |   |   |   |-- C_F_F_.py
|   |   |       |   |   |   |-- C_F_F__2.py
|   |   |       |   |   |   |-- C_O_L_R_.py
|   |   |       |   |   |   |-- C_P_A_L_.py
|   |   |       |   |   |   |-- D__e_b_g.py
|   |   |       |   |   |   |-- D_S_I_G_.py
|   |   |       |   |   |   |-- DefaultTable.py
|   |   |       |   |   |   |-- E_B_D_T_.py
|   |   |       |   |   |   |-- E_B_L_C_.py
|   |   |       |   |   |   |-- F__e_a_t.py
|   |   |       |   |   |   |-- F_F_T_M_.py
|   |   |       |   |   |   |-- G__l_a_t.py
|   |   |       |   |   |   |-- G__l_o_c.py
|   |   |       |   |   |   |-- G_D_E_F_.py
|   |   |       |   |   |   |-- G_M_A_P_.py
|   |   |       |   |   |   |-- G_P_K_G_.py
|   |   |       |   |   |   |-- G_P_O_S_.py
|   |   |       |   |   |   |-- G_S_U_B_.py
|   |   |       |   |   |   |-- G_V_A_R_.py
|   |   |       |   |   |   |-- grUtils.py
|   |   |       |   |   |   |-- H_V_A_R_.py
|   |   |       |   |   |   |-- J_S_T_F_.py
|   |   |       |   |   |   |-- L_T_S_H_.py
|   |   |       |   |   |   |-- M_A_T_H_.py
|   |   |       |   |   |   |-- M_E_T_A_.py
|   |   |       |   |   |   |-- M_V_A_R_.py
|   |   |       |   |   |   |-- O_S_2f_2.py
|   |   |       |   |   |   |-- otBase.py
|   |   |       |   |   |   |-- otConverters.py
|   |   |       |   |   |   |-- otData.py
|   |   |       |   |   |   |-- otTables.py
|   |   |       |   |   |   |-- otTraverse.py
|   |   |       |   |   |   |-- S__i_l_f.py
|   |   |       |   |   |   |-- S__i_l_l.py
|   |   |       |   |   |   |-- S_I_N_G_.py
|   |   |       |   |   |   |-- S_T_A_T_.py
|   |   |       |   |   |   |-- S_V_G_.py
|   |   |       |   |   |   |-- sbixGlyph.py
|   |   |       |   |   |   |-- sbixStrike.py
|   |   |       |   |   |   |-- T_S_I__0.py
|   |   |       |   |   |   |-- T_S_I__1.py
|   |   |       |   |   |   |-- T_S_I__2.py
|   |   |       |   |   |   |-- T_S_I__3.py
|   |   |       |   |   |   |-- T_S_I__5.py
|   |   |       |   |   |   |-- T_S_I_B_.py
|   |   |       |   |   |   |-- T_S_I_C_.py
|   |   |       |   |   |   |-- T_S_I_D_.py
|   |   |       |   |   |   |-- T_S_I_J_.py
|   |   |       |   |   |   |-- T_S_I_P_.py
|   |   |       |   |   |   |-- T_S_I_S_.py
|   |   |       |   |   |   |-- T_S_I_V_.py
|   |   |       |   |   |   |-- T_T_F_A_.py
|   |   |       |   |   |   |-- table_API_readme.txt
|   |   |       |   |   |   |-- ttProgram.py
|   |   |       |   |   |   |-- TupleVariation.py
|   |   |       |   |   |   |-- V_A_R_C_.py
|   |   |       |   |   |   |-- V_D_M_X_.py
|   |   |       |   |   |   |-- V_O_R_G_.py
|   |   |       |   |   |   +-- V_V_A_R_.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- macUtils.py
|   |   |       |   |   |-- removeOverlaps.py
|   |   |       |   |   |-- reorderGlyphs.py
|   |   |       |   |   |-- scaleUpem.py
|   |   |       |   |   |-- sfnt.py
|   |   |       |   |   |-- standardGlyphOrder.py
|   |   |       |   |   |-- ttCollection.py
|   |   |       |   |   |-- ttFont.py
|   |   |       |   |   |-- ttGlyphSet.py
|   |   |       |   |   |-- ttVisitor.py
|   |   |       |   |   +-- woff2.py
|   |   |       |   |-- ufoLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- converters.cpython-313.pyc
|   |   |       |   |   |   |-- errors.cpython-313.pyc
|   |   |       |   |   |   |-- etree.cpython-313.pyc
|   |   |       |   |   |   |-- filenames.cpython-313.pyc
|   |   |       |   |   |   |-- glifLib.cpython-313.pyc
|   |   |       |   |   |   |-- kerning.cpython-313.pyc
|   |   |       |   |   |   |-- plistlib.cpython-313.pyc
|   |   |       |   |   |   |-- pointPen.cpython-313.pyc
|   |   |       |   |   |   |-- utils.cpython-313.pyc
|   |   |       |   |   |   +-- validators.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- converters.py
|   |   |       |   |   |-- errors.py
|   |   |       |   |   |-- etree.py
|   |   |       |   |   |-- filenames.py
|   |   |       |   |   |-- glifLib.py
|   |   |       |   |   |-- kerning.py
|   |   |       |   |   |-- plistlib.py
|   |   |       |   |   |-- pointPen.py
|   |   |       |   |   |-- utils.py
|   |   |       |   |   +-- validators.py
|   |   |       |   |-- unicodedata
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- Blocks.cpython-313.pyc
|   |   |       |   |   |   |-- Mirrored.cpython-313.pyc
|   |   |       |   |   |   |-- OTTags.cpython-313.pyc
|   |   |       |   |   |   |-- ScriptExtensions.cpython-313.pyc
|   |   |       |   |   |   +-- Scripts.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- Blocks.py
|   |   |       |   |   |-- Mirrored.py
|   |   |       |   |   |-- OTTags.py
|   |   |       |   |   |-- ScriptExtensions.py
|   |   |       |   |   +-- Scripts.py
|   |   |       |   |-- varLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- avarPlanner.cpython-313.pyc
|   |   |       |   |   |   |-- builder.cpython-313.pyc
|   |   |       |   |   |   |-- cff.cpython-313.pyc
|   |   |       |   |   |   |-- errors.cpython-313.pyc
|   |   |       |   |   |   |-- featureVars.cpython-313.pyc
|   |   |       |   |   |   |-- hvar.cpython-313.pyc
|   |   |       |   |   |   |-- interpolatable.cpython-313.pyc
|   |   |       |   |   |   |-- interpolatableHelpers.cpython-313.pyc
|   |   |       |   |   |   |-- interpolatablePlot.cpython-313.pyc
|   |   |       |   |   |   |-- interpolatableTestContourOrder.cpython-313.pyc
|   |   |       |   |   |   |-- interpolatableTestStartingPoint.cpython-313.pyc
|   |   |       |   |   |   |-- interpolate_layout.cpython-313.pyc
|   |   |       |   |   |   |-- iup.cpython-313.pyc
|   |   |       |   |   |   |-- merger.cpython-313.pyc
|   |   |       |   |   |   |-- models.cpython-313.pyc
|   |   |       |   |   |   |-- multiVarStore.cpython-313.pyc
|   |   |       |   |   |   |-- mutator.cpython-313.pyc
|   |   |       |   |   |   |-- mvar.cpython-313.pyc
|   |   |       |   |   |   |-- plot.cpython-313.pyc
|   |   |       |   |   |   |-- stat.cpython-313.pyc
|   |   |       |   |   |   +-- varStore.cpython-313.pyc
|   |   |       |   |   |-- avar
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   |-- build.cpython-313.pyc
|   |   |       |   |   |   |   |-- map.cpython-313.pyc
|   |   |       |   |   |   |   |-- plan.cpython-313.pyc
|   |   |       |   |   |   |   +-- unbuild.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- build.py
|   |   |       |   |   |   |-- map.py
|   |   |       |   |   |   |-- plan.py
|   |   |       |   |   |   +-- unbuild.py
|   |   |       |   |   |-- instancer
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   |-- featureVars.cpython-313.pyc
|   |   |       |   |   |   |   |-- names.cpython-313.pyc
|   |   |       |   |   |   |   +-- solver.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- featureVars.py
|   |   |       |   |   |   |-- names.py
|   |   |       |   |   |   +-- solver.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- avarPlanner.py
|   |   |       |   |   |-- builder.py
|   |   |       |   |   |-- cff.py
|   |   |       |   |   |-- errors.py
|   |   |       |   |   |-- featureVars.py
|   |   |       |   |   |-- hvar.py
|   |   |       |   |   |-- interpolatable.py
|   |   |       |   |   |-- interpolatableHelpers.py
|   |   |       |   |   |-- interpolatablePlot.py
|   |   |       |   |   |-- interpolatableTestContourOrder.py
|   |   |       |   |   |-- interpolatableTestStartingPoint.py
|   |   |       |   |   |-- interpolate_layout.py
|   |   |       |   |   |-- iup.c
|   |   |       |   |   |-- iup.cp313-win_amd64.pyd
|   |   |       |   |   |-- iup.py
|   |   |       |   |   |-- merger.py
|   |   |       |   |   |-- models.py
|   |   |       |   |   |-- multiVarStore.py
|   |   |       |   |   |-- mutator.py
|   |   |       |   |   |-- mvar.py
|   |   |       |   |   |-- plot.py
|   |   |       |   |   |-- stat.py
|   |   |       |   |   +-- varStore.py
|   |   |       |   |-- voltLib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- ast.cpython-313.pyc
|   |   |       |   |   |   |-- error.cpython-313.pyc
|   |   |       |   |   |   |-- lexer.cpython-313.pyc
|   |   |       |   |   |   |-- parser.cpython-313.pyc
|   |   |       |   |   |   +-- voltToFea.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- ast.py
|   |   |       |   |   |-- error.py
|   |   |       |   |   |-- lexer.py
|   |   |       |   |   |-- parser.py
|   |   |       |   |   +-- voltToFea.py
|   |   |       |   |-- __init__.py
|   |   |       |   |-- __main__.py
|   |   |       |   |-- afmLib.py
|   |   |       |   |-- agl.py
|   |   |       |   |-- annotations.py
|   |   |       |   |-- fontBuilder.py
|   |   |       |   |-- help.py
|   |   |       |   |-- tfmLib.py
|   |   |       |   |-- ttx.py
|   |   |       |   +-- unicode.py
|   |   |       |-- fonttools-4.60.1.dist-info
|   |   |       |   |-- licenses
|   |   |       |   |   |-- LICENSE
|   |   |       |   |   +-- LICENSE.external
|   |   |       |   |-- entry_points.txt
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- top_level.txt
|   |   |       |   +-- WHEEL
|   |   |       |-- kiwisolver
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   +-- exceptions.cpython-313.pyc
|   |   |       |   |-- __init__.py
|   |   |       |   |-- _cext.cp313-win_amd64.pyd
|   |   |       |   |-- _cext.pyi
|   |   |       |   |-- exceptions.py
|   |   |       |   +-- py.typed
|   |   |       |-- kiwisolver-1.4.9.dist-info
|   |   |       |   |-- licenses
|   |   |       |   |   +-- LICENSE
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- top_level.txt
|   |   |       |   +-- WHEEL
|   |   |       |-- matplotlib
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- _afm.cpython-313.pyc
|   |   |       |   |   |-- _animation_data.cpython-313.pyc
|   |   |       |   |   |-- _blocking_input.cpython-313.pyc
|   |   |       |   |   |-- _cm.cpython-313.pyc
|   |   |       |   |   |-- _cm_bivar.cpython-313.pyc
|   |   |       |   |   |-- _cm_listed.cpython-313.pyc
|   |   |       |   |   |-- _cm_multivar.cpython-313.pyc
|   |   |       |   |   |-- _color_data.cpython-313.pyc
|   |   |       |   |   |-- _constrained_layout.cpython-313.pyc
|   |   |       |   |   |-- _docstring.cpython-313.pyc
|   |   |       |   |   |-- _enums.cpython-313.pyc
|   |   |       |   |   |-- _fontconfig_pattern.cpython-313.pyc
|   |   |       |   |   |-- _internal_utils.cpython-313.pyc
|   |   |       |   |   |-- _layoutgrid.cpython-313.pyc
|   |   |       |   |   |-- _mathtext.cpython-313.pyc
|   |   |       |   |   |-- _mathtext_data.cpython-313.pyc
|   |   |       |   |   |-- _pylab_helpers.cpython-313.pyc
|   |   |       |   |   |-- _text_helpers.cpython-313.pyc
|   |   |       |   |   |-- _tight_bbox.cpython-313.pyc
|   |   |       |   |   |-- _tight_layout.cpython-313.pyc
|   |   |       |   |   |-- _type1font.cpython-313.pyc
|   |   |       |   |   |-- _version.cpython-313.pyc
|   |   |       |   |   |-- animation.cpython-313.pyc
|   |   |       |   |   |-- artist.cpython-313.pyc
|   |   |       |   |   |-- axis.cpython-313.pyc
|   |   |       |   |   |-- backend_bases.cpython-313.pyc
|   |   |       |   |   |-- backend_managers.cpython-313.pyc
|   |   |       |   |   |-- backend_tools.cpython-313.pyc
|   |   |       |   |   |-- bezier.cpython-313.pyc
|   |   |       |   |   |-- category.cpython-313.pyc
|   |   |       |   |   |-- cbook.cpython-313.pyc
|   |   |       |   |   |-- cm.cpython-313.pyc
|   |   |       |   |   |-- collections.cpython-313.pyc
|   |   |       |   |   |-- colorbar.cpython-313.pyc
|   |   |       |   |   |-- colorizer.cpython-313.pyc
|   |   |       |   |   |-- colors.cpython-313.pyc
|   |   |       |   |   |-- container.cpython-313.pyc
|   |   |       |   |   |-- contour.cpython-313.pyc
|   |   |       |   |   |-- dates.cpython-313.pyc
|   |   |       |   |   |-- dviread.cpython-313.pyc
|   |   |       |   |   |-- figure.cpython-313.pyc
|   |   |       |   |   |-- font_manager.cpython-313.pyc
|   |   |       |   |   |-- gridspec.cpython-313.pyc
|   |   |       |   |   |-- hatch.cpython-313.pyc
|   |   |       |   |   |-- image.cpython-313.pyc
|   |   |       |   |   |-- inset.cpython-313.pyc
|   |   |       |   |   |-- layout_engine.cpython-313.pyc
|   |   |       |   |   |-- legend.cpython-313.pyc
|   |   |       |   |   |-- legend_handler.cpython-313.pyc
|   |   |       |   |   |-- lines.cpython-313.pyc
|   |   |       |   |   |-- markers.cpython-313.pyc
|   |   |       |   |   |-- mathtext.cpython-313.pyc
|   |   |       |   |   |-- mlab.cpython-313.pyc
|   |   |       |   |   |-- offsetbox.cpython-313.pyc
|   |   |       |   |   |-- patches.cpython-313.pyc
|   |   |       |   |   |-- path.cpython-313.pyc
|   |   |       |   |   |-- patheffects.cpython-313.pyc
|   |   |       |   |   |-- pylab.cpython-313.pyc
|   |   |       |   |   |-- pyplot.cpython-313.pyc
|   |   |       |   |   |-- quiver.cpython-313.pyc
|   |   |       |   |   |-- rcsetup.cpython-313.pyc
|   |   |       |   |   |-- sankey.cpython-313.pyc
|   |   |       |   |   |-- scale.cpython-313.pyc
|   |   |       |   |   |-- spines.cpython-313.pyc
|   |   |       |   |   |-- stackplot.cpython-313.pyc
|   |   |       |   |   |-- streamplot.cpython-313.pyc
|   |   |       |   |   |-- table.cpython-313.pyc
|   |   |       |   |   |-- texmanager.cpython-313.pyc
|   |   |       |   |   |-- text.cpython-313.pyc
|   |   |       |   |   |-- textpath.cpython-313.pyc
|   |   |       |   |   |-- ticker.cpython-313.pyc
|   |   |       |   |   |-- transforms.cpython-313.pyc
|   |   |       |   |   |-- typing.cpython-313.pyc
|   |   |       |   |   |-- units.cpython-313.pyc
|   |   |       |   |   +-- widgets.cpython-313.pyc
|   |   |       |   |-- _api
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- deprecation.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- deprecation.py
|   |   |       |   |   +-- deprecation.pyi
|   |   |       |   |-- axes
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _axes.cpython-313.pyc
|   |   |       |   |   |   |-- _base.cpython-313.pyc
|   |   |       |   |   |   +-- _secondary_axes.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _axes.py
|   |   |       |   |   |-- _axes.pyi
|   |   |       |   |   |-- _base.py
|   |   |       |   |   |-- _base.pyi
|   |   |       |   |   |-- _secondary_axes.py
|   |   |       |   |   +-- _secondary_axes.pyi
|   |   |       |   |-- backends
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _backend_gtk.cpython-313.pyc
|   |   |       |   |   |   |-- _backend_pdf_ps.cpython-313.pyc
|   |   |       |   |   |   |-- _backend_tk.cpython-313.pyc
|   |   |       |   |   |   |-- backend_agg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_cairo.cpython-313.pyc
|   |   |       |   |   |   |-- backend_gtk3.cpython-313.pyc
|   |   |       |   |   |   |-- backend_gtk3agg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_gtk3cairo.cpython-313.pyc
|   |   |       |   |   |   |-- backend_gtk4.cpython-313.pyc
|   |   |       |   |   |   |-- backend_gtk4agg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_gtk4cairo.cpython-313.pyc
|   |   |       |   |   |   |-- backend_macosx.cpython-313.pyc
|   |   |       |   |   |   |-- backend_mixed.cpython-313.pyc
|   |   |       |   |   |   |-- backend_nbagg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_pdf.cpython-313.pyc
|   |   |       |   |   |   |-- backend_pgf.cpython-313.pyc
|   |   |       |   |   |   |-- backend_ps.cpython-313.pyc
|   |   |       |   |   |   |-- backend_qt.cpython-313.pyc
|   |   |       |   |   |   |-- backend_qt5.cpython-313.pyc
|   |   |       |   |   |   |-- backend_qt5agg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_qt5cairo.cpython-313.pyc
|   |   |       |   |   |   |-- backend_qtagg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_qtcairo.cpython-313.pyc
|   |   |       |   |   |   |-- backend_svg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_template.cpython-313.pyc
|   |   |       |   |   |   |-- backend_tkagg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_tkcairo.cpython-313.pyc
|   |   |       |   |   |   |-- backend_webagg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_webagg_core.cpython-313.pyc
|   |   |       |   |   |   |-- backend_wx.cpython-313.pyc
|   |   |       |   |   |   |-- backend_wxagg.cpython-313.pyc
|   |   |       |   |   |   |-- backend_wxcairo.cpython-313.pyc
|   |   |       |   |   |   |-- qt_compat.cpython-313.pyc
|   |   |       |   |   |   +-- registry.cpython-313.pyc
|   |   |       |   |   |-- qt_editor
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _formlayout.cpython-313.pyc
|   |   |       |   |   |   |   +-- figureoptions.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _formlayout.py
|   |   |       |   |   |   +-- figureoptions.py
|   |   |       |   |   |-- web_backend
|   |   |       |   |   |   |-- css
|   |   |       |   |   |   |   |-- boilerplate.css
|   |   |       |   |   |   |   |-- fbm.css
|   |   |       |   |   |   |   |-- mpl.css
|   |   |       |   |   |   |   +-- page.css
|   |   |       |   |   |   |-- js
|   |   |       |   |   |   |   |-- mpl.js
|   |   |       |   |   |   |   |-- mpl_tornado.js
|   |   |       |   |   |   |   +-- nbagg_mpl.js
|   |   |       |   |   |   |-- all_figures.html
|   |   |       |   |   |   |-- ipython_inline_figure.html
|   |   |       |   |   |   +-- single_figure.html
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _backend_agg.cp313-win_amd64.pyd
|   |   |       |   |   |-- _backend_agg.pyi
|   |   |       |   |   |-- _backend_gtk.py
|   |   |       |   |   |-- _backend_pdf_ps.py
|   |   |       |   |   |-- _backend_tk.py
|   |   |       |   |   |-- _macosx.pyi
|   |   |       |   |   |-- _tkagg.cp313-win_amd64.pyd
|   |   |       |   |   |-- _tkagg.pyi
|   |   |       |   |   |-- backend_agg.py
|   |   |       |   |   |-- backend_cairo.py
|   |   |       |   |   |-- backend_gtk3.py
|   |   |       |   |   |-- backend_gtk3agg.py
|   |   |       |   |   |-- backend_gtk3cairo.py
|   |   |       |   |   |-- backend_gtk4.py
|   |   |       |   |   |-- backend_gtk4agg.py
|   |   |       |   |   |-- backend_gtk4cairo.py
|   |   |       |   |   |-- backend_macosx.py
|   |   |       |   |   |-- backend_mixed.py
|   |   |       |   |   |-- backend_nbagg.py
|   |   |       |   |   |-- backend_pdf.py
|   |   |       |   |   |-- backend_pgf.py
|   |   |       |   |   |-- backend_ps.py
|   |   |       |   |   |-- backend_qt.py
|   |   |       |   |   |-- backend_qt5.py
|   |   |       |   |   |-- backend_qt5agg.py
|   |   |       |   |   |-- backend_qt5cairo.py
|   |   |       |   |   |-- backend_qtagg.py
|   |   |       |   |   |-- backend_qtcairo.py
|   |   |       |   |   |-- backend_svg.py
|   |   |       |   |   |-- backend_template.py
|   |   |       |   |   |-- backend_tkagg.py
|   |   |       |   |   |-- backend_tkcairo.py
|   |   |       |   |   |-- backend_webagg.py
|   |   |       |   |   |-- backend_webagg_core.py
|   |   |       |   |   |-- backend_wx.py
|   |   |       |   |   |-- backend_wxagg.py
|   |   |       |   |   |-- backend_wxcairo.py
|   |   |       |   |   |-- qt_compat.py
|   |   |       |   |   +-- registry.py
|   |   |       |   |-- mpl-data
|   |   |       |   |   |-- fonts
|   |   |       |   |   |   |-- afm
|   |   |       |   |   |   |   |-- cmex10.afm
|   |   |       |   |   |   |   |-- cmmi10.afm
|   |   |       |   |   |   |   |-- cmr10.afm
|   |   |       |   |   |   |   |-- cmsy10.afm
|   |   |       |   |   |   |   |-- cmtt10.afm
|   |   |       |   |   |   |   |-- pagd8a.afm
|   |   |       |   |   |   |   |-- pagdo8a.afm
|   |   |       |   |   |   |   |-- pagk8a.afm
|   |   |       |   |   |   |   |-- pagko8a.afm
|   |   |       |   |   |   |   |-- pbkd8a.afm
|   |   |       |   |   |   |   |-- pbkdi8a.afm
|   |   |       |   |   |   |   |-- pbkl8a.afm
|   |   |       |   |   |   |   |-- pbkli8a.afm
|   |   |       |   |   |   |   |-- pcrb8a.afm
|   |   |       |   |   |   |   |-- pcrbo8a.afm
|   |   |       |   |   |   |   |-- pcrr8a.afm
|   |   |       |   |   |   |   |-- pcrro8a.afm
|   |   |       |   |   |   |   |-- phvb8a.afm
|   |   |       |   |   |   |   |-- phvb8an.afm
|   |   |       |   |   |   |   |-- phvbo8a.afm
|   |   |       |   |   |   |   |-- phvbo8an.afm
|   |   |       |   |   |   |   |-- phvl8a.afm
|   |   |       |   |   |   |   |-- phvlo8a.afm
|   |   |       |   |   |   |   |-- phvr8a.afm
|   |   |       |   |   |   |   |-- phvr8an.afm
|   |   |       |   |   |   |   |-- phvro8a.afm
|   |   |       |   |   |   |   |-- phvro8an.afm
|   |   |       |   |   |   |   |-- pncb8a.afm
|   |   |       |   |   |   |   |-- pncbi8a.afm
|   |   |       |   |   |   |   |-- pncr8a.afm
|   |   |       |   |   |   |   |-- pncri8a.afm
|   |   |       |   |   |   |   |-- pplb8a.afm
|   |   |       |   |   |   |   |-- pplbi8a.afm
|   |   |       |   |   |   |   |-- pplr8a.afm
|   |   |       |   |   |   |   |-- pplri8a.afm
|   |   |       |   |   |   |   |-- psyr.afm
|   |   |       |   |   |   |   |-- ptmb8a.afm
|   |   |       |   |   |   |   |-- ptmbi8a.afm
|   |   |       |   |   |   |   |-- ptmr8a.afm
|   |   |       |   |   |   |   |-- ptmri8a.afm
|   |   |       |   |   |   |   |-- putb8a.afm
|   |   |       |   |   |   |   |-- putbi8a.afm
|   |   |       |   |   |   |   |-- putr8a.afm
|   |   |       |   |   |   |   |-- putri8a.afm
|   |   |       |   |   |   |   |-- pzcmi8a.afm
|   |   |       |   |   |   |   +-- pzdr.afm
|   |   |       |   |   |   |-- pdfcorefonts
|   |   |       |   |   |   |   |-- Courier.afm
|   |   |       |   |   |   |   |-- Courier-Bold.afm
|   |   |       |   |   |   |   |-- Courier-BoldOblique.afm
|   |   |       |   |   |   |   |-- Courier-Oblique.afm
|   |   |       |   |   |   |   |-- Helvetica.afm
|   |   |       |   |   |   |   |-- Helvetica-Bold.afm
|   |   |       |   |   |   |   |-- Helvetica-BoldOblique.afm
|   |   |       |   |   |   |   |-- Helvetica-Oblique.afm
|   |   |       |   |   |   |   |-- readme.txt
|   |   |       |   |   |   |   |-- Symbol.afm
|   |   |       |   |   |   |   |-- Times-Bold.afm
|   |   |       |   |   |   |   |-- Times-BoldItalic.afm
|   |   |       |   |   |   |   |-- Times-Italic.afm
|   |   |       |   |   |   |   |-- Times-Roman.afm
|   |   |       |   |   |   |   +-- ZapfDingbats.afm
|   |   |       |   |   |   +-- ttf
|   |   |       |   |   |       |-- cmb10.ttf
|   |   |       |   |   |       |-- cmex10.ttf
|   |   |       |   |   |       |-- cmmi10.ttf
|   |   |       |   |   |       |-- cmr10.ttf
|   |   |       |   |   |       |-- cmss10.ttf
|   |   |       |   |   |       |-- cmsy10.ttf
|   |   |       |   |   |       |-- cmtt10.ttf
|   |   |       |   |   |       |-- DejaVuSans.ttf
|   |   |       |   |   |       |-- DejaVuSans-Bold.ttf
|   |   |       |   |   |       |-- DejaVuSans-BoldOblique.ttf
|   |   |       |   |   |       |-- DejaVuSansDisplay.ttf
|   |   |       |   |   |       |-- DejaVuSansMono.ttf
|   |   |       |   |   |       |-- DejaVuSansMono-Bold.ttf
|   |   |       |   |   |       |-- DejaVuSansMono-BoldOblique.ttf
|   |   |       |   |   |       |-- DejaVuSansMono-Oblique.ttf
|   |   |       |   |   |       |-- DejaVuSans-Oblique.ttf
|   |   |       |   |   |       |-- DejaVuSerif.ttf
|   |   |       |   |   |       |-- DejaVuSerif-Bold.ttf
|   |   |       |   |   |       |-- DejaVuSerif-BoldItalic.ttf
|   |   |       |   |   |       |-- DejaVuSerifDisplay.ttf
|   |   |       |   |   |       |-- DejaVuSerif-Italic.ttf
|   |   |       |   |   |       |-- LICENSE_DEJAVU
|   |   |       |   |   |       |-- LICENSE_STIX
|   |   |       |   |   |       |-- STIXGeneral.ttf
|   |   |       |   |   |       |-- STIXGeneralBol.ttf
|   |   |       |   |   |       |-- STIXGeneralBolIta.ttf
|   |   |       |   |   |       |-- STIXGeneralItalic.ttf
|   |   |       |   |   |       |-- STIXNonUni.ttf
|   |   |       |   |   |       |-- STIXNonUniBol.ttf
|   |   |       |   |   |       |-- STIXNonUniBolIta.ttf
|   |   |       |   |   |       |-- STIXNonUniIta.ttf
|   |   |       |   |   |       |-- STIXSizFiveSymReg.ttf
|   |   |       |   |   |       |-- STIXSizFourSymBol.ttf
|   |   |       |   |   |       |-- STIXSizFourSymReg.ttf
|   |   |       |   |   |       |-- STIXSizOneSymBol.ttf
|   |   |       |   |   |       |-- STIXSizOneSymReg.ttf
|   |   |       |   |   |       |-- STIXSizThreeSymBol.ttf
|   |   |       |   |   |       |-- STIXSizThreeSymReg.ttf
|   |   |       |   |   |       |-- STIXSizTwoSymBol.ttf
|   |   |       |   |   |       +-- STIXSizTwoSymReg.ttf
|   |   |       |   |   |-- images
|   |   |       |   |   |   |-- back.pdf
|   |   |       |   |   |   |-- back.png
|   |   |       |   |   |   |-- back.svg
|   |   |       |   |   |   |-- back_large.png
|   |   |       |   |   |   |-- back-symbolic.svg
|   |   |       |   |   |   |-- filesave.pdf
|   |   |       |   |   |   |-- filesave.png
|   |   |       |   |   |   |-- filesave.svg
|   |   |       |   |   |   |-- filesave_large.png
|   |   |       |   |   |   |-- filesave-symbolic.svg
|   |   |       |   |   |   |-- forward.pdf
|   |   |       |   |   |   |-- forward.png
|   |   |       |   |   |   |-- forward.svg
|   |   |       |   |   |   |-- forward_large.png
|   |   |       |   |   |   |-- forward-symbolic.svg
|   |   |       |   |   |   |-- hand.pdf
|   |   |       |   |   |   |-- hand.png
|   |   |       |   |   |   |-- hand.svg
|   |   |       |   |   |   |-- help.pdf
|   |   |       |   |   |   |-- help.png
|   |   |       |   |   |   |-- help.svg
|   |   |       |   |   |   |-- help_large.png
|   |   |       |   |   |   |-- help-symbolic.svg
|   |   |       |   |   |   |-- home.pdf
|   |   |       |   |   |   |-- home.png
|   |   |       |   |   |   |-- home.svg
|   |   |       |   |   |   |-- home_large.png
|   |   |       |   |   |   |-- home-symbolic.svg
|   |   |       |   |   |   |-- matplotlib.pdf
|   |   |       |   |   |   |-- matplotlib.png
|   |   |       |   |   |   |-- matplotlib.svg
|   |   |       |   |   |   |-- matplotlib_large.png
|   |   |       |   |   |   |-- move.pdf
|   |   |       |   |   |   |-- move.png
|   |   |       |   |   |   |-- move.svg
|   |   |       |   |   |   |-- move_large.png
|   |   |       |   |   |   |-- move-symbolic.svg
|   |   |       |   |   |   |-- qt4_editor_options.pdf
|   |   |       |   |   |   |-- qt4_editor_options.png
|   |   |       |   |   |   |-- qt4_editor_options.svg
|   |   |       |   |   |   |-- qt4_editor_options_large.png
|   |   |       |   |   |   |-- subplots.pdf
|   |   |       |   |   |   |-- subplots.png
|   |   |       |   |   |   |-- subplots.svg
|   |   |       |   |   |   |-- subplots_large.png
|   |   |       |   |   |   |-- subplots-symbolic.svg
|   |   |       |   |   |   |-- zoom_to_rect.pdf
|   |   |       |   |   |   |-- zoom_to_rect.png
|   |   |       |   |   |   |-- zoom_to_rect.svg
|   |   |       |   |   |   |-- zoom_to_rect_large.png
|   |   |       |   |   |   +-- zoom_to_rect-symbolic.svg
|   |   |       |   |   |-- plot_directive
|   |   |       |   |   |   +-- plot_directive.css
|   |   |       |   |   |-- sample_data
|   |   |       |   |   |   |-- axes_grid
|   |   |       |   |   |   |   +-- bivariate_normal.npy
|   |   |       |   |   |   |-- data_x_x2_x3.csv
|   |   |       |   |   |   |-- eeg.dat
|   |   |       |   |   |   |-- embedding_in_wx3.xrc
|   |   |       |   |   |   |-- goog.npz
|   |   |       |   |   |   |-- grace_hopper.jpg
|   |   |       |   |   |   |-- jacksboro_fault_dem.npz
|   |   |       |   |   |   |-- logo2.png
|   |   |       |   |   |   |-- membrane.dat
|   |   |       |   |   |   |-- Minduka_Present_Blue_Pack.png
|   |   |       |   |   |   |-- msft.csv
|   |   |       |   |   |   |-- README.txt
|   |   |       |   |   |   |-- s1045.ima.gz
|   |   |       |   |   |   |-- Stocks.csv
|   |   |       |   |   |   +-- topobathy.npz
|   |   |       |   |   |-- stylelib
|   |   |       |   |   |   |-- _classic_test_patch.mplstyle
|   |   |       |   |   |   |-- _mpl-gallery.mplstyle
|   |   |       |   |   |   |-- _mpl-gallery-nogrid.mplstyle
|   |   |       |   |   |   |-- bmh.mplstyle
|   |   |       |   |   |   |-- classic.mplstyle
|   |   |       |   |   |   |-- dark_background.mplstyle
|   |   |       |   |   |   |-- fast.mplstyle
|   |   |       |   |   |   |-- fivethirtyeight.mplstyle
|   |   |       |   |   |   |-- ggplot.mplstyle
|   |   |       |   |   |   |-- grayscale.mplstyle
|   |   |       |   |   |   |-- petroff10.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-bright.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-colorblind.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-dark.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-darkgrid.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-dark-palette.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-deep.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-muted.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-notebook.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-paper.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-pastel.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-poster.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-talk.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-ticks.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-white.mplstyle
|   |   |       |   |   |   |-- seaborn-v0_8-whitegrid.mplstyle
|   |   |       |   |   |   |-- Solarize_Light2.mplstyle
|   |   |       |   |   |   +-- tableau-colorblind10.mplstyle
|   |   |       |   |   |-- kpsewhich.lua
|   |   |       |   |   +-- matplotlibrc
|   |   |       |   |-- projections
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- geo.cpython-313.pyc
|   |   |       |   |   |   +-- polar.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- geo.py
|   |   |       |   |   |-- geo.pyi
|   |   |       |   |   |-- polar.py
|   |   |       |   |   +-- polar.pyi
|   |   |       |   |-- sphinxext
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- figmpl_directive.cpython-313.pyc
|   |   |       |   |   |   |-- mathmpl.cpython-313.pyc
|   |   |       |   |   |   |-- plot_directive.cpython-313.pyc
|   |   |       |   |   |   +-- roles.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- figmpl_directive.py
|   |   |       |   |   |-- mathmpl.py
|   |   |       |   |   |-- plot_directive.py
|   |   |       |   |   +-- roles.py
|   |   |       |   |-- style
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- core.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- core.py
|   |   |       |   |   +-- core.pyi
|   |   |       |   |-- testing
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _markers.cpython-313.pyc
|   |   |       |   |   |   |-- compare.cpython-313.pyc
|   |   |       |   |   |   |-- conftest.cpython-313.pyc
|   |   |       |   |   |   |-- decorators.cpython-313.pyc
|   |   |       |   |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |   +-- widgets.cpython-313.pyc
|   |   |       |   |   |-- jpl_units
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- Duration.cpython-313.pyc
|   |   |       |   |   |   |   |-- Epoch.cpython-313.pyc
|   |   |       |   |   |   |   |-- EpochConverter.cpython-313.pyc
|   |   |       |   |   |   |   |-- StrConverter.cpython-313.pyc
|   |   |       |   |   |   |   |-- UnitDbl.cpython-313.pyc
|   |   |       |   |   |   |   |-- UnitDblConverter.cpython-313.pyc
|   |   |       |   |   |   |   +-- UnitDblFormatter.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- Duration.py
|   |   |       |   |   |   |-- Epoch.py
|   |   |       |   |   |   |-- EpochConverter.py
|   |   |       |   |   |   |-- StrConverter.py
|   |   |       |   |   |   |-- UnitDbl.py
|   |   |       |   |   |   |-- UnitDblConverter.py
|   |   |       |   |   |   +-- UnitDblFormatter.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _markers.py
|   |   |       |   |   |-- compare.py
|   |   |       |   |   |-- compare.pyi
|   |   |       |   |   |-- conftest.py
|   |   |       |   |   |-- conftest.pyi
|   |   |       |   |   |-- decorators.py
|   |   |       |   |   |-- decorators.pyi
|   |   |       |   |   |-- exceptions.py
|   |   |       |   |   |-- widgets.py
|   |   |       |   |   +-- widgets.pyi
|   |   |       |   |-- tests
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- conftest.cpython-313.pyc
|   |   |       |   |   |   |-- test_afm.cpython-313.pyc
|   |   |       |   |   |   |-- test_agg.cpython-313.pyc
|   |   |       |   |   |   |-- test_agg_filter.cpython-313.pyc
|   |   |       |   |   |   |-- test_animation.cpython-313.pyc
|   |   |       |   |   |   |-- test_api.cpython-313.pyc
|   |   |       |   |   |   |-- test_arrow_patches.cpython-313.pyc
|   |   |       |   |   |   |-- test_artist.cpython-313.pyc
|   |   |       |   |   |   |-- test_axes.cpython-313.pyc
|   |   |       |   |   |   |-- test_axis.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_bases.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_cairo.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_gtk3.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_inline.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_macosx.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_nbagg.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_pdf.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_pgf.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_ps.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_qt.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_registry.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_svg.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_template.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_tk.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_tools.cpython-313.pyc
|   |   |       |   |   |   |-- test_backend_webagg.cpython-313.pyc
|   |   |       |   |   |   |-- test_backends_interactive.cpython-313.pyc
|   |   |       |   |   |   |-- test_basic.cpython-313.pyc
|   |   |       |   |   |   |-- test_bbox_tight.cpython-313.pyc
|   |   |       |   |   |   |-- test_bezier.cpython-313.pyc
|   |   |       |   |   |   |-- test_category.cpython-313.pyc
|   |   |       |   |   |   |-- test_cbook.cpython-313.pyc
|   |   |       |   |   |   |-- test_collections.cpython-313.pyc
|   |   |       |   |   |   |-- test_colorbar.cpython-313.pyc
|   |   |       |   |   |   |-- test_colors.cpython-313.pyc
|   |   |       |   |   |   |-- test_compare_images.cpython-313.pyc
|   |   |       |   |   |   |-- test_constrainedlayout.cpython-313.pyc
|   |   |       |   |   |   |-- test_container.cpython-313.pyc
|   |   |       |   |   |   |-- test_contour.cpython-313.pyc
|   |   |       |   |   |   |-- test_cycles.cpython-313.pyc
|   |   |       |   |   |   |-- test_dates.cpython-313.pyc
|   |   |       |   |   |   |-- test_datetime.cpython-313.pyc
|   |   |       |   |   |   |-- test_determinism.cpython-313.pyc
|   |   |       |   |   |   |-- test_doc.cpython-313.pyc
|   |   |       |   |   |   |-- test_dviread.cpython-313.pyc
|   |   |       |   |   |   |-- test_figure.cpython-313.pyc
|   |   |       |   |   |   |-- test_font_manager.cpython-313.pyc
|   |   |       |   |   |   |-- test_fontconfig_pattern.cpython-313.pyc
|   |   |       |   |   |   |-- test_ft2font.cpython-313.pyc
|   |   |       |   |   |   |-- test_getattr.cpython-313.pyc
|   |   |       |   |   |   |-- test_gridspec.cpython-313.pyc
|   |   |       |   |   |   |-- test_image.cpython-313.pyc
|   |   |       |   |   |   |-- test_legend.cpython-313.pyc
|   |   |       |   |   |   |-- test_lines.cpython-313.pyc
|   |   |       |   |   |   |-- test_marker.cpython-313.pyc
|   |   |       |   |   |   |-- test_mathtext.cpython-313.pyc
|   |   |       |   |   |   |-- test_matplotlib.cpython-313.pyc
|   |   |       |   |   |   |-- test_mlab.cpython-313.pyc
|   |   |       |   |   |   |-- test_multivariate_colormaps.cpython-313.pyc
|   |   |       |   |   |   |-- test_offsetbox.cpython-313.pyc
|   |   |       |   |   |   |-- test_patches.cpython-313.pyc
|   |   |       |   |   |   |-- test_path.cpython-313.pyc
|   |   |       |   |   |   |-- test_patheffects.cpython-313.pyc
|   |   |       |   |   |   |-- test_pickle.cpython-313.pyc
|   |   |       |   |   |   |-- test_png.cpython-313.pyc
|   |   |       |   |   |   |-- test_polar.cpython-313.pyc
|   |   |       |   |   |   |-- test_preprocess_data.cpython-313.pyc
|   |   |       |   |   |   |-- test_pyplot.cpython-313.pyc
|   |   |       |   |   |   |-- test_quiver.cpython-313.pyc
|   |   |       |   |   |   |-- test_rcparams.cpython-313.pyc
|   |   |       |   |   |   |-- test_sankey.cpython-313.pyc
|   |   |       |   |   |   |-- test_scale.cpython-313.pyc
|   |   |       |   |   |   |-- test_simplification.cpython-313.pyc
|   |   |       |   |   |   |-- test_skew.cpython-313.pyc
|   |   |       |   |   |   |-- test_sphinxext.cpython-313.pyc
|   |   |       |   |   |   |-- test_spines.cpython-313.pyc
|   |   |       |   |   |   |-- test_streamplot.cpython-313.pyc
|   |   |       |   |   |   |-- test_style.cpython-313.pyc
|   |   |       |   |   |   |-- test_subplots.cpython-313.pyc
|   |   |       |   |   |   |-- test_table.cpython-313.pyc
|   |   |       |   |   |   |-- test_testing.cpython-313.pyc
|   |   |       |   |   |   |-- test_texmanager.cpython-313.pyc
|   |   |       |   |   |   |-- test_text.cpython-313.pyc
|   |   |       |   |   |   |-- test_textpath.cpython-313.pyc
|   |   |       |   |   |   |-- test_ticker.cpython-313.pyc
|   |   |       |   |   |   |-- test_tightlayout.cpython-313.pyc
|   |   |       |   |   |   |-- test_transforms.cpython-313.pyc
|   |   |       |   |   |   |-- test_triangulation.cpython-313.pyc
|   |   |       |   |   |   |-- test_type1font.cpython-313.pyc
|   |   |       |   |   |   |-- test_units.cpython-313.pyc
|   |   |       |   |   |   |-- test_usetex.cpython-313.pyc
|   |   |       |   |   |   +-- test_widgets.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- conftest.py
|   |   |       |   |   |-- test_afm.py
|   |   |       |   |   |-- test_agg.py
|   |   |       |   |   |-- test_agg_filter.py
|   |   |       |   |   |-- test_animation.py
|   |   |       |   |   |-- test_api.py
|   |   |       |   |   |-- test_arrow_patches.py
|   |   |       |   |   |-- test_artist.py
|   |   |       |   |   |-- test_axes.py
|   |   |       |   |   |-- test_axis.py
|   |   |       |   |   |-- test_backend_bases.py
|   |   |       |   |   |-- test_backend_cairo.py
|   |   |       |   |   |-- test_backend_gtk3.py
|   |   |       |   |   |-- test_backend_inline.py
|   |   |       |   |   |-- test_backend_macosx.py
|   |   |       |   |   |-- test_backend_nbagg.py
|   |   |       |   |   |-- test_backend_pdf.py
|   |   |       |   |   |-- test_backend_pgf.py
|   |   |       |   |   |-- test_backend_ps.py
|   |   |       |   |   |-- test_backend_qt.py
|   |   |       |   |   |-- test_backend_registry.py
|   |   |       |   |   |-- test_backend_svg.py
|   |   |       |   |   |-- test_backend_template.py
|   |   |       |   |   |-- test_backend_tk.py
|   |   |       |   |   |-- test_backend_tools.py
|   |   |       |   |   |-- test_backend_webagg.py
|   |   |       |   |   |-- test_backends_interactive.py
|   |   |       |   |   |-- test_basic.py
|   |   |       |   |   |-- test_bbox_tight.py
|   |   |       |   |   |-- test_bezier.py
|   |   |       |   |   |-- test_category.py
|   |   |       |   |   |-- test_cbook.py
|   |   |       |   |   |-- test_collections.py
|   |   |       |   |   |-- test_colorbar.py
|   |   |       |   |   |-- test_colors.py
|   |   |       |   |   |-- test_compare_images.py
|   |   |       |   |   |-- test_constrainedlayout.py
|   |   |       |   |   |-- test_container.py
|   |   |       |   |   |-- test_contour.py
|   |   |       |   |   |-- test_cycles.py
|   |   |       |   |   |-- test_dates.py
|   |   |       |   |   |-- test_datetime.py
|   |   |       |   |   |-- test_determinism.py
|   |   |       |   |   |-- test_doc.py
|   |   |       |   |   |-- test_dviread.py
|   |   |       |   |   |-- test_figure.py
|   |   |       |   |   |-- test_font_manager.py
|   |   |       |   |   |-- test_fontconfig_pattern.py
|   |   |       |   |   |-- test_ft2font.py
|   |   |       |   |   |-- test_getattr.py
|   |   |       |   |   |-- test_gridspec.py
|   |   |       |   |   |-- test_image.py
|   |   |       |   |   |-- test_legend.py
|   |   |       |   |   |-- test_lines.py
|   |   |       |   |   |-- test_marker.py
|   |   |       |   |   |-- test_mathtext.py
|   |   |       |   |   |-- test_matplotlib.py
|   |   |       |   |   |-- test_mlab.py
|   |   |       |   |   |-- test_multivariate_colormaps.py
|   |   |       |   |   |-- test_offsetbox.py
|   |   |       |   |   |-- test_patches.py
|   |   |       |   |   |-- test_path.py
|   |   |       |   |   |-- test_patheffects.py
|   |   |       |   |   |-- test_pickle.py
|   |   |       |   |   |-- test_png.py
|   |   |       |   |   |-- test_polar.py
|   |   |       |   |   |-- test_preprocess_data.py
|   |   |       |   |   |-- test_pyplot.py
|   |   |       |   |   |-- test_quiver.py
|   |   |       |   |   |-- test_rcparams.py
|   |   |       |   |   |-- test_sankey.py
|   |   |       |   |   |-- test_scale.py
|   |   |       |   |   |-- test_simplification.py
|   |   |       |   |   |-- test_skew.py
|   |   |       |   |   |-- test_sphinxext.py
|   |   |       |   |   |-- test_spines.py
|   |   |       |   |   |-- test_streamplot.py
|   |   |       |   |   |-- test_style.py
|   |   |       |   |   |-- test_subplots.py
|   |   |       |   |   |-- test_table.py
|   |   |       |   |   |-- test_testing.py
|   |   |       |   |   |-- test_texmanager.py
|   |   |       |   |   |-- test_text.py
|   |   |       |   |   |-- test_textpath.py
|   |   |       |   |   |-- test_ticker.py
|   |   |       |   |   |-- test_tightlayout.py
|   |   |       |   |   |-- test_transforms.py
|   |   |       |   |   |-- test_triangulation.py
|   |   |       |   |   |-- test_type1font.py
|   |   |       |   |   |-- test_units.py
|   |   |       |   |   |-- test_usetex.py
|   |   |       |   |   +-- test_widgets.py
|   |   |       |   |-- tri
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _triangulation.cpython-313.pyc
|   |   |       |   |   |   |-- _tricontour.cpython-313.pyc
|   |   |       |   |   |   |-- _trifinder.cpython-313.pyc
|   |   |       |   |   |   |-- _triinterpolate.cpython-313.pyc
|   |   |       |   |   |   |-- _tripcolor.cpython-313.pyc
|   |   |       |   |   |   |-- _triplot.cpython-313.pyc
|   |   |       |   |   |   |-- _trirefine.cpython-313.pyc
|   |   |       |   |   |   +-- _tritools.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _triangulation.py
|   |   |       |   |   |-- _triangulation.pyi
|   |   |       |   |   |-- _tricontour.py
|   |   |       |   |   |-- _tricontour.pyi
|   |   |       |   |   |-- _trifinder.py
|   |   |       |   |   |-- _trifinder.pyi
|   |   |       |   |   |-- _triinterpolate.py
|   |   |       |   |   |-- _triinterpolate.pyi
|   |   |       |   |   |-- _tripcolor.py
|   |   |       |   |   |-- _tripcolor.pyi
|   |   |       |   |   |-- _triplot.py
|   |   |       |   |   |-- _triplot.pyi
|   |   |       |   |   |-- _trirefine.py
|   |   |       |   |   |-- _trirefine.pyi
|   |   |       |   |   |-- _tritools.py
|   |   |       |   |   +-- _tritools.pyi
|   |   |       |   |-- __init__.py
|   |   |       |   |-- __init__.pyi
|   |   |       |   |-- _afm.py
|   |   |       |   |-- _animation_data.py
|   |   |       |   |-- _blocking_input.py
|   |   |       |   |-- _c_internal_utils.cp313-win_amd64.pyd
|   |   |       |   |-- _c_internal_utils.pyi
|   |   |       |   |-- _cm.py
|   |   |       |   |-- _cm_bivar.py
|   |   |       |   |-- _cm_listed.py
|   |   |       |   |-- _cm_multivar.py
|   |   |       |   |-- _color_data.py
|   |   |       |   |-- _color_data.pyi
|   |   |       |   |-- _constrained_layout.py
|   |   |       |   |-- _docstring.py
|   |   |       |   |-- _docstring.pyi
|   |   |       |   |-- _enums.py
|   |   |       |   |-- _enums.pyi
|   |   |       |   |-- _fontconfig_pattern.py
|   |   |       |   |-- _image.cp313-win_amd64.pyd
|   |   |       |   |-- _image.pyi
|   |   |       |   |-- _internal_utils.py
|   |   |       |   |-- _layoutgrid.py
|   |   |       |   |-- _mathtext.py
|   |   |       |   |-- _mathtext_data.py
|   |   |       |   |-- _path.cp313-win_amd64.pyd
|   |   |       |   |-- _path.pyi
|   |   |       |   |-- _pylab_helpers.py
|   |   |       |   |-- _pylab_helpers.pyi
|   |   |       |   |-- _qhull.cp313-win_amd64.pyd
|   |   |       |   |-- _qhull.pyi
|   |   |       |   |-- _text_helpers.py
|   |   |       |   |-- _tight_bbox.py
|   |   |       |   |-- _tight_layout.py
|   |   |       |   |-- _tri.cp313-win_amd64.pyd
|   |   |       |   |-- _tri.pyi
|   |   |       |   |-- _type1font.py
|   |   |       |   |-- _version.py
|   |   |       |   |-- animation.py
|   |   |       |   |-- animation.pyi
|   |   |       |   |-- artist.py
|   |   |       |   |-- artist.pyi
|   |   |       |   |-- axis.py
|   |   |       |   |-- axis.pyi
|   |   |       |   |-- backend_bases.py
|   |   |       |   |-- backend_bases.pyi
|   |   |       |   |-- backend_managers.py
|   |   |       |   |-- backend_managers.pyi
|   |   |       |   |-- backend_tools.py
|   |   |       |   |-- backend_tools.pyi
|   |   |       |   |-- bezier.py
|   |   |       |   |-- bezier.pyi
|   |   |       |   |-- category.py
|   |   |       |   |-- cbook.py
|   |   |       |   |-- cbook.pyi
|   |   |       |   |-- cm.py
|   |   |       |   |-- cm.pyi
|   |   |       |   |-- collections.py
|   |   |       |   |-- collections.pyi
|   |   |       |   |-- colorbar.py
|   |   |       |   |-- colorbar.pyi
|   |   |       |   |-- colorizer.py
|   |   |       |   |-- colorizer.pyi
|   |   |       |   |-- colors.py
|   |   |       |   |-- colors.pyi
|   |   |       |   |-- container.py
|   |   |       |   |-- container.pyi
|   |   |       |   |-- contour.py
|   |   |       |   |-- contour.pyi
|   |   |       |   |-- dates.py
|   |   |       |   |-- dviread.py
|   |   |       |   |-- dviread.pyi
|   |   |       |   |-- figure.py
|   |   |       |   |-- figure.pyi
|   |   |       |   |-- font_manager.py
|   |   |       |   |-- font_manager.pyi
|   |   |       |   |-- ft2font.cp313-win_amd64.pyd
|   |   |       |   |-- ft2font.pyi
|   |   |       |   |-- gridspec.py
|   |   |       |   |-- gridspec.pyi
|   |   |       |   |-- hatch.py
|   |   |       |   |-- hatch.pyi
|   |   |       |   |-- image.py
|   |   |       |   |-- image.pyi
|   |   |       |   |-- inset.py
|   |   |       |   |-- inset.pyi
|   |   |       |   |-- layout_engine.py
|   |   |       |   |-- layout_engine.pyi
|   |   |       |   |-- legend.py
|   |   |       |   |-- legend.pyi
|   |   |       |   |-- legend_handler.py
|   |   |       |   |-- legend_handler.pyi
|   |   |       |   |-- lines.py
|   |   |       |   |-- lines.pyi
|   |   |       |   |-- markers.py
|   |   |       |   |-- markers.pyi
|   |   |       |   |-- mathtext.py
|   |   |       |   |-- mathtext.pyi
|   |   |       |   |-- mlab.py
|   |   |       |   |-- mlab.pyi
|   |   |       |   |-- offsetbox.py
|   |   |       |   |-- offsetbox.pyi
|   |   |       |   |-- patches.py
|   |   |       |   |-- patches.pyi
|   |   |       |   |-- path.py
|   |   |       |   |-- path.pyi
|   |   |       |   |-- patheffects.py
|   |   |       |   |-- patheffects.pyi
|   |   |       |   |-- py.typed
|   |   |       |   |-- pylab.py
|   |   |       |   |-- pyplot.py
|   |   |       |   |-- quiver.py
|   |   |       |   |-- quiver.pyi
|   |   |       |   |-- rcsetup.py
|   |   |       |   |-- rcsetup.pyi
|   |   |       |   |-- sankey.py
|   |   |       |   |-- sankey.pyi
|   |   |       |   |-- scale.py
|   |   |       |   |-- scale.pyi
|   |   |       |   |-- spines.py
|   |   |       |   |-- spines.pyi
|   |   |       |   |-- stackplot.py
|   |   |       |   |-- stackplot.pyi
|   |   |       |   |-- streamplot.py
|   |   |       |   |-- streamplot.pyi
|   |   |       |   |-- table.py
|   |   |       |   |-- table.pyi
|   |   |       |   |-- texmanager.py
|   |   |       |   |-- texmanager.pyi
|   |   |       |   |-- text.py
|   |   |       |   |-- text.pyi
|   |   |       |   |-- textpath.py
|   |   |       |   |-- textpath.pyi
|   |   |       |   |-- ticker.py
|   |   |       |   |-- ticker.pyi
|   |   |       |   |-- transforms.py
|   |   |       |   |-- transforms.pyi
|   |   |       |   |-- typing.py
|   |   |       |   |-- units.py
|   |   |       |   |-- widgets.py
|   |   |       |   +-- widgets.pyi
|   |   |       |-- matplotlib-3.10.7.dist-info
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- LICENSE
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- REQUESTED
|   |   |       |   +-- WHEEL
|   |   |       |-- mpl_toolkits
|   |   |       |   |-- axes_grid1
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- anchored_artists.cpython-313.pyc
|   |   |       |   |   |   |-- axes_divider.cpython-313.pyc
|   |   |       |   |   |   |-- axes_grid.cpython-313.pyc
|   |   |       |   |   |   |-- axes_rgb.cpython-313.pyc
|   |   |       |   |   |   |-- axes_size.cpython-313.pyc
|   |   |       |   |   |   |-- inset_locator.cpython-313.pyc
|   |   |       |   |   |   |-- mpl_axes.cpython-313.pyc
|   |   |       |   |   |   +-- parasite_axes.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- conftest.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_axes_grid1.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- conftest.py
|   |   |       |   |   |   +-- test_axes_grid1.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- anchored_artists.py
|   |   |       |   |   |-- axes_divider.py
|   |   |       |   |   |-- axes_grid.py
|   |   |       |   |   |-- axes_rgb.py
|   |   |       |   |   |-- axes_size.py
|   |   |       |   |   |-- inset_locator.py
|   |   |       |   |   |-- mpl_axes.py
|   |   |       |   |   +-- parasite_axes.py
|   |   |       |   |-- axisartist
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- angle_helper.cpython-313.pyc
|   |   |       |   |   |   |-- axes_divider.cpython-313.pyc
|   |   |       |   |   |   |-- axis_artist.cpython-313.pyc
|   |   |       |   |   |   |-- axisline_style.cpython-313.pyc
|   |   |       |   |   |   |-- axislines.cpython-313.pyc
|   |   |       |   |   |   |-- floating_axes.cpython-313.pyc
|   |   |       |   |   |   |-- grid_finder.cpython-313.pyc
|   |   |       |   |   |   |-- grid_helper_curvelinear.cpython-313.pyc
|   |   |       |   |   |   +-- parasite_axes.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- conftest.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_angle_helper.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_axis_artist.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_axislines.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_floating_axes.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_grid_finder.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_grid_helper_curvelinear.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- conftest.py
|   |   |       |   |   |   |-- test_angle_helper.py
|   |   |       |   |   |   |-- test_axis_artist.py
|   |   |       |   |   |   |-- test_axislines.py
|   |   |       |   |   |   |-- test_floating_axes.py
|   |   |       |   |   |   |-- test_grid_finder.py
|   |   |       |   |   |   +-- test_grid_helper_curvelinear.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- angle_helper.py
|   |   |       |   |   |-- axes_divider.py
|   |   |       |   |   |-- axis_artist.py
|   |   |       |   |   |-- axisline_style.py
|   |   |       |   |   |-- axislines.py
|   |   |       |   |   |-- floating_axes.py
|   |   |       |   |   |-- grid_finder.py
|   |   |       |   |   |-- grid_helper_curvelinear.py
|   |   |       |   |   +-- parasite_axes.py
|   |   |       |   +-- mplot3d
|   |   |       |       |-- __pycache__
|   |   |       |       |   |-- __init__.cpython-313.pyc
|   |   |       |       |   |-- art3d.cpython-313.pyc
|   |   |       |       |   |-- axes3d.cpython-313.pyc
|   |   |       |       |   |-- axis3d.cpython-313.pyc
|   |   |       |       |   +-- proj3d.cpython-313.pyc
|   |   |       |       |-- tests
|   |   |       |       |   |-- __pycache__
|   |   |       |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |       |   |   |-- conftest.cpython-313.pyc
|   |   |       |       |   |   |-- test_art3d.cpython-313.pyc
|   |   |       |       |   |   |-- test_axes3d.cpython-313.pyc
|   |   |       |       |   |   +-- test_legend3d.cpython-313.pyc
|   |   |       |       |   |-- __init__.py
|   |   |       |       |   |-- conftest.py
|   |   |       |       |   |-- test_art3d.py
|   |   |       |       |   |-- test_axes3d.py
|   |   |       |       |   +-- test_legend3d.py
|   |   |       |       |-- __init__.py
|   |   |       |       |-- art3d.py
|   |   |       |       |-- axes3d.py
|   |   |       |       |-- axis3d.py
|   |   |       |       +-- proj3d.py
|   |   |       |-- numpy
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __config__.cpython-313.pyc
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- _array_api_info.cpython-313.pyc
|   |   |       |   |   |-- _configtool.cpython-313.pyc
|   |   |       |   |   |-- _distributor_init.cpython-313.pyc
|   |   |       |   |   |-- _expired_attrs_2_0.cpython-313.pyc
|   |   |       |   |   |-- _globals.cpython-313.pyc
|   |   |       |   |   |-- _pytesttester.cpython-313.pyc
|   |   |       |   |   |-- conftest.cpython-313.pyc
|   |   |       |   |   |-- dtypes.cpython-313.pyc
|   |   |       |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |-- matlib.cpython-313.pyc
|   |   |       |   |   +-- version.cpython-313.pyc
|   |   |       |   |-- _core
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _add_newdocs.cpython-313.pyc
|   |   |       |   |   |   |-- _add_newdocs_scalars.cpython-313.pyc
|   |   |       |   |   |   |-- _asarray.cpython-313.pyc
|   |   |       |   |   |   |-- _dtype.cpython-313.pyc
|   |   |       |   |   |   |-- _dtype_ctypes.cpython-313.pyc
|   |   |       |   |   |   |-- _exceptions.cpython-313.pyc
|   |   |       |   |   |   |-- _internal.cpython-313.pyc
|   |   |       |   |   |   |-- _machar.cpython-313.pyc
|   |   |       |   |   |   |-- _methods.cpython-313.pyc
|   |   |       |   |   |   |-- _string_helpers.cpython-313.pyc
|   |   |       |   |   |   |-- _type_aliases.cpython-313.pyc
|   |   |       |   |   |   |-- _ufunc_config.cpython-313.pyc
|   |   |       |   |   |   |-- arrayprint.cpython-313.pyc
|   |   |       |   |   |   |-- cversions.cpython-313.pyc
|   |   |       |   |   |   |-- defchararray.cpython-313.pyc
|   |   |       |   |   |   |-- einsumfunc.cpython-313.pyc
|   |   |       |   |   |   |-- fromnumeric.cpython-313.pyc
|   |   |       |   |   |   |-- function_base.cpython-313.pyc
|   |   |       |   |   |   |-- getlimits.cpython-313.pyc
|   |   |       |   |   |   |-- memmap.cpython-313.pyc
|   |   |       |   |   |   |-- multiarray.cpython-313.pyc
|   |   |       |   |   |   |-- numeric.cpython-313.pyc
|   |   |       |   |   |   |-- numerictypes.cpython-313.pyc
|   |   |       |   |   |   |-- overrides.cpython-313.pyc
|   |   |       |   |   |   |-- printoptions.cpython-313.pyc
|   |   |       |   |   |   |-- records.cpython-313.pyc
|   |   |       |   |   |   |-- shape_base.cpython-313.pyc
|   |   |       |   |   |   |-- strings.cpython-313.pyc
|   |   |       |   |   |   +-- umath.cpython-313.pyc
|   |   |       |   |   |-- include
|   |   |       |   |   |   +-- numpy
|   |   |       |   |   |       |-- random
|   |   |       |   |   |       |   |-- bitgen.h
|   |   |       |   |   |       |   |-- distributions.h
|   |   |       |   |   |       |   |-- libdivide.h
|   |   |       |   |   |       |   +-- LICENSE.txt
|   |   |       |   |   |       |-- __multiarray_api.c
|   |   |       |   |   |       |-- __multiarray_api.h
|   |   |       |   |   |       |-- __ufunc_api.c
|   |   |       |   |   |       |-- __ufunc_api.h
|   |   |       |   |   |       |-- _neighborhood_iterator_imp.h
|   |   |       |   |   |       |-- _numpyconfig.h
|   |   |       |   |   |       |-- _public_dtype_api_table.h
|   |   |       |   |   |       |-- arrayobject.h
|   |   |       |   |   |       |-- arrayscalars.h
|   |   |       |   |   |       |-- dtype_api.h
|   |   |       |   |   |       |-- halffloat.h
|   |   |       |   |   |       |-- ndarrayobject.h
|   |   |       |   |   |       |-- ndarraytypes.h
|   |   |       |   |   |       |-- npy_2_compat.h
|   |   |       |   |   |       |-- npy_2_complexcompat.h
|   |   |       |   |   |       |-- npy_3kcompat.h
|   |   |       |   |   |       |-- npy_common.h
|   |   |       |   |   |       |-- npy_cpu.h
|   |   |       |   |   |       |-- npy_endian.h
|   |   |       |   |   |       |-- npy_math.h
|   |   |       |   |   |       |-- npy_no_deprecated_api.h
|   |   |       |   |   |       |-- npy_os.h
|   |   |       |   |   |       |-- numpyconfig.h
|   |   |       |   |   |       |-- ufuncobject.h
|   |   |       |   |   |       +-- utils.h
|   |   |       |   |   |-- lib
|   |   |       |   |   |   |-- npy-pkg-config
|   |   |       |   |   |   |   |-- mlib.ini
|   |   |       |   |   |   |   +-- npymath.ini
|   |   |       |   |   |   |-- pkgconfig
|   |   |       |   |   |   |   +-- numpy.pc
|   |   |       |   |   |   +-- npymath.lib
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- _locales.cpython-313.pyc
|   |   |       |   |   |   |   |-- _natype.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__exceptions.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_abc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_api.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_argparse.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_api_info.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_coercion.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_interface.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arraymethod.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arrayobject.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arrayprint.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_casting_floatingpoint_errors.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_casting_unittests.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_conversion_utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cpu_dispatcher.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cpu_features.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_custom_dtypes.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cython.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_datetime.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_defchararray.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_deprecations.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_dlpack.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_dtype.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_einsum.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_errstate.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_extint128.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_function_base.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_getlimits.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_half.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hashtable.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_indexerrors.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_indexing.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_item_selection.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_limited_api.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_longdouble.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_machar.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mem_overlap.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mem_policy.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_memmap.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_multiarray.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_multithreading.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_nditer.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_nep50_promotions.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_numeric.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_numerictypes.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_overrides.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_print.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_protocols.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_records.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_scalar_ctors.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_scalar_methods.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_scalarbuffer.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_scalarinherit.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_scalarmath.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_scalarprint.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_shape_base.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_simd.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_simd_module.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_stringdtype.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_strings.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ufunc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_umath.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_umath_accuracy.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_umath_complex.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_unicode.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- astype_copy.pkl
|   |   |       |   |   |   |   |-- generate_umath_validation_data.cpp
|   |   |       |   |   |   |   |-- recarray_from_file.fits
|   |   |       |   |   |   |   |-- umath-validation-set-arccos.csv
|   |   |       |   |   |   |   |-- umath-validation-set-arccosh.csv
|   |   |       |   |   |   |   |-- umath-validation-set-arcsin.csv
|   |   |       |   |   |   |   |-- umath-validation-set-arcsinh.csv
|   |   |       |   |   |   |   |-- umath-validation-set-arctan.csv
|   |   |       |   |   |   |   |-- umath-validation-set-arctanh.csv
|   |   |       |   |   |   |   |-- umath-validation-set-cbrt.csv
|   |   |       |   |   |   |   |-- umath-validation-set-cos.csv
|   |   |       |   |   |   |   |-- umath-validation-set-cosh.csv
|   |   |       |   |   |   |   |-- umath-validation-set-exp.csv
|   |   |       |   |   |   |   |-- umath-validation-set-exp2.csv
|   |   |       |   |   |   |   |-- umath-validation-set-expm1.csv
|   |   |       |   |   |   |   |-- umath-validation-set-log.csv
|   |   |       |   |   |   |   |-- umath-validation-set-log10.csv
|   |   |       |   |   |   |   |-- umath-validation-set-log1p.csv
|   |   |       |   |   |   |   |-- umath-validation-set-log2.csv
|   |   |       |   |   |   |   |-- umath-validation-set-README.txt
|   |   |       |   |   |   |   |-- umath-validation-set-sin.csv
|   |   |       |   |   |   |   |-- umath-validation-set-sinh.csv
|   |   |       |   |   |   |   |-- umath-validation-set-tan.csv
|   |   |       |   |   |   |   +-- umath-validation-set-tanh.csv
|   |   |       |   |   |   |-- examples
|   |   |       |   |   |   |   |-- cython
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   +-- setup.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- checks.pyx
|   |   |       |   |   |   |   |   |-- meson.build
|   |   |       |   |   |   |   |   +-- setup.py
|   |   |       |   |   |   |   +-- limited_api
|   |   |       |   |   |   |       |-- __pycache__
|   |   |       |   |   |   |       |   +-- setup.cpython-313.pyc
|   |   |       |   |   |   |       |-- limited_api_latest.c
|   |   |       |   |   |   |       |-- limited_api1.c
|   |   |       |   |   |   |       |-- limited_api2.pyx
|   |   |       |   |   |   |       |-- meson.build
|   |   |       |   |   |   |       +-- setup.py
|   |   |       |   |   |   |-- _locales.py
|   |   |       |   |   |   |-- _natype.py
|   |   |       |   |   |   |-- test__exceptions.py
|   |   |       |   |   |   |-- test_abc.py
|   |   |       |   |   |   |-- test_api.py
|   |   |       |   |   |   |-- test_argparse.py
|   |   |       |   |   |   |-- test_array_api_info.py
|   |   |       |   |   |   |-- test_array_coercion.py
|   |   |       |   |   |   |-- test_array_interface.py
|   |   |       |   |   |   |-- test_arraymethod.py
|   |   |       |   |   |   |-- test_arrayobject.py
|   |   |       |   |   |   |-- test_arrayprint.py
|   |   |       |   |   |   |-- test_casting_floatingpoint_errors.py
|   |   |       |   |   |   |-- test_casting_unittests.py
|   |   |       |   |   |   |-- test_conversion_utils.py
|   |   |       |   |   |   |-- test_cpu_dispatcher.py
|   |   |       |   |   |   |-- test_cpu_features.py
|   |   |       |   |   |   |-- test_custom_dtypes.py
|   |   |       |   |   |   |-- test_cython.py
|   |   |       |   |   |   |-- test_datetime.py
|   |   |       |   |   |   |-- test_defchararray.py
|   |   |       |   |   |   |-- test_deprecations.py
|   |   |       |   |   |   |-- test_dlpack.py
|   |   |       |   |   |   |-- test_dtype.py
|   |   |       |   |   |   |-- test_einsum.py
|   |   |       |   |   |   |-- test_errstate.py
|   |   |       |   |   |   |-- test_extint128.py
|   |   |       |   |   |   |-- test_function_base.py
|   |   |       |   |   |   |-- test_getlimits.py
|   |   |       |   |   |   |-- test_half.py
|   |   |       |   |   |   |-- test_hashtable.py
|   |   |       |   |   |   |-- test_indexerrors.py
|   |   |       |   |   |   |-- test_indexing.py
|   |   |       |   |   |   |-- test_item_selection.py
|   |   |       |   |   |   |-- test_limited_api.py
|   |   |       |   |   |   |-- test_longdouble.py
|   |   |       |   |   |   |-- test_machar.py
|   |   |       |   |   |   |-- test_mem_overlap.py
|   |   |       |   |   |   |-- test_mem_policy.py
|   |   |       |   |   |   |-- test_memmap.py
|   |   |       |   |   |   |-- test_multiarray.py
|   |   |       |   |   |   |-- test_multithreading.py
|   |   |       |   |   |   |-- test_nditer.py
|   |   |       |   |   |   |-- test_nep50_promotions.py
|   |   |       |   |   |   |-- test_numeric.py
|   |   |       |   |   |   |-- test_numerictypes.py
|   |   |       |   |   |   |-- test_overrides.py
|   |   |       |   |   |   |-- test_print.py
|   |   |       |   |   |   |-- test_protocols.py
|   |   |       |   |   |   |-- test_records.py
|   |   |       |   |   |   |-- test_regression.py
|   |   |       |   |   |   |-- test_scalar_ctors.py
|   |   |       |   |   |   |-- test_scalar_methods.py
|   |   |       |   |   |   |-- test_scalarbuffer.py
|   |   |       |   |   |   |-- test_scalarinherit.py
|   |   |       |   |   |   |-- test_scalarmath.py
|   |   |       |   |   |   |-- test_scalarprint.py
|   |   |       |   |   |   |-- test_shape_base.py
|   |   |       |   |   |   |-- test_simd.py
|   |   |       |   |   |   |-- test_simd_module.py
|   |   |       |   |   |   |-- test_stringdtype.py
|   |   |       |   |   |   |-- test_strings.py
|   |   |       |   |   |   |-- test_ufunc.py
|   |   |       |   |   |   |-- test_umath.py
|   |   |       |   |   |   |-- test_umath_accuracy.py
|   |   |       |   |   |   |-- test_umath_complex.py
|   |   |       |   |   |   +-- test_unicode.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _add_newdocs.py
|   |   |       |   |   |-- _add_newdocs.pyi
|   |   |       |   |   |-- _add_newdocs_scalars.py
|   |   |       |   |   |-- _add_newdocs_scalars.pyi
|   |   |       |   |   |-- _asarray.py
|   |   |       |   |   |-- _asarray.pyi
|   |   |       |   |   |-- _dtype.py
|   |   |       |   |   |-- _dtype.pyi
|   |   |       |   |   |-- _dtype_ctypes.py
|   |   |       |   |   |-- _dtype_ctypes.pyi
|   |   |       |   |   |-- _exceptions.py
|   |   |       |   |   |-- _exceptions.pyi
|   |   |       |   |   |-- _internal.py
|   |   |       |   |   |-- _internal.pyi
|   |   |       |   |   |-- _machar.py
|   |   |       |   |   |-- _machar.pyi
|   |   |       |   |   |-- _methods.py
|   |   |       |   |   |-- _methods.pyi
|   |   |       |   |   |-- _multiarray_tests.cp313-win_amd64.lib
|   |   |       |   |   |-- _multiarray_tests.cp313-win_amd64.pyd
|   |   |       |   |   |-- _multiarray_umath.cp313-win_amd64.lib
|   |   |       |   |   |-- _multiarray_umath.cp313-win_amd64.pyd
|   |   |       |   |   |-- _operand_flag_tests.cp313-win_amd64.lib
|   |   |       |   |   |-- _operand_flag_tests.cp313-win_amd64.pyd
|   |   |       |   |   |-- _rational_tests.cp313-win_amd64.lib
|   |   |       |   |   |-- _rational_tests.cp313-win_amd64.pyd
|   |   |       |   |   |-- _simd.cp313-win_amd64.lib
|   |   |       |   |   |-- _simd.cp313-win_amd64.pyd
|   |   |       |   |   |-- _simd.pyi
|   |   |       |   |   |-- _string_helpers.py
|   |   |       |   |   |-- _string_helpers.pyi
|   |   |       |   |   |-- _struct_ufunc_tests.cp313-win_amd64.lib
|   |   |       |   |   |-- _struct_ufunc_tests.cp313-win_amd64.pyd
|   |   |       |   |   |-- _type_aliases.py
|   |   |       |   |   |-- _type_aliases.pyi
|   |   |       |   |   |-- _ufunc_config.py
|   |   |       |   |   |-- _ufunc_config.pyi
|   |   |       |   |   |-- _umath_tests.cp313-win_amd64.lib
|   |   |       |   |   |-- _umath_tests.cp313-win_amd64.pyd
|   |   |       |   |   |-- arrayprint.py
|   |   |       |   |   |-- arrayprint.pyi
|   |   |       |   |   |-- cversions.py
|   |   |       |   |   |-- defchararray.py
|   |   |       |   |   |-- defchararray.pyi
|   |   |       |   |   |-- einsumfunc.py
|   |   |       |   |   |-- einsumfunc.pyi
|   |   |       |   |   |-- fromnumeric.py
|   |   |       |   |   |-- fromnumeric.pyi
|   |   |       |   |   |-- function_base.py
|   |   |       |   |   |-- function_base.pyi
|   |   |       |   |   |-- getlimits.py
|   |   |       |   |   |-- getlimits.pyi
|   |   |       |   |   |-- memmap.py
|   |   |       |   |   |-- memmap.pyi
|   |   |       |   |   |-- multiarray.py
|   |   |       |   |   |-- multiarray.pyi
|   |   |       |   |   |-- numeric.py
|   |   |       |   |   |-- numeric.pyi
|   |   |       |   |   |-- numerictypes.py
|   |   |       |   |   |-- numerictypes.pyi
|   |   |       |   |   |-- overrides.py
|   |   |       |   |   |-- overrides.pyi
|   |   |       |   |   |-- printoptions.py
|   |   |       |   |   |-- printoptions.pyi
|   |   |       |   |   |-- records.py
|   |   |       |   |   |-- records.pyi
|   |   |       |   |   |-- shape_base.py
|   |   |       |   |   |-- shape_base.pyi
|   |   |       |   |   |-- strings.py
|   |   |       |   |   |-- strings.pyi
|   |   |       |   |   |-- umath.py
|   |   |       |   |   +-- umath.pyi
|   |   |       |   |-- _pyinstaller
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- hook-numpy.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- pyinstaller-smoke.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_pyinstaller.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- pyinstaller-smoke.py
|   |   |       |   |   |   +-- test_pyinstaller.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- hook-numpy.py
|   |   |       |   |   +-- hook-numpy.pyi
|   |   |       |   |-- _typing
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _add_docstring.cpython-313.pyc
|   |   |       |   |   |   |-- _array_like.cpython-313.pyc
|   |   |       |   |   |   |-- _char_codes.cpython-313.pyc
|   |   |       |   |   |   |-- _dtype_like.cpython-313.pyc
|   |   |       |   |   |   |-- _extended_precision.cpython-313.pyc
|   |   |       |   |   |   |-- _nbit.cpython-313.pyc
|   |   |       |   |   |   |-- _nbit_base.cpython-313.pyc
|   |   |       |   |   |   |-- _nested_sequence.cpython-313.pyc
|   |   |       |   |   |   |-- _scalars.cpython-313.pyc
|   |   |       |   |   |   |-- _shape.cpython-313.pyc
|   |   |       |   |   |   +-- _ufunc.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _add_docstring.py
|   |   |       |   |   |-- _array_like.py
|   |   |       |   |   |-- _char_codes.py
|   |   |       |   |   |-- _dtype_like.py
|   |   |       |   |   |-- _extended_precision.py
|   |   |       |   |   |-- _nbit.py
|   |   |       |   |   |-- _nbit_base.py
|   |   |       |   |   |-- _nbit_base.pyi
|   |   |       |   |   |-- _nested_sequence.py
|   |   |       |   |   |-- _scalars.py
|   |   |       |   |   |-- _shape.py
|   |   |       |   |   |-- _ufunc.py
|   |   |       |   |   +-- _ufunc.pyi
|   |   |       |   |-- _utils
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _convertions.cpython-313.pyc
|   |   |       |   |   |   |-- _inspect.cpython-313.pyc
|   |   |       |   |   |   +-- _pep440.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _convertions.py
|   |   |       |   |   |-- _convertions.pyi
|   |   |       |   |   |-- _inspect.py
|   |   |       |   |   |-- _inspect.pyi
|   |   |       |   |   |-- _pep440.py
|   |   |       |   |   +-- _pep440.pyi
|   |   |       |   |-- char
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- __init__.pyi
|   |   |       |   |-- core
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _dtype.cpython-313.pyc
|   |   |       |   |   |   |-- _dtype_ctypes.cpython-313.pyc
|   |   |       |   |   |   |-- _internal.cpython-313.pyc
|   |   |       |   |   |   |-- _multiarray_umath.cpython-313.pyc
|   |   |       |   |   |   |-- _utils.cpython-313.pyc
|   |   |       |   |   |   |-- arrayprint.cpython-313.pyc
|   |   |       |   |   |   |-- defchararray.cpython-313.pyc
|   |   |       |   |   |   |-- einsumfunc.cpython-313.pyc
|   |   |       |   |   |   |-- fromnumeric.cpython-313.pyc
|   |   |       |   |   |   |-- function_base.cpython-313.pyc
|   |   |       |   |   |   |-- getlimits.cpython-313.pyc
|   |   |       |   |   |   |-- multiarray.cpython-313.pyc
|   |   |       |   |   |   |-- numeric.cpython-313.pyc
|   |   |       |   |   |   |-- numerictypes.cpython-313.pyc
|   |   |       |   |   |   |-- overrides.cpython-313.pyc
|   |   |       |   |   |   |-- records.cpython-313.pyc
|   |   |       |   |   |   |-- shape_base.cpython-313.pyc
|   |   |       |   |   |   +-- umath.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _dtype.py
|   |   |       |   |   |-- _dtype.pyi
|   |   |       |   |   |-- _dtype_ctypes.py
|   |   |       |   |   |-- _dtype_ctypes.pyi
|   |   |       |   |   |-- _internal.py
|   |   |       |   |   |-- _multiarray_umath.py
|   |   |       |   |   |-- _utils.py
|   |   |       |   |   |-- arrayprint.py
|   |   |       |   |   |-- defchararray.py
|   |   |       |   |   |-- einsumfunc.py
|   |   |       |   |   |-- fromnumeric.py
|   |   |       |   |   |-- function_base.py
|   |   |       |   |   |-- getlimits.py
|   |   |       |   |   |-- multiarray.py
|   |   |       |   |   |-- numeric.py
|   |   |       |   |   |-- numerictypes.py
|   |   |       |   |   |-- overrides.py
|   |   |       |   |   |-- overrides.pyi
|   |   |       |   |   |-- records.py
|   |   |       |   |   |-- shape_base.py
|   |   |       |   |   +-- umath.py
|   |   |       |   |-- ctypeslib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- _ctypeslib.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _ctypeslib.py
|   |   |       |   |   +-- _ctypeslib.pyi
|   |   |       |   |-- doc
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- ufuncs.cpython-313.pyc
|   |   |       |   |   +-- ufuncs.py
|   |   |       |   |-- f2py
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |-- __version__.cpython-313.pyc
|   |   |       |   |   |   |-- _isocbind.cpython-313.pyc
|   |   |       |   |   |   |-- _src_pyf.cpython-313.pyc
|   |   |       |   |   |   |-- auxfuncs.cpython-313.pyc
|   |   |       |   |   |   |-- capi_maps.cpython-313.pyc
|   |   |       |   |   |   |-- cb_rules.cpython-313.pyc
|   |   |       |   |   |   |-- cfuncs.cpython-313.pyc
|   |   |       |   |   |   |-- common_rules.cpython-313.pyc
|   |   |       |   |   |   |-- crackfortran.cpython-313.pyc
|   |   |       |   |   |   |-- diagnose.cpython-313.pyc
|   |   |       |   |   |   |-- f2py2e.cpython-313.pyc
|   |   |       |   |   |   |-- f90mod_rules.cpython-313.pyc
|   |   |       |   |   |   |-- func2subr.cpython-313.pyc
|   |   |       |   |   |   |-- rules.cpython-313.pyc
|   |   |       |   |   |   |-- symbolic.cpython-313.pyc
|   |   |       |   |   |   +-- use_rules.cpython-313.pyc
|   |   |       |   |   |-- _backends
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _backend.cpython-313.pyc
|   |   |       |   |   |   |   |-- _distutils.cpython-313.pyc
|   |   |       |   |   |   |   +-- _meson.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __init__.pyi
|   |   |       |   |   |   |-- _backend.py
|   |   |       |   |   |   |-- _backend.pyi
|   |   |       |   |   |   |-- _distutils.py
|   |   |       |   |   |   |-- _distutils.pyi
|   |   |       |   |   |   |-- _meson.py
|   |   |       |   |   |   |-- _meson.pyi
|   |   |       |   |   |   +-- meson.build.template
|   |   |       |   |   |-- src
|   |   |       |   |   |   |-- fortranobject.c
|   |   |       |   |   |   +-- fortranobject.h
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_abstract_interface.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_from_pyobj.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_assumed_shape.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_block_docstring.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_callback.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_character.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_common.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_crackfortran.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_data.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_docs.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_f2cmap.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_f2py2e.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_isoc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_kind.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mixed.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_modules.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_parameter.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_pyf_src.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_quoted_character.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_return_character.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_return_complex.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_return_integer.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_return_logical.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_return_real.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_routines.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_semicolon_split.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_size.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_string.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_symbolic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_value_attrspec.cpython-313.pyc
|   |   |       |   |   |   |   +-- util.cpython-313.pyc
|   |   |       |   |   |   |-- src
|   |   |       |   |   |   |   |-- abstract_interface
|   |   |       |   |   |   |   |   |-- foo.f90
|   |   |       |   |   |   |   |   +-- gh18403_mod.f90
|   |   |       |   |   |   |   |-- array_from_pyobj
|   |   |       |   |   |   |   |   +-- wrapmodule.c
|   |   |       |   |   |   |   |-- assumed_shape
|   |   |       |   |   |   |   |   |-- .f2py_f2cmap
|   |   |       |   |   |   |   |   |-- foo_free.f90
|   |   |       |   |   |   |   |   |-- foo_mod.f90
|   |   |       |   |   |   |   |   |-- foo_use.f90
|   |   |       |   |   |   |   |   +-- precision.f90
|   |   |       |   |   |   |   |-- block_docstring
|   |   |       |   |   |   |   |   +-- foo.f
|   |   |       |   |   |   |   |-- callback
|   |   |       |   |   |   |   |   |-- foo.f
|   |   |       |   |   |   |   |   |-- gh17797.f90
|   |   |       |   |   |   |   |   |-- gh18335.f90
|   |   |       |   |   |   |   |   |-- gh25211.f
|   |   |       |   |   |   |   |   |-- gh25211.pyf
|   |   |       |   |   |   |   |   +-- gh26681.f90
|   |   |       |   |   |   |   |-- cli
|   |   |       |   |   |   |   |   |-- gh_22819.pyf
|   |   |       |   |   |   |   |   |-- hi77.f
|   |   |       |   |   |   |   |   +-- hiworld.f90
|   |   |       |   |   |   |   |-- common
|   |   |       |   |   |   |   |   |-- block.f
|   |   |       |   |   |   |   |   +-- gh19161.f90
|   |   |       |   |   |   |   |-- crackfortran
|   |   |       |   |   |   |   |   |-- accesstype.f90
|   |   |       |   |   |   |   |   |-- common_with_division.f
|   |   |       |   |   |   |   |   |-- data_common.f
|   |   |       |   |   |   |   |   |-- data_multiplier.f
|   |   |       |   |   |   |   |   |-- data_stmts.f90
|   |   |       |   |   |   |   |   |-- data_with_comments.f
|   |   |       |   |   |   |   |   |-- foo_deps.f90
|   |   |       |   |   |   |   |   |-- gh15035.f
|   |   |       |   |   |   |   |   |-- gh17859.f
|   |   |       |   |   |   |   |   |-- gh22648.pyf
|   |   |       |   |   |   |   |   |-- gh23533.f
|   |   |       |   |   |   |   |   |-- gh23598.f90
|   |   |       |   |   |   |   |   |-- gh23598Warn.f90
|   |   |       |   |   |   |   |   |-- gh23879.f90
|   |   |       |   |   |   |   |   |-- gh27697.f90
|   |   |       |   |   |   |   |   |-- gh2848.f90
|   |   |       |   |   |   |   |   |-- operators.f90
|   |   |       |   |   |   |   |   |-- privatemod.f90
|   |   |       |   |   |   |   |   |-- publicmod.f90
|   |   |       |   |   |   |   |   |-- pubprivmod.f90
|   |   |       |   |   |   |   |   +-- unicode_comment.f90
|   |   |       |   |   |   |   |-- f2cmap
|   |   |       |   |   |   |   |   |-- .f2py_f2cmap
|   |   |       |   |   |   |   |   +-- isoFortranEnvMap.f90
|   |   |       |   |   |   |   |-- isocintrin
|   |   |       |   |   |   |   |   +-- isoCtests.f90
|   |   |       |   |   |   |   |-- kind
|   |   |       |   |   |   |   |   +-- foo.f90
|   |   |       |   |   |   |   |-- mixed
|   |   |       |   |   |   |   |   |-- foo.f
|   |   |       |   |   |   |   |   |-- foo_fixed.f90
|   |   |       |   |   |   |   |   +-- foo_free.f90
|   |   |       |   |   |   |   |-- modules
|   |   |       |   |   |   |   |   |-- gh25337
|   |   |       |   |   |   |   |   |   |-- data.f90
|   |   |       |   |   |   |   |   |   +-- use_data.f90
|   |   |       |   |   |   |   |   |-- gh26920
|   |   |       |   |   |   |   |   |   |-- two_mods_with_no_public_entities.f90
|   |   |       |   |   |   |   |   |   +-- two_mods_with_one_public_routine.f90
|   |   |       |   |   |   |   |   |-- module_data_docstring.f90
|   |   |       |   |   |   |   |   +-- use_modules.f90
|   |   |       |   |   |   |   |-- negative_bounds
|   |   |       |   |   |   |   |   +-- issue_20853.f90
|   |   |       |   |   |   |   |-- parameter
|   |   |       |   |   |   |   |   |-- constant_array.f90
|   |   |       |   |   |   |   |   |-- constant_both.f90
|   |   |       |   |   |   |   |   |-- constant_compound.f90
|   |   |       |   |   |   |   |   |-- constant_integer.f90
|   |   |       |   |   |   |   |   |-- constant_non_compound.f90
|   |   |       |   |   |   |   |   +-- constant_real.f90
|   |   |       |   |   |   |   |-- quoted_character
|   |   |       |   |   |   |   |   +-- foo.f
|   |   |       |   |   |   |   |-- regression
|   |   |       |   |   |   |   |   |-- AB.inc
|   |   |       |   |   |   |   |   |-- assignOnlyModule.f90
|   |   |       |   |   |   |   |   |-- datonly.f90
|   |   |       |   |   |   |   |   |-- f77comments.f
|   |   |       |   |   |   |   |   |-- f77fixedform.f95
|   |   |       |   |   |   |   |   |-- f90continuation.f90
|   |   |       |   |   |   |   |   |-- incfile.f90
|   |   |       |   |   |   |   |   |-- inout.f90
|   |   |       |   |   |   |   |   |-- lower_f2py_fortran.f90
|   |   |       |   |   |   |   |   +-- mod_derived_types.f90
|   |   |       |   |   |   |   |-- return_character
|   |   |       |   |   |   |   |   |-- foo77.f
|   |   |       |   |   |   |   |   +-- foo90.f90
|   |   |       |   |   |   |   |-- return_complex
|   |   |       |   |   |   |   |   |-- foo77.f
|   |   |       |   |   |   |   |   +-- foo90.f90
|   |   |       |   |   |   |   |-- return_integer
|   |   |       |   |   |   |   |   |-- foo77.f
|   |   |       |   |   |   |   |   +-- foo90.f90
|   |   |       |   |   |   |   |-- return_logical
|   |   |       |   |   |   |   |   |-- foo77.f
|   |   |       |   |   |   |   |   +-- foo90.f90
|   |   |       |   |   |   |   |-- return_real
|   |   |       |   |   |   |   |   |-- foo77.f
|   |   |       |   |   |   |   |   +-- foo90.f90
|   |   |       |   |   |   |   |-- routines
|   |   |       |   |   |   |   |   |-- funcfortranname.f
|   |   |       |   |   |   |   |   |-- funcfortranname.pyf
|   |   |       |   |   |   |   |   |-- subrout.f
|   |   |       |   |   |   |   |   +-- subrout.pyf
|   |   |       |   |   |   |   |-- size
|   |   |       |   |   |   |   |   +-- foo.f90
|   |   |       |   |   |   |   |-- string
|   |   |       |   |   |   |   |   |-- char.f90
|   |   |       |   |   |   |   |   |-- fixed_string.f90
|   |   |       |   |   |   |   |   |-- gh24008.f
|   |   |       |   |   |   |   |   |-- gh24662.f90
|   |   |       |   |   |   |   |   |-- gh25286.f90
|   |   |       |   |   |   |   |   |-- gh25286.pyf
|   |   |       |   |   |   |   |   |-- gh25286_bc.pyf
|   |   |       |   |   |   |   |   |-- scalar_string.f90
|   |   |       |   |   |   |   |   +-- string.f
|   |   |       |   |   |   |   +-- value_attrspec
|   |   |       |   |   |   |       +-- gh21665.f90
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_abstract_interface.py
|   |   |       |   |   |   |-- test_array_from_pyobj.py
|   |   |       |   |   |   |-- test_assumed_shape.py
|   |   |       |   |   |   |-- test_block_docstring.py
|   |   |       |   |   |   |-- test_callback.py
|   |   |       |   |   |   |-- test_character.py
|   |   |       |   |   |   |-- test_common.py
|   |   |       |   |   |   |-- test_crackfortran.py
|   |   |       |   |   |   |-- test_data.py
|   |   |       |   |   |   |-- test_docs.py
|   |   |       |   |   |   |-- test_f2cmap.py
|   |   |       |   |   |   |-- test_f2py2e.py
|   |   |       |   |   |   |-- test_isoc.py
|   |   |       |   |   |   |-- test_kind.py
|   |   |       |   |   |   |-- test_mixed.py
|   |   |       |   |   |   |-- test_modules.py
|   |   |       |   |   |   |-- test_parameter.py
|   |   |       |   |   |   |-- test_pyf_src.py
|   |   |       |   |   |   |-- test_quoted_character.py
|   |   |       |   |   |   |-- test_regression.py
|   |   |       |   |   |   |-- test_return_character.py
|   |   |       |   |   |   |-- test_return_complex.py
|   |   |       |   |   |   |-- test_return_integer.py
|   |   |       |   |   |   |-- test_return_logical.py
|   |   |       |   |   |   |-- test_return_real.py
|   |   |       |   |   |   |-- test_routines.py
|   |   |       |   |   |   |-- test_semicolon_split.py
|   |   |       |   |   |   |-- test_size.py
|   |   |       |   |   |   |-- test_string.py
|   |   |       |   |   |   |-- test_symbolic.py
|   |   |       |   |   |   |-- test_value_attrspec.py
|   |   |       |   |   |   +-- util.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- __main__.py
|   |   |       |   |   |-- __version__.py
|   |   |       |   |   |-- __version__.pyi
|   |   |       |   |   |-- _isocbind.py
|   |   |       |   |   |-- _isocbind.pyi
|   |   |       |   |   |-- _src_pyf.py
|   |   |       |   |   |-- _src_pyf.pyi
|   |   |       |   |   |-- auxfuncs.py
|   |   |       |   |   |-- auxfuncs.pyi
|   |   |       |   |   |-- capi_maps.py
|   |   |       |   |   |-- capi_maps.pyi
|   |   |       |   |   |-- cb_rules.py
|   |   |       |   |   |-- cb_rules.pyi
|   |   |       |   |   |-- cfuncs.py
|   |   |       |   |   |-- cfuncs.pyi
|   |   |       |   |   |-- common_rules.py
|   |   |       |   |   |-- common_rules.pyi
|   |   |       |   |   |-- crackfortran.py
|   |   |       |   |   |-- crackfortran.pyi
|   |   |       |   |   |-- diagnose.py
|   |   |       |   |   |-- diagnose.pyi
|   |   |       |   |   |-- f2py2e.py
|   |   |       |   |   |-- f2py2e.pyi
|   |   |       |   |   |-- f90mod_rules.py
|   |   |       |   |   |-- f90mod_rules.pyi
|   |   |       |   |   |-- func2subr.py
|   |   |       |   |   |-- func2subr.pyi
|   |   |       |   |   |-- rules.py
|   |   |       |   |   |-- rules.pyi
|   |   |       |   |   |-- setup.cfg
|   |   |       |   |   |-- symbolic.py
|   |   |       |   |   |-- symbolic.pyi
|   |   |       |   |   |-- use_rules.py
|   |   |       |   |   +-- use_rules.pyi
|   |   |       |   |-- fft
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _helper.cpython-313.pyc
|   |   |       |   |   |   |-- _pocketfft.cpython-313.pyc
|   |   |       |   |   |   +-- helper.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_helper.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_pocketfft.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_helper.py
|   |   |       |   |   |   +-- test_pocketfft.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _helper.py
|   |   |       |   |   |-- _helper.pyi
|   |   |       |   |   |-- _pocketfft.py
|   |   |       |   |   |-- _pocketfft.pyi
|   |   |       |   |   |-- _pocketfft_umath.cp313-win_amd64.lib
|   |   |       |   |   |-- _pocketfft_umath.cp313-win_amd64.pyd
|   |   |       |   |   |-- helper.py
|   |   |       |   |   +-- helper.pyi
|   |   |       |   |-- lib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _array_utils_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _arraypad_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _arraysetops_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _arrayterator_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _datasource.cpython-313.pyc
|   |   |       |   |   |   |-- _format_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _function_base_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _histograms_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _index_tricks_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _iotools.cpython-313.pyc
|   |   |       |   |   |   |-- _nanfunctions_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _npyio_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _polynomial_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _scimath_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _shape_base_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _stride_tricks_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _twodim_base_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _type_check_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _ufunclike_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _user_array_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _utils_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _version.cpython-313.pyc
|   |   |       |   |   |   |-- array_utils.cpython-313.pyc
|   |   |       |   |   |   |-- format.cpython-313.pyc
|   |   |       |   |   |   |-- introspect.cpython-313.pyc
|   |   |       |   |   |   |-- mixins.cpython-313.pyc
|   |   |       |   |   |   |-- npyio.cpython-313.pyc
|   |   |       |   |   |   |-- recfunctions.cpython-313.pyc
|   |   |       |   |   |   |-- scimath.cpython-313.pyc
|   |   |       |   |   |   |-- stride_tricks.cpython-313.pyc
|   |   |       |   |   |   +-- user_array.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__datasource.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__iotools.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__version.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arraypad.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arraysetops.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arrayterator.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_format.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_function_base.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_histograms.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_index_tricks.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_io.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_loadtxt.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mixins.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_nanfunctions.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_packbits.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_polynomial.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_recfunctions.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_shape_base.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_stride_tricks.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_twodim_base.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_type_check.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ufunclike.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_utils.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- py2-np0-objarr.npy
|   |   |       |   |   |   |   |-- py2-objarr.npy
|   |   |       |   |   |   |   |-- py2-objarr.npz
|   |   |       |   |   |   |   |-- py3-objarr.npy
|   |   |       |   |   |   |   |-- py3-objarr.npz
|   |   |       |   |   |   |   |-- python3.npy
|   |   |       |   |   |   |   +-- win64python2.npy
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test__datasource.py
|   |   |       |   |   |   |-- test__iotools.py
|   |   |       |   |   |   |-- test__version.py
|   |   |       |   |   |   |-- test_array_utils.py
|   |   |       |   |   |   |-- test_arraypad.py
|   |   |       |   |   |   |-- test_arraysetops.py
|   |   |       |   |   |   |-- test_arrayterator.py
|   |   |       |   |   |   |-- test_format.py
|   |   |       |   |   |   |-- test_function_base.py
|   |   |       |   |   |   |-- test_histograms.py
|   |   |       |   |   |   |-- test_index_tricks.py
|   |   |       |   |   |   |-- test_io.py
|   |   |       |   |   |   |-- test_loadtxt.py
|   |   |       |   |   |   |-- test_mixins.py
|   |   |       |   |   |   |-- test_nanfunctions.py
|   |   |       |   |   |   |-- test_packbits.py
|   |   |       |   |   |   |-- test_polynomial.py
|   |   |       |   |   |   |-- test_recfunctions.py
|   |   |       |   |   |   |-- test_regression.py
|   |   |       |   |   |   |-- test_shape_base.py
|   |   |       |   |   |   |-- test_stride_tricks.py
|   |   |       |   |   |   |-- test_twodim_base.py
|   |   |       |   |   |   |-- test_type_check.py
|   |   |       |   |   |   |-- test_ufunclike.py
|   |   |       |   |   |   +-- test_utils.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _array_utils_impl.py
|   |   |       |   |   |-- _array_utils_impl.pyi
|   |   |       |   |   |-- _arraypad_impl.py
|   |   |       |   |   |-- _arraypad_impl.pyi
|   |   |       |   |   |-- _arraysetops_impl.py
|   |   |       |   |   |-- _arraysetops_impl.pyi
|   |   |       |   |   |-- _arrayterator_impl.py
|   |   |       |   |   |-- _arrayterator_impl.pyi
|   |   |       |   |   |-- _datasource.py
|   |   |       |   |   |-- _datasource.pyi
|   |   |       |   |   |-- _format_impl.py
|   |   |       |   |   |-- _format_impl.pyi
|   |   |       |   |   |-- _function_base_impl.py
|   |   |       |   |   |-- _function_base_impl.pyi
|   |   |       |   |   |-- _histograms_impl.py
|   |   |       |   |   |-- _histograms_impl.pyi
|   |   |       |   |   |-- _index_tricks_impl.py
|   |   |       |   |   |-- _index_tricks_impl.pyi
|   |   |       |   |   |-- _iotools.py
|   |   |       |   |   |-- _iotools.pyi
|   |   |       |   |   |-- _nanfunctions_impl.py
|   |   |       |   |   |-- _nanfunctions_impl.pyi
|   |   |       |   |   |-- _npyio_impl.py
|   |   |       |   |   |-- _npyio_impl.pyi
|   |   |       |   |   |-- _polynomial_impl.py
|   |   |       |   |   |-- _polynomial_impl.pyi
|   |   |       |   |   |-- _scimath_impl.py
|   |   |       |   |   |-- _scimath_impl.pyi
|   |   |       |   |   |-- _shape_base_impl.py
|   |   |       |   |   |-- _shape_base_impl.pyi
|   |   |       |   |   |-- _stride_tricks_impl.py
|   |   |       |   |   |-- _stride_tricks_impl.pyi
|   |   |       |   |   |-- _twodim_base_impl.py
|   |   |       |   |   |-- _twodim_base_impl.pyi
|   |   |       |   |   |-- _type_check_impl.py
|   |   |       |   |   |-- _type_check_impl.pyi
|   |   |       |   |   |-- _ufunclike_impl.py
|   |   |       |   |   |-- _ufunclike_impl.pyi
|   |   |       |   |   |-- _user_array_impl.py
|   |   |       |   |   |-- _user_array_impl.pyi
|   |   |       |   |   |-- _utils_impl.py
|   |   |       |   |   |-- _utils_impl.pyi
|   |   |       |   |   |-- _version.py
|   |   |       |   |   |-- _version.pyi
|   |   |       |   |   |-- array_utils.py
|   |   |       |   |   |-- array_utils.pyi
|   |   |       |   |   |-- format.py
|   |   |       |   |   |-- format.pyi
|   |   |       |   |   |-- introspect.py
|   |   |       |   |   |-- introspect.pyi
|   |   |       |   |   |-- mixins.py
|   |   |       |   |   |-- mixins.pyi
|   |   |       |   |   |-- npyio.py
|   |   |       |   |   |-- npyio.pyi
|   |   |       |   |   |-- recfunctions.py
|   |   |       |   |   |-- recfunctions.pyi
|   |   |       |   |   |-- scimath.py
|   |   |       |   |   |-- scimath.pyi
|   |   |       |   |   |-- stride_tricks.py
|   |   |       |   |   |-- stride_tricks.pyi
|   |   |       |   |   |-- user_array.py
|   |   |       |   |   +-- user_array.pyi
|   |   |       |   |-- linalg
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _linalg.cpython-313.pyc
|   |   |       |   |   |   +-- linalg.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_deprecations.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_linalg.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_deprecations.py
|   |   |       |   |   |   |-- test_linalg.py
|   |   |       |   |   |   +-- test_regression.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _linalg.py
|   |   |       |   |   |-- _linalg.pyi
|   |   |       |   |   |-- _umath_linalg.cp313-win_amd64.lib
|   |   |       |   |   |-- _umath_linalg.cp313-win_amd64.pyd
|   |   |       |   |   |-- _umath_linalg.pyi
|   |   |       |   |   |-- lapack_lite.cp313-win_amd64.lib
|   |   |       |   |   |-- lapack_lite.cp313-win_amd64.pyd
|   |   |       |   |   |-- lapack_lite.pyi
|   |   |       |   |   |-- linalg.py
|   |   |       |   |   +-- linalg.pyi
|   |   |       |   |-- ma
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- core.cpython-313.pyc
|   |   |       |   |   |   |-- extras.cpython-313.pyc
|   |   |       |   |   |   |-- mrecords.cpython-313.pyc
|   |   |       |   |   |   +-- testutils.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arrayobject.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_core.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_deprecations.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_extras.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mrecords.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_old_ma.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_subclassing.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_arrayobject.py
|   |   |       |   |   |   |-- test_core.py
|   |   |       |   |   |   |-- test_deprecations.py
|   |   |       |   |   |   |-- test_extras.py
|   |   |       |   |   |   |-- test_mrecords.py
|   |   |       |   |   |   |-- test_old_ma.py
|   |   |       |   |   |   |-- test_regression.py
|   |   |       |   |   |   +-- test_subclassing.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- API_CHANGES.txt
|   |   |       |   |   |-- core.py
|   |   |       |   |   |-- core.pyi
|   |   |       |   |   |-- extras.py
|   |   |       |   |   |-- extras.pyi
|   |   |       |   |   |-- LICENSE
|   |   |       |   |   |-- mrecords.py
|   |   |       |   |   |-- mrecords.pyi
|   |   |       |   |   |-- README.rst
|   |   |       |   |   +-- testutils.py
|   |   |       |   |-- matrixlib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- defmatrix.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_defmatrix.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_interaction.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_masked_matrix.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_matrix_linalg.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_multiarray.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_numeric.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_defmatrix.py
|   |   |       |   |   |   |-- test_interaction.py
|   |   |       |   |   |   |-- test_masked_matrix.py
|   |   |       |   |   |   |-- test_matrix_linalg.py
|   |   |       |   |   |   |-- test_multiarray.py
|   |   |       |   |   |   |-- test_numeric.py
|   |   |       |   |   |   +-- test_regression.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- defmatrix.py
|   |   |       |   |   +-- defmatrix.pyi
|   |   |       |   |-- polynomial
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _polybase.cpython-313.pyc
|   |   |       |   |   |   |-- chebyshev.cpython-313.pyc
|   |   |       |   |   |   |-- hermite.cpython-313.pyc
|   |   |       |   |   |   |-- hermite_e.cpython-313.pyc
|   |   |       |   |   |   |-- laguerre.cpython-313.pyc
|   |   |       |   |   |   |-- legendre.cpython-313.pyc
|   |   |       |   |   |   |-- polynomial.cpython-313.pyc
|   |   |       |   |   |   +-- polyutils.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_chebyshev.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_classes.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hermite.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hermite_e.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_laguerre.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_legendre.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_polynomial.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_polyutils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_printing.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_symbol.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_chebyshev.py
|   |   |       |   |   |   |-- test_classes.py
|   |   |       |   |   |   |-- test_hermite.py
|   |   |       |   |   |   |-- test_hermite_e.py
|   |   |       |   |   |   |-- test_laguerre.py
|   |   |       |   |   |   |-- test_legendre.py
|   |   |       |   |   |   |-- test_polynomial.py
|   |   |       |   |   |   |-- test_polyutils.py
|   |   |       |   |   |   |-- test_printing.py
|   |   |       |   |   |   +-- test_symbol.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _polybase.py
|   |   |       |   |   |-- _polybase.pyi
|   |   |       |   |   |-- _polytypes.pyi
|   |   |       |   |   |-- chebyshev.py
|   |   |       |   |   |-- chebyshev.pyi
|   |   |       |   |   |-- hermite.py
|   |   |       |   |   |-- hermite.pyi
|   |   |       |   |   |-- hermite_e.py
|   |   |       |   |   |-- hermite_e.pyi
|   |   |       |   |   |-- laguerre.py
|   |   |       |   |   |-- laguerre.pyi
|   |   |       |   |   |-- legendre.py
|   |   |       |   |   |-- legendre.pyi
|   |   |       |   |   |-- polynomial.py
|   |   |       |   |   |-- polynomial.pyi
|   |   |       |   |   |-- polyutils.py
|   |   |       |   |   +-- polyutils.pyi
|   |   |       |   |-- random
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- _pickle.cpython-313.pyc
|   |   |       |   |   |-- _examples
|   |   |       |   |   |   |-- cffi
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- extending.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- parse.cpython-313.pyc
|   |   |       |   |   |   |   |-- extending.py
|   |   |       |   |   |   |   +-- parse.py
|   |   |       |   |   |   |-- cython
|   |   |       |   |   |   |   |-- extending.pyx
|   |   |       |   |   |   |   |-- extending_distributions.pyx
|   |   |       |   |   |   |   +-- meson.build
|   |   |       |   |   |   +-- numba
|   |   |       |   |   |       |-- __pycache__
|   |   |       |   |   |       |   |-- extending.cpython-313.pyc
|   |   |       |   |   |       |   +-- extending_distributions.cpython-313.pyc
|   |   |       |   |   |       |-- extending.py
|   |   |       |   |   |       +-- extending_distributions.py
|   |   |       |   |   |-- lib
|   |   |       |   |   |   +-- npyrandom.lib
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_direct.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_extending.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_generator_mt19937.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_generator_mt19937_regressions.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_random.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_randomstate.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_randomstate_regression.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_seed_sequence.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_smoke.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- generator_pcg64_np121.pkl.gz
|   |   |       |   |   |   |   |-- generator_pcg64_np126.pkl.gz
|   |   |       |   |   |   |   |-- mt19937-testset-1.csv
|   |   |       |   |   |   |   |-- mt19937-testset-2.csv
|   |   |       |   |   |   |   |-- pcg64dxsm-testset-1.csv
|   |   |       |   |   |   |   |-- pcg64dxsm-testset-2.csv
|   |   |       |   |   |   |   |-- pcg64-testset-1.csv
|   |   |       |   |   |   |   |-- pcg64-testset-2.csv
|   |   |       |   |   |   |   |-- philox-testset-1.csv
|   |   |       |   |   |   |   |-- philox-testset-2.csv
|   |   |       |   |   |   |   |-- sfc64_np126.pkl.gz
|   |   |       |   |   |   |   |-- sfc64-testset-1.csv
|   |   |       |   |   |   |   +-- sfc64-testset-2.csv
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_direct.py
|   |   |       |   |   |   |-- test_extending.py
|   |   |       |   |   |   |-- test_generator_mt19937.py
|   |   |       |   |   |   |-- test_generator_mt19937_regressions.py
|   |   |       |   |   |   |-- test_random.py
|   |   |       |   |   |   |-- test_randomstate.py
|   |   |       |   |   |   |-- test_randomstate_regression.py
|   |   |       |   |   |   |-- test_regression.py
|   |   |       |   |   |   |-- test_seed_sequence.py
|   |   |       |   |   |   +-- test_smoke.py
|   |   |       |   |   |-- __init__.pxd
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- _bounded_integers.cp313-win_amd64.lib
|   |   |       |   |   |-- _bounded_integers.cp313-win_amd64.pyd
|   |   |       |   |   |-- _bounded_integers.pxd
|   |   |       |   |   |-- _bounded_integers.pyi
|   |   |       |   |   |-- _common.cp313-win_amd64.lib
|   |   |       |   |   |-- _common.cp313-win_amd64.pyd
|   |   |       |   |   |-- _common.pxd
|   |   |       |   |   |-- _common.pyi
|   |   |       |   |   |-- _generator.cp313-win_amd64.lib
|   |   |       |   |   |-- _generator.cp313-win_amd64.pyd
|   |   |       |   |   |-- _generator.pyi
|   |   |       |   |   |-- _mt19937.cp313-win_amd64.lib
|   |   |       |   |   |-- _mt19937.cp313-win_amd64.pyd
|   |   |       |   |   |-- _mt19937.pyi
|   |   |       |   |   |-- _pcg64.cp313-win_amd64.lib
|   |   |       |   |   |-- _pcg64.cp313-win_amd64.pyd
|   |   |       |   |   |-- _pcg64.pyi
|   |   |       |   |   |-- _philox.cp313-win_amd64.lib
|   |   |       |   |   |-- _philox.cp313-win_amd64.pyd
|   |   |       |   |   |-- _philox.pyi
|   |   |       |   |   |-- _pickle.py
|   |   |       |   |   |-- _pickle.pyi
|   |   |       |   |   |-- _sfc64.cp313-win_amd64.lib
|   |   |       |   |   |-- _sfc64.cp313-win_amd64.pyd
|   |   |       |   |   |-- _sfc64.pyi
|   |   |       |   |   |-- bit_generator.cp313-win_amd64.lib
|   |   |       |   |   |-- bit_generator.cp313-win_amd64.pyd
|   |   |       |   |   |-- bit_generator.pxd
|   |   |       |   |   |-- bit_generator.pyi
|   |   |       |   |   |-- c_distributions.pxd
|   |   |       |   |   |-- LICENSE.md
|   |   |       |   |   |-- mtrand.cp313-win_amd64.lib
|   |   |       |   |   |-- mtrand.cp313-win_amd64.pyd
|   |   |       |   |   +-- mtrand.pyi
|   |   |       |   |-- rec
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- __init__.pyi
|   |   |       |   |-- strings
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- __init__.pyi
|   |   |       |   |-- testing
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- overrides.cpython-313.pyc
|   |   |       |   |   |   +-- print_coercion_tables.cpython-313.pyc
|   |   |       |   |   |-- _private
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- extbuild.cpython-313.pyc
|   |   |       |   |   |   |   +-- utils.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __init__.pyi
|   |   |       |   |   |   |-- extbuild.py
|   |   |       |   |   |   |-- extbuild.pyi
|   |   |       |   |   |   |-- utils.py
|   |   |       |   |   |   +-- utils.pyi
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_utils.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   +-- test_utils.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __init__.pyi
|   |   |       |   |   |-- overrides.py
|   |   |       |   |   |-- overrides.pyi
|   |   |       |   |   |-- print_coercion_tables.py
|   |   |       |   |   +-- print_coercion_tables.pyi
|   |   |       |   |-- tests
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- test__all__.cpython-313.pyc
|   |   |       |   |   |   |-- test_configtool.cpython-313.pyc
|   |   |       |   |   |   |-- test_ctypeslib.cpython-313.pyc
|   |   |       |   |   |   |-- test_lazyloading.cpython-313.pyc
|   |   |       |   |   |   |-- test_matlib.cpython-313.pyc
|   |   |       |   |   |   |-- test_numpy_config.cpython-313.pyc
|   |   |       |   |   |   |-- test_numpy_version.cpython-313.pyc
|   |   |       |   |   |   |-- test_public_api.cpython-313.pyc
|   |   |       |   |   |   |-- test_reloading.cpython-313.pyc
|   |   |       |   |   |   |-- test_scripts.cpython-313.pyc
|   |   |       |   |   |   +-- test_warnings.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- test__all__.py
|   |   |       |   |   |-- test_configtool.py
|   |   |       |   |   |-- test_ctypeslib.py
|   |   |       |   |   |-- test_lazyloading.py
|   |   |       |   |   |-- test_matlib.py
|   |   |       |   |   |-- test_numpy_config.py
|   |   |       |   |   |-- test_numpy_version.py
|   |   |       |   |   |-- test_public_api.py
|   |   |       |   |   |-- test_reloading.py
|   |   |       |   |   |-- test_scripts.py
|   |   |       |   |   +-- test_warnings.py
|   |   |       |   |-- typing
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- mypy_plugin.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_isfile.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_runtime.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_typing.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- fail
|   |   |       |   |   |   |   |   |-- arithmetic.pyi
|   |   |       |   |   |   |   |   |-- array_constructors.pyi
|   |   |       |   |   |   |   |   |-- array_like.pyi
|   |   |       |   |   |   |   |   |-- array_pad.pyi
|   |   |       |   |   |   |   |   |-- arrayprint.pyi
|   |   |       |   |   |   |   |   |-- arrayterator.pyi
|   |   |       |   |   |   |   |   |-- bitwise_ops.pyi
|   |   |       |   |   |   |   |   |-- char.pyi
|   |   |       |   |   |   |   |   |-- chararray.pyi
|   |   |       |   |   |   |   |   |-- comparisons.pyi
|   |   |       |   |   |   |   |   |-- constants.pyi
|   |   |       |   |   |   |   |   |-- datasource.pyi
|   |   |       |   |   |   |   |   |-- dtype.pyi
|   |   |       |   |   |   |   |   |-- einsumfunc.pyi
|   |   |       |   |   |   |   |   |-- flatiter.pyi
|   |   |       |   |   |   |   |   |-- fromnumeric.pyi
|   |   |       |   |   |   |   |   |-- histograms.pyi
|   |   |       |   |   |   |   |   |-- index_tricks.pyi
|   |   |       |   |   |   |   |   |-- lib_function_base.pyi
|   |   |       |   |   |   |   |   |-- lib_polynomial.pyi
|   |   |       |   |   |   |   |   |-- lib_utils.pyi
|   |   |       |   |   |   |   |   |-- lib_version.pyi
|   |   |       |   |   |   |   |   |-- linalg.pyi
|   |   |       |   |   |   |   |   |-- ma.pyi
|   |   |       |   |   |   |   |   |-- memmap.pyi
|   |   |       |   |   |   |   |   |-- modules.pyi
|   |   |       |   |   |   |   |   |-- multiarray.pyi
|   |   |       |   |   |   |   |   |-- ndarray.pyi
|   |   |       |   |   |   |   |   |-- ndarray_misc.pyi
|   |   |       |   |   |   |   |   |-- nditer.pyi
|   |   |       |   |   |   |   |   |-- nested_sequence.pyi
|   |   |       |   |   |   |   |   |-- npyio.pyi
|   |   |       |   |   |   |   |   |-- numerictypes.pyi
|   |   |       |   |   |   |   |   |-- random.pyi
|   |   |       |   |   |   |   |   |-- rec.pyi
|   |   |       |   |   |   |   |   |-- scalars.pyi
|   |   |       |   |   |   |   |   |-- shape.pyi
|   |   |       |   |   |   |   |   |-- shape_base.pyi
|   |   |       |   |   |   |   |   |-- stride_tricks.pyi
|   |   |       |   |   |   |   |   |-- strings.pyi
|   |   |       |   |   |   |   |   |-- testing.pyi
|   |   |       |   |   |   |   |   |-- twodim_base.pyi
|   |   |       |   |   |   |   |   |-- type_check.pyi
|   |   |       |   |   |   |   |   |-- ufunc_config.pyi
|   |   |       |   |   |   |   |   |-- ufunclike.pyi
|   |   |       |   |   |   |   |   |-- ufuncs.pyi
|   |   |       |   |   |   |   |   +-- warnings_and_errors.pyi
|   |   |       |   |   |   |   |-- misc
|   |   |       |   |   |   |   |   +-- extended_precision.pyi
|   |   |       |   |   |   |   |-- pass
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- arithmetic.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- array_constructors.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- array_like.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- arrayprint.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- arrayterator.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- bitwise_ops.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- comparisons.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- dtype.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- einsumfunc.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- flatiter.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- fromnumeric.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- index_tricks.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- lib_user_array.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- lib_utils.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- lib_version.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- literal.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- ma.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- mod.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- modules.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- multiarray.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- ndarray_conversion.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- ndarray_misc.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- ndarray_shape_manipulation.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- nditer.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- numeric.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- numerictypes.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- random.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- recfunctions.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- scalars.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- shape.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- simple.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- simple_py3.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- ufunc_config.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- ufunclike.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- ufuncs.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- warnings_and_errors.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- arithmetic.py
|   |   |       |   |   |   |   |   |-- array_constructors.py
|   |   |       |   |   |   |   |   |-- array_like.py
|   |   |       |   |   |   |   |   |-- arrayprint.py
|   |   |       |   |   |   |   |   |-- arrayterator.py
|   |   |       |   |   |   |   |   |-- bitwise_ops.py
|   |   |       |   |   |   |   |   |-- comparisons.py
|   |   |       |   |   |   |   |   |-- dtype.py
|   |   |       |   |   |   |   |   |-- einsumfunc.py
|   |   |       |   |   |   |   |   |-- flatiter.py
|   |   |       |   |   |   |   |   |-- fromnumeric.py
|   |   |       |   |   |   |   |   |-- index_tricks.py
|   |   |       |   |   |   |   |   |-- lib_user_array.py
|   |   |       |   |   |   |   |   |-- lib_utils.py
|   |   |       |   |   |   |   |   |-- lib_version.py
|   |   |       |   |   |   |   |   |-- literal.py
|   |   |       |   |   |   |   |   |-- ma.py
|   |   |       |   |   |   |   |   |-- mod.py
|   |   |       |   |   |   |   |   |-- modules.py
|   |   |       |   |   |   |   |   |-- multiarray.py
|   |   |       |   |   |   |   |   |-- ndarray_conversion.py
|   |   |       |   |   |   |   |   |-- ndarray_misc.py
|   |   |       |   |   |   |   |   |-- ndarray_shape_manipulation.py
|   |   |       |   |   |   |   |   |-- nditer.py
|   |   |       |   |   |   |   |   |-- numeric.py
|   |   |       |   |   |   |   |   |-- numerictypes.py
|   |   |       |   |   |   |   |   |-- random.py
|   |   |       |   |   |   |   |   |-- recfunctions.py
|   |   |       |   |   |   |   |   |-- scalars.py
|   |   |       |   |   |   |   |   |-- shape.py
|   |   |       |   |   |   |   |   |-- simple.py
|   |   |       |   |   |   |   |   |-- simple_py3.py
|   |   |       |   |   |   |   |   |-- ufunc_config.py
|   |   |       |   |   |   |   |   |-- ufunclike.py
|   |   |       |   |   |   |   |   |-- ufuncs.py
|   |   |       |   |   |   |   |   +-- warnings_and_errors.py
|   |   |       |   |   |   |   |-- reveal
|   |   |       |   |   |   |   |   |-- arithmetic.pyi
|   |   |       |   |   |   |   |   |-- array_api_info.pyi
|   |   |       |   |   |   |   |   |-- array_constructors.pyi
|   |   |       |   |   |   |   |   |-- arraypad.pyi
|   |   |       |   |   |   |   |   |-- arrayprint.pyi
|   |   |       |   |   |   |   |   |-- arraysetops.pyi
|   |   |       |   |   |   |   |   |-- arrayterator.pyi
|   |   |       |   |   |   |   |   |-- bitwise_ops.pyi
|   |   |       |   |   |   |   |   |-- char.pyi
|   |   |       |   |   |   |   |   |-- chararray.pyi
|   |   |       |   |   |   |   |   |-- comparisons.pyi
|   |   |       |   |   |   |   |   |-- constants.pyi
|   |   |       |   |   |   |   |   |-- ctypeslib.pyi
|   |   |       |   |   |   |   |   |-- datasource.pyi
|   |   |       |   |   |   |   |   |-- dtype.pyi
|   |   |       |   |   |   |   |   |-- einsumfunc.pyi
|   |   |       |   |   |   |   |   |-- emath.pyi
|   |   |       |   |   |   |   |   |-- fft.pyi
|   |   |       |   |   |   |   |   |-- flatiter.pyi
|   |   |       |   |   |   |   |   |-- fromnumeric.pyi
|   |   |       |   |   |   |   |   |-- getlimits.pyi
|   |   |       |   |   |   |   |   |-- histograms.pyi
|   |   |       |   |   |   |   |   |-- index_tricks.pyi
|   |   |       |   |   |   |   |   |-- lib_function_base.pyi
|   |   |       |   |   |   |   |   |-- lib_polynomial.pyi
|   |   |       |   |   |   |   |   |-- lib_utils.pyi
|   |   |       |   |   |   |   |   |-- lib_version.pyi
|   |   |       |   |   |   |   |   |-- linalg.pyi
|   |   |       |   |   |   |   |   |-- ma.pyi
|   |   |       |   |   |   |   |   |-- matrix.pyi
|   |   |       |   |   |   |   |   |-- memmap.pyi
|   |   |       |   |   |   |   |   |-- mod.pyi
|   |   |       |   |   |   |   |   |-- modules.pyi
|   |   |       |   |   |   |   |   |-- multiarray.pyi
|   |   |       |   |   |   |   |   |-- nbit_base_example.pyi
|   |   |       |   |   |   |   |   |-- ndarray_assignability.pyi
|   |   |       |   |   |   |   |   |-- ndarray_conversion.pyi
|   |   |       |   |   |   |   |   |-- ndarray_misc.pyi
|   |   |       |   |   |   |   |   |-- ndarray_shape_manipulation.pyi
|   |   |       |   |   |   |   |   |-- nditer.pyi
|   |   |       |   |   |   |   |   |-- nested_sequence.pyi
|   |   |       |   |   |   |   |   |-- npyio.pyi
|   |   |       |   |   |   |   |   |-- numeric.pyi
|   |   |       |   |   |   |   |   |-- numerictypes.pyi
|   |   |       |   |   |   |   |   |-- polynomial_polybase.pyi
|   |   |       |   |   |   |   |   |-- polynomial_polyutils.pyi
|   |   |       |   |   |   |   |   |-- polynomial_series.pyi
|   |   |       |   |   |   |   |   |-- random.pyi
|   |   |       |   |   |   |   |   |-- rec.pyi
|   |   |       |   |   |   |   |   |-- scalars.pyi
|   |   |       |   |   |   |   |   |-- shape.pyi
|   |   |       |   |   |   |   |   |-- shape_base.pyi
|   |   |       |   |   |   |   |   |-- stride_tricks.pyi
|   |   |       |   |   |   |   |   |-- strings.pyi
|   |   |       |   |   |   |   |   |-- testing.pyi
|   |   |       |   |   |   |   |   |-- twodim_base.pyi
|   |   |       |   |   |   |   |   |-- type_check.pyi
|   |   |       |   |   |   |   |   |-- ufunc_config.pyi
|   |   |       |   |   |   |   |   |-- ufunclike.pyi
|   |   |       |   |   |   |   |   |-- ufuncs.pyi
|   |   |       |   |   |   |   |   +-- warnings_and_errors.pyi
|   |   |       |   |   |   |   +-- mypy.ini
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_isfile.py
|   |   |       |   |   |   |-- test_runtime.py
|   |   |       |   |   |   +-- test_typing.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- mypy_plugin.py
|   |   |       |   |-- __config__.py
|   |   |       |   |-- __config__.pyi
|   |   |       |   |-- __init__.cython-30.pxd
|   |   |       |   |-- __init__.pxd
|   |   |       |   |-- __init__.py
|   |   |       |   |-- __init__.pyi
|   |   |       |   |-- _array_api_info.py
|   |   |       |   |-- _array_api_info.pyi
|   |   |       |   |-- _configtool.py
|   |   |       |   |-- _configtool.pyi
|   |   |       |   |-- _distributor_init.py
|   |   |       |   |-- _distributor_init.pyi
|   |   |       |   |-- _expired_attrs_2_0.py
|   |   |       |   |-- _expired_attrs_2_0.pyi
|   |   |       |   |-- _globals.py
|   |   |       |   |-- _globals.pyi
|   |   |       |   |-- _pytesttester.py
|   |   |       |   |-- _pytesttester.pyi
|   |   |       |   |-- conftest.py
|   |   |       |   |-- dtypes.py
|   |   |       |   |-- dtypes.pyi
|   |   |       |   |-- exceptions.py
|   |   |       |   |-- exceptions.pyi
|   |   |       |   |-- matlib.py
|   |   |       |   |-- matlib.pyi
|   |   |       |   |-- py.typed
|   |   |       |   |-- version.py
|   |   |       |   +-- version.pyi
|   |   |       |-- numpy.libs
|   |   |       |   |-- libscipy_openblas64_-860d95b1c38e637ce4509f5fa24fbf2a.dll
|   |   |       |   +-- msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
|   |   |       |-- numpy-2.3.4.dist-info
|   |   |       |   |-- DELVEWHEEL
|   |   |       |   |-- entry_points.txt
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- LICENSE.txt
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- REQUESTED
|   |   |       |   +-- WHEEL
|   |   |       |-- packaging
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- _elffile.cpython-313.pyc
|   |   |       |   |   |-- _manylinux.cpython-313.pyc
|   |   |       |   |   |-- _musllinux.cpython-313.pyc
|   |   |       |   |   |-- _parser.cpython-313.pyc
|   |   |       |   |   |-- _structures.cpython-313.pyc
|   |   |       |   |   |-- _tokenizer.cpython-313.pyc
|   |   |       |   |   |-- markers.cpython-313.pyc
|   |   |       |   |   |-- metadata.cpython-313.pyc
|   |   |       |   |   |-- requirements.cpython-313.pyc
|   |   |       |   |   |-- specifiers.cpython-313.pyc
|   |   |       |   |   |-- tags.cpython-313.pyc
|   |   |       |   |   |-- utils.cpython-313.pyc
|   |   |       |   |   +-- version.cpython-313.pyc
|   |   |       |   |-- licenses
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- _spdx.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- _spdx.py
|   |   |       |   |-- __init__.py
|   |   |       |   |-- _elffile.py
|   |   |       |   |-- _manylinux.py
|   |   |       |   |-- _musllinux.py
|   |   |       |   |-- _parser.py
|   |   |       |   |-- _structures.py
|   |   |       |   |-- _tokenizer.py
|   |   |       |   |-- markers.py
|   |   |       |   |-- metadata.py
|   |   |       |   |-- py.typed
|   |   |       |   |-- requirements.py
|   |   |       |   |-- specifiers.py
|   |   |       |   |-- tags.py
|   |   |       |   |-- utils.py
|   |   |       |   +-- version.py
|   |   |       |-- packaging-25.0.dist-info
|   |   |       |   |-- licenses
|   |   |       |   |   |-- LICENSE
|   |   |       |   |   |-- LICENSE.APACHE
|   |   |       |   |   +-- LICENSE.BSD
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   +-- WHEEL
|   |   |       |-- PIL
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |-- _binary.cpython-313.pyc
|   |   |       |   |   |-- _deprecate.cpython-313.pyc
|   |   |       |   |   |-- _tkinter_finder.cpython-313.pyc
|   |   |       |   |   |-- _typing.cpython-313.pyc
|   |   |       |   |   |-- _util.cpython-313.pyc
|   |   |       |   |   |-- _version.cpython-313.pyc
|   |   |       |   |   |-- AvifImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- BdfFontFile.cpython-313.pyc
|   |   |       |   |   |-- BlpImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- BmpImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- BufrStubImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- ContainerIO.cpython-313.pyc
|   |   |       |   |   |-- CurImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- DcxImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- DdsImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- EpsImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- ExifTags.cpython-313.pyc
|   |   |       |   |   |-- features.cpython-313.pyc
|   |   |       |   |   |-- FitsImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- FliImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- FontFile.cpython-313.pyc
|   |   |       |   |   |-- FpxImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- FtexImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- GbrImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- GdImageFile.cpython-313.pyc
|   |   |       |   |   |-- GifImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- GimpGradientFile.cpython-313.pyc
|   |   |       |   |   |-- GimpPaletteFile.cpython-313.pyc
|   |   |       |   |   |-- GribStubImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- Hdf5StubImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- IcnsImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- IcoImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- Image.cpython-313.pyc
|   |   |       |   |   |-- ImageChops.cpython-313.pyc
|   |   |       |   |   |-- ImageCms.cpython-313.pyc
|   |   |       |   |   |-- ImageColor.cpython-313.pyc
|   |   |       |   |   |-- ImageDraw.cpython-313.pyc
|   |   |       |   |   |-- ImageDraw2.cpython-313.pyc
|   |   |       |   |   |-- ImageEnhance.cpython-313.pyc
|   |   |       |   |   |-- ImageFile.cpython-313.pyc
|   |   |       |   |   |-- ImageFilter.cpython-313.pyc
|   |   |       |   |   |-- ImageFont.cpython-313.pyc
|   |   |       |   |   |-- ImageGrab.cpython-313.pyc
|   |   |       |   |   |-- ImageMath.cpython-313.pyc
|   |   |       |   |   |-- ImageMode.cpython-313.pyc
|   |   |       |   |   |-- ImageMorph.cpython-313.pyc
|   |   |       |   |   |-- ImageOps.cpython-313.pyc
|   |   |       |   |   |-- ImagePalette.cpython-313.pyc
|   |   |       |   |   |-- ImagePath.cpython-313.pyc
|   |   |       |   |   |-- ImageQt.cpython-313.pyc
|   |   |       |   |   |-- ImageSequence.cpython-313.pyc
|   |   |       |   |   |-- ImageShow.cpython-313.pyc
|   |   |       |   |   |-- ImageStat.cpython-313.pyc
|   |   |       |   |   |-- ImageText.cpython-313.pyc
|   |   |       |   |   |-- ImageTk.cpython-313.pyc
|   |   |       |   |   |-- ImageTransform.cpython-313.pyc
|   |   |       |   |   |-- ImageWin.cpython-313.pyc
|   |   |       |   |   |-- ImImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- ImtImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- IptcImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- Jpeg2KImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- JpegImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- JpegPresets.cpython-313.pyc
|   |   |       |   |   |-- McIdasImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- MicImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- MpegImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- MpoImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- MspImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PaletteFile.cpython-313.pyc
|   |   |       |   |   |-- PalmImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PcdImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PcfFontFile.cpython-313.pyc
|   |   |       |   |   |-- PcxImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PdfImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PdfParser.cpython-313.pyc
|   |   |       |   |   |-- PixarImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PngImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PpmImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PsdImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- PSDraw.cpython-313.pyc
|   |   |       |   |   |-- QoiImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- report.cpython-313.pyc
|   |   |       |   |   |-- SgiImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- SpiderImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- SunImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- TarIO.cpython-313.pyc
|   |   |       |   |   |-- TgaImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- TiffImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- TiffTags.cpython-313.pyc
|   |   |       |   |   |-- WalImageFile.cpython-313.pyc
|   |   |       |   |   |-- WebPImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- WmfImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- XbmImagePlugin.cpython-313.pyc
|   |   |       |   |   |-- XpmImagePlugin.cpython-313.pyc
|   |   |       |   |   +-- XVThumbImagePlugin.cpython-313.pyc
|   |   |       |   |-- __init__.py
|   |   |       |   |-- __main__.py
|   |   |       |   |-- _avif.cp313-win_amd64.pyd
|   |   |       |   |-- _avif.pyi
|   |   |       |   |-- _binary.py
|   |   |       |   |-- _deprecate.py
|   |   |       |   |-- _imaging.cp313-win_amd64.pyd
|   |   |       |   |-- _imaging.pyi
|   |   |       |   |-- _imagingcms.cp313-win_amd64.pyd
|   |   |       |   |-- _imagingcms.pyi
|   |   |       |   |-- _imagingft.cp313-win_amd64.pyd
|   |   |       |   |-- _imagingft.pyi
|   |   |       |   |-- _imagingmath.cp313-win_amd64.pyd
|   |   |       |   |-- _imagingmath.pyi
|   |   |       |   |-- _imagingmorph.cp313-win_amd64.pyd
|   |   |       |   |-- _imagingmorph.pyi
|   |   |       |   |-- _imagingtk.cp313-win_amd64.pyd
|   |   |       |   |-- _imagingtk.pyi
|   |   |       |   |-- _tkinter_finder.py
|   |   |       |   |-- _typing.py
|   |   |       |   |-- _util.py
|   |   |       |   |-- _version.py
|   |   |       |   |-- _webp.cp313-win_amd64.pyd
|   |   |       |   |-- _webp.pyi
|   |   |       |   |-- AvifImagePlugin.py
|   |   |       |   |-- BdfFontFile.py
|   |   |       |   |-- BlpImagePlugin.py
|   |   |       |   |-- BmpImagePlugin.py
|   |   |       |   |-- BufrStubImagePlugin.py
|   |   |       |   |-- ContainerIO.py
|   |   |       |   |-- CurImagePlugin.py
|   |   |       |   |-- DcxImagePlugin.py
|   |   |       |   |-- DdsImagePlugin.py
|   |   |       |   |-- EpsImagePlugin.py
|   |   |       |   |-- ExifTags.py
|   |   |       |   |-- features.py
|   |   |       |   |-- FitsImagePlugin.py
|   |   |       |   |-- FliImagePlugin.py
|   |   |       |   |-- FontFile.py
|   |   |       |   |-- FpxImagePlugin.py
|   |   |       |   |-- FtexImagePlugin.py
|   |   |       |   |-- GbrImagePlugin.py
|   |   |       |   |-- GdImageFile.py
|   |   |       |   |-- GifImagePlugin.py
|   |   |       |   |-- GimpGradientFile.py
|   |   |       |   |-- GimpPaletteFile.py
|   |   |       |   |-- GribStubImagePlugin.py
|   |   |       |   |-- Hdf5StubImagePlugin.py
|   |   |       |   |-- IcnsImagePlugin.py
|   |   |       |   |-- IcoImagePlugin.py
|   |   |       |   |-- Image.py
|   |   |       |   |-- ImageChops.py
|   |   |       |   |-- ImageCms.py
|   |   |       |   |-- ImageColor.py
|   |   |       |   |-- ImageDraw.py
|   |   |       |   |-- ImageDraw2.py
|   |   |       |   |-- ImageEnhance.py
|   |   |       |   |-- ImageFile.py
|   |   |       |   |-- ImageFilter.py
|   |   |       |   |-- ImageFont.py
|   |   |       |   |-- ImageGrab.py
|   |   |       |   |-- ImageMath.py
|   |   |       |   |-- ImageMode.py
|   |   |       |   |-- ImageMorph.py
|   |   |       |   |-- ImageOps.py
|   |   |       |   |-- ImagePalette.py
|   |   |       |   |-- ImagePath.py
|   |   |       |   |-- ImageQt.py
|   |   |       |   |-- ImageSequence.py
|   |   |       |   |-- ImageShow.py
|   |   |       |   |-- ImageStat.py
|   |   |       |   |-- ImageText.py
|   |   |       |   |-- ImageTk.py
|   |   |       |   |-- ImageTransform.py
|   |   |       |   |-- ImageWin.py
|   |   |       |   |-- ImImagePlugin.py
|   |   |       |   |-- ImtImagePlugin.py
|   |   |       |   |-- IptcImagePlugin.py
|   |   |       |   |-- Jpeg2KImagePlugin.py
|   |   |       |   |-- JpegImagePlugin.py
|   |   |       |   |-- JpegPresets.py
|   |   |       |   |-- McIdasImagePlugin.py
|   |   |       |   |-- MicImagePlugin.py
|   |   |       |   |-- MpegImagePlugin.py
|   |   |       |   |-- MpoImagePlugin.py
|   |   |       |   |-- MspImagePlugin.py
|   |   |       |   |-- PaletteFile.py
|   |   |       |   |-- PalmImagePlugin.py
|   |   |       |   |-- PcdImagePlugin.py
|   |   |       |   |-- PcfFontFile.py
|   |   |       |   |-- PcxImagePlugin.py
|   |   |       |   |-- PdfImagePlugin.py
|   |   |       |   |-- PdfParser.py
|   |   |       |   |-- PixarImagePlugin.py
|   |   |       |   |-- PngImagePlugin.py
|   |   |       |   |-- PpmImagePlugin.py
|   |   |       |   |-- PsdImagePlugin.py
|   |   |       |   |-- PSDraw.py
|   |   |       |   |-- py.typed
|   |   |       |   |-- QoiImagePlugin.py
|   |   |       |   |-- report.py
|   |   |       |   |-- SgiImagePlugin.py
|   |   |       |   |-- SpiderImagePlugin.py
|   |   |       |   |-- SunImagePlugin.py
|   |   |       |   |-- TarIO.py
|   |   |       |   |-- TgaImagePlugin.py
|   |   |       |   |-- TiffImagePlugin.py
|   |   |       |   |-- TiffTags.py
|   |   |       |   |-- WalImageFile.py
|   |   |       |   |-- WebPImagePlugin.py
|   |   |       |   |-- WmfImagePlugin.py
|   |   |       |   |-- XbmImagePlugin.py
|   |   |       |   |-- XpmImagePlugin.py
|   |   |       |   +-- XVThumbImagePlugin.py
|   |   |       |-- pillow-12.0.0.dist-info
|   |   |       |   |-- licenses
|   |   |       |   |   +-- LICENSE
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- top_level.txt
|   |   |       |   |-- WHEEL
|   |   |       |   +-- zip-safe
|   |   |       |-- pip
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   +-- __pip-runner__.cpython-313.pyc
|   |   |       |   |-- _internal
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- build_env.cpython-313.pyc
|   |   |       |   |   |   |-- cache.cpython-313.pyc
|   |   |       |   |   |   |-- configuration.cpython-313.pyc
|   |   |       |   |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |   |-- main.cpython-313.pyc
|   |   |       |   |   |   |-- pyproject.cpython-313.pyc
|   |   |       |   |   |   |-- self_outdated_check.cpython-313.pyc
|   |   |       |   |   |   +-- wheel_builder.cpython-313.pyc
|   |   |       |   |   |-- cli
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- autocompletion.cpython-313.pyc
|   |   |       |   |   |   |   |-- base_command.cpython-313.pyc
|   |   |       |   |   |   |   |-- cmdoptions.cpython-313.pyc
|   |   |       |   |   |   |   |-- command_context.cpython-313.pyc
|   |   |       |   |   |   |   |-- index_command.cpython-313.pyc
|   |   |       |   |   |   |   |-- main.cpython-313.pyc
|   |   |       |   |   |   |   |-- main_parser.cpython-313.pyc
|   |   |       |   |   |   |   |-- parser.cpython-313.pyc
|   |   |       |   |   |   |   |-- progress_bars.cpython-313.pyc
|   |   |       |   |   |   |   |-- req_command.cpython-313.pyc
|   |   |       |   |   |   |   |-- spinners.cpython-313.pyc
|   |   |       |   |   |   |   +-- status_codes.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- autocompletion.py
|   |   |       |   |   |   |-- base_command.py
|   |   |       |   |   |   |-- cmdoptions.py
|   |   |       |   |   |   |-- command_context.py
|   |   |       |   |   |   |-- index_command.py
|   |   |       |   |   |   |-- main.py
|   |   |       |   |   |   |-- main_parser.py
|   |   |       |   |   |   |-- parser.py
|   |   |       |   |   |   |-- progress_bars.py
|   |   |       |   |   |   |-- req_command.py
|   |   |       |   |   |   |-- spinners.py
|   |   |       |   |   |   +-- status_codes.py
|   |   |       |   |   |-- commands
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- cache.cpython-313.pyc
|   |   |       |   |   |   |   |-- check.cpython-313.pyc
|   |   |       |   |   |   |   |-- completion.cpython-313.pyc
|   |   |       |   |   |   |   |-- configuration.cpython-313.pyc
|   |   |       |   |   |   |   |-- debug.cpython-313.pyc
|   |   |       |   |   |   |   |-- download.cpython-313.pyc
|   |   |       |   |   |   |   |-- freeze.cpython-313.pyc
|   |   |       |   |   |   |   |-- hash.cpython-313.pyc
|   |   |       |   |   |   |   |-- help.cpython-313.pyc
|   |   |       |   |   |   |   |-- index.cpython-313.pyc
|   |   |       |   |   |   |   |-- inspect.cpython-313.pyc
|   |   |       |   |   |   |   |-- install.cpython-313.pyc
|   |   |       |   |   |   |   |-- list.cpython-313.pyc
|   |   |       |   |   |   |   |-- lock.cpython-313.pyc
|   |   |       |   |   |   |   |-- search.cpython-313.pyc
|   |   |       |   |   |   |   |-- show.cpython-313.pyc
|   |   |       |   |   |   |   |-- uninstall.cpython-313.pyc
|   |   |       |   |   |   |   +-- wheel.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- cache.py
|   |   |       |   |   |   |-- check.py
|   |   |       |   |   |   |-- completion.py
|   |   |       |   |   |   |-- configuration.py
|   |   |       |   |   |   |-- debug.py
|   |   |       |   |   |   |-- download.py
|   |   |       |   |   |   |-- freeze.py
|   |   |       |   |   |   |-- hash.py
|   |   |       |   |   |   |-- help.py
|   |   |       |   |   |   |-- index.py
|   |   |       |   |   |   |-- inspect.py
|   |   |       |   |   |   |-- install.py
|   |   |       |   |   |   |-- list.py
|   |   |       |   |   |   |-- lock.py
|   |   |       |   |   |   |-- search.py
|   |   |       |   |   |   |-- show.py
|   |   |       |   |   |   |-- uninstall.py
|   |   |       |   |   |   +-- wheel.py
|   |   |       |   |   |-- distributions
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- base.cpython-313.pyc
|   |   |       |   |   |   |   |-- installed.cpython-313.pyc
|   |   |       |   |   |   |   |-- sdist.cpython-313.pyc
|   |   |       |   |   |   |   +-- wheel.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- base.py
|   |   |       |   |   |   |-- installed.py
|   |   |       |   |   |   |-- sdist.py
|   |   |       |   |   |   +-- wheel.py
|   |   |       |   |   |-- index
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- collector.cpython-313.pyc
|   |   |       |   |   |   |   |-- package_finder.cpython-313.pyc
|   |   |       |   |   |   |   +-- sources.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- collector.py
|   |   |       |   |   |   |-- package_finder.py
|   |   |       |   |   |   +-- sources.py
|   |   |       |   |   |-- locations
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _distutils.cpython-313.pyc
|   |   |       |   |   |   |   |-- _sysconfig.cpython-313.pyc
|   |   |       |   |   |   |   +-- base.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _distutils.py
|   |   |       |   |   |   |-- _sysconfig.py
|   |   |       |   |   |   +-- base.py
|   |   |       |   |   |-- metadata
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _json.cpython-313.pyc
|   |   |       |   |   |   |   |-- base.cpython-313.pyc
|   |   |       |   |   |   |   +-- pkg_resources.cpython-313.pyc
|   |   |       |   |   |   |-- importlib
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _compat.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _dists.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _envs.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _compat.py
|   |   |       |   |   |   |   |-- _dists.py
|   |   |       |   |   |   |   +-- _envs.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _json.py
|   |   |       |   |   |   |-- base.py
|   |   |       |   |   |   +-- pkg_resources.py
|   |   |       |   |   |-- models
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- candidate.cpython-313.pyc
|   |   |       |   |   |   |   |-- direct_url.cpython-313.pyc
|   |   |       |   |   |   |   |-- format_control.cpython-313.pyc
|   |   |       |   |   |   |   |-- index.cpython-313.pyc
|   |   |       |   |   |   |   |-- installation_report.cpython-313.pyc
|   |   |       |   |   |   |   |-- link.cpython-313.pyc
|   |   |       |   |   |   |   |-- pylock.cpython-313.pyc
|   |   |       |   |   |   |   |-- scheme.cpython-313.pyc
|   |   |       |   |   |   |   |-- search_scope.cpython-313.pyc
|   |   |       |   |   |   |   |-- selection_prefs.cpython-313.pyc
|   |   |       |   |   |   |   |-- target_python.cpython-313.pyc
|   |   |       |   |   |   |   +-- wheel.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- candidate.py
|   |   |       |   |   |   |-- direct_url.py
|   |   |       |   |   |   |-- format_control.py
|   |   |       |   |   |   |-- index.py
|   |   |       |   |   |   |-- installation_report.py
|   |   |       |   |   |   |-- link.py
|   |   |       |   |   |   |-- pylock.py
|   |   |       |   |   |   |-- scheme.py
|   |   |       |   |   |   |-- search_scope.py
|   |   |       |   |   |   |-- selection_prefs.py
|   |   |       |   |   |   |-- target_python.py
|   |   |       |   |   |   +-- wheel.py
|   |   |       |   |   |-- network
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- auth.cpython-313.pyc
|   |   |       |   |   |   |   |-- cache.cpython-313.pyc
|   |   |       |   |   |   |   |-- download.cpython-313.pyc
|   |   |       |   |   |   |   |-- lazy_wheel.cpython-313.pyc
|   |   |       |   |   |   |   |-- session.cpython-313.pyc
|   |   |       |   |   |   |   |-- utils.cpython-313.pyc
|   |   |       |   |   |   |   +-- xmlrpc.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- auth.py
|   |   |       |   |   |   |-- cache.py
|   |   |       |   |   |   |-- download.py
|   |   |       |   |   |   |-- lazy_wheel.py
|   |   |       |   |   |   |-- session.py
|   |   |       |   |   |   |-- utils.py
|   |   |       |   |   |   +-- xmlrpc.py
|   |   |       |   |   |-- operations
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- check.cpython-313.pyc
|   |   |       |   |   |   |   |-- freeze.cpython-313.pyc
|   |   |       |   |   |   |   +-- prepare.cpython-313.pyc
|   |   |       |   |   |   |-- build
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- build_tracker.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- metadata.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- metadata_editable.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- metadata_legacy.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- wheel.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- wheel_editable.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- wheel_legacy.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- build_tracker.py
|   |   |       |   |   |   |   |-- metadata.py
|   |   |       |   |   |   |   |-- metadata_editable.py
|   |   |       |   |   |   |   |-- metadata_legacy.py
|   |   |       |   |   |   |   |-- wheel.py
|   |   |       |   |   |   |   |-- wheel_editable.py
|   |   |       |   |   |   |   +-- wheel_legacy.py
|   |   |       |   |   |   |-- install
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- editable_legacy.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- wheel.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- editable_legacy.py
|   |   |       |   |   |   |   +-- wheel.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- check.py
|   |   |       |   |   |   |-- freeze.py
|   |   |       |   |   |   +-- prepare.py
|   |   |       |   |   |-- req
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- constructors.cpython-313.pyc
|   |   |       |   |   |   |   |-- req_dependency_group.cpython-313.pyc
|   |   |       |   |   |   |   |-- req_file.cpython-313.pyc
|   |   |       |   |   |   |   |-- req_install.cpython-313.pyc
|   |   |       |   |   |   |   |-- req_set.cpython-313.pyc
|   |   |       |   |   |   |   +-- req_uninstall.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- constructors.py
|   |   |       |   |   |   |-- req_dependency_group.py
|   |   |       |   |   |   |-- req_file.py
|   |   |       |   |   |   |-- req_install.py
|   |   |       |   |   |   |-- req_set.py
|   |   |       |   |   |   +-- req_uninstall.py
|   |   |       |   |   |-- resolution
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- base.cpython-313.pyc
|   |   |       |   |   |   |-- legacy
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- resolver.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   +-- resolver.py
|   |   |       |   |   |   |-- resolvelib
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- base.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- candidates.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- factory.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- found_candidates.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- provider.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- reporter.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- requirements.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- resolver.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- base.py
|   |   |       |   |   |   |   |-- candidates.py
|   |   |       |   |   |   |   |-- factory.py
|   |   |       |   |   |   |   |-- found_candidates.py
|   |   |       |   |   |   |   |-- provider.py
|   |   |       |   |   |   |   |-- reporter.py
|   |   |       |   |   |   |   |-- requirements.py
|   |   |       |   |   |   |   +-- resolver.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   +-- base.py
|   |   |       |   |   |-- utils
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _jaraco_text.cpython-313.pyc
|   |   |       |   |   |   |   |-- _log.cpython-313.pyc
|   |   |       |   |   |   |   |-- appdirs.cpython-313.pyc
|   |   |       |   |   |   |   |-- compat.cpython-313.pyc
|   |   |       |   |   |   |   |-- compatibility_tags.cpython-313.pyc
|   |   |       |   |   |   |   |-- datetime.cpython-313.pyc
|   |   |       |   |   |   |   |-- deprecation.cpython-313.pyc
|   |   |       |   |   |   |   |-- direct_url_helpers.cpython-313.pyc
|   |   |       |   |   |   |   |-- egg_link.cpython-313.pyc
|   |   |       |   |   |   |   |-- entrypoints.cpython-313.pyc
|   |   |       |   |   |   |   |-- filesystem.cpython-313.pyc
|   |   |       |   |   |   |   |-- filetypes.cpython-313.pyc
|   |   |       |   |   |   |   |-- glibc.cpython-313.pyc
|   |   |       |   |   |   |   |-- hashes.cpython-313.pyc
|   |   |       |   |   |   |   |-- logging.cpython-313.pyc
|   |   |       |   |   |   |   |-- misc.cpython-313.pyc
|   |   |       |   |   |   |   |-- packaging.cpython-313.pyc
|   |   |       |   |   |   |   |-- retry.cpython-313.pyc
|   |   |       |   |   |   |   |-- setuptools_build.cpython-313.pyc
|   |   |       |   |   |   |   |-- subprocess.cpython-313.pyc
|   |   |       |   |   |   |   |-- temp_dir.cpython-313.pyc
|   |   |       |   |   |   |   |-- unpacking.cpython-313.pyc
|   |   |       |   |   |   |   |-- urls.cpython-313.pyc
|   |   |       |   |   |   |   |-- virtualenv.cpython-313.pyc
|   |   |       |   |   |   |   +-- wheel.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _jaraco_text.py
|   |   |       |   |   |   |-- _log.py
|   |   |       |   |   |   |-- appdirs.py
|   |   |       |   |   |   |-- compat.py
|   |   |       |   |   |   |-- compatibility_tags.py
|   |   |       |   |   |   |-- datetime.py
|   |   |       |   |   |   |-- deprecation.py
|   |   |       |   |   |   |-- direct_url_helpers.py
|   |   |       |   |   |   |-- egg_link.py
|   |   |       |   |   |   |-- entrypoints.py
|   |   |       |   |   |   |-- filesystem.py
|   |   |       |   |   |   |-- filetypes.py
|   |   |       |   |   |   |-- glibc.py
|   |   |       |   |   |   |-- hashes.py
|   |   |       |   |   |   |-- logging.py
|   |   |       |   |   |   |-- misc.py
|   |   |       |   |   |   |-- packaging.py
|   |   |       |   |   |   |-- retry.py
|   |   |       |   |   |   |-- setuptools_build.py
|   |   |       |   |   |   |-- subprocess.py
|   |   |       |   |   |   |-- temp_dir.py
|   |   |       |   |   |   |-- unpacking.py
|   |   |       |   |   |   |-- urls.py
|   |   |       |   |   |   |-- virtualenv.py
|   |   |       |   |   |   +-- wheel.py
|   |   |       |   |   |-- vcs
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- bazaar.cpython-313.pyc
|   |   |       |   |   |   |   |-- git.cpython-313.pyc
|   |   |       |   |   |   |   |-- mercurial.cpython-313.pyc
|   |   |       |   |   |   |   |-- subversion.cpython-313.pyc
|   |   |       |   |   |   |   +-- versioncontrol.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- bazaar.py
|   |   |       |   |   |   |-- git.py
|   |   |       |   |   |   |-- mercurial.py
|   |   |       |   |   |   |-- subversion.py
|   |   |       |   |   |   +-- versioncontrol.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- build_env.py
|   |   |       |   |   |-- cache.py
|   |   |       |   |   |-- configuration.py
|   |   |       |   |   |-- exceptions.py
|   |   |       |   |   |-- main.py
|   |   |       |   |   |-- pyproject.py
|   |   |       |   |   |-- self_outdated_check.py
|   |   |       |   |   +-- wheel_builder.py
|   |   |       |   |-- _vendor
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |-- cachecontrol
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _cmd.cpython-313.pyc
|   |   |       |   |   |   |   |-- adapter.cpython-313.pyc
|   |   |       |   |   |   |   |-- cache.cpython-313.pyc
|   |   |       |   |   |   |   |-- controller.cpython-313.pyc
|   |   |       |   |   |   |   |-- filewrapper.cpython-313.pyc
|   |   |       |   |   |   |   |-- heuristics.cpython-313.pyc
|   |   |       |   |   |   |   |-- serialize.cpython-313.pyc
|   |   |       |   |   |   |   +-- wrapper.cpython-313.pyc
|   |   |       |   |   |   |-- caches
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- file_cache.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- redis_cache.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- file_cache.py
|   |   |       |   |   |   |   +-- redis_cache.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _cmd.py
|   |   |       |   |   |   |-- adapter.py
|   |   |       |   |   |   |-- cache.py
|   |   |       |   |   |   |-- controller.py
|   |   |       |   |   |   |-- filewrapper.py
|   |   |       |   |   |   |-- heuristics.py
|   |   |       |   |   |   |-- py.typed
|   |   |       |   |   |   |-- serialize.py
|   |   |       |   |   |   +-- wrapper.py
|   |   |       |   |   |-- certifi
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   +-- core.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- cacert.pem
|   |   |       |   |   |   |-- core.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- dependency_groups
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _implementation.cpython-313.pyc
|   |   |       |   |   |   |   |-- _lint_dependency_groups.cpython-313.pyc
|   |   |       |   |   |   |   |-- _pip_wrapper.cpython-313.pyc
|   |   |       |   |   |   |   +-- _toml_compat.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- _implementation.py
|   |   |       |   |   |   |-- _lint_dependency_groups.py
|   |   |       |   |   |   |-- _pip_wrapper.py
|   |   |       |   |   |   |-- _toml_compat.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- distlib
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- compat.cpython-313.pyc
|   |   |       |   |   |   |   |-- resources.cpython-313.pyc
|   |   |       |   |   |   |   |-- scripts.cpython-313.pyc
|   |   |       |   |   |   |   +-- util.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- compat.py
|   |   |       |   |   |   |-- resources.py
|   |   |       |   |   |   |-- scripts.py
|   |   |       |   |   |   |-- t32.exe
|   |   |       |   |   |   |-- t64.exe
|   |   |       |   |   |   |-- t64-arm.exe
|   |   |       |   |   |   |-- util.py
|   |   |       |   |   |   |-- w32.exe
|   |   |       |   |   |   |-- w64.exe
|   |   |       |   |   |   +-- w64-arm.exe
|   |   |       |   |   |-- distro
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   +-- distro.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- distro.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- idna
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- codec.cpython-313.pyc
|   |   |       |   |   |   |   |-- compat.cpython-313.pyc
|   |   |       |   |   |   |   |-- core.cpython-313.pyc
|   |   |       |   |   |   |   |-- idnadata.cpython-313.pyc
|   |   |       |   |   |   |   |-- intranges.cpython-313.pyc
|   |   |       |   |   |   |   |-- package_data.cpython-313.pyc
|   |   |       |   |   |   |   +-- uts46data.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- codec.py
|   |   |       |   |   |   |-- compat.py
|   |   |       |   |   |   |-- core.py
|   |   |       |   |   |   |-- idnadata.py
|   |   |       |   |   |   |-- intranges.py
|   |   |       |   |   |   |-- package_data.py
|   |   |       |   |   |   |-- py.typed
|   |   |       |   |   |   +-- uts46data.py
|   |   |       |   |   |-- msgpack
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |   |   |-- ext.cpython-313.pyc
|   |   |       |   |   |   |   +-- fallback.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- exceptions.py
|   |   |       |   |   |   |-- ext.py
|   |   |       |   |   |   +-- fallback.py
|   |   |       |   |   |-- packaging
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _elffile.cpython-313.pyc
|   |   |       |   |   |   |   |-- _manylinux.cpython-313.pyc
|   |   |       |   |   |   |   |-- _musllinux.cpython-313.pyc
|   |   |       |   |   |   |   |-- _parser.cpython-313.pyc
|   |   |       |   |   |   |   |-- _structures.cpython-313.pyc
|   |   |       |   |   |   |   |-- _tokenizer.cpython-313.pyc
|   |   |       |   |   |   |   |-- markers.cpython-313.pyc
|   |   |       |   |   |   |   |-- metadata.cpython-313.pyc
|   |   |       |   |   |   |   |-- requirements.cpython-313.pyc
|   |   |       |   |   |   |   |-- specifiers.cpython-313.pyc
|   |   |       |   |   |   |   |-- tags.cpython-313.pyc
|   |   |       |   |   |   |   |-- utils.cpython-313.pyc
|   |   |       |   |   |   |   +-- version.cpython-313.pyc
|   |   |       |   |   |   |-- licenses
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _spdx.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   +-- _spdx.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _elffile.py
|   |   |       |   |   |   |-- _manylinux.py
|   |   |       |   |   |   |-- _musllinux.py
|   |   |       |   |   |   |-- _parser.py
|   |   |       |   |   |   |-- _structures.py
|   |   |       |   |   |   |-- _tokenizer.py
|   |   |       |   |   |   |-- markers.py
|   |   |       |   |   |   |-- metadata.py
|   |   |       |   |   |   |-- py.typed
|   |   |       |   |   |   |-- requirements.py
|   |   |       |   |   |   |-- specifiers.py
|   |   |       |   |   |   |-- tags.py
|   |   |       |   |   |   |-- utils.py
|   |   |       |   |   |   +-- version.py
|   |   |       |   |   |-- pkg_resources
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- __init__.py
|   |   |       |   |   |-- platformdirs
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   |-- android.cpython-313.pyc
|   |   |       |   |   |   |   |-- api.cpython-313.pyc
|   |   |       |   |   |   |   |-- macos.cpython-313.pyc
|   |   |       |   |   |   |   |-- unix.cpython-313.pyc
|   |   |       |   |   |   |   |-- version.cpython-313.pyc
|   |   |       |   |   |   |   +-- windows.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- android.py
|   |   |       |   |   |   |-- api.py
|   |   |       |   |   |   |-- macos.py
|   |   |       |   |   |   |-- py.typed
|   |   |       |   |   |   |-- unix.py
|   |   |       |   |   |   |-- version.py
|   |   |       |   |   |   +-- windows.py
|   |   |       |   |   |-- pygments
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   |-- console.cpython-313.pyc
|   |   |       |   |   |   |   |-- filter.cpython-313.pyc
|   |   |       |   |   |   |   |-- formatter.cpython-313.pyc
|   |   |       |   |   |   |   |-- lexer.cpython-313.pyc
|   |   |       |   |   |   |   |-- modeline.cpython-313.pyc
|   |   |       |   |   |   |   |-- plugin.cpython-313.pyc
|   |   |       |   |   |   |   |-- regexopt.cpython-313.pyc
|   |   |       |   |   |   |   |-- scanner.cpython-313.pyc
|   |   |       |   |   |   |   |-- sphinxext.cpython-313.pyc
|   |   |       |   |   |   |   |-- style.cpython-313.pyc
|   |   |       |   |   |   |   |-- token.cpython-313.pyc
|   |   |       |   |   |   |   |-- unistring.cpython-313.pyc
|   |   |       |   |   |   |   +-- util.cpython-313.pyc
|   |   |       |   |   |   |-- filters
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- __init__.py
|   |   |       |   |   |   |-- formatters
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _mapping.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   +-- _mapping.py
|   |   |       |   |   |   |-- lexers
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _mapping.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- python.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _mapping.py
|   |   |       |   |   |   |   +-- python.py
|   |   |       |   |   |   |-- styles
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _mapping.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   +-- _mapping.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- console.py
|   |   |       |   |   |   |-- filter.py
|   |   |       |   |   |   |-- formatter.py
|   |   |       |   |   |   |-- lexer.py
|   |   |       |   |   |   |-- modeline.py
|   |   |       |   |   |   |-- plugin.py
|   |   |       |   |   |   |-- regexopt.py
|   |   |       |   |   |   |-- scanner.py
|   |   |       |   |   |   |-- sphinxext.py
|   |   |       |   |   |   |-- style.py
|   |   |       |   |   |   |-- token.py
|   |   |       |   |   |   |-- unistring.py
|   |   |       |   |   |   +-- util.py
|   |   |       |   |   |-- pyproject_hooks
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- _impl.cpython-313.pyc
|   |   |       |   |   |   |-- _in_process
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _in_process.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   +-- _in_process.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _impl.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- requests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __version__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _internal_utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- adapters.cpython-313.pyc
|   |   |       |   |   |   |   |-- api.cpython-313.pyc
|   |   |       |   |   |   |   |-- auth.cpython-313.pyc
|   |   |       |   |   |   |   |-- certs.cpython-313.pyc
|   |   |       |   |   |   |   |-- compat.cpython-313.pyc
|   |   |       |   |   |   |   |-- cookies.cpython-313.pyc
|   |   |       |   |   |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |   |   |-- help.cpython-313.pyc
|   |   |       |   |   |   |   |-- hooks.cpython-313.pyc
|   |   |       |   |   |   |   |-- models.cpython-313.pyc
|   |   |       |   |   |   |   |-- packages.cpython-313.pyc
|   |   |       |   |   |   |   |-- sessions.cpython-313.pyc
|   |   |       |   |   |   |   |-- status_codes.cpython-313.pyc
|   |   |       |   |   |   |   |-- structures.cpython-313.pyc
|   |   |       |   |   |   |   +-- utils.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __version__.py
|   |   |       |   |   |   |-- _internal_utils.py
|   |   |       |   |   |   |-- adapters.py
|   |   |       |   |   |   |-- api.py
|   |   |       |   |   |   |-- auth.py
|   |   |       |   |   |   |-- certs.py
|   |   |       |   |   |   |-- compat.py
|   |   |       |   |   |   |-- cookies.py
|   |   |       |   |   |   |-- exceptions.py
|   |   |       |   |   |   |-- help.py
|   |   |       |   |   |   |-- hooks.py
|   |   |       |   |   |   |-- models.py
|   |   |       |   |   |   |-- packages.py
|   |   |       |   |   |   |-- sessions.py
|   |   |       |   |   |   |-- status_codes.py
|   |   |       |   |   |   |-- structures.py
|   |   |       |   |   |   +-- utils.py
|   |   |       |   |   |-- resolvelib
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- providers.cpython-313.pyc
|   |   |       |   |   |   |   |-- reporters.cpython-313.pyc
|   |   |       |   |   |   |   +-- structs.cpython-313.pyc
|   |   |       |   |   |   |-- resolvers
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- abstract.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- criterion.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- resolution.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- abstract.py
|   |   |       |   |   |   |   |-- criterion.py
|   |   |       |   |   |   |   |-- exceptions.py
|   |   |       |   |   |   |   +-- resolution.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- providers.py
|   |   |       |   |   |   |-- py.typed
|   |   |       |   |   |   |-- reporters.py
|   |   |       |   |   |   +-- structs.py
|   |   |       |   |   |-- rich
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __main__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _cell_widths.cpython-313.pyc
|   |   |       |   |   |   |   |-- _emoji_codes.cpython-313.pyc
|   |   |       |   |   |   |   |-- _emoji_replace.cpython-313.pyc
|   |   |       |   |   |   |   |-- _export_format.cpython-313.pyc
|   |   |       |   |   |   |   |-- _extension.cpython-313.pyc
|   |   |       |   |   |   |   |-- _fileno.cpython-313.pyc
|   |   |       |   |   |   |   |-- _inspect.cpython-313.pyc
|   |   |       |   |   |   |   |-- _log_render.cpython-313.pyc
|   |   |       |   |   |   |   |-- _loop.cpython-313.pyc
|   |   |       |   |   |   |   |-- _null_file.cpython-313.pyc
|   |   |       |   |   |   |   |-- _palettes.cpython-313.pyc
|   |   |       |   |   |   |   |-- _pick.cpython-313.pyc
|   |   |       |   |   |   |   |-- _ratio.cpython-313.pyc
|   |   |       |   |   |   |   |-- _spinners.cpython-313.pyc
|   |   |       |   |   |   |   |-- _stack.cpython-313.pyc
|   |   |       |   |   |   |   |-- _timer.cpython-313.pyc
|   |   |       |   |   |   |   |-- _win32_console.cpython-313.pyc
|   |   |       |   |   |   |   |-- _windows.cpython-313.pyc
|   |   |       |   |   |   |   |-- _windows_renderer.cpython-313.pyc
|   |   |       |   |   |   |   |-- _wrap.cpython-313.pyc
|   |   |       |   |   |   |   |-- abc.cpython-313.pyc
|   |   |       |   |   |   |   |-- align.cpython-313.pyc
|   |   |       |   |   |   |   |-- ansi.cpython-313.pyc
|   |   |       |   |   |   |   |-- bar.cpython-313.pyc
|   |   |       |   |   |   |   |-- box.cpython-313.pyc
|   |   |       |   |   |   |   |-- cells.cpython-313.pyc
|   |   |       |   |   |   |   |-- color.cpython-313.pyc
|   |   |       |   |   |   |   |-- color_triplet.cpython-313.pyc
|   |   |       |   |   |   |   |-- columns.cpython-313.pyc
|   |   |       |   |   |   |   |-- console.cpython-313.pyc
|   |   |       |   |   |   |   |-- constrain.cpython-313.pyc
|   |   |       |   |   |   |   |-- containers.cpython-313.pyc
|   |   |       |   |   |   |   |-- control.cpython-313.pyc
|   |   |       |   |   |   |   |-- default_styles.cpython-313.pyc
|   |   |       |   |   |   |   |-- diagnose.cpython-313.pyc
|   |   |       |   |   |   |   |-- emoji.cpython-313.pyc
|   |   |       |   |   |   |   |-- errors.cpython-313.pyc
|   |   |       |   |   |   |   |-- file_proxy.cpython-313.pyc
|   |   |       |   |   |   |   |-- filesize.cpython-313.pyc
|   |   |       |   |   |   |   |-- highlighter.cpython-313.pyc
|   |   |       |   |   |   |   |-- json.cpython-313.pyc
|   |   |       |   |   |   |   |-- jupyter.cpython-313.pyc
|   |   |       |   |   |   |   |-- layout.cpython-313.pyc
|   |   |       |   |   |   |   |-- live.cpython-313.pyc
|   |   |       |   |   |   |   |-- live_render.cpython-313.pyc
|   |   |       |   |   |   |   |-- logging.cpython-313.pyc
|   |   |       |   |   |   |   |-- markup.cpython-313.pyc
|   |   |       |   |   |   |   |-- measure.cpython-313.pyc
|   |   |       |   |   |   |   |-- padding.cpython-313.pyc
|   |   |       |   |   |   |   |-- pager.cpython-313.pyc
|   |   |       |   |   |   |   |-- palette.cpython-313.pyc
|   |   |       |   |   |   |   |-- panel.cpython-313.pyc
|   |   |       |   |   |   |   |-- pretty.cpython-313.pyc
|   |   |       |   |   |   |   |-- progress.cpython-313.pyc
|   |   |       |   |   |   |   |-- progress_bar.cpython-313.pyc
|   |   |       |   |   |   |   |-- prompt.cpython-313.pyc
|   |   |       |   |   |   |   |-- protocol.cpython-313.pyc
|   |   |       |   |   |   |   |-- region.cpython-313.pyc
|   |   |       |   |   |   |   |-- repr.cpython-313.pyc
|   |   |       |   |   |   |   |-- rule.cpython-313.pyc
|   |   |       |   |   |   |   |-- scope.cpython-313.pyc
|   |   |       |   |   |   |   |-- screen.cpython-313.pyc
|   |   |       |   |   |   |   |-- segment.cpython-313.pyc
|   |   |       |   |   |   |   |-- spinner.cpython-313.pyc
|   |   |       |   |   |   |   |-- status.cpython-313.pyc
|   |   |       |   |   |   |   |-- style.cpython-313.pyc
|   |   |       |   |   |   |   |-- styled.cpython-313.pyc
|   |   |       |   |   |   |   |-- syntax.cpython-313.pyc
|   |   |       |   |   |   |   |-- table.cpython-313.pyc
|   |   |       |   |   |   |   |-- terminal_theme.cpython-313.pyc
|   |   |       |   |   |   |   |-- text.cpython-313.pyc
|   |   |       |   |   |   |   |-- theme.cpython-313.pyc
|   |   |       |   |   |   |   |-- themes.cpython-313.pyc
|   |   |       |   |   |   |   |-- traceback.cpython-313.pyc
|   |   |       |   |   |   |   +-- tree.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- __main__.py
|   |   |       |   |   |   |-- _cell_widths.py
|   |   |       |   |   |   |-- _emoji_codes.py
|   |   |       |   |   |   |-- _emoji_replace.py
|   |   |       |   |   |   |-- _export_format.py
|   |   |       |   |   |   |-- _extension.py
|   |   |       |   |   |   |-- _fileno.py
|   |   |       |   |   |   |-- _inspect.py
|   |   |       |   |   |   |-- _log_render.py
|   |   |       |   |   |   |-- _loop.py
|   |   |       |   |   |   |-- _null_file.py
|   |   |       |   |   |   |-- _palettes.py
|   |   |       |   |   |   |-- _pick.py
|   |   |       |   |   |   |-- _ratio.py
|   |   |       |   |   |   |-- _spinners.py
|   |   |       |   |   |   |-- _stack.py
|   |   |       |   |   |   |-- _timer.py
|   |   |       |   |   |   |-- _win32_console.py
|   |   |       |   |   |   |-- _windows.py
|   |   |       |   |   |   |-- _windows_renderer.py
|   |   |       |   |   |   |-- _wrap.py
|   |   |       |   |   |   |-- abc.py
|   |   |       |   |   |   |-- align.py
|   |   |       |   |   |   |-- ansi.py
|   |   |       |   |   |   |-- bar.py
|   |   |       |   |   |   |-- box.py
|   |   |       |   |   |   |-- cells.py
|   |   |       |   |   |   |-- color.py
|   |   |       |   |   |   |-- color_triplet.py
|   |   |       |   |   |   |-- columns.py
|   |   |       |   |   |   |-- console.py
|   |   |       |   |   |   |-- constrain.py
|   |   |       |   |   |   |-- containers.py
|   |   |       |   |   |   |-- control.py
|   |   |       |   |   |   |-- default_styles.py
|   |   |       |   |   |   |-- diagnose.py
|   |   |       |   |   |   |-- emoji.py
|   |   |       |   |   |   |-- errors.py
|   |   |       |   |   |   |-- file_proxy.py
|   |   |       |   |   |   |-- filesize.py
|   |   |       |   |   |   |-- highlighter.py
|   |   |       |   |   |   |-- json.py
|   |   |       |   |   |   |-- jupyter.py
|   |   |       |   |   |   |-- layout.py
|   |   |       |   |   |   |-- live.py
|   |   |       |   |   |   |-- live_render.py
|   |   |       |   |   |   |-- logging.py
|   |   |       |   |   |   |-- markup.py
|   |   |       |   |   |   |-- measure.py
|   |   |       |   |   |   |-- padding.py
|   |   |       |   |   |   |-- pager.py
|   |   |       |   |   |   |-- palette.py
|   |   |       |   |   |   |-- panel.py
|   |   |       |   |   |   |-- pretty.py
|   |   |       |   |   |   |-- progress.py
|   |   |       |   |   |   |-- progress_bar.py
|   |   |       |   |   |   |-- prompt.py
|   |   |       |   |   |   |-- protocol.py
|   |   |       |   |   |   |-- py.typed
|   |   |       |   |   |   |-- region.py
|   |   |       |   |   |   |-- repr.py
|   |   |       |   |   |   |-- rule.py
|   |   |       |   |   |   |-- scope.py
|   |   |       |   |   |   |-- screen.py
|   |   |       |   |   |   |-- segment.py
|   |   |       |   |   |   |-- spinner.py
|   |   |       |   |   |   |-- status.py
|   |   |       |   |   |   |-- style.py
|   |   |       |   |   |   |-- styled.py
|   |   |       |   |   |   |-- syntax.py
|   |   |       |   |   |   |-- table.py
|   |   |       |   |   |   |-- terminal_theme.py
|   |   |       |   |   |   |-- text.py
|   |   |       |   |   |   |-- theme.py
|   |   |       |   |   |   |-- themes.py
|   |   |       |   |   |   |-- traceback.py
|   |   |       |   |   |   +-- tree.py
|   |   |       |   |   |-- tomli
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _parser.cpython-313.pyc
|   |   |       |   |   |   |   |-- _re.cpython-313.pyc
|   |   |       |   |   |   |   +-- _types.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _parser.py
|   |   |       |   |   |   |-- _re.py
|   |   |       |   |   |   |-- _types.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- tomli_w
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- _writer.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _writer.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- truststore
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _api.cpython-313.pyc
|   |   |       |   |   |   |   |-- _macos.cpython-313.pyc
|   |   |       |   |   |   |   |-- _openssl.cpython-313.pyc
|   |   |       |   |   |   |   |-- _ssl_constants.cpython-313.pyc
|   |   |       |   |   |   |   +-- _windows.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _api.py
|   |   |       |   |   |   |-- _macos.py
|   |   |       |   |   |   |-- _openssl.py
|   |   |       |   |   |   |-- _ssl_constants.py
|   |   |       |   |   |   |-- _windows.py
|   |   |       |   |   |   +-- py.typed
|   |   |       |   |   |-- urllib3
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _collections.cpython-313.pyc
|   |   |       |   |   |   |   |-- _version.cpython-313.pyc
|   |   |       |   |   |   |   |-- connection.cpython-313.pyc
|   |   |       |   |   |   |   |-- connectionpool.cpython-313.pyc
|   |   |       |   |   |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |   |   |-- fields.cpython-313.pyc
|   |   |       |   |   |   |   |-- filepost.cpython-313.pyc
|   |   |       |   |   |   |   |-- poolmanager.cpython-313.pyc
|   |   |       |   |   |   |   |-- request.cpython-313.pyc
|   |   |       |   |   |   |   +-- response.cpython-313.pyc
|   |   |       |   |   |   |-- contrib
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _appengine_environ.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- appengine.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- ntlmpool.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- pyopenssl.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- securetransport.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- socks.cpython-313.pyc
|   |   |       |   |   |   |   |-- _securetransport
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- bindings.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- low_level.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |-- bindings.py
|   |   |       |   |   |   |   |   +-- low_level.py
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _appengine_environ.py
|   |   |       |   |   |   |   |-- appengine.py
|   |   |       |   |   |   |   |-- ntlmpool.py
|   |   |       |   |   |   |   |-- pyopenssl.py
|   |   |       |   |   |   |   |-- securetransport.py
|   |   |       |   |   |   |   +-- socks.py
|   |   |       |   |   |   |-- packages
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- six.cpython-313.pyc
|   |   |       |   |   |   |   |-- backports
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- makefile.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- weakref_finalize.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |-- makefile.py
|   |   |       |   |   |   |   |   +-- weakref_finalize.py
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   +-- six.py
|   |   |       |   |   |   |-- util
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- connection.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- proxy.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- queue.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- request.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- response.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- retry.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- ssl_.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- ssl_match_hostname.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- ssltransport.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- timeout.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- url.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- wait.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- connection.py
|   |   |       |   |   |   |   |-- proxy.py
|   |   |       |   |   |   |   |-- queue.py
|   |   |       |   |   |   |   |-- request.py
|   |   |       |   |   |   |   |-- response.py
|   |   |       |   |   |   |   |-- retry.py
|   |   |       |   |   |   |   |-- ssl_.py
|   |   |       |   |   |   |   |-- ssl_match_hostname.py
|   |   |       |   |   |   |   |-- ssltransport.py
|   |   |       |   |   |   |   |-- timeout.py
|   |   |       |   |   |   |   |-- url.py
|   |   |       |   |   |   |   +-- wait.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _collections.py
|   |   |       |   |   |   |-- _version.py
|   |   |       |   |   |   |-- connection.py
|   |   |       |   |   |   |-- connectionpool.py
|   |   |       |   |   |   |-- exceptions.py
|   |   |       |   |   |   |-- fields.py
|   |   |       |   |   |   |-- filepost.py
|   |   |       |   |   |   |-- poolmanager.py
|   |   |       |   |   |   |-- request.py
|   |   |       |   |   |   +-- response.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- vendor.txt
|   |   |       |   |-- __init__.py
|   |   |       |   |-- __main__.py
|   |   |       |   |-- __pip-runner__.py
|   |   |       |   +-- py.typed
|   |   |       |-- pip-25.2.dist-info
|   |   |       |   |-- licenses
|   |   |       |   |   |-- src
|   |   |       |   |   |   +-- pip
|   |   |       |   |   |       +-- _vendor
|   |   |       |   |   |           |-- cachecontrol
|   |   |       |   |   |           |   +-- LICENSE.txt
|   |   |       |   |   |           |-- certifi
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- dependency_groups
|   |   |       |   |   |           |   +-- LICENSE.txt
|   |   |       |   |   |           |-- distlib
|   |   |       |   |   |           |   +-- LICENSE.txt
|   |   |       |   |   |           |-- distro
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- idna
|   |   |       |   |   |           |   +-- LICENSE.md
|   |   |       |   |   |           |-- msgpack
|   |   |       |   |   |           |   +-- COPYING
|   |   |       |   |   |           |-- packaging
|   |   |       |   |   |           |   |-- LICENSE
|   |   |       |   |   |           |   |-- LICENSE.APACHE
|   |   |       |   |   |           |   +-- LICENSE.BSD
|   |   |       |   |   |           |-- pkg_resources
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- platformdirs
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- pygments
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- pyproject_hooks
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- requests
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- resolvelib
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- rich
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- tomli
|   |   |       |   |   |           |   |-- LICENSE
|   |   |       |   |   |           |   +-- LICENSE-HEADER
|   |   |       |   |   |           |-- tomli_w
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           |-- truststore
|   |   |       |   |   |           |   +-- LICENSE
|   |   |       |   |   |           +-- urllib3
|   |   |       |   |   |               +-- LICENSE.txt
|   |   |       |   |   |-- AUTHORS.txt
|   |   |       |   |   +-- LICENSE.txt
|   |   |       |   |-- entry_points.txt
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- REQUESTED
|   |   |       |   |-- top_level.txt
|   |   |       |   +-- WHEEL
|   |   |       |-- pyparsing
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- actions.cpython-313.pyc
|   |   |       |   |   |-- common.cpython-313.pyc
|   |   |       |   |   |-- core.cpython-313.pyc
|   |   |       |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |-- helpers.cpython-313.pyc
|   |   |       |   |   |-- results.cpython-313.pyc
|   |   |       |   |   |-- testing.cpython-313.pyc
|   |   |       |   |   |-- unicode.cpython-313.pyc
|   |   |       |   |   +-- util.cpython-313.pyc
|   |   |       |   |-- diagram
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   +-- __init__.py
|   |   |       |   |-- tools
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- cvt_pyparsing_pep8_names.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- cvt_pyparsing_pep8_names.py
|   |   |       |   |-- __init__.py
|   |   |       |   |-- actions.py
|   |   |       |   |-- common.py
|   |   |       |   |-- core.py
|   |   |       |   |-- exceptions.py
|   |   |       |   |-- helpers.py
|   |   |       |   |-- py.typed
|   |   |       |   |-- results.py
|   |   |       |   |-- testing.py
|   |   |       |   |-- unicode.py
|   |   |       |   +-- util.py
|   |   |       |-- pyparsing-3.2.5.dist-info
|   |   |       |   |-- licenses
|   |   |       |   |   +-- LICENSE
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   +-- WHEEL
|   |   |       |-- python_dateutil-2.9.0.post0.dist-info
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- LICENSE
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- top_level.txt
|   |   |       |   |-- WHEEL
|   |   |       |   +-- zip-safe
|   |   |       |-- scipy
|   |   |       |   |-- __pycache__
|   |   |       |   |   |-- __config__.cpython-313.pyc
|   |   |       |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |-- _distributor_init.cpython-313.pyc
|   |   |       |   |   |-- conftest.cpython-313.pyc
|   |   |       |   |   +-- version.cpython-313.pyc
|   |   |       |   |-- _lib
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _array_api.cpython-313.pyc
|   |   |       |   |   |   |-- _array_api_compat_vendor.cpython-313.pyc
|   |   |       |   |   |   |-- _array_api_no_0d.cpython-313.pyc
|   |   |       |   |   |   |-- _bunch.cpython-313.pyc
|   |   |       |   |   |   |-- _ccallback.cpython-313.pyc
|   |   |       |   |   |   |-- _disjoint_set.cpython-313.pyc
|   |   |       |   |   |   |-- _docscrape.cpython-313.pyc
|   |   |       |   |   |   |-- _elementwise_iterative_method.cpython-313.pyc
|   |   |       |   |   |   |-- _gcutils.cpython-313.pyc
|   |   |       |   |   |   |-- _pep440.cpython-313.pyc
|   |   |       |   |   |   |-- _sparse.cpython-313.pyc
|   |   |       |   |   |   |-- _testutils.cpython-313.pyc
|   |   |       |   |   |   |-- _threadsafety.cpython-313.pyc
|   |   |       |   |   |   |-- _tmpdirs.cpython-313.pyc
|   |   |       |   |   |   |-- _util.cpython-313.pyc
|   |   |       |   |   |   |-- decorator.cpython-313.pyc
|   |   |       |   |   |   |-- deprecation.cpython-313.pyc
|   |   |       |   |   |   |-- doccer.cpython-313.pyc
|   |   |       |   |   |   +-- uarray.cpython-313.pyc
|   |   |       |   |   |-- _uarray
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- _backend.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _backend.py
|   |   |       |   |   |   |-- _uarray.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _uarray.cp313-win_amd64.pyd
|   |   |       |   |   |   +-- LICENSE
|   |   |       |   |   |-- array_api_compat
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- _internal.cpython-313.pyc
|   |   |       |   |   |   |-- common
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _aliases.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _fft.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _helpers.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _linalg.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _typing.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _aliases.py
|   |   |       |   |   |   |   |-- _fft.py
|   |   |       |   |   |   |   |-- _helpers.py
|   |   |       |   |   |   |   |-- _linalg.py
|   |   |       |   |   |   |   +-- _typing.py
|   |   |       |   |   |   |-- cupy
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _aliases.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _info.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _typing.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- fft.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- linalg.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _aliases.py
|   |   |       |   |   |   |   |-- _info.py
|   |   |       |   |   |   |   |-- _typing.py
|   |   |       |   |   |   |   |-- fft.py
|   |   |       |   |   |   |   +-- linalg.py
|   |   |       |   |   |   |-- dask
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- array
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- _aliases.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- _info.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- fft.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- linalg.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |-- _aliases.py
|   |   |       |   |   |   |   |   |-- _info.py
|   |   |       |   |   |   |   |   |-- fft.py
|   |   |       |   |   |   |   |   +-- linalg.py
|   |   |       |   |   |   |   +-- __init__.py
|   |   |       |   |   |   |-- numpy
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _aliases.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _info.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _typing.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- fft.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- linalg.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _aliases.py
|   |   |       |   |   |   |   |-- _info.py
|   |   |       |   |   |   |   |-- _typing.py
|   |   |       |   |   |   |   |-- fft.py
|   |   |       |   |   |   |   +-- linalg.py
|   |   |       |   |   |   |-- torch
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _aliases.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _info.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _typing.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- fft.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- linalg.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _aliases.py
|   |   |       |   |   |   |   |-- _info.py
|   |   |       |   |   |   |   |-- _typing.py
|   |   |       |   |   |   |   |-- fft.py
|   |   |       |   |   |   |   +-- linalg.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   +-- _internal.py
|   |   |       |   |   |-- array_api_extra
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _delegation.cpython-313.pyc
|   |   |       |   |   |   |   +-- testing.cpython-313.pyc
|   |   |       |   |   |   |-- _lib
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _at.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _backends.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _funcs.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _lazy.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _testing.cpython-313.pyc
|   |   |       |   |   |   |   |-- _utils
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- _compat.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- _helpers.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- _typing.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |-- _compat.py
|   |   |       |   |   |   |   |   |-- _compat.pyi
|   |   |       |   |   |   |   |   |-- _helpers.py
|   |   |       |   |   |   |   |   |-- _typing.py
|   |   |       |   |   |   |   |   +-- _typing.pyi
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _at.py
|   |   |       |   |   |   |   |-- _backends.py
|   |   |       |   |   |   |   |-- _funcs.py
|   |   |       |   |   |   |   |-- _lazy.py
|   |   |       |   |   |   |   +-- _testing.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _delegation.py
|   |   |       |   |   |   +-- testing.py
|   |   |       |   |   |-- cobyqa
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- framework.cpython-313.pyc
|   |   |       |   |   |   |   |-- main.cpython-313.pyc
|   |   |       |   |   |   |   |-- models.cpython-313.pyc
|   |   |       |   |   |   |   |-- problem.cpython-313.pyc
|   |   |       |   |   |   |   +-- settings.cpython-313.pyc
|   |   |       |   |   |   |-- subsolvers
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- geometry.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- optim.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- geometry.py
|   |   |       |   |   |   |   +-- optim.py
|   |   |       |   |   |   |-- utils
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- exceptions.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- math.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- versions.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- exceptions.py
|   |   |       |   |   |   |   |-- math.py
|   |   |       |   |   |   |   +-- versions.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- framework.py
|   |   |       |   |   |   |-- main.py
|   |   |       |   |   |   |-- models.py
|   |   |       |   |   |   |-- problem.py
|   |   |       |   |   |   +-- settings.py
|   |   |       |   |   |-- pyprima
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- cobyla
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- cobyla.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- cobylb.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- geometry.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- initialize.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- trustregion.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- update.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- cobyla.py
|   |   |       |   |   |   |   |-- cobylb.py
|   |   |       |   |   |   |   |-- geometry.py
|   |   |       |   |   |   |   |-- initialize.py
|   |   |       |   |   |   |   |-- trustregion.py
|   |   |       |   |   |   |   +-- update.py
|   |   |       |   |   |   |-- common
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _bounds.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _linear_constraints.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _nonlinear_constraints.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _project.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- checkbreak.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- consts.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- evaluate.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- history.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- infos.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- linalg.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- message.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- powalg.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- preproc.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- present.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- ratio.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- redrho.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- selectx.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _bounds.py
|   |   |       |   |   |   |   |-- _linear_constraints.py
|   |   |       |   |   |   |   |-- _nonlinear_constraints.py
|   |   |       |   |   |   |   |-- _project.py
|   |   |       |   |   |   |   |-- checkbreak.py
|   |   |       |   |   |   |   |-- consts.py
|   |   |       |   |   |   |   |-- evaluate.py
|   |   |       |   |   |   |   |-- history.py
|   |   |       |   |   |   |   |-- infos.py
|   |   |       |   |   |   |   |-- linalg.py
|   |   |       |   |   |   |   |-- message.py
|   |   |       |   |   |   |   |-- powalg.py
|   |   |       |   |   |   |   |-- preproc.py
|   |   |       |   |   |   |   |-- present.py
|   |   |       |   |   |   |   |-- ratio.py
|   |   |       |   |   |   |   |-- redrho.py
|   |   |       |   |   |   |   +-- selectx.py
|   |   |       |   |   |   +-- __init__.py
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__gcutils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__pep440.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__testutils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__threadsafety.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__util.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_api.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_bunch.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ccallback.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_config.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_deprecation.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_doccer.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_import_cycles.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_public_api.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_scipy_version.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_tmpdirs.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_warnings.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test__gcutils.py
|   |   |       |   |   |   |-- test__pep440.py
|   |   |       |   |   |   |-- test__testutils.py
|   |   |       |   |   |   |-- test__threadsafety.py
|   |   |       |   |   |   |-- test__util.py
|   |   |       |   |   |   |-- test_array_api.py
|   |   |       |   |   |   |-- test_bunch.py
|   |   |       |   |   |   |-- test_ccallback.py
|   |   |       |   |   |   |-- test_config.py
|   |   |       |   |   |   |-- test_deprecation.py
|   |   |       |   |   |   |-- test_doccer.py
|   |   |       |   |   |   |-- test_import_cycles.py
|   |   |       |   |   |   |-- test_public_api.py
|   |   |       |   |   |   |-- test_scipy_version.py
|   |   |       |   |   |   |-- test_tmpdirs.py
|   |   |       |   |   |   +-- test_warnings.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _array_api.py
|   |   |       |   |   |-- _array_api_compat_vendor.py
|   |   |       |   |   |-- _array_api_no_0d.py
|   |   |       |   |   |-- _bunch.py
|   |   |       |   |   |-- _ccallback.py
|   |   |       |   |   |-- _ccallback_c.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ccallback_c.cp313-win_amd64.pyd
|   |   |       |   |   |-- _disjoint_set.py
|   |   |       |   |   |-- _docscrape.py
|   |   |       |   |   |-- _elementwise_iterative_method.py
|   |   |       |   |   |-- _fpumode.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _fpumode.cp313-win_amd64.pyd
|   |   |       |   |   |-- _gcutils.py
|   |   |       |   |   |-- _pep440.py
|   |   |       |   |   |-- _sparse.py
|   |   |       |   |   |-- _test_ccallback.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _test_ccallback.cp313-win_amd64.pyd
|   |   |       |   |   |-- _test_deprecation_call.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _test_deprecation_call.cp313-win_amd64.pyd
|   |   |       |   |   |-- _test_deprecation_def.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _test_deprecation_def.cp313-win_amd64.pyd
|   |   |       |   |   |-- _testutils.py
|   |   |       |   |   |-- _threadsafety.py
|   |   |       |   |   |-- _tmpdirs.py
|   |   |       |   |   |-- _util.py
|   |   |       |   |   |-- decorator.py
|   |   |       |   |   |-- deprecation.py
|   |   |       |   |   |-- doccer.py
|   |   |       |   |   |-- messagestream.cp313-win_amd64.dll.a
|   |   |       |   |   |-- messagestream.cp313-win_amd64.pyd
|   |   |       |   |   +-- uarray.py
|   |   |       |   |-- cluster
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- hierarchy.cpython-313.pyc
|   |   |       |   |   |   +-- vq.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- hierarchy_test_data.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_disjoint_set.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hierarchy.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_vq.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- hierarchy_test_data.py
|   |   |       |   |   |   |-- test_disjoint_set.py
|   |   |       |   |   |   |-- test_hierarchy.py
|   |   |       |   |   |   +-- test_vq.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _hierarchy.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _hierarchy.cp313-win_amd64.pyd
|   |   |       |   |   |-- _optimal_leaf_ordering.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _optimal_leaf_ordering.cp313-win_amd64.pyd
|   |   |       |   |   |-- _vq.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _vq.cp313-win_amd64.pyd
|   |   |       |   |   |-- hierarchy.py
|   |   |       |   |   +-- vq.py
|   |   |       |   |-- constants
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _codata.cpython-313.pyc
|   |   |       |   |   |   |-- _constants.cpython-313.pyc
|   |   |       |   |   |   |-- codata.cpython-313.pyc
|   |   |       |   |   |   +-- constants.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_codata.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_constants.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_codata.py
|   |   |       |   |   |   +-- test_constants.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _codata.py
|   |   |       |   |   |-- _constants.py
|   |   |       |   |   |-- codata.py
|   |   |       |   |   +-- constants.py
|   |   |       |   |-- datasets
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _download_all.cpython-313.pyc
|   |   |       |   |   |   |-- _fetchers.cpython-313.pyc
|   |   |       |   |   |   |-- _registry.cpython-313.pyc
|   |   |       |   |   |   +-- _utils.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_data.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   +-- test_data.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _download_all.py
|   |   |       |   |   |-- _fetchers.py
|   |   |       |   |   |-- _registry.py
|   |   |       |   |   +-- _utils.py
|   |   |       |   |-- differentiate
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   +-- _differentiate.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_differentiate.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   +-- test_differentiate.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   +-- _differentiate.py
|   |   |       |   |-- fft
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _backend.cpython-313.pyc
|   |   |       |   |   |   |-- _basic.cpython-313.pyc
|   |   |       |   |   |   |-- _basic_backend.cpython-313.pyc
|   |   |       |   |   |   |-- _debug_backends.cpython-313.pyc
|   |   |       |   |   |   |-- _fftlog.cpython-313.pyc
|   |   |       |   |   |   |-- _fftlog_backend.cpython-313.pyc
|   |   |       |   |   |   |-- _helper.cpython-313.pyc
|   |   |       |   |   |   |-- _realtransforms.cpython-313.pyc
|   |   |       |   |   |   +-- _realtransforms_backend.cpython-313.pyc
|   |   |       |   |   |-- _pocketfft
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- helper.cpython-313.pyc
|   |   |       |   |   |   |   +-- realtransforms.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_basic.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_real_transforms.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- test_basic.py
|   |   |       |   |   |   |   +-- test_real_transforms.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- basic.py
|   |   |       |   |   |   |-- helper.py
|   |   |       |   |   |   |-- LICENSE.md
|   |   |       |   |   |   |-- pypocketfft.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- pypocketfft.cp313-win_amd64.pyd
|   |   |       |   |   |   +-- realtransforms.py
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- mock_backend.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_backend.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fftlog.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_helper.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_multithreading.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_real_transforms.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- mock_backend.py
|   |   |       |   |   |   |-- test_backend.py
|   |   |       |   |   |   |-- test_basic.py
|   |   |       |   |   |   |-- test_fftlog.py
|   |   |       |   |   |   |-- test_helper.py
|   |   |       |   |   |   |-- test_multithreading.py
|   |   |       |   |   |   +-- test_real_transforms.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _backend.py
|   |   |       |   |   |-- _basic.py
|   |   |       |   |   |-- _basic_backend.py
|   |   |       |   |   |-- _debug_backends.py
|   |   |       |   |   |-- _fftlog.py
|   |   |       |   |   |-- _fftlog_backend.py
|   |   |       |   |   |-- _helper.py
|   |   |       |   |   |-- _realtransforms.py
|   |   |       |   |   +-- _realtransforms_backend.py
|   |   |       |   |-- fftpack
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _basic.cpython-313.pyc
|   |   |       |   |   |   |-- _helper.cpython-313.pyc
|   |   |       |   |   |   |-- _pseudo_diffs.cpython-313.pyc
|   |   |       |   |   |   |-- _realtransforms.cpython-313.pyc
|   |   |       |   |   |   |-- basic.cpython-313.pyc
|   |   |       |   |   |   |-- helper.cpython-313.pyc
|   |   |       |   |   |   |-- pseudo_diffs.cpython-313.pyc
|   |   |       |   |   |   +-- realtransforms.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_helper.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_import.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_pseudo_diffs.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_real_transforms.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- fftw_double_ref.npz
|   |   |       |   |   |   |-- fftw_longdouble_ref.npz
|   |   |       |   |   |   |-- fftw_single_ref.npz
|   |   |       |   |   |   |-- test.npz
|   |   |       |   |   |   |-- test_basic.py
|   |   |       |   |   |   |-- test_helper.py
|   |   |       |   |   |   |-- test_import.py
|   |   |       |   |   |   |-- test_pseudo_diffs.py
|   |   |       |   |   |   +-- test_real_transforms.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _basic.py
|   |   |       |   |   |-- _helper.py
|   |   |       |   |   |-- _pseudo_diffs.py
|   |   |       |   |   |-- _realtransforms.py
|   |   |       |   |   |-- basic.py
|   |   |       |   |   |-- convolve.cp313-win_amd64.dll.a
|   |   |       |   |   |-- convolve.cp313-win_amd64.pyd
|   |   |       |   |   |-- helper.py
|   |   |       |   |   |-- pseudo_diffs.py
|   |   |       |   |   +-- realtransforms.py
|   |   |       |   |-- integrate
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _bvp.cpython-313.pyc
|   |   |       |   |   |   |-- _cubature.cpython-313.pyc
|   |   |       |   |   |   |-- _lebedev.cpython-313.pyc
|   |   |       |   |   |   |-- _ode.cpython-313.pyc
|   |   |       |   |   |   |-- _odepack_py.cpython-313.pyc
|   |   |       |   |   |   |-- _quad_vec.cpython-313.pyc
|   |   |       |   |   |   |-- _quadpack_py.cpython-313.pyc
|   |   |       |   |   |   |-- _quadrature.cpython-313.pyc
|   |   |       |   |   |   |-- _tanhsinh.cpython-313.pyc
|   |   |       |   |   |   |-- dop.cpython-313.pyc
|   |   |       |   |   |   |-- lsoda.cpython-313.pyc
|   |   |       |   |   |   |-- odepack.cpython-313.pyc
|   |   |       |   |   |   |-- quadpack.cpython-313.pyc
|   |   |       |   |   |   +-- vode.cpython-313.pyc
|   |   |       |   |   |-- _ivp
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- base.cpython-313.pyc
|   |   |       |   |   |   |   |-- bdf.cpython-313.pyc
|   |   |       |   |   |   |   |-- common.cpython-313.pyc
|   |   |       |   |   |   |   |-- dop853_coefficients.cpython-313.pyc
|   |   |       |   |   |   |   |-- ivp.cpython-313.pyc
|   |   |       |   |   |   |   |-- lsoda.cpython-313.pyc
|   |   |       |   |   |   |   |-- radau.cpython-313.pyc
|   |   |       |   |   |   |   +-- rk.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_ivp.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_rk.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- test_ivp.py
|   |   |       |   |   |   |   +-- test_rk.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- base.py
|   |   |       |   |   |   |-- bdf.py
|   |   |       |   |   |   |-- common.py
|   |   |       |   |   |   |-- dop853_coefficients.py
|   |   |       |   |   |   |-- ivp.py
|   |   |       |   |   |   |-- lsoda.py
|   |   |       |   |   |   |-- radau.py
|   |   |       |   |   |   +-- rk.py
|   |   |       |   |   |-- _rules
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _base.cpython-313.pyc
|   |   |       |   |   |   |   |-- _gauss_kronrod.cpython-313.pyc
|   |   |       |   |   |   |   |-- _gauss_legendre.cpython-313.pyc
|   |   |       |   |   |   |   +-- _genz_malik.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _base.py
|   |   |       |   |   |   |-- _gauss_kronrod.py
|   |   |       |   |   |   |-- _gauss_legendre.py
|   |   |       |   |   |   +-- _genz_malik.py
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__quad_vec.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_banded_ode_solvers.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_bvp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cubature.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_integrate.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_odeint_jac.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_quadpack.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_quadrature.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_tanhsinh.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test__quad_vec.py
|   |   |       |   |   |   |-- test_banded_ode_solvers.py
|   |   |       |   |   |   |-- test_bvp.py
|   |   |       |   |   |   |-- test_cubature.py
|   |   |       |   |   |   |-- test_integrate.py
|   |   |       |   |   |   |-- test_odeint_jac.py
|   |   |       |   |   |   |-- test_quadpack.py
|   |   |       |   |   |   |-- test_quadrature.py
|   |   |       |   |   |   +-- test_tanhsinh.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _bvp.py
|   |   |       |   |   |-- _cubature.py
|   |   |       |   |   |-- _dop.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _dop.cp313-win_amd64.pyd
|   |   |       |   |   |-- _lebedev.py
|   |   |       |   |   |-- _lsoda.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _lsoda.cp313-win_amd64.pyd
|   |   |       |   |   |-- _ode.py
|   |   |       |   |   |-- _odepack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _odepack.cp313-win_amd64.pyd
|   |   |       |   |   |-- _odepack_py.py
|   |   |       |   |   |-- _quad_vec.py
|   |   |       |   |   |-- _quadpack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _quadpack.cp313-win_amd64.pyd
|   |   |       |   |   |-- _quadpack_py.py
|   |   |       |   |   |-- _quadrature.py
|   |   |       |   |   |-- _tanhsinh.py
|   |   |       |   |   |-- _test_multivariate.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _test_multivariate.cp313-win_amd64.pyd
|   |   |       |   |   |-- _test_odeint_banded.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _test_odeint_banded.cp313-win_amd64.pyd
|   |   |       |   |   |-- _vode.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _vode.cp313-win_amd64.pyd
|   |   |       |   |   |-- dop.py
|   |   |       |   |   |-- lsoda.py
|   |   |       |   |   |-- odepack.py
|   |   |       |   |   |-- quadpack.py
|   |   |       |   |   +-- vode.py
|   |   |       |   |-- interpolate
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _bary_rational.cpython-313.pyc
|   |   |       |   |   |   |-- _bsplines.cpython-313.pyc
|   |   |       |   |   |   |-- _cubic.cpython-313.pyc
|   |   |       |   |   |   |-- _fitpack_impl.cpython-313.pyc
|   |   |       |   |   |   |-- _fitpack_py.cpython-313.pyc
|   |   |       |   |   |   |-- _fitpack_repro.cpython-313.pyc
|   |   |       |   |   |   |-- _fitpack2.cpython-313.pyc
|   |   |       |   |   |   |-- _interpolate.cpython-313.pyc
|   |   |       |   |   |   |-- _ndbspline.cpython-313.pyc
|   |   |       |   |   |   |-- _ndgriddata.cpython-313.pyc
|   |   |       |   |   |   |-- _pade.cpython-313.pyc
|   |   |       |   |   |   |-- _polyint.cpython-313.pyc
|   |   |       |   |   |   |-- _rbf.cpython-313.pyc
|   |   |       |   |   |   |-- _rbfinterp.cpython-313.pyc
|   |   |       |   |   |   |-- _rgi.cpython-313.pyc
|   |   |       |   |   |   |-- dfitpack.cpython-313.pyc
|   |   |       |   |   |   |-- fitpack.cpython-313.pyc
|   |   |       |   |   |   |-- fitpack2.cpython-313.pyc
|   |   |       |   |   |   |-- interpnd.cpython-313.pyc
|   |   |       |   |   |   |-- interpolate.cpython-313.pyc
|   |   |       |   |   |   |-- ndgriddata.cpython-313.pyc
|   |   |       |   |   |   |-- polyint.cpython-313.pyc
|   |   |       |   |   |   +-- rbf.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_bary_rational.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_bsplines.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fitpack.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fitpack2.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_gil.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_interpnd.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_interpolate.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ndgriddata.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_pade.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_polyint.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_rbf.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_rbfinterp.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_rgi.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- bug-1310.npz
|   |   |       |   |   |   |   |-- estimate_gradients_hang.npy
|   |   |       |   |   |   |   +-- gcvspl.npz
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_bary_rational.py
|   |   |       |   |   |   |-- test_bsplines.py
|   |   |       |   |   |   |-- test_fitpack.py
|   |   |       |   |   |   |-- test_fitpack2.py
|   |   |       |   |   |   |-- test_gil.py
|   |   |       |   |   |   |-- test_interpnd.py
|   |   |       |   |   |   |-- test_interpolate.py
|   |   |       |   |   |   |-- test_ndgriddata.py
|   |   |       |   |   |   |-- test_pade.py
|   |   |       |   |   |   |-- test_polyint.py
|   |   |       |   |   |   |-- test_rbf.py
|   |   |       |   |   |   |-- test_rbfinterp.py
|   |   |       |   |   |   +-- test_rgi.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _bary_rational.py
|   |   |       |   |   |-- _bsplines.py
|   |   |       |   |   |-- _cubic.py
|   |   |       |   |   |-- _dfitpack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _dfitpack.cp313-win_amd64.pyd
|   |   |       |   |   |-- _dierckx.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _dierckx.cp313-win_amd64.pyd
|   |   |       |   |   |-- _fitpack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _fitpack.cp313-win_amd64.pyd
|   |   |       |   |   |-- _fitpack_impl.py
|   |   |       |   |   |-- _fitpack_py.py
|   |   |       |   |   |-- _fitpack_repro.py
|   |   |       |   |   |-- _fitpack2.py
|   |   |       |   |   |-- _interpnd.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _interpnd.cp313-win_amd64.pyd
|   |   |       |   |   |-- _interpolate.py
|   |   |       |   |   |-- _ndbspline.py
|   |   |       |   |   |-- _ndgriddata.py
|   |   |       |   |   |-- _pade.py
|   |   |       |   |   |-- _polyint.py
|   |   |       |   |   |-- _ppoly.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ppoly.cp313-win_amd64.pyd
|   |   |       |   |   |-- _rbf.py
|   |   |       |   |   |-- _rbfinterp.py
|   |   |       |   |   |-- _rbfinterp_pythran.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _rbfinterp_pythran.cp313-win_amd64.pyd
|   |   |       |   |   |-- _rgi.py
|   |   |       |   |   |-- _rgi_cython.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _rgi_cython.cp313-win_amd64.pyd
|   |   |       |   |   |-- dfitpack.py
|   |   |       |   |   |-- fitpack.py
|   |   |       |   |   |-- fitpack2.py
|   |   |       |   |   |-- interpnd.py
|   |   |       |   |   |-- interpolate.py
|   |   |       |   |   |-- ndgriddata.py
|   |   |       |   |   |-- polyint.py
|   |   |       |   |   +-- rbf.py
|   |   |       |   |-- io
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _fortran.cpython-313.pyc
|   |   |       |   |   |   |-- _idl.cpython-313.pyc
|   |   |       |   |   |   |-- _mmio.cpython-313.pyc
|   |   |       |   |   |   |-- _netcdf.cpython-313.pyc
|   |   |       |   |   |   |-- harwell_boeing.cpython-313.pyc
|   |   |       |   |   |   |-- idl.cpython-313.pyc
|   |   |       |   |   |   |-- mmio.cpython-313.pyc
|   |   |       |   |   |   |-- netcdf.cpython-313.pyc
|   |   |       |   |   |   +-- wavfile.cpython-313.pyc
|   |   |       |   |   |-- _fast_matrix_market
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _fmm_core.cp313-win_amd64.dll.a
|   |   |       |   |   |   +-- _fmm_core.cp313-win_amd64.pyd
|   |   |       |   |   |-- _harwell_boeing
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _fortran_format_parser.cpython-313.pyc
|   |   |       |   |   |   |   +-- hb.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_fortran_format.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_hb.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- test_fortran_format.py
|   |   |       |   |   |   |   +-- test_hb.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _fortran_format_parser.py
|   |   |       |   |   |   +-- hb.py
|   |   |       |   |   |-- arff
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _arffread.cpython-313.pyc
|   |   |       |   |   |   |   +-- arffread.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_arffread.cpython-313.pyc
|   |   |       |   |   |   |   |-- data
|   |   |       |   |   |   |   |   |-- iris.arff
|   |   |       |   |   |   |   |   |-- missing.arff
|   |   |       |   |   |   |   |   |-- nodata.arff
|   |   |       |   |   |   |   |   |-- quoted_nominal.arff
|   |   |       |   |   |   |   |   |-- quoted_nominal_spaces.arff
|   |   |       |   |   |   |   |   |-- test1.arff
|   |   |       |   |   |   |   |   |-- test10.arff
|   |   |       |   |   |   |   |   |-- test11.arff
|   |   |       |   |   |   |   |   |-- test2.arff
|   |   |       |   |   |   |   |   |-- test3.arff
|   |   |       |   |   |   |   |   |-- test4.arff
|   |   |       |   |   |   |   |   |-- test5.arff
|   |   |       |   |   |   |   |   |-- test6.arff
|   |   |       |   |   |   |   |   |-- test7.arff
|   |   |       |   |   |   |   |   |-- test8.arff
|   |   |       |   |   |   |   |   +-- test9.arff
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   +-- test_arffread.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _arffread.py
|   |   |       |   |   |   +-- arffread.py
|   |   |       |   |   |-- matlab
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _byteordercodes.cpython-313.pyc
|   |   |       |   |   |   |   |-- _mio.cpython-313.pyc
|   |   |       |   |   |   |   |-- _mio4.cpython-313.pyc
|   |   |       |   |   |   |   |-- _mio5.cpython-313.pyc
|   |   |       |   |   |   |   |-- _mio5_params.cpython-313.pyc
|   |   |       |   |   |   |   |-- _miobase.cpython-313.pyc
|   |   |       |   |   |   |   |-- byteordercodes.cpython-313.pyc
|   |   |       |   |   |   |   |-- mio.cpython-313.pyc
|   |   |       |   |   |   |   |-- mio_utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- mio4.cpython-313.pyc
|   |   |       |   |   |   |   |-- mio5.cpython-313.pyc
|   |   |       |   |   |   |   |-- mio5_params.cpython-313.pyc
|   |   |       |   |   |   |   |-- mio5_utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- miobase.cpython-313.pyc
|   |   |       |   |   |   |   +-- streams.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_byteordercodes.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_mio.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_mio_funcs.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_mio_utils.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_mio5_utils.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_miobase.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_pathological.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_streams.cpython-313.pyc
|   |   |       |   |   |   |   |-- data
|   |   |       |   |   |   |   |   |-- bad_miuint32.mat
|   |   |       |   |   |   |   |   |-- bad_miutf8_array_name.mat
|   |   |       |   |   |   |   |   |-- big_endian.mat
|   |   |       |   |   |   |   |   |-- broken_utf8.mat
|   |   |       |   |   |   |   |   |-- corrupted_zlib_checksum.mat
|   |   |       |   |   |   |   |   |-- corrupted_zlib_data.mat
|   |   |       |   |   |   |   |   |-- debigged_m4.mat
|   |   |       |   |   |   |   |   |-- japanese_utf8.txt
|   |   |       |   |   |   |   |   |-- little_endian.mat
|   |   |       |   |   |   |   |   |-- logical_sparse.mat
|   |   |       |   |   |   |   |   |-- malformed1.mat
|   |   |       |   |   |   |   |   |-- miuint32_for_miint32.mat
|   |   |       |   |   |   |   |   |-- miutf8_array_name.mat
|   |   |       |   |   |   |   |   |-- nasty_duplicate_fieldnames.mat
|   |   |       |   |   |   |   |   |-- one_by_zero_char.mat
|   |   |       |   |   |   |   |   |-- parabola.mat
|   |   |       |   |   |   |   |   |-- single_empty_string.mat
|   |   |       |   |   |   |   |   |-- some_functions.mat
|   |   |       |   |   |   |   |   |-- sqr.mat
|   |   |       |   |   |   |   |   |-- test_empty_struct.mat
|   |   |       |   |   |   |   |   |-- test_mat4_le_floats.mat
|   |   |       |   |   |   |   |   |-- test_skip_variable.mat
|   |   |       |   |   |   |   |   |-- test3dmatrix_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- test3dmatrix_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- test3dmatrix_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- test3dmatrix_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testbool_8_WIN64.mat
|   |   |       |   |   |   |   |   |-- testcell_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testcell_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcell_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcell_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcellnest_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testcellnest_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcellnest_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcellnest_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcomplex_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testcomplex_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testcomplex_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcomplex_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testcomplex_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testdouble_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testdouble_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testdouble_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testdouble_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testdouble_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testemptycell_5.3_SOL2.mat
|   |   |       |   |   |   |   |   |-- testemptycell_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testemptycell_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testemptycell_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testfunc_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testhdf5_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testmatrix_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testmatrix_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testmatrix_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testmatrix_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testmatrix_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testminus_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testminus_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testminus_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testminus_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testminus_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testmulti_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testmulti_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testmulti_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testobject_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testobject_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testobject_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testobject_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testonechar_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testonechar_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testonechar_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testonechar_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testonechar_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testscalarcell_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testsimplecell.mat
|   |   |       |   |   |   |   |   |-- testsparse_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testsparse_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testsparse_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testsparse_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testsparse_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testsparsecomplex_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- testsparsecomplex_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- testsparsecomplex_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testsparsecomplex_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testsparsecomplex_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testsparsefloat_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststring_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- teststring_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- teststring_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststring_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststring_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststringarray_4.2c_SOL2.mat
|   |   |       |   |   |   |   |   |-- teststringarray_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- teststringarray_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststringarray_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststringarray_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststruct_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- teststruct_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststruct_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststruct_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststructarr_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- teststructarr_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststructarr_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststructarr_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststructnest_6.1_SOL2.mat
|   |   |       |   |   |   |   |   |-- teststructnest_6.5.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststructnest_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- teststructnest_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testunicode_7.1_GLNX86.mat
|   |   |       |   |   |   |   |   |-- testunicode_7.4_GLNX86.mat
|   |   |       |   |   |   |   |   +-- testvec_4_GLNX86.mat
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- test_byteordercodes.py
|   |   |       |   |   |   |   |-- test_mio.py
|   |   |       |   |   |   |   |-- test_mio_funcs.py
|   |   |       |   |   |   |   |-- test_mio_utils.py
|   |   |       |   |   |   |   |-- test_mio5_utils.py
|   |   |       |   |   |   |   |-- test_miobase.py
|   |   |       |   |   |   |   |-- test_pathological.py
|   |   |       |   |   |   |   +-- test_streams.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _byteordercodes.py
|   |   |       |   |   |   |-- _mio.py
|   |   |       |   |   |   |-- _mio_utils.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _mio_utils.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _mio4.py
|   |   |       |   |   |   |-- _mio5.py
|   |   |       |   |   |   |-- _mio5_params.py
|   |   |       |   |   |   |-- _mio5_utils.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _mio5_utils.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _miobase.py
|   |   |       |   |   |   |-- _streams.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _streams.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- byteordercodes.py
|   |   |       |   |   |   |-- mio.py
|   |   |       |   |   |   |-- mio_utils.py
|   |   |       |   |   |   |-- mio4.py
|   |   |       |   |   |   |-- mio5.py
|   |   |       |   |   |   |-- mio5_params.py
|   |   |       |   |   |   |-- mio5_utils.py
|   |   |       |   |   |   |-- miobase.py
|   |   |       |   |   |   +-- streams.py
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fortran.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_idl.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mmio.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_netcdf.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_paths.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_wavfile.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- array_float32_1d.sav
|   |   |       |   |   |   |   |-- array_float32_2d.sav
|   |   |       |   |   |   |   |-- array_float32_3d.sav
|   |   |       |   |   |   |   |-- array_float32_4d.sav
|   |   |       |   |   |   |   |-- array_float32_5d.sav
|   |   |       |   |   |   |   |-- array_float32_6d.sav
|   |   |       |   |   |   |   |-- array_float32_7d.sav
|   |   |       |   |   |   |   |-- array_float32_8d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_1d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_2d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_3d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_4d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_5d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_6d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_7d.sav
|   |   |       |   |   |   |   |-- array_float32_pointer_8d.sav
|   |   |       |   |   |   |   |-- example_1.nc
|   |   |       |   |   |   |   |-- example_2.nc
|   |   |       |   |   |   |   |-- example_3_maskedvals.nc
|   |   |       |   |   |   |   |-- fortran-3x3d-2i.dat
|   |   |       |   |   |   |   |-- fortran-mixed.dat
|   |   |       |   |   |   |   |-- fortran-sf8-11x1x10.dat
|   |   |       |   |   |   |   |-- fortran-sf8-15x10x22.dat
|   |   |       |   |   |   |   |-- fortran-sf8-1x1x1.dat
|   |   |       |   |   |   |   |-- fortran-sf8-1x1x5.dat
|   |   |       |   |   |   |   |-- fortran-sf8-1x1x7.dat
|   |   |       |   |   |   |   |-- fortran-sf8-1x3x5.dat
|   |   |       |   |   |   |   |-- fortran-si4-11x1x10.dat
|   |   |       |   |   |   |   |-- fortran-si4-15x10x22.dat
|   |   |       |   |   |   |   |-- fortran-si4-1x1x1.dat
|   |   |       |   |   |   |   |-- fortran-si4-1x1x5.dat
|   |   |       |   |   |   |   |-- fortran-si4-1x1x7.dat
|   |   |       |   |   |   |   |-- fortran-si4-1x3x5.dat
|   |   |       |   |   |   |   |-- invalid_pointer.sav
|   |   |       |   |   |   |   |-- null_pointer.sav
|   |   |       |   |   |   |   |-- scalar_byte.sav
|   |   |       |   |   |   |   |-- scalar_byte_descr.sav
|   |   |       |   |   |   |   |-- scalar_complex32.sav
|   |   |       |   |   |   |   |-- scalar_complex64.sav
|   |   |       |   |   |   |   |-- scalar_float32.sav
|   |   |       |   |   |   |   |-- scalar_float64.sav
|   |   |       |   |   |   |   |-- scalar_heap_pointer.sav
|   |   |       |   |   |   |   |-- scalar_int16.sav
|   |   |       |   |   |   |   |-- scalar_int32.sav
|   |   |       |   |   |   |   |-- scalar_int64.sav
|   |   |       |   |   |   |   |-- scalar_string.sav
|   |   |       |   |   |   |   |-- scalar_uint16.sav
|   |   |       |   |   |   |   |-- scalar_uint32.sav
|   |   |       |   |   |   |   |-- scalar_uint64.sav
|   |   |       |   |   |   |   |-- struct_arrays.sav
|   |   |       |   |   |   |   |-- struct_arrays_byte_idl80.sav
|   |   |       |   |   |   |   |-- struct_arrays_replicated.sav
|   |   |       |   |   |   |   |-- struct_arrays_replicated_3d.sav
|   |   |       |   |   |   |   |-- struct_inherit.sav
|   |   |       |   |   |   |   |-- struct_pointer_arrays.sav
|   |   |       |   |   |   |   |-- struct_pointer_arrays_replicated.sav
|   |   |       |   |   |   |   |-- struct_pointer_arrays_replicated_3d.sav
|   |   |       |   |   |   |   |-- struct_pointers.sav
|   |   |       |   |   |   |   |-- struct_pointers_replicated.sav
|   |   |       |   |   |   |   |-- struct_pointers_replicated_3d.sav
|   |   |       |   |   |   |   |-- struct_scalars.sav
|   |   |       |   |   |   |   |-- struct_scalars_replicated.sav
|   |   |       |   |   |   |   |-- struct_scalars_replicated_3d.sav
|   |   |       |   |   |   |   |-- test-1234Hz-le-1ch-10S-20bit-extra.wav
|   |   |       |   |   |   |   |-- test-44100Hz-2ch-32bit-float-be.wav
|   |   |       |   |   |   |   |-- test-44100Hz-2ch-32bit-float-le.wav
|   |   |       |   |   |   |   |-- test-44100Hz-be-1ch-4bytes.wav
|   |   |       |   |   |   |   |-- test-44100Hz-le-1ch-4bytes.wav
|   |   |       |   |   |   |   |-- test-44100Hz-le-1ch-4bytes-early-eof.wav
|   |   |       |   |   |   |   |-- test-44100Hz-le-1ch-4bytes-early-eof-no-data.wav
|   |   |       |   |   |   |   |-- test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
|   |   |       |   |   |   |   |-- test-44100Hz-le-1ch-4bytes-rf64.wav
|   |   |       |   |   |   |   |-- test-48000Hz-2ch-64bit-float-le-wavex.wav
|   |   |       |   |   |   |   |-- test-8000Hz-be-3ch-5S-24bit.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-1ch-1byte-ulaw.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-2ch-1byteu.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-3ch-5S-24bit.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-3ch-5S-24bit-inconsistent.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-3ch-5S-24bit-rf64.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-3ch-5S-36bit.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-3ch-5S-45bit.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-3ch-5S-53bit.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-3ch-5S-64bit.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-4ch-9S-12bit.wav
|   |   |       |   |   |   |   |-- test-8000Hz-le-5ch-9S-5bit.wav
|   |   |       |   |   |   |   |-- Transparent Busy.ani
|   |   |       |   |   |   |   +-- various_compressed.sav
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_fortran.py
|   |   |       |   |   |   |-- test_idl.py
|   |   |       |   |   |   |-- test_mmio.py
|   |   |       |   |   |   |-- test_netcdf.py
|   |   |       |   |   |   |-- test_paths.py
|   |   |       |   |   |   +-- test_wavfile.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _fortran.py
|   |   |       |   |   |-- _idl.py
|   |   |       |   |   |-- _mmio.py
|   |   |       |   |   |-- _netcdf.py
|   |   |       |   |   |-- _test_fortran.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _test_fortran.cp313-win_amd64.pyd
|   |   |       |   |   |-- harwell_boeing.py
|   |   |       |   |   |-- idl.py
|   |   |       |   |   |-- mmio.py
|   |   |       |   |   |-- netcdf.py
|   |   |       |   |   +-- wavfile.py
|   |   |       |   |-- linalg
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _basic.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_cholesky.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_cossin.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_ldl.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_lu.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_polar.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_qr.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_qz.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_schur.cpython-313.pyc
|   |   |       |   |   |   |-- _decomp_svd.cpython-313.pyc
|   |   |       |   |   |   |-- _expm_frechet.cpython-313.pyc
|   |   |       |   |   |   |-- _matfuncs.cpython-313.pyc
|   |   |       |   |   |   |-- _matfuncs_inv_ssq.cpython-313.pyc
|   |   |       |   |   |   |-- _matfuncs_sqrtm.cpython-313.pyc
|   |   |       |   |   |   |-- _misc.cpython-313.pyc
|   |   |       |   |   |   |-- _procrustes.cpython-313.pyc
|   |   |       |   |   |   |-- _sketches.cpython-313.pyc
|   |   |       |   |   |   |-- _solvers.cpython-313.pyc
|   |   |       |   |   |   |-- _special_matrices.cpython-313.pyc
|   |   |       |   |   |   |-- _testutils.cpython-313.pyc
|   |   |       |   |   |   |-- basic.cpython-313.pyc
|   |   |       |   |   |   |-- blas.cpython-313.pyc
|   |   |       |   |   |   |-- decomp.cpython-313.pyc
|   |   |       |   |   |   |-- decomp_cholesky.cpython-313.pyc
|   |   |       |   |   |   |-- decomp_lu.cpython-313.pyc
|   |   |       |   |   |   |-- decomp_qr.cpython-313.pyc
|   |   |       |   |   |   |-- decomp_schur.cpython-313.pyc
|   |   |       |   |   |   |-- decomp_svd.cpython-313.pyc
|   |   |       |   |   |   |-- interpolative.cpython-313.pyc
|   |   |       |   |   |   |-- lapack.cpython-313.pyc
|   |   |       |   |   |   |-- matfuncs.cpython-313.pyc
|   |   |       |   |   |   |-- misc.cpython-313.pyc
|   |   |       |   |   |   +-- special_matrices.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_batch.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_blas.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cython_blas.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cython_lapack.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cythonized_array_utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_decomp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_decomp_cholesky.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_decomp_cossin.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_decomp_ldl.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_decomp_lu.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_decomp_polar.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_decomp_update.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_extending.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fblas.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_interpolative.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_lapack.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_matfuncs.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_matmul_toeplitz.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_procrustes.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_sketches.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_solve_toeplitz.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_solvers.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_special_matrices.cpython-313.pyc
|   |   |       |   |   |   |-- _cython_examples
|   |   |       |   |   |   |   |-- extending.pyx
|   |   |       |   |   |   |   +-- meson.build
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- carex_15_data.npz
|   |   |       |   |   |   |   |-- carex_18_data.npz
|   |   |       |   |   |   |   |-- carex_19_data.npz
|   |   |       |   |   |   |   |-- carex_20_data.npz
|   |   |       |   |   |   |   |-- carex_6_data.npz
|   |   |       |   |   |   |   +-- gendare_20170120_data.npz
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_basic.py
|   |   |       |   |   |   |-- test_batch.py
|   |   |       |   |   |   |-- test_blas.py
|   |   |       |   |   |   |-- test_cython_blas.py
|   |   |       |   |   |   |-- test_cython_lapack.py
|   |   |       |   |   |   |-- test_cythonized_array_utils.py
|   |   |       |   |   |   |-- test_decomp.py
|   |   |       |   |   |   |-- test_decomp_cholesky.py
|   |   |       |   |   |   |-- test_decomp_cossin.py
|   |   |       |   |   |   |-- test_decomp_ldl.py
|   |   |       |   |   |   |-- test_decomp_lu.py
|   |   |       |   |   |   |-- test_decomp_polar.py
|   |   |       |   |   |   |-- test_decomp_update.py
|   |   |       |   |   |   |-- test_extending.py
|   |   |       |   |   |   |-- test_fblas.py
|   |   |       |   |   |   |-- test_interpolative.py
|   |   |       |   |   |   |-- test_lapack.py
|   |   |       |   |   |   |-- test_matfuncs.py
|   |   |       |   |   |   |-- test_matmul_toeplitz.py
|   |   |       |   |   |   |-- test_procrustes.py
|   |   |       |   |   |   |-- test_sketches.py
|   |   |       |   |   |   |-- test_solve_toeplitz.py
|   |   |       |   |   |   |-- test_solvers.py
|   |   |       |   |   |   +-- test_special_matrices.py
|   |   |       |   |   |-- __init__.pxd
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _basic.py
|   |   |       |   |   |-- _blas_subroutines.h
|   |   |       |   |   |-- _cythonized_array_utils.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _cythonized_array_utils.cp313-win_amd64.pyd
|   |   |       |   |   |-- _cythonized_array_utils.pxd
|   |   |       |   |   |-- _cythonized_array_utils.pyi
|   |   |       |   |   |-- _decomp.py
|   |   |       |   |   |-- _decomp_cholesky.py
|   |   |       |   |   |-- _decomp_cossin.py
|   |   |       |   |   |-- _decomp_interpolative.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _decomp_interpolative.cp313-win_amd64.pyd
|   |   |       |   |   |-- _decomp_ldl.py
|   |   |       |   |   |-- _decomp_lu.py
|   |   |       |   |   |-- _decomp_lu_cython.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _decomp_lu_cython.cp313-win_amd64.pyd
|   |   |       |   |   |-- _decomp_lu_cython.pyi
|   |   |       |   |   |-- _decomp_polar.py
|   |   |       |   |   |-- _decomp_qr.py
|   |   |       |   |   |-- _decomp_qz.py
|   |   |       |   |   |-- _decomp_schur.py
|   |   |       |   |   |-- _decomp_svd.py
|   |   |       |   |   |-- _decomp_update.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _decomp_update.cp313-win_amd64.pyd
|   |   |       |   |   |-- _expm_frechet.py
|   |   |       |   |   |-- _fblas.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _fblas.cp313-win_amd64.pyd
|   |   |       |   |   |-- _flapack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _flapack.cp313-win_amd64.pyd
|   |   |       |   |   |-- _lapack_subroutines.h
|   |   |       |   |   |-- _linalg_pythran.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _linalg_pythran.cp313-win_amd64.pyd
|   |   |       |   |   |-- _matfuncs.py
|   |   |       |   |   |-- _matfuncs_expm.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _matfuncs_expm.cp313-win_amd64.pyd
|   |   |       |   |   |-- _matfuncs_expm.pyi
|   |   |       |   |   |-- _matfuncs_inv_ssq.py
|   |   |       |   |   |-- _matfuncs_schur_sqrtm.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _matfuncs_schur_sqrtm.cp313-win_amd64.pyd
|   |   |       |   |   |-- _matfuncs_sqrtm.py
|   |   |       |   |   |-- _matfuncs_sqrtm_triu.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _matfuncs_sqrtm_triu.cp313-win_amd64.pyd
|   |   |       |   |   |-- _misc.py
|   |   |       |   |   |-- _procrustes.py
|   |   |       |   |   |-- _sketches.py
|   |   |       |   |   |-- _solve_toeplitz.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _solve_toeplitz.cp313-win_amd64.pyd
|   |   |       |   |   |-- _solvers.py
|   |   |       |   |   |-- _special_matrices.py
|   |   |       |   |   |-- _testutils.py
|   |   |       |   |   |-- basic.py
|   |   |       |   |   |-- blas.py
|   |   |       |   |   |-- cython_blas.cp313-win_amd64.dll.a
|   |   |       |   |   |-- cython_blas.cp313-win_amd64.pyd
|   |   |       |   |   |-- cython_blas.pxd
|   |   |       |   |   |-- cython_blas.pyx
|   |   |       |   |   |-- cython_lapack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- cython_lapack.cp313-win_amd64.pyd
|   |   |       |   |   |-- cython_lapack.pxd
|   |   |       |   |   |-- cython_lapack.pyx
|   |   |       |   |   |-- decomp.py
|   |   |       |   |   |-- decomp_cholesky.py
|   |   |       |   |   |-- decomp_lu.py
|   |   |       |   |   |-- decomp_qr.py
|   |   |       |   |   |-- decomp_schur.py
|   |   |       |   |   |-- decomp_svd.py
|   |   |       |   |   |-- interpolative.py
|   |   |       |   |   |-- lapack.py
|   |   |       |   |   |-- matfuncs.py
|   |   |       |   |   |-- misc.py
|   |   |       |   |   +-- special_matrices.py
|   |   |       |   |-- misc
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- common.cpython-313.pyc
|   |   |       |   |   |   +-- doccer.cpython-313.pyc
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- common.py
|   |   |       |   |   +-- doccer.py
|   |   |       |   |-- ndimage
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _delegators.cpython-313.pyc
|   |   |       |   |   |   |-- _filters.cpython-313.pyc
|   |   |       |   |   |   |-- _fourier.cpython-313.pyc
|   |   |       |   |   |   |-- _interpolation.cpython-313.pyc
|   |   |       |   |   |   |-- _measurements.cpython-313.pyc
|   |   |       |   |   |   |-- _morphology.cpython-313.pyc
|   |   |       |   |   |   |-- _ndimage_api.cpython-313.pyc
|   |   |       |   |   |   |-- _ni_docstrings.cpython-313.pyc
|   |   |       |   |   |   |-- _ni_support.cpython-313.pyc
|   |   |       |   |   |   |-- _support_alternative_backends.cpython-313.pyc
|   |   |       |   |   |   |-- filters.cpython-313.pyc
|   |   |       |   |   |   |-- fourier.cpython-313.pyc
|   |   |       |   |   |   |-- interpolation.cpython-313.pyc
|   |   |       |   |   |   |-- measurements.cpython-313.pyc
|   |   |       |   |   |   +-- morphology.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_c_api.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_datatypes.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_filters.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fourier.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_interpolation.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_measurements.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_morphology.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ni_support.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_splines.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- label_inputs.txt
|   |   |       |   |   |   |   |-- label_results.txt
|   |   |       |   |   |   |   +-- label_strels.txt
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- dots.png
|   |   |       |   |   |   |-- test_c_api.py
|   |   |       |   |   |   |-- test_datatypes.py
|   |   |       |   |   |   |-- test_filters.py
|   |   |       |   |   |   |-- test_fourier.py
|   |   |       |   |   |   |-- test_interpolation.py
|   |   |       |   |   |   |-- test_measurements.py
|   |   |       |   |   |   |-- test_morphology.py
|   |   |       |   |   |   |-- test_ni_support.py
|   |   |       |   |   |   +-- test_splines.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _ctest.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ctest.cp313-win_amd64.pyd
|   |   |       |   |   |-- _cytest.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _cytest.cp313-win_amd64.pyd
|   |   |       |   |   |-- _delegators.py
|   |   |       |   |   |-- _filters.py
|   |   |       |   |   |-- _fourier.py
|   |   |       |   |   |-- _interpolation.py
|   |   |       |   |   |-- _measurements.py
|   |   |       |   |   |-- _morphology.py
|   |   |       |   |   |-- _nd_image.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _nd_image.cp313-win_amd64.pyd
|   |   |       |   |   |-- _ndimage_api.py
|   |   |       |   |   |-- _ni_docstrings.py
|   |   |       |   |   |-- _ni_label.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ni_label.cp313-win_amd64.pyd
|   |   |       |   |   |-- _ni_support.py
|   |   |       |   |   |-- _rank_filter_1d.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _rank_filter_1d.cp313-win_amd64.pyd
|   |   |       |   |   |-- _support_alternative_backends.py
|   |   |       |   |   |-- filters.py
|   |   |       |   |   |-- fourier.py
|   |   |       |   |   |-- interpolation.py
|   |   |       |   |   |-- measurements.py
|   |   |       |   |   +-- morphology.py
|   |   |       |   |-- odr
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _add_newdocs.cpython-313.pyc
|   |   |       |   |   |   |-- _models.cpython-313.pyc
|   |   |       |   |   |   |-- _odrpack.cpython-313.pyc
|   |   |       |   |   |   |-- models.cpython-313.pyc
|   |   |       |   |   |   +-- odrpack.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_odr.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   +-- test_odr.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- __odrpack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- __odrpack.cp313-win_amd64.pyd
|   |   |       |   |   |-- _add_newdocs.py
|   |   |       |   |   |-- _models.py
|   |   |       |   |   |-- _odrpack.py
|   |   |       |   |   |-- models.py
|   |   |       |   |   +-- odrpack.py
|   |   |       |   |-- optimize
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _basinhopping.cpython-313.pyc
|   |   |       |   |   |   |-- _bracket.cpython-313.pyc
|   |   |       |   |   |   |-- _chandrupatla.cpython-313.pyc
|   |   |       |   |   |   |-- _cobyla_py.cpython-313.pyc
|   |   |       |   |   |   |-- _cobyqa_py.cpython-313.pyc
|   |   |       |   |   |   |-- _constraints.cpython-313.pyc
|   |   |       |   |   |   |-- _dcsrch.cpython-313.pyc
|   |   |       |   |   |   |-- _differentiable_functions.cpython-313.pyc
|   |   |       |   |   |   |-- _differentialevolution.cpython-313.pyc
|   |   |       |   |   |   |-- _direct_py.cpython-313.pyc
|   |   |       |   |   |   |-- _dual_annealing.cpython-313.pyc
|   |   |       |   |   |   |-- _elementwise.cpython-313.pyc
|   |   |       |   |   |   |-- _hessian_update_strategy.cpython-313.pyc
|   |   |       |   |   |   |-- _isotonic.cpython-313.pyc
|   |   |       |   |   |   |-- _lbfgsb_py.cpython-313.pyc
|   |   |       |   |   |   |-- _linesearch.cpython-313.pyc
|   |   |       |   |   |   |-- _linprog.cpython-313.pyc
|   |   |       |   |   |   |-- _linprog_doc.cpython-313.pyc
|   |   |       |   |   |   |-- _linprog_highs.cpython-313.pyc
|   |   |       |   |   |   |-- _linprog_ip.cpython-313.pyc
|   |   |       |   |   |   |-- _linprog_rs.cpython-313.pyc
|   |   |       |   |   |   |-- _linprog_simplex.cpython-313.pyc
|   |   |       |   |   |   |-- _linprog_util.cpython-313.pyc
|   |   |       |   |   |   |-- _milp.cpython-313.pyc
|   |   |       |   |   |   |-- _minimize.cpython-313.pyc
|   |   |       |   |   |   |-- _minpack_py.cpython-313.pyc
|   |   |       |   |   |   |-- _nnls.cpython-313.pyc
|   |   |       |   |   |   |-- _nonlin.cpython-313.pyc
|   |   |       |   |   |   |-- _numdiff.cpython-313.pyc
|   |   |       |   |   |   |-- _optimize.cpython-313.pyc
|   |   |       |   |   |   |-- _qap.cpython-313.pyc
|   |   |       |   |   |   |-- _remove_redundancy.cpython-313.pyc
|   |   |       |   |   |   |-- _root.cpython-313.pyc
|   |   |       |   |   |   |-- _root_scalar.cpython-313.pyc
|   |   |       |   |   |   |-- _shgo.cpython-313.pyc
|   |   |       |   |   |   |-- _slsqp_py.cpython-313.pyc
|   |   |       |   |   |   |-- _spectral.cpython-313.pyc
|   |   |       |   |   |   |-- _tnc.cpython-313.pyc
|   |   |       |   |   |   |-- _trustregion.cpython-313.pyc
|   |   |       |   |   |   |-- _trustregion_dogleg.cpython-313.pyc
|   |   |       |   |   |   |-- _trustregion_exact.cpython-313.pyc
|   |   |       |   |   |   |-- _trustregion_krylov.cpython-313.pyc
|   |   |       |   |   |   |-- _trustregion_ncg.cpython-313.pyc
|   |   |       |   |   |   |-- _tstutils.cpython-313.pyc
|   |   |       |   |   |   |-- _zeros_py.cpython-313.pyc
|   |   |       |   |   |   |-- cobyla.cpython-313.pyc
|   |   |       |   |   |   |-- elementwise.cpython-313.pyc
|   |   |       |   |   |   |-- lbfgsb.cpython-313.pyc
|   |   |       |   |   |   |-- linesearch.cpython-313.pyc
|   |   |       |   |   |   |-- minpack.cpython-313.pyc
|   |   |       |   |   |   |-- minpack2.cpython-313.pyc
|   |   |       |   |   |   |-- moduleTNC.cpython-313.pyc
|   |   |       |   |   |   |-- nonlin.cpython-313.pyc
|   |   |       |   |   |   |-- optimize.cpython-313.pyc
|   |   |       |   |   |   |-- slsqp.cpython-313.pyc
|   |   |       |   |   |   |-- tnc.cpython-313.pyc
|   |   |       |   |   |   +-- zeros.cpython-313.pyc
|   |   |       |   |   |-- _highspy
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   +-- _highs_wrapper.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _core.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _core.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _highs_options.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _highs_options.cp313-win_amd64.pyd
|   |   |       |   |   |   +-- _highs_wrapper.py
|   |   |       |   |   |-- _lsq
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- bvls.cpython-313.pyc
|   |   |       |   |   |   |   |-- common.cpython-313.pyc
|   |   |       |   |   |   |   |-- dogbox.cpython-313.pyc
|   |   |       |   |   |   |   |-- least_squares.cpython-313.pyc
|   |   |       |   |   |   |   |-- lsq_linear.cpython-313.pyc
|   |   |       |   |   |   |   |-- trf.cpython-313.pyc
|   |   |       |   |   |   |   +-- trf_linear.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- bvls.py
|   |   |       |   |   |   |-- common.py
|   |   |       |   |   |   |-- dogbox.py
|   |   |       |   |   |   |-- givens_elimination.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- givens_elimination.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- least_squares.py
|   |   |       |   |   |   |-- lsq_linear.py
|   |   |       |   |   |   |-- trf.py
|   |   |       |   |   |   +-- trf_linear.py
|   |   |       |   |   |-- _shgo_lib
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _complex.cpython-313.pyc
|   |   |       |   |   |   |   +-- _vertex.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _complex.py
|   |   |       |   |   |   +-- _vertex.py
|   |   |       |   |   |-- _trlib
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _trlib.cp313-win_amd64.dll.a
|   |   |       |   |   |   +-- _trlib.cp313-win_amd64.pyd
|   |   |       |   |   |-- _trustregion_constr
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- canonical_constraint.cpython-313.pyc
|   |   |       |   |   |   |   |-- equality_constrained_sqp.cpython-313.pyc
|   |   |       |   |   |   |   |-- minimize_trustregion_constr.cpython-313.pyc
|   |   |       |   |   |   |   |-- projections.cpython-313.pyc
|   |   |       |   |   |   |   |-- qp_subproblem.cpython-313.pyc
|   |   |       |   |   |   |   |-- report.cpython-313.pyc
|   |   |       |   |   |   |   +-- tr_interior_point.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_canonical_constraint.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_nested_minimize.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_projections.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_qp_subproblem.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_report.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- test_canonical_constraint.py
|   |   |       |   |   |   |   |-- test_nested_minimize.py
|   |   |       |   |   |   |   |-- test_projections.py
|   |   |       |   |   |   |   |-- test_qp_subproblem.py
|   |   |       |   |   |   |   +-- test_report.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- canonical_constraint.py
|   |   |       |   |   |   |-- equality_constrained_sqp.py
|   |   |       |   |   |   |-- minimize_trustregion_constr.py
|   |   |       |   |   |   |-- projections.py
|   |   |       |   |   |   |-- qp_subproblem.py
|   |   |       |   |   |   |-- report.py
|   |   |       |   |   |   +-- tr_interior_point.py
|   |   |       |   |   |-- cython_optimize
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _zeros.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _zeros.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _zeros.pxd
|   |   |       |   |   |   +-- c_zeros.pxd
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__basinhopping.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__differential_evolution.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__dual_annealing.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__linprog_clean_inputs.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__numdiff.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__remove_redundancy.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__root.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__shgo.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__spectral.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_bracket.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_chandrupatla.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cobyla.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cobyqa.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_constraint_conversion.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_constraints.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cython_optimize.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_differentiable_functions.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_direct.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_extending.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hessian_update_strategy.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_isotonic_regression.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_lbfgsb_hessinv.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_lbfgsb_setulb.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_least_squares.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_linear_assignment.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_linesearch.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_linprog.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_lsq_common.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_lsq_linear.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_milp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_minimize_constrained.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_minpack.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_nnls.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_nonlin.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_optimize.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_quadratic_assignment.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_regression.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_slsqp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_tnc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_trustregion.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_trustregion_exact.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_trustregion_krylov.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_zeros.cpython-313.pyc
|   |   |       |   |   |   |-- _cython_examples
|   |   |       |   |   |   |   |-- extending.pyx
|   |   |       |   |   |   |   +-- meson.build
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test__basinhopping.py
|   |   |       |   |   |   |-- test__differential_evolution.py
|   |   |       |   |   |   |-- test__dual_annealing.py
|   |   |       |   |   |   |-- test__linprog_clean_inputs.py
|   |   |       |   |   |   |-- test__numdiff.py
|   |   |       |   |   |   |-- test__remove_redundancy.py
|   |   |       |   |   |   |-- test__root.py
|   |   |       |   |   |   |-- test__shgo.py
|   |   |       |   |   |   |-- test__spectral.py
|   |   |       |   |   |   |-- test_bracket.py
|   |   |       |   |   |   |-- test_chandrupatla.py
|   |   |       |   |   |   |-- test_cobyla.py
|   |   |       |   |   |   |-- test_cobyqa.py
|   |   |       |   |   |   |-- test_constraint_conversion.py
|   |   |       |   |   |   |-- test_constraints.py
|   |   |       |   |   |   |-- test_cython_optimize.py
|   |   |       |   |   |   |-- test_differentiable_functions.py
|   |   |       |   |   |   |-- test_direct.py
|   |   |       |   |   |   |-- test_extending.py
|   |   |       |   |   |   |-- test_hessian_update_strategy.py
|   |   |       |   |   |   |-- test_isotonic_regression.py
|   |   |       |   |   |   |-- test_lbfgsb_hessinv.py
|   |   |       |   |   |   |-- test_lbfgsb_setulb.py
|   |   |       |   |   |   |-- test_least_squares.py
|   |   |       |   |   |   |-- test_linear_assignment.py
|   |   |       |   |   |   |-- test_linesearch.py
|   |   |       |   |   |   |-- test_linprog.py
|   |   |       |   |   |   |-- test_lsq_common.py
|   |   |       |   |   |   |-- test_lsq_linear.py
|   |   |       |   |   |   |-- test_milp.py
|   |   |       |   |   |   |-- test_minimize_constrained.py
|   |   |       |   |   |   |-- test_minpack.py
|   |   |       |   |   |   |-- test_nnls.py
|   |   |       |   |   |   |-- test_nonlin.py
|   |   |       |   |   |   |-- test_optimize.py
|   |   |       |   |   |   |-- test_quadratic_assignment.py
|   |   |       |   |   |   |-- test_regression.py
|   |   |       |   |   |   |-- test_slsqp.py
|   |   |       |   |   |   |-- test_tnc.py
|   |   |       |   |   |   |-- test_trustregion.py
|   |   |       |   |   |   |-- test_trustregion_exact.py
|   |   |       |   |   |   |-- test_trustregion_krylov.py
|   |   |       |   |   |   +-- test_zeros.py
|   |   |       |   |   |-- __init__.pxd
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _basinhopping.py
|   |   |       |   |   |-- _bglu_dense.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _bglu_dense.cp313-win_amd64.pyd
|   |   |       |   |   |-- _bracket.py
|   |   |       |   |   |-- _chandrupatla.py
|   |   |       |   |   |-- _cobyla_py.py
|   |   |       |   |   |-- _cobyqa_py.py
|   |   |       |   |   |-- _constraints.py
|   |   |       |   |   |-- _dcsrch.py
|   |   |       |   |   |-- _differentiable_functions.py
|   |   |       |   |   |-- _differentialevolution.py
|   |   |       |   |   |-- _direct.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _direct.cp313-win_amd64.pyd
|   |   |       |   |   |-- _direct_py.py
|   |   |       |   |   |-- _dual_annealing.py
|   |   |       |   |   |-- _elementwise.py
|   |   |       |   |   |-- _group_columns.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _group_columns.cp313-win_amd64.pyd
|   |   |       |   |   |-- _hessian_update_strategy.py
|   |   |       |   |   |-- _isotonic.py
|   |   |       |   |   |-- _lbfgsb.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _lbfgsb.cp313-win_amd64.pyd
|   |   |       |   |   |-- _lbfgsb_py.py
|   |   |       |   |   |-- _linesearch.py
|   |   |       |   |   |-- _linprog.py
|   |   |       |   |   |-- _linprog_doc.py
|   |   |       |   |   |-- _linprog_highs.py
|   |   |       |   |   |-- _linprog_ip.py
|   |   |       |   |   |-- _linprog_rs.py
|   |   |       |   |   |-- _linprog_simplex.py
|   |   |       |   |   |-- _linprog_util.py
|   |   |       |   |   |-- _lsap.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _lsap.cp313-win_amd64.pyd
|   |   |       |   |   |-- _milp.py
|   |   |       |   |   |-- _minimize.py
|   |   |       |   |   |-- _minpack.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _minpack.cp313-win_amd64.pyd
|   |   |       |   |   |-- _minpack_py.py
|   |   |       |   |   |-- _moduleTNC.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _moduleTNC.cp313-win_amd64.pyd
|   |   |       |   |   |-- _nnls.py
|   |   |       |   |   |-- _nonlin.py
|   |   |       |   |   |-- _numdiff.py
|   |   |       |   |   |-- _optimize.py
|   |   |       |   |   |-- _pava_pybind.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _pava_pybind.cp313-win_amd64.pyd
|   |   |       |   |   |-- _qap.py
|   |   |       |   |   |-- _remove_redundancy.py
|   |   |       |   |   |-- _root.py
|   |   |       |   |   |-- _root_scalar.py
|   |   |       |   |   |-- _shgo.py
|   |   |       |   |   |-- _slsqp_py.py
|   |   |       |   |   |-- _slsqplib.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _slsqplib.cp313-win_amd64.pyd
|   |   |       |   |   |-- _spectral.py
|   |   |       |   |   |-- _tnc.py
|   |   |       |   |   |-- _trustregion.py
|   |   |       |   |   |-- _trustregion_dogleg.py
|   |   |       |   |   |-- _trustregion_exact.py
|   |   |       |   |   |-- _trustregion_krylov.py
|   |   |       |   |   |-- _trustregion_ncg.py
|   |   |       |   |   |-- _tstutils.py
|   |   |       |   |   |-- _zeros.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _zeros.cp313-win_amd64.pyd
|   |   |       |   |   |-- _zeros_py.py
|   |   |       |   |   |-- cobyla.py
|   |   |       |   |   |-- cython_optimize.pxd
|   |   |       |   |   |-- elementwise.py
|   |   |       |   |   |-- lbfgsb.py
|   |   |       |   |   |-- linesearch.py
|   |   |       |   |   |-- minpack.py
|   |   |       |   |   |-- minpack2.py
|   |   |       |   |   |-- moduleTNC.py
|   |   |       |   |   |-- nonlin.py
|   |   |       |   |   |-- optimize.py
|   |   |       |   |   |-- slsqp.py
|   |   |       |   |   |-- tnc.py
|   |   |       |   |   +-- zeros.py
|   |   |       |   |-- signal
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _arraytools.cpython-313.pyc
|   |   |       |   |   |   |-- _czt.cpython-313.pyc
|   |   |       |   |   |   |-- _delegators.cpython-313.pyc
|   |   |       |   |   |   |-- _filter_design.cpython-313.pyc
|   |   |       |   |   |   |-- _fir_filter_design.cpython-313.pyc
|   |   |       |   |   |   |-- _lti_conversion.cpython-313.pyc
|   |   |       |   |   |   |-- _ltisys.cpython-313.pyc
|   |   |       |   |   |   |-- _max_len_seq.cpython-313.pyc
|   |   |       |   |   |   |-- _peak_finding.cpython-313.pyc
|   |   |       |   |   |   |-- _polyutils.cpython-313.pyc
|   |   |       |   |   |   |-- _savitzky_golay.cpython-313.pyc
|   |   |       |   |   |   |-- _short_time_fft.cpython-313.pyc
|   |   |       |   |   |   |-- _signal_api.cpython-313.pyc
|   |   |       |   |   |   |-- _signaltools.cpython-313.pyc
|   |   |       |   |   |   |-- _spectral_py.cpython-313.pyc
|   |   |       |   |   |   |-- _spline_filters.cpython-313.pyc
|   |   |       |   |   |   |-- _support_alternative_backends.cpython-313.pyc
|   |   |       |   |   |   |-- _upfirdn.cpython-313.pyc
|   |   |       |   |   |   |-- _waveforms.cpython-313.pyc
|   |   |       |   |   |   |-- _wavelets.cpython-313.pyc
|   |   |       |   |   |   |-- bsplines.cpython-313.pyc
|   |   |       |   |   |   |-- filter_design.cpython-313.pyc
|   |   |       |   |   |   |-- fir_filter_design.cpython-313.pyc
|   |   |       |   |   |   |-- lti_conversion.cpython-313.pyc
|   |   |       |   |   |   |-- ltisys.cpython-313.pyc
|   |   |       |   |   |   |-- signaltools.cpython-313.pyc
|   |   |       |   |   |   |-- spectral.cpython-313.pyc
|   |   |       |   |   |   |-- spline.cpython-313.pyc
|   |   |       |   |   |   |-- waveforms.cpython-313.pyc
|   |   |       |   |   |   +-- wavelets.cpython-313.pyc
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _scipy_spectral_test_shim.cpython-313.pyc
|   |   |       |   |   |   |   |-- mpsig.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_tools.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_bsplines.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cont2discrete.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_czt.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_dltisys.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_filter_design.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fir_filter_design.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ltisys.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_max_len_seq.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_peak_finding.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_result_type.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_savitzky_golay.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_short_time_fft.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_signaltools.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_spectral.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_splines.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_upfirdn.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_waveforms.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_wavelets.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_windows.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _scipy_spectral_test_shim.py
|   |   |       |   |   |   |-- mpsig.py
|   |   |       |   |   |   |-- test_array_tools.py
|   |   |       |   |   |   |-- test_bsplines.py
|   |   |       |   |   |   |-- test_cont2discrete.py
|   |   |       |   |   |   |-- test_czt.py
|   |   |       |   |   |   |-- test_dltisys.py
|   |   |       |   |   |   |-- test_filter_design.py
|   |   |       |   |   |   |-- test_fir_filter_design.py
|   |   |       |   |   |   |-- test_ltisys.py
|   |   |       |   |   |   |-- test_max_len_seq.py
|   |   |       |   |   |   |-- test_peak_finding.py
|   |   |       |   |   |   |-- test_result_type.py
|   |   |       |   |   |   |-- test_savitzky_golay.py
|   |   |       |   |   |   |-- test_short_time_fft.py
|   |   |       |   |   |   |-- test_signaltools.py
|   |   |       |   |   |   |-- test_spectral.py
|   |   |       |   |   |   |-- test_splines.py
|   |   |       |   |   |   |-- test_upfirdn.py
|   |   |       |   |   |   |-- test_waveforms.py
|   |   |       |   |   |   |-- test_wavelets.py
|   |   |       |   |   |   +-- test_windows.py
|   |   |       |   |   |-- windows
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _windows.cpython-313.pyc
|   |   |       |   |   |   |   +-- windows.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _windows.py
|   |   |       |   |   |   +-- windows.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _arraytools.py
|   |   |       |   |   |-- _czt.py
|   |   |       |   |   |-- _delegators.py
|   |   |       |   |   |-- _filter_design.py
|   |   |       |   |   |-- _fir_filter_design.py
|   |   |       |   |   |-- _lti_conversion.py
|   |   |       |   |   |-- _ltisys.py
|   |   |       |   |   |-- _max_len_seq.py
|   |   |       |   |   |-- _max_len_seq_inner.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _max_len_seq_inner.cp313-win_amd64.pyd
|   |   |       |   |   |-- _peak_finding.py
|   |   |       |   |   |-- _peak_finding_utils.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _peak_finding_utils.cp313-win_amd64.pyd
|   |   |       |   |   |-- _polyutils.py
|   |   |       |   |   |-- _savitzky_golay.py
|   |   |       |   |   |-- _short_time_fft.py
|   |   |       |   |   |-- _signal_api.py
|   |   |       |   |   |-- _signaltools.py
|   |   |       |   |   |-- _sigtools.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _sigtools.cp313-win_amd64.pyd
|   |   |       |   |   |-- _sosfilt.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _sosfilt.cp313-win_amd64.pyd
|   |   |       |   |   |-- _spectral_py.py
|   |   |       |   |   |-- _spline.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _spline.cp313-win_amd64.pyd
|   |   |       |   |   |-- _spline.pyi
|   |   |       |   |   |-- _spline_filters.py
|   |   |       |   |   |-- _support_alternative_backends.py
|   |   |       |   |   |-- _upfirdn.py
|   |   |       |   |   |-- _upfirdn_apply.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _upfirdn_apply.cp313-win_amd64.pyd
|   |   |       |   |   |-- _waveforms.py
|   |   |       |   |   |-- _wavelets.py
|   |   |       |   |   |-- bsplines.py
|   |   |       |   |   |-- filter_design.py
|   |   |       |   |   |-- fir_filter_design.py
|   |   |       |   |   |-- lti_conversion.py
|   |   |       |   |   |-- ltisys.py
|   |   |       |   |   |-- signaltools.py
|   |   |       |   |   |-- spectral.py
|   |   |       |   |   |-- spline.py
|   |   |       |   |   |-- waveforms.py
|   |   |       |   |   +-- wavelets.py
|   |   |       |   |-- sparse
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _base.cpython-313.pyc
|   |   |       |   |   |   |-- _bsr.cpython-313.pyc
|   |   |       |   |   |   |-- _compressed.cpython-313.pyc
|   |   |       |   |   |   |-- _construct.cpython-313.pyc
|   |   |       |   |   |   |-- _coo.cpython-313.pyc
|   |   |       |   |   |   |-- _csc.cpython-313.pyc
|   |   |       |   |   |   |-- _csr.cpython-313.pyc
|   |   |       |   |   |   |-- _data.cpython-313.pyc
|   |   |       |   |   |   |-- _dia.cpython-313.pyc
|   |   |       |   |   |   |-- _dok.cpython-313.pyc
|   |   |       |   |   |   |-- _extract.cpython-313.pyc
|   |   |       |   |   |   |-- _index.cpython-313.pyc
|   |   |       |   |   |   |-- _lil.cpython-313.pyc
|   |   |       |   |   |   |-- _matrix.cpython-313.pyc
|   |   |       |   |   |   |-- _matrix_io.cpython-313.pyc
|   |   |       |   |   |   |-- _spfuncs.cpython-313.pyc
|   |   |       |   |   |   |-- _sputils.cpython-313.pyc
|   |   |       |   |   |   |-- base.cpython-313.pyc
|   |   |       |   |   |   |-- bsr.cpython-313.pyc
|   |   |       |   |   |   |-- compressed.cpython-313.pyc
|   |   |       |   |   |   |-- construct.cpython-313.pyc
|   |   |       |   |   |   |-- coo.cpython-313.pyc
|   |   |       |   |   |   |-- csc.cpython-313.pyc
|   |   |       |   |   |   |-- csr.cpython-313.pyc
|   |   |       |   |   |   |-- data.cpython-313.pyc
|   |   |       |   |   |   |-- dia.cpython-313.pyc
|   |   |       |   |   |   |-- dok.cpython-313.pyc
|   |   |       |   |   |   |-- extract.cpython-313.pyc
|   |   |       |   |   |   |-- lil.cpython-313.pyc
|   |   |       |   |   |   |-- sparsetools.cpython-313.pyc
|   |   |       |   |   |   |-- spfuncs.cpython-313.pyc
|   |   |       |   |   |   +-- sputils.cpython-313.pyc
|   |   |       |   |   |-- csgraph
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _laplacian.cpython-313.pyc
|   |   |       |   |   |   |   +-- _validation.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_connected_components.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_conversions.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_flow.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_graph_laplacian.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_matching.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_pydata_sparse.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_reordering.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_shortest_path.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_spanning_tree.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_traversal.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- test_connected_components.py
|   |   |       |   |   |   |   |-- test_conversions.py
|   |   |       |   |   |   |   |-- test_flow.py
|   |   |       |   |   |   |   |-- test_graph_laplacian.py
|   |   |       |   |   |   |   |-- test_matching.py
|   |   |       |   |   |   |   |-- test_pydata_sparse.py
|   |   |       |   |   |   |   |-- test_reordering.py
|   |   |       |   |   |   |   |-- test_shortest_path.py
|   |   |       |   |   |   |   |-- test_spanning_tree.py
|   |   |       |   |   |   |   +-- test_traversal.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _flow.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _flow.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _laplacian.py
|   |   |       |   |   |   |-- _matching.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _matching.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _min_spanning_tree.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _min_spanning_tree.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _reordering.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _reordering.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _shortest_path.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _shortest_path.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _tools.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _tools.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _traversal.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _traversal.cp313-win_amd64.pyd
|   |   |       |   |   |   +-- _validation.py
|   |   |       |   |   |-- linalg
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _expm_multiply.cpython-313.pyc
|   |   |       |   |   |   |   |-- _interface.cpython-313.pyc
|   |   |       |   |   |   |   |-- _matfuncs.cpython-313.pyc
|   |   |       |   |   |   |   |-- _norm.cpython-313.pyc
|   |   |       |   |   |   |   |-- _onenormest.cpython-313.pyc
|   |   |       |   |   |   |   |-- _special_sparse_arrays.cpython-313.pyc
|   |   |       |   |   |   |   |-- _svdp.cpython-313.pyc
|   |   |       |   |   |   |   |-- dsolve.cpython-313.pyc
|   |   |       |   |   |   |   |-- eigen.cpython-313.pyc
|   |   |       |   |   |   |   |-- interface.cpython-313.pyc
|   |   |       |   |   |   |   |-- isolve.cpython-313.pyc
|   |   |       |   |   |   |   +-- matfuncs.cpython-313.pyc
|   |   |       |   |   |   |-- _dsolve
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _add_newdocs.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- linsolve.cpython-313.pyc
|   |   |       |   |   |   |   |-- tests
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- test_linsolve.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   +-- test_linsolve.py
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _add_newdocs.py
|   |   |       |   |   |   |   |-- _superlu.cp313-win_amd64.dll.a
|   |   |       |   |   |   |   |-- _superlu.cp313-win_amd64.pyd
|   |   |       |   |   |   |   +-- linsolve.py
|   |   |       |   |   |   |-- _eigen
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _svds.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- _svds_doc.cpython-313.pyc
|   |   |       |   |   |   |   |-- arpack
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- arpack.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- tests
|   |   |       |   |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |   +-- test_arpack.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |   +-- test_arpack.py
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |-- _arpack.cp313-win_amd64.dll.a
|   |   |       |   |   |   |   |   |-- _arpack.cp313-win_amd64.pyd
|   |   |       |   |   |   |   |   |-- arpack.py
|   |   |       |   |   |   |   |   +-- COPYING
|   |   |       |   |   |   |   |-- lobpcg
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- lobpcg.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- tests
|   |   |       |   |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |   +-- test_lobpcg.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |   +-- test_lobpcg.py
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   +-- lobpcg.py
|   |   |       |   |   |   |   |-- tests
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- test_svds.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   +-- test_svds.py
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _svds.py
|   |   |       |   |   |   |   +-- _svds_doc.py
|   |   |       |   |   |   |-- _isolve
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- _gcrotmk.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- iterative.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- lgmres.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- lsmr.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- lsqr.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- minres.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- tfqmr.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- tests
|   |   |       |   |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- test_gcrotmk.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- test_iterative.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- test_lgmres.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- test_lsmr.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- test_lsqr.cpython-313.pyc
|   |   |       |   |   |   |   |   |   |-- test_minres.cpython-313.pyc
|   |   |       |   |   |   |   |   |   +-- test_utils.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |   |-- test_gcrotmk.py
|   |   |       |   |   |   |   |   |-- test_iterative.py
|   |   |       |   |   |   |   |   |-- test_lgmres.py
|   |   |       |   |   |   |   |   |-- test_lsmr.py
|   |   |       |   |   |   |   |   |-- test_lsqr.py
|   |   |       |   |   |   |   |   |-- test_minres.py
|   |   |       |   |   |   |   |   +-- test_utils.py
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- _gcrotmk.py
|   |   |       |   |   |   |   |-- iterative.py
|   |   |       |   |   |   |   |-- lgmres.py
|   |   |       |   |   |   |   |-- lsmr.py
|   |   |       |   |   |   |   |-- lsqr.py
|   |   |       |   |   |   |   |-- minres.py
|   |   |       |   |   |   |   |-- tfqmr.py
|   |   |       |   |   |   |   +-- utils.py
|   |   |       |   |   |   |-- _propack
|   |   |       |   |   |   |   |-- _cpropack.cp313-win_amd64.dll.a
|   |   |       |   |   |   |   |-- _cpropack.cp313-win_amd64.pyd
|   |   |       |   |   |   |   |-- _dpropack.cp313-win_amd64.dll.a
|   |   |       |   |   |   |   |-- _dpropack.cp313-win_amd64.pyd
|   |   |       |   |   |   |   |-- _spropack.cp313-win_amd64.dll.a
|   |   |       |   |   |   |   |-- _spropack.cp313-win_amd64.pyd
|   |   |       |   |   |   |   |-- _zpropack.cp313-win_amd64.dll.a
|   |   |       |   |   |   |   +-- _zpropack.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_expm_multiply.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_interface.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_matfuncs.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_norm.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_onenormest.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_propack.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_pydata_sparse.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_special_sparse_arrays.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- propack_test_data.npz
|   |   |       |   |   |   |   |-- test_expm_multiply.py
|   |   |       |   |   |   |   |-- test_interface.py
|   |   |       |   |   |   |   |-- test_matfuncs.py
|   |   |       |   |   |   |   |-- test_norm.py
|   |   |       |   |   |   |   |-- test_onenormest.py
|   |   |       |   |   |   |   |-- test_propack.py
|   |   |       |   |   |   |   |-- test_pydata_sparse.py
|   |   |       |   |   |   |   +-- test_special_sparse_arrays.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _expm_multiply.py
|   |   |       |   |   |   |-- _interface.py
|   |   |       |   |   |   |-- _matfuncs.py
|   |   |       |   |   |   |-- _norm.py
|   |   |       |   |   |   |-- _onenormest.py
|   |   |       |   |   |   |-- _special_sparse_arrays.py
|   |   |       |   |   |   |-- _svdp.py
|   |   |       |   |   |   |-- dsolve.py
|   |   |       |   |   |   |-- eigen.py
|   |   |       |   |   |   |-- interface.py
|   |   |       |   |   |   |-- isolve.py
|   |   |       |   |   |   +-- matfuncs.py
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_arithmetic1d.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_array_api.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_base.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_common1d.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_construct.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_coo.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_csc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_csr.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_dok.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_extract.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_indexing1d.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_matrix_io.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_minmax1d.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_sparsetools.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_spfuncs.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_sputils.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- csc_py2.npz
|   |   |       |   |   |   |   +-- csc_py3.npz
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_arithmetic1d.py
|   |   |       |   |   |   |-- test_array_api.py
|   |   |       |   |   |   |-- test_base.py
|   |   |       |   |   |   |-- test_common1d.py
|   |   |       |   |   |   |-- test_construct.py
|   |   |       |   |   |   |-- test_coo.py
|   |   |       |   |   |   |-- test_csc.py
|   |   |       |   |   |   |-- test_csr.py
|   |   |       |   |   |   |-- test_dok.py
|   |   |       |   |   |   |-- test_extract.py
|   |   |       |   |   |   |-- test_indexing1d.py
|   |   |       |   |   |   |-- test_matrix_io.py
|   |   |       |   |   |   |-- test_minmax1d.py
|   |   |       |   |   |   |-- test_sparsetools.py
|   |   |       |   |   |   |-- test_spfuncs.py
|   |   |       |   |   |   +-- test_sputils.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _base.py
|   |   |       |   |   |-- _bsr.py
|   |   |       |   |   |-- _compressed.py
|   |   |       |   |   |-- _construct.py
|   |   |       |   |   |-- _coo.py
|   |   |       |   |   |-- _csc.py
|   |   |       |   |   |-- _csparsetools.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _csparsetools.cp313-win_amd64.pyd
|   |   |       |   |   |-- _csr.py
|   |   |       |   |   |-- _data.py
|   |   |       |   |   |-- _dia.py
|   |   |       |   |   |-- _dok.py
|   |   |       |   |   |-- _extract.py
|   |   |       |   |   |-- _index.py
|   |   |       |   |   |-- _lil.py
|   |   |       |   |   |-- _matrix.py
|   |   |       |   |   |-- _matrix_io.py
|   |   |       |   |   |-- _sparsetools.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _sparsetools.cp313-win_amd64.pyd
|   |   |       |   |   |-- _spfuncs.py
|   |   |       |   |   |-- _sputils.py
|   |   |       |   |   |-- base.py
|   |   |       |   |   |-- bsr.py
|   |   |       |   |   |-- compressed.py
|   |   |       |   |   |-- construct.py
|   |   |       |   |   |-- coo.py
|   |   |       |   |   |-- csc.py
|   |   |       |   |   |-- csr.py
|   |   |       |   |   |-- data.py
|   |   |       |   |   |-- dia.py
|   |   |       |   |   |-- dok.py
|   |   |       |   |   |-- extract.py
|   |   |       |   |   |-- lil.py
|   |   |       |   |   |-- sparsetools.py
|   |   |       |   |   |-- spfuncs.py
|   |   |       |   |   +-- sputils.py
|   |   |       |   |-- spatial
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _geometric_slerp.cpython-313.pyc
|   |   |       |   |   |   |-- _kdtree.cpython-313.pyc
|   |   |       |   |   |   |-- _plotutils.cpython-313.pyc
|   |   |       |   |   |   |-- _procrustes.cpython-313.pyc
|   |   |       |   |   |   |-- _spherical_voronoi.cpython-313.pyc
|   |   |       |   |   |   |-- ckdtree.cpython-313.pyc
|   |   |       |   |   |   |-- distance.cpython-313.pyc
|   |   |       |   |   |   |-- kdtree.cpython-313.pyc
|   |   |       |   |   |   +-- qhull.cpython-313.pyc
|   |   |       |   |   |-- qhull_src
|   |   |       |   |   |   +-- COPYING_QHULL.txt
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__plotutils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test__procrustes.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_distance.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hausdorff.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_kdtree.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_qhull.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_slerp.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_spherical_voronoi.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- cdist-X1.txt
|   |   |       |   |   |   |   |-- cdist-X2.txt
|   |   |       |   |   |   |   |-- degenerate_pointset.npz
|   |   |       |   |   |   |   |-- iris.txt
|   |   |       |   |   |   |   |-- pdist-boolean-inp.txt
|   |   |       |   |   |   |   |-- pdist-chebyshev-ml.txt
|   |   |       |   |   |   |   |-- pdist-chebyshev-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-cityblock-ml.txt
|   |   |       |   |   |   |   |-- pdist-cityblock-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-correlation-ml.txt
|   |   |       |   |   |   |   |-- pdist-correlation-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-cosine-ml.txt
|   |   |       |   |   |   |   |-- pdist-cosine-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-double-inp.txt
|   |   |       |   |   |   |   |-- pdist-euclidean-ml.txt
|   |   |       |   |   |   |   |-- pdist-euclidean-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-hamming-ml.txt
|   |   |       |   |   |   |   |-- pdist-jaccard-ml.txt
|   |   |       |   |   |   |   |-- pdist-jensenshannon-ml.txt
|   |   |       |   |   |   |   |-- pdist-jensenshannon-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-minkowski-3.2-ml.txt
|   |   |       |   |   |   |   |-- pdist-minkowski-3.2-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-minkowski-5.8-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-seuclidean-ml.txt
|   |   |       |   |   |   |   |-- pdist-seuclidean-ml-iris.txt
|   |   |       |   |   |   |   |-- pdist-spearman-ml.txt
|   |   |       |   |   |   |   |-- random-bool-data.txt
|   |   |       |   |   |   |   |-- random-double-data.txt
|   |   |       |   |   |   |   |-- random-int-data.txt
|   |   |       |   |   |   |   |-- random-uint-data.txt
|   |   |       |   |   |   |   +-- selfdual-4d-polytope.txt
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test__plotutils.py
|   |   |       |   |   |   |-- test__procrustes.py
|   |   |       |   |   |   |-- test_distance.py
|   |   |       |   |   |   |-- test_hausdorff.py
|   |   |       |   |   |   |-- test_kdtree.py
|   |   |       |   |   |   |-- test_qhull.py
|   |   |       |   |   |   |-- test_slerp.py
|   |   |       |   |   |   +-- test_spherical_voronoi.py
|   |   |       |   |   |-- transform
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- _rotation_groups.cpython-313.pyc
|   |   |       |   |   |   |   |-- _rotation_spline.cpython-313.pyc
|   |   |       |   |   |   |   +-- rotation.cpython-313.pyc
|   |   |       |   |   |   |-- tests
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_rigid_transform.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_rotation.cpython-313.pyc
|   |   |       |   |   |   |   |   |-- test_rotation_groups.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- test_rotation_spline.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- test_rigid_transform.py
|   |   |       |   |   |   |   |-- test_rotation.py
|   |   |       |   |   |   |   |-- test_rotation_groups.py
|   |   |       |   |   |   |   +-- test_rotation_spline.py
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- _rigid_transform.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _rigid_transform.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _rotation.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- _rotation.cp313-win_amd64.pyd
|   |   |       |   |   |   |-- _rotation_groups.py
|   |   |       |   |   |   |-- _rotation_spline.py
|   |   |       |   |   |   +-- rotation.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _ckdtree.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ckdtree.cp313-win_amd64.pyd
|   |   |       |   |   |-- _distance_pybind.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _distance_pybind.cp313-win_amd64.pyd
|   |   |       |   |   |-- _distance_wrap.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _distance_wrap.cp313-win_amd64.pyd
|   |   |       |   |   |-- _geometric_slerp.py
|   |   |       |   |   |-- _hausdorff.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _hausdorff.cp313-win_amd64.pyd
|   |   |       |   |   |-- _kdtree.py
|   |   |       |   |   |-- _plotutils.py
|   |   |       |   |   |-- _procrustes.py
|   |   |       |   |   |-- _qhull.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _qhull.cp313-win_amd64.pyd
|   |   |       |   |   |-- _qhull.pyi
|   |   |       |   |   |-- _spherical_voronoi.py
|   |   |       |   |   |-- _voronoi.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _voronoi.cp313-win_amd64.pyd
|   |   |       |   |   |-- _voronoi.pyi
|   |   |       |   |   |-- ckdtree.py
|   |   |       |   |   |-- distance.py
|   |   |       |   |   |-- distance.pyi
|   |   |       |   |   |-- kdtree.py
|   |   |       |   |   +-- qhull.py
|   |   |       |   |-- special
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _add_newdocs.cpython-313.pyc
|   |   |       |   |   |   |-- _basic.cpython-313.pyc
|   |   |       |   |   |   |-- _ellip_harm.cpython-313.pyc
|   |   |       |   |   |   |-- _input_validation.cpython-313.pyc
|   |   |       |   |   |   |-- _lambertw.cpython-313.pyc
|   |   |       |   |   |   |-- _logsumexp.cpython-313.pyc
|   |   |       |   |   |   |-- _mptestutils.cpython-313.pyc
|   |   |       |   |   |   |-- _multiufuncs.cpython-313.pyc
|   |   |       |   |   |   |-- _orthogonal.cpython-313.pyc
|   |   |       |   |   |   |-- _sf_error.cpython-313.pyc
|   |   |       |   |   |   |-- _spfun_stats.cpython-313.pyc
|   |   |       |   |   |   |-- _spherical_bessel.cpython-313.pyc
|   |   |       |   |   |   |-- _support_alternative_backends.cpython-313.pyc
|   |   |       |   |   |   |-- _testutils.cpython-313.pyc
|   |   |       |   |   |   |-- add_newdocs.cpython-313.pyc
|   |   |       |   |   |   |-- basic.cpython-313.pyc
|   |   |       |   |   |   |-- orthogonal.cpython-313.pyc
|   |   |       |   |   |   |-- sf_error.cpython-313.pyc
|   |   |       |   |   |   |-- specfun.cpython-313.pyc
|   |   |       |   |   |   +-- spfun_stats.cpython-313.pyc
|   |   |       |   |   |-- _precompute
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- cosine_cdf.cpython-313.pyc
|   |   |       |   |   |   |   |-- expn_asy.cpython-313.pyc
|   |   |       |   |   |   |   |-- gammainc_asy.cpython-313.pyc
|   |   |       |   |   |   |   |-- gammainc_data.cpython-313.pyc
|   |   |       |   |   |   |   |-- hyp2f1_data.cpython-313.pyc
|   |   |       |   |   |   |   |-- lambertw.cpython-313.pyc
|   |   |       |   |   |   |   |-- loggamma.cpython-313.pyc
|   |   |       |   |   |   |   |-- struve_convergence.cpython-313.pyc
|   |   |       |   |   |   |   |-- utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- wright_bessel.cpython-313.pyc
|   |   |       |   |   |   |   |-- wright_bessel_data.cpython-313.pyc
|   |   |       |   |   |   |   |-- wrightomega.cpython-313.pyc
|   |   |       |   |   |   |   +-- zetac.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- cosine_cdf.py
|   |   |       |   |   |   |-- expn_asy.py
|   |   |       |   |   |   |-- gammainc_asy.py
|   |   |       |   |   |   |-- gammainc_data.py
|   |   |       |   |   |   |-- hyp2f1_data.py
|   |   |       |   |   |   |-- lambertw.py
|   |   |       |   |   |   |-- loggamma.py
|   |   |       |   |   |   |-- struve_convergence.py
|   |   |       |   |   |   |-- utils.py
|   |   |       |   |   |   |-- wright_bessel.py
|   |   |       |   |   |   |-- wright_bessel_data.py
|   |   |       |   |   |   |-- wrightomega.py
|   |   |       |   |   |   +-- zetac.py
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_bdtr.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_boost_ufuncs.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_boxcox.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cdflib.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cdft_asymptotic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cephes_intp_cast.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cosine_distr.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_cython_special.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_data.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_dd.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_digamma.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ellip_harm.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_erfinv.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_exponential_integrals.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_extending.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_faddeeva.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_gamma.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_gammainc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hyp2f1.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hypergeometric.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_iv_ratio.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_kolmogorov.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_lambertw.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_legendre.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_log1mexp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_loggamma.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_logit.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_logsumexp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mpmath.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_nan_inputs.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ndtr.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ndtri_exp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_orthogonal.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_orthogonal_eval.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_owens_t.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_pcf.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_pdtr.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_powm1.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_precompute_expn_asy.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_precompute_gammainc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_precompute_utils.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_round.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_sf_error.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_sici.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_specfun.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_spence.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_spfun_stats.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_sph_harm.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_spherical_bessel.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_support_alternative_backends.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_trig.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_ufunc_signatures.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_wright_bessel.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_wrightomega.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_zeta.cpython-313.pyc
|   |   |       |   |   |   |-- _cython_examples
|   |   |       |   |   |   |   |-- extending.pyx
|   |   |       |   |   |   |   +-- meson.build
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- __init__.py
|   |   |       |   |   |   |   |-- boost.npz
|   |   |       |   |   |   |   |-- gsl.npz
|   |   |       |   |   |   |   +-- local.npz
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- test_basic.py
|   |   |       |   |   |   |-- test_bdtr.py
|   |   |       |   |   |   |-- test_boost_ufuncs.py
|   |   |       |   |   |   |-- test_boxcox.py
|   |   |       |   |   |   |-- test_cdflib.py
|   |   |       |   |   |   |-- test_cdft_asymptotic.py
|   |   |       |   |   |   |-- test_cephes_intp_cast.py
|   |   |       |   |   |   |-- test_cosine_distr.py
|   |   |       |   |   |   |-- test_cython_special.py
|   |   |       |   |   |   |-- test_data.py
|   |   |       |   |   |   |-- test_dd.py
|   |   |       |   |   |   |-- test_digamma.py
|   |   |       |   |   |   |-- test_ellip_harm.py
|   |   |       |   |   |   |-- test_erfinv.py
|   |   |       |   |   |   |-- test_exponential_integrals.py
|   |   |       |   |   |   |-- test_extending.py
|   |   |       |   |   |   |-- test_faddeeva.py
|   |   |       |   |   |   |-- test_gamma.py
|   |   |       |   |   |   |-- test_gammainc.py
|   |   |       |   |   |   |-- test_hyp2f1.py
|   |   |       |   |   |   |-- test_hypergeometric.py
|   |   |       |   |   |   |-- test_iv_ratio.py
|   |   |       |   |   |   |-- test_kolmogorov.py
|   |   |       |   |   |   |-- test_lambertw.py
|   |   |       |   |   |   |-- test_legendre.py
|   |   |       |   |   |   |-- test_log1mexp.py
|   |   |       |   |   |   |-- test_loggamma.py
|   |   |       |   |   |   |-- test_logit.py
|   |   |       |   |   |   |-- test_logsumexp.py
|   |   |       |   |   |   |-- test_mpmath.py
|   |   |       |   |   |   |-- test_nan_inputs.py
|   |   |       |   |   |   |-- test_ndtr.py
|   |   |       |   |   |   |-- test_ndtri_exp.py
|   |   |       |   |   |   |-- test_orthogonal.py
|   |   |       |   |   |   |-- test_orthogonal_eval.py
|   |   |       |   |   |   |-- test_owens_t.py
|   |   |       |   |   |   |-- test_pcf.py
|   |   |       |   |   |   |-- test_pdtr.py
|   |   |       |   |   |   |-- test_powm1.py
|   |   |       |   |   |   |-- test_precompute_expn_asy.py
|   |   |       |   |   |   |-- test_precompute_gammainc.py
|   |   |       |   |   |   |-- test_precompute_utils.py
|   |   |       |   |   |   |-- test_round.py
|   |   |       |   |   |   |-- test_sf_error.py
|   |   |       |   |   |   |-- test_sici.py
|   |   |       |   |   |   |-- test_specfun.py
|   |   |       |   |   |   |-- test_spence.py
|   |   |       |   |   |   |-- test_spfun_stats.py
|   |   |       |   |   |   |-- test_sph_harm.py
|   |   |       |   |   |   |-- test_spherical_bessel.py
|   |   |       |   |   |   |-- test_support_alternative_backends.py
|   |   |       |   |   |   |-- test_trig.py
|   |   |       |   |   |   |-- test_ufunc_signatures.py
|   |   |       |   |   |   |-- test_wright_bessel.py
|   |   |       |   |   |   |-- test_wrightomega.py
|   |   |       |   |   |   +-- test_zeta.py
|   |   |       |   |   |-- __init__.pxd
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _add_newdocs.py
|   |   |       |   |   |-- _basic.py
|   |   |       |   |   |-- _comb.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _comb.cp313-win_amd64.pyd
|   |   |       |   |   |-- _ellip_harm.py
|   |   |       |   |   |-- _ellip_harm_2.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ellip_harm_2.cp313-win_amd64.pyd
|   |   |       |   |   |-- _gufuncs.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _gufuncs.cp313-win_amd64.pyd
|   |   |       |   |   |-- _input_validation.py
|   |   |       |   |   |-- _lambertw.py
|   |   |       |   |   |-- _logsumexp.py
|   |   |       |   |   |-- _mptestutils.py
|   |   |       |   |   |-- _multiufuncs.py
|   |   |       |   |   |-- _orthogonal.py
|   |   |       |   |   |-- _orthogonal.pyi
|   |   |       |   |   |-- _sf_error.py
|   |   |       |   |   |-- _specfun.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _specfun.cp313-win_amd64.pyd
|   |   |       |   |   |-- _special_ufuncs.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _special_ufuncs.cp313-win_amd64.pyd
|   |   |       |   |   |-- _spfun_stats.py
|   |   |       |   |   |-- _spherical_bessel.py
|   |   |       |   |   |-- _support_alternative_backends.py
|   |   |       |   |   |-- _test_internal.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _test_internal.cp313-win_amd64.pyd
|   |   |       |   |   |-- _test_internal.pyi
|   |   |       |   |   |-- _testutils.py
|   |   |       |   |   |-- _ufuncs.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ufuncs.cp313-win_amd64.pyd
|   |   |       |   |   |-- _ufuncs.pyi
|   |   |       |   |   |-- _ufuncs.pyx
|   |   |       |   |   |-- _ufuncs_cxx.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ufuncs_cxx.cp313-win_amd64.pyd
|   |   |       |   |   |-- _ufuncs_cxx.pxd
|   |   |       |   |   |-- _ufuncs_cxx.pyx
|   |   |       |   |   |-- _ufuncs_cxx_defs.h
|   |   |       |   |   |-- _ufuncs_defs.h
|   |   |       |   |   |-- add_newdocs.py
|   |   |       |   |   |-- basic.py
|   |   |       |   |   |-- cython_special.cp313-win_amd64.dll.a
|   |   |       |   |   |-- cython_special.cp313-win_amd64.pyd
|   |   |       |   |   |-- cython_special.pxd
|   |   |       |   |   |-- cython_special.pyi
|   |   |       |   |   |-- orthogonal.py
|   |   |       |   |   |-- sf_error.py
|   |   |       |   |   |-- specfun.py
|   |   |       |   |   +-- spfun_stats.py
|   |   |       |   |-- stats
|   |   |       |   |   |-- __pycache__
|   |   |       |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- _axis_nan_policy.cpython-313.pyc
|   |   |       |   |   |   |-- _binned_statistic.cpython-313.pyc
|   |   |       |   |   |   |-- _binomtest.cpython-313.pyc
|   |   |       |   |   |   |-- _bws_test.cpython-313.pyc
|   |   |       |   |   |   |-- _censored_data.cpython-313.pyc
|   |   |       |   |   |   |-- _common.cpython-313.pyc
|   |   |       |   |   |   |-- _constants.cpython-313.pyc
|   |   |       |   |   |   |-- _continued_fraction.cpython-313.pyc
|   |   |       |   |   |   |-- _continuous_distns.cpython-313.pyc
|   |   |       |   |   |   |-- _correlation.cpython-313.pyc
|   |   |       |   |   |   |-- _covariance.cpython-313.pyc
|   |   |       |   |   |   |-- _crosstab.cpython-313.pyc
|   |   |       |   |   |   |-- _discrete_distns.cpython-313.pyc
|   |   |       |   |   |   |-- _distn_infrastructure.cpython-313.pyc
|   |   |       |   |   |   |-- _distr_params.cpython-313.pyc
|   |   |       |   |   |   |-- _distribution_infrastructure.cpython-313.pyc
|   |   |       |   |   |   |-- _entropy.cpython-313.pyc
|   |   |       |   |   |   |-- _finite_differences.cpython-313.pyc
|   |   |       |   |   |   |-- _fit.cpython-313.pyc
|   |   |       |   |   |   |-- _hypotests.cpython-313.pyc
|   |   |       |   |   |   |-- _kde.cpython-313.pyc
|   |   |       |   |   |   |-- _ksstats.cpython-313.pyc
|   |   |       |   |   |   |-- _mannwhitneyu.cpython-313.pyc
|   |   |       |   |   |   |-- _mgc.cpython-313.pyc
|   |   |       |   |   |   |-- _morestats.cpython-313.pyc
|   |   |       |   |   |   |-- _mstats_basic.cpython-313.pyc
|   |   |       |   |   |   |-- _mstats_extras.cpython-313.pyc
|   |   |       |   |   |   |-- _multicomp.cpython-313.pyc
|   |   |       |   |   |   |-- _multivariate.cpython-313.pyc
|   |   |       |   |   |   |-- _new_distributions.cpython-313.pyc
|   |   |       |   |   |   |-- _odds_ratio.cpython-313.pyc
|   |   |       |   |   |   |-- _page_trend_test.cpython-313.pyc
|   |   |       |   |   |   |-- _probability_distribution.cpython-313.pyc
|   |   |       |   |   |   |-- _qmc.cpython-313.pyc
|   |   |       |   |   |   |-- _qmvnt.cpython-313.pyc
|   |   |       |   |   |   |-- _quantile.cpython-313.pyc
|   |   |       |   |   |   |-- _relative_risk.cpython-313.pyc
|   |   |       |   |   |   |-- _resampling.cpython-313.pyc
|   |   |       |   |   |   |-- _result_classes.cpython-313.pyc
|   |   |       |   |   |   |-- _sampling.cpython-313.pyc
|   |   |       |   |   |   |-- _sensitivity_analysis.cpython-313.pyc
|   |   |       |   |   |   |-- _stats_mstats_common.cpython-313.pyc
|   |   |       |   |   |   |-- _stats_py.cpython-313.pyc
|   |   |       |   |   |   |-- _survival.cpython-313.pyc
|   |   |       |   |   |   |-- _tukeylambda_stats.cpython-313.pyc
|   |   |       |   |   |   |-- _variation.cpython-313.pyc
|   |   |       |   |   |   |-- _warnings_errors.cpython-313.pyc
|   |   |       |   |   |   |-- _wilcoxon.cpython-313.pyc
|   |   |       |   |   |   |-- biasedurn.cpython-313.pyc
|   |   |       |   |   |   |-- contingency.cpython-313.pyc
|   |   |       |   |   |   |-- distributions.cpython-313.pyc
|   |   |       |   |   |   |-- kde.cpython-313.pyc
|   |   |       |   |   |   |-- morestats.cpython-313.pyc
|   |   |       |   |   |   |-- mstats.cpython-313.pyc
|   |   |       |   |   |   |-- mstats_basic.cpython-313.pyc
|   |   |       |   |   |   |-- mstats_extras.cpython-313.pyc
|   |   |       |   |   |   |-- mvn.cpython-313.pyc
|   |   |       |   |   |   |-- qmc.cpython-313.pyc
|   |   |       |   |   |   |-- sampling.cpython-313.pyc
|   |   |       |   |   |   +-- stats.cpython-313.pyc
|   |   |       |   |   |-- _levy_stable
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- levyst.cp313-win_amd64.dll.a
|   |   |       |   |   |   +-- levyst.cp313-win_amd64.pyd
|   |   |       |   |   |-- _rcont
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- rcont.cp313-win_amd64.dll.a
|   |   |       |   |   |   +-- rcont.cp313-win_amd64.pyd
|   |   |       |   |   |-- _unuran
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   +-- __init__.cpython-313.pyc
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- unuran_wrapper.cp313-win_amd64.dll.a
|   |   |       |   |   |   |-- unuran_wrapper.cp313-win_amd64.pyd
|   |   |       |   |   |   +-- unuran_wrapper.pyi
|   |   |       |   |   |-- tests
|   |   |       |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |-- __init__.cpython-313.pyc
|   |   |       |   |   |   |   |-- common_tests.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_axis_nan_policy.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_binned_statistic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_censored_data.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_contingency.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_continued_fraction.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_continuous.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_continuous_basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_continuous_fit_censored.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_correlation.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_crosstab.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_discrete_basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_discrete_distns.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_distributions.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_entropy.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fast_gen_inversion.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_fit.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_hypotests.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_kdeoth.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_marray.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mgc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_morestats.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mstats_basic.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_mstats_extras.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_multicomp.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_multivariate.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_odds_ratio.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_qmc.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_quantile.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_rank.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_relative_risk.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_resampling.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_sampling.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_sensitivity_analysis.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_stats.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_survival.cpython-313.pyc
|   |   |       |   |   |   |   |-- test_tukeylambda_stats.cpython-313.pyc
|   |   |       |   |   |   |   +-- test_variation.cpython-313.pyc
|   |   |       |   |   |   |-- data
|   |   |       |   |   |   |   |-- __pycache__
|   |   |       |   |   |   |   |   |-- _mvt.cpython-313.pyc
|   |   |       |   |   |   |   |   +-- fisher_exact_results_from_r.cpython-313.pyc
|   |   |       |   |   |   |   |-- levy_stable
|   |   |       |   |   |   |   |   |-- stable-loc-scale-sample-data.npy
|   |   |       |   |   |   |   |   |-- stable-Z1-cdf-sample-data.npy
|   |   |       |   |   |   |   |   +-- stable-Z1-pdf-sample-data.npy
|   |   |       |   |   |   |   |-- nist_anova
|   |   |       |   |   |   |   |   |-- AtmWtAg.dat
|   |   |       |   |   |   |   |   |-- SiRstv.dat
|   |   |       |   |   |   |   |   |-- SmLs01.dat
|   |   |       |   |   |   |   |   |-- SmLs02.dat
|   |   |       |   |   |   |   |   |-- SmLs03.dat
|   |   |       |   |   |   |   |   |-- SmLs04.dat
|   |   |       |   |   |   |   |   |-- SmLs05.dat
|   |   |       |   |   |   |   |   |-- SmLs06.dat
|   |   |       |   |   |   |   |   |-- SmLs07.dat
|   |   |       |   |   |   |   |   |-- SmLs08.dat
|   |   |       |   |   |   |   |   +-- SmLs09.dat
|   |   |       |   |   |   |   |-- nist_linregress
|   |   |       |   |   |   |   |   +-- Norris.dat
|   |   |       |   |   |   |   |-- _mvt.py
|   |   |       |   |   |   |   |-- fisher_exact_results_from_r.py
|   |   |       |   |   |   |   |-- jf_skew_t_gamlss_pdf_data.npy
|   |   |       |   |   |   |   |-- rel_breitwigner_pdf_sample_data_ROOT.npy
|   |   |       |   |   |   |   +-- studentized_range_mpmath_ref.json
|   |   |       |   |   |   |-- __init__.py
|   |   |       |   |   |   |-- common_tests.py
|   |   |       |   |   |   |-- test_axis_nan_policy.py
|   |   |       |   |   |   |-- test_binned_statistic.py
|   |   |       |   |   |   |-- test_censored_data.py
|   |   |       |   |   |   |-- test_contingency.py
|   |   |       |   |   |   |-- test_continued_fraction.py
|   |   |       |   |   |   |-- test_continuous.py
|   |   |       |   |   |   |-- test_continuous_basic.py
|   |   |       |   |   |   |-- test_continuous_fit_censored.py
|   |   |       |   |   |   |-- test_correlation.py
|   |   |       |   |   |   |-- test_crosstab.py
|   |   |       |   |   |   |-- test_discrete_basic.py
|   |   |       |   |   |   |-- test_discrete_distns.py
|   |   |       |   |   |   |-- test_distributions.py
|   |   |       |   |   |   |-- test_entropy.py
|   |   |       |   |   |   |-- test_fast_gen_inversion.py
|   |   |       |   |   |   |-- test_fit.py
|   |   |       |   |   |   |-- test_hypotests.py
|   |   |       |   |   |   |-- test_kdeoth.py
|   |   |       |   |   |   |-- test_marray.py
|   |   |       |   |   |   |-- test_mgc.py
|   |   |       |   |   |   |-- test_morestats.py
|   |   |       |   |   |   |-- test_mstats_basic.py
|   |   |       |   |   |   |-- test_mstats_extras.py
|   |   |       |   |   |   |-- test_multicomp.py
|   |   |       |   |   |   |-- test_multivariate.py
|   |   |       |   |   |   |-- test_odds_ratio.py
|   |   |       |   |   |   |-- test_qmc.py
|   |   |       |   |   |   |-- test_quantile.py
|   |   |       |   |   |   |-- test_rank.py
|   |   |       |   |   |   |-- test_relative_risk.py
|   |   |       |   |   |   |-- test_resampling.py
|   |   |       |   |   |   |-- test_sampling.py
|   |   |       |   |   |   |-- test_sensitivity_analysis.py
|   |   |       |   |   |   |-- test_stats.py
|   |   |       |   |   |   |-- test_survival.py
|   |   |       |   |   |   |-- test_tukeylambda_stats.py
|   |   |       |   |   |   +-- test_variation.py
|   |   |       |   |   |-- __init__.py
|   |   |       |   |   |-- _ansari_swilk_statistics.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _ansari_swilk_statistics.cp313-win_amd64.pyd
|   |   |       |   |   |-- _axis_nan_policy.py
|   |   |       |   |   |-- _biasedurn.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _biasedurn.cp313-win_amd64.pyd
|   |   |       |   |   |-- _biasedurn.pxd
|   |   |       |   |   |-- _binned_statistic.py
|   |   |       |   |   |-- _binomtest.py
|   |   |       |   |   |-- _bws_test.py
|   |   |       |   |   |-- _censored_data.py
|   |   |       |   |   |-- _common.py
|   |   |       |   |   |-- _constants.py
|   |   |       |   |   |-- _continued_fraction.py
|   |   |       |   |   |-- _continuous_distns.py
|   |   |       |   |   |-- _correlation.py
|   |   |       |   |   |-- _covariance.py
|   |   |       |   |   |-- _crosstab.py
|   |   |       |   |   |-- _discrete_distns.py
|   |   |       |   |   |-- _distn_infrastructure.py
|   |   |       |   |   |-- _distr_params.py
|   |   |       |   |   |-- _distribution_infrastructure.py
|   |   |       |   |   |-- _entropy.py
|   |   |       |   |   |-- _finite_differences.py
|   |   |       |   |   |-- _fit.py
|   |   |       |   |   |-- _hypotests.py
|   |   |       |   |   |-- _kde.py
|   |   |       |   |   |-- _ksstats.py
|   |   |       |   |   |-- _mannwhitneyu.py
|   |   |       |   |   |-- _mgc.py
|   |   |       |   |   |-- _morestats.py
|   |   |       |   |   |-- _mstats_basic.py
|   |   |       |   |   |-- _mstats_extras.py
|   |   |       |   |   |-- _multicomp.py
|   |   |       |   |   |-- _multivariate.py
|   |   |       |   |   |-- _new_distributions.py
|   |   |       |   |   |-- _odds_ratio.py
|   |   |       |   |   |-- _page_trend_test.py
|   |   |       |   |   |-- _probability_distribution.py
|   |   |       |   |   |-- _qmc.py
|   |   |       |   |   |-- _qmc_cy.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _qmc_cy.cp313-win_amd64.pyd
|   |   |       |   |   |-- _qmc_cy.pyi
|   |   |       |   |   |-- _qmvnt.py
|   |   |       |   |   |-- _qmvnt_cy.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _qmvnt_cy.cp313-win_amd64.pyd
|   |   |       |   |   |-- _quantile.py
|   |   |       |   |   |-- _relative_risk.py
|   |   |       |   |   |-- _resampling.py
|   |   |       |   |   |-- _result_classes.py
|   |   |       |   |   |-- _sampling.py
|   |   |       |   |   |-- _sensitivity_analysis.py
|   |   |       |   |   |-- _sobol.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _sobol.cp313-win_amd64.pyd
|   |   |       |   |   |-- _sobol.pyi
|   |   |       |   |   |-- _sobol_direction_numbers.npz
|   |   |       |   |   |-- _stats.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _stats.cp313-win_amd64.pyd
|   |   |       |   |   |-- _stats.pxd
|   |   |       |   |   |-- _stats_mstats_common.py
|   |   |       |   |   |-- _stats_py.py
|   |   |       |   |   |-- _stats_pythran.cp313-win_amd64.dll.a
|   |   |       |   |   |-- _stats_pythran.cp313-win_amd64.pyd
|   |   |       |   |   |-- _survival.py
|   |   |       |   |   |-- _tukeylambda_stats.py
|   |   |       |   |   |-- _variation.py
|   |   |       |   |   |-- _warnings_errors.py
|   |   |       |   |   |-- _wilcoxon.py
|   |   |       |   |   |-- biasedurn.py
|   |   |       |   |   |-- contingency.py
|   |   |       |   |   |-- distributions.py
|   |   |       |   |   |-- kde.py
|   |   |       |   |   |-- morestats.py
|   |   |       |   |   |-- mstats.py
|   |   |       |   |   |-- mstats_basic.py
|   |   |       |   |   |-- mstats_extras.py
|   |   |       |   |   |-- mvn.py
|   |   |       |   |   |-- qmc.py
|   |   |       |   |   |-- sampling.py
|   |   |       |   |   +-- stats.py
|   |   |       |   |-- __config__.py
|   |   |       |   |-- __init__.py
|   |   |       |   |-- _cyutility.cp313-win_amd64.dll.a
|   |   |       |   |-- _cyutility.cp313-win_amd64.pyd
|   |   |       |   |-- _distributor_init.py
|   |   |       |   |-- conftest.py
|   |   |       |   +-- version.py
|   |   |       |-- scipy.libs
|   |   |       |   +-- libscipy_openblas-48c358d105077551cc9cc3ba79387ed5.dll
|   |   |       |-- scipy-1.16.2.dist-info
|   |   |       |   |-- DELVEWHEEL
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- LICENSE.txt
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- REQUESTED
|   |   |       |   +-- WHEEL
|   |   |       |-- six-1.17.0.dist-info
|   |   |       |   |-- INSTALLER
|   |   |       |   |-- LICENSE
|   |   |       |   |-- METADATA
|   |   |       |   |-- RECORD
|   |   |       |   |-- top_level.txt
|   |   |       |   +-- WHEEL
|   |   |       |-- pylab.py
|   |   |       |-- scipy-1.16.2-cp313-cp313-win_amd64.whl
|   |   |       +-- six.py
|   |   |-- Scripts
|   |   |   |-- activate
|   |   |   |-- activate.bat
|   |   |   |-- activate.fish
|   |   |   |-- Activate.ps1
|   |   |   |-- deactivate.bat
|   |   |   |-- f2py.exe
|   |   |   |-- fonttools.exe
|   |   |   |-- numpy-config.exe
|   |   |   |-- pip.exe
|   |   |   |-- pip3.13.exe
|   |   |   |-- pip3.exe
|   |   |   |-- pyftmerge.exe
|   |   |   |-- pyftsubset.exe
|   |   |   |-- python.exe
|   |   |   |-- pythonw.exe
|   |   |   +-- ttx.exe
|   |   |-- share
|   |   |   +-- man
|   |   |       +-- man1
|   |   |           +-- ttx.1
|   |   |-- .gitignore
|   |   +-- pyvenv.cfg
|   |-- Export-ProjectStructure.ps1
|   |-- README.md
|   +-- requirements.txt
|-- .git
|   |-- hooks
|   |   |-- applypatch-msg.sample
|   |   |-- commit-msg.sample
|   |   |-- fsmonitor-watchman.sample
|   |   |-- post-update.sample
|   |   |-- pre-applypatch.sample
|   |   |-- pre-commit.sample
|   |   |-- pre-merge-commit.sample
|   |   |-- prepare-commit-msg.sample
|   |   |-- pre-push.sample
|   |   |-- pre-rebase.sample
|   |   |-- pre-receive.sample
|   |   |-- push-to-checkout.sample
|   |   |-- sendemail-validate.sample
|   |   +-- update.sample
|   |-- info
|   |   +-- exclude
|   |-- logs
|   |   |-- refs
|   |   |   |-- heads
|   |   |   |   +-- main
|   |   |   +-- remotes
|   |   |       +-- origin
|   |   |           |-- HEAD
|   |   |           +-- main
|   |   +-- HEAD
|   |-- objects
|   |   |-- 05
|   |   |   +-- 105c5e85945b2fb27c1c24768dfc41ce554de0
|   |   |-- 07
|   |   |   +-- c3ba7efcce07becfe0bb84eb99589e4e2fba4a
|   |   |-- 0b
|   |   |   +-- eb83f430e3d586042eb83903918410c7b2280c
|   |   |-- 12
|   |   |   +-- db87b429e5137c7691511847ac07c085aaecd9
|   |   |-- 13
|   |   |   +-- c8e265ebd70b6616159218a544f9b2d25176fc
|   |   |-- 16
|   |   |   +-- c12754690604f0c976f8550101e1e77e59f7d6
|   |   |-- 17
|   |   |   +-- 07a247cec2cd1f4929ea79a3bcdcd095dcf4dc
|   |   |-- 19
|   |   |   +-- a5a27da24b66a4767656ec9237539698caa895
|   |   |-- 1a
|   |   |   +-- 544575dc709e05e0e04e10203a2576b705961b
|   |   |-- 20
|   |   |   +-- 80f9a55525081bbcc0211de1d227a93cc531a7
|   |   |-- 23
|   |   |   +-- 0be9061e3f38963a1e24e740fa16f87ba070d5
|   |   |-- 2c
|   |   |   +-- 1c36589ad1bca27f24d0bf9bb1d38f5cceae13
|   |   |-- 2d
|   |   |   +-- 6cc0d25782e4df6eef21cb656962fb0780ce54
|   |   |-- 31
|   |   |   +-- 6c766a945d23171e10c6bf001b07876779faa3
|   |   |-- 36
|   |   |   +-- fb9fc2c8cb2803a4bed4653e671a7983eb693e
|   |   |-- 3d
|   |   |   |-- 8ab809838aee47b2d4de1235b3b1e3d9e7cf0b
|   |   |   +-- 9b381269f552e7158625f495f5c4030b690d23
|   |   |-- 3e
|   |   |   +-- 2e47099e6f84d2382603313e4cb4374d0511c1
|   |   |-- 40
|   |   |   +-- 0f568ee6420e7c058098ad6b331a6caebe393c
|   |   |-- 45
|   |   |   +-- 3b13d94c015d85467b6adcd9a752b67f38bbe4
|   |   |-- 4a
|   |   |   +-- 45bf1e1be3fe252e75f03b1f5ea1800d970058
|   |   |-- 53
|   |   |   +-- 91e15f836e598c66e8eb0594577861a213d561
|   |   |-- 6b
|   |   |   +-- de0ff85d69386038a76e88f5ee0acb6106b8f1
|   |   |-- 70
|   |   |   +-- 5cdccd3c69271bf2bb965bf78d1fc24af9e6cc
|   |   |-- 72
|   |   |   +-- 83f73277033337a56db881ed848b58b60ff99a
|   |   |-- 75
|   |   |   +-- f2eb1700546b4254013cfeadf2a72e9f9e523a
|   |   |-- 77
|   |   |   +-- 42fb93c0999257bcc648714ffc988982e70142
|   |   |-- 7b
|   |   |   +-- f9acd44ac88d277a1bc0a5e31332bbebc81bb8
|   |   |-- 7c
|   |   |   +-- 521e495ac93f6196a6b08f9df5d67af0d7152e
|   |   |-- 82
|   |   |   +-- 764460cc21a55e78b50fd8eb475933351cb110
|   |   |-- 85
|   |   |   +-- a4cb4970633acf1f4e5aed7c8a749642ab97d1
|   |   |-- 8b
|   |   |   +-- 52fb81e9d9c6c522849bb9e958cdabb7808202
|   |   |-- 97
|   |   |   +-- 4de2a6ea5e0b2b2ed2849a9fdc628f8646b0a8
|   |   |-- 9f
|   |   |   +-- 228d54a93338c9018ed147f5fbdf7481f8ea19
|   |   |-- a3
|   |   |   +-- 8a0a1dc3ddf77f65cf46e22466bf1202a14a18
|   |   |-- a4
|   |   |   +-- 985cb302244b75b402b856c51db27c91b867f4
|   |   |-- a5
|   |   |   +-- a5d525bb3b4ea0ea07192d2bb65f4a53db2fcc
|   |   |-- a7
|   |   |   +-- 7e028f3359b42021f774088b46d863cfdaec27
|   |   |-- a8
|   |   |   +-- c60643e96db91ec04bacd989f49fcbb71d5151
|   |   |-- ab
|   |   |   +-- 9380a8fda2ddb5a0519fee3fad73fc6737d1df
|   |   |-- ac
|   |   |   |-- 4fb4ab557a80279ac510ef033f9be40dd93b8d
|   |   |   +-- c03ab419496ebd00d674bc32d0ba17d40590c3
|   |   |-- b8
|   |   |   +-- f5b10cd242e35c0fd0f970502868e3613bdccf
|   |   |-- bd
|   |   |   +-- 0e4b97c617ebd4988e3463e183604d52617692
|   |   |-- be
|   |   |   +-- 01495bdd095fc3b648d9b2c3ae5deb7e8e91e3
|   |   |-- bf
|   |   |   +-- 09c1360e344752be9f1936c53f105d0cea5fb0
|   |   |-- c0
|   |   |   |-- 9f42440fd5723bc52656af42a6cf520fa2c6d8
|   |   |   +-- c534be3ebc6a56d3d5c4b45d48c8c9ef3e3166
|   |   |-- c1
|   |   |   +-- 1bbdaea8823ba25b8f268769313f8d3d2458b8
|   |   |-- c8
|   |   |   +-- 5924f90fd635267305606cf9bfe1c433a1a4bc
|   |   |-- cb
|   |   |   +-- 3b92edae2b004bc709bb54c3b012d95a2cb81a
|   |   |-- d2
|   |   |   +-- 382f9a2f90a4df23bb206766cedfaec4004a71
|   |   |-- d5
|   |   |   +-- 64d0bc3dd917926892c55e3706cc116d5b165e
|   |   |-- d6
|   |   |   +-- 63b8891c83ea78ecc6086a1b147b72e7056196
|   |   |-- d7
|   |   |   +-- 42439fef5852f5d09c78be7cfa02667320b9dd
|   |   |-- de
|   |   |   +-- c107b84761b7507f2205e5e66114a8bce021a2
|   |   |-- df
|   |   |   +-- e0770424b2a19faf507a501ebfc23be8f54e7b
|   |   |-- e6
|   |   |   +-- 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
|   |   |-- f0
|   |   |   +-- 89e04f21c825aca70205ae6749b2e00c3338e2
|   |   |-- f4
|   |   |   +-- 489fce0491b77ffcb021946c05ce8721a6b35c
|   |   +-- fc
|   |       |-- 2ed1d019def8785cdd93e38d634c5e435b5da2
|   |       |-- 792286e3a12365338d38fde21c58c606096818
|   |       +-- 7dc41c8a42452b087f570ee748fa479a9243fd
|   |-- refs
|   |   |-- heads
|   |   |   +-- main
|   |   +-- remotes
|   |       +-- origin
|   |           |-- HEAD
|   |           +-- main
|   |-- COMMIT_EDITMSG
|   |-- config
|   |-- description
|   |-- FETCH_HEAD
|   |-- HEAD
|   +-- index
|-- .vscode
|   +-- settings.json
|-- .gitattributes
+-- .gitignore
```

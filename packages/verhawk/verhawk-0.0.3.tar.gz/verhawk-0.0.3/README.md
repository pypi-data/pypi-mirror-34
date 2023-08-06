# What is verhawk?

A simple Python package version scanner. 

## What isn't verhawk?

A complex Python package version scanner. Verhawk does not account for every edge case, nor does it provide advanced filtering of any kind. For example, depending how modules are nested for each sub-package you may even encounter output such as `"package.thing=module <module '/path/to/module/module.py'>"`, and it breaks JSON. In which case, use `--exclude` to remove the offending module from the output stream, or pipe `verhawk` through `grep` and filter such results, then convert the keypairs (`module=version`) manually.

These are known issues and unlikely to be addressed.


## Usage

```bash
usage: verhawk [-h] [-V] [-e EXCLUDE] [-v] [-j] [-p] [-r] parent_package

positional arguments:
  parent_package

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Display version information
  -e EXCLUDE, --exclude EXCLUDE
                        Ignore sub-[package|module] by name.
  -v, --verbose         Show packages without version data.
  -j, --json            Emit JSON to stdout
  -p, --packages-only   Ignore non-packages (i.e modules)
  -r, --recursive       Descend into package looking for additional version
                        data.
```

## Examples

### Examining the top-level version of a package

```bash
% verhawk drizzlepac
drizzlepac=2.1.5
```

### Examining the top-level and all sub-packages (including modules)

```bash
% verhawk -r drizzlepac
ImportError(drizzlepac.mdriz): cannot import name 'AstroDrizzle'
drizzlepac=2.1.5
drizzlepac.ablot=2.1.5
drizzlepac.adrizzle=2.1.5
drizzlepac.astrodrizzle=2.1.5
drizzlepac.buildwcs=0.1.0
drizzlepac.createMedian=2.1.5
drizzlepac.drizCR=2.1.5
drizzlepac.imageObject=2.1.5
drizzlepac.imagefindpars=2.1.5
drizzlepac.linearfit=0.4.0
drizzlepac.mapreg=0.1
drizzlepac.minmed=2.1.5
drizzlepac.photeq=0.2
drizzlepac.pixreplace=0.1
drizzlepac.pixtopix=0.1
drizzlepac.pixtosky=0.1
drizzlepac.quickDeriv=2.1.5
drizzlepac.refimagefindpars=2.1.5
drizzlepac.regfilter=0.1
drizzlepac.resetbits=1.0.0
drizzlepac.runastrodriz=1.5.2
drizzlepac.sky=2.1.5
drizzlepac.skytopix=0.1
drizzlepac.tweakback=0.4.0
drizzlepac.tweakreg=1.4.3
drizzlepac.updatehdr=0.2.0
drizzlepac.updatenpol=1.1.0
drizzlepac.util=2.1.5
drizzlepac.version=2.1.5
```

### Examining the top-level and all sub-packages (excluding modules)

```bash
# drizzlepac does not use sub-packages interally, as you can see.
# Only the top-level is returned.

% verhawk -r -p drizzlepac
drizzlepac=2.1.5
```

### Examining the top-level and all sub-packages (with modules; with verbose mode)

```bash
# Verbose mode returns sub-packages and/or modules regardless if it defines '__version__'

% verhawk -r -v drizzlepac
ImportError(drizzlepac.mdriz): cannot import name 'AstroDrizzle'
drizzlepac=2.1.5
drizzlepac.ablot=2.1.5
drizzlepac.acsData=None
drizzlepac.adrizzle=2.1.5
drizzlepac.astrodrizzle=2.1.5
drizzlepac.buildmask=None
drizzlepac.buildwcs=0.1.0
drizzlepac.catalogs=None
drizzlepac.cdriz=None
drizzlepac.createMedian=2.1.5
drizzlepac.drizCR=2.1.5
drizzlepac.findobj=None
drizzlepac.imageObject=2.1.5
drizzlepac.imagefindpars=2.1.5
drizzlepac.imgclasses=None
drizzlepac.irData=None
drizzlepac.linearfit=0.4.0
drizzlepac.mapreg=0.1
drizzlepac.mdzhandler=None
drizzlepac.minmed=2.1.5
drizzlepac.nicmosData=None
drizzlepac.outputimage=None
drizzlepac.photeq=0.2
drizzlepac.pixreplace=0.1
drizzlepac.pixtopix=0.1
drizzlepac.pixtosky=0.1
drizzlepac.processInput=None
drizzlepac.quickDeriv=2.1.5
drizzlepac.refimagefindpars=2.1.5
drizzlepac.regfilter=0.1
drizzlepac.resetbits=1.0.0
drizzlepac.runastrodriz=1.5.2
drizzlepac.sky=2.1.5
drizzlepac.skytopix=0.1
drizzlepac.staticMask=None
drizzlepac.stisData=None
drizzlepac.tests=None
drizzlepac.tweakback=0.4.0
drizzlepac.tweakreg=1.4.3
drizzlepac.tweakutils=None
drizzlepac.updatehdr=0.2.0
drizzlepac.updatenpol=1.1.0
drizzlepac.util=2.1.5
drizzlepac.version=2.1.5
drizzlepac.wcs_functions=None
drizzlepac.wfc3Data=None
drizzlepac.wfpc2Data=None
```

### Exporting to JSON

```bash
# The "ImportError" is written to stderr, so redirecting stdout will not be an issue.

% verhawk -r -j -v drizzlepac
ImportError(drizzlepac.mdriz): cannot import name 'AstroDrizzle'
{"drizzlepac": "2.1.5", "drizzlepac.ablot": "2.1.5", "drizzlepac.acsData": null, "drizzlepac.adrizzle": "2.1.5", "drizzlepac.astrodrizzle": "2.1.5", "drizzlepac.buildmask": null, "drizzlepac.buildwcs": "0.1.0", "drizzlepac.catalogs": null, "drizzlepac.cdriz": null, "drizzlepac.createMedian": "2.1.5", "drizzlepac.drizCR": "2.1.5", "drizzlepac.findobj": null, "drizzlepac.imageObject": "2.1.5", "drizzlepac.imagefindpars": "2.1.5", "drizzlepac.imgclasses": null, "drizzlepac.irData": null, "drizzlepac.linearfit": "0.4.0", "drizzlepac.mapreg": "0.1", "drizzlepac.mdzhandler": null, "drizzlepac.minmed": "2.1.5", "drizzlepac.nicmosData": null, "drizzlepac.outputimage": null, "drizzlepac.photeq": "0.2", "drizzlepac.pixreplace": "0.1", "drizzlepac.pixtopix": "0.1", "drizzlepac.pixtosky": "0.1", "drizzlepac.processInput": null, "drizzlepac.quickDeriv": "2.1.5", "drizzlepac.refimagefindpars": "2.1.5", "drizzlepac.regfilter": "0.1", "drizzlepac.resetbits": "1.0.0", "drizzlepac.runastrodriz": "1.5.2", "drizzlepac.sky": "2.1.5", "drizzlepac.skytopix": "0.1", "drizzlepac.staticMask": null, "drizzlepac.stisData": null, "drizzlepac.tests": null, "drizzlepac.tweakback": "0.4.0", "drizzlepac.tweakreg": "1.4.3", "drizzlepac.tweakutils": null, "drizzlepac.updatehdr": "0.2.0", "drizzlepac.updatenpol": "1.1.0", "drizzlepac.util": "2.1.5", "drizzlepac.version": "2.1.5", "drizzlepac.wcs_functions": null, "drizzlepac.wfc3Data": null, "drizzlepac.wfpc2Data": null}

# Confirming stderr claim

% verhawk -r -j -v drizzlepac > drizzle.json
ImportError(drizzlepac.mdriz): cannot import name 'AstroDrizzle'

% cat drizzle.json
{"drizzlepac": "2.1.5", "drizzlepac.ablot": "2.1.5", "drizzlepac.acsData": null, "drizzlepac.adrizzle": "2.1.5", "drizzlepac.astrodrizzle": "2.1.5", "drizzlepac.buildmask": null, "drizzlepac.buildwcs": "0.1.0", "drizzlepac.catalogs": null, "drizzlepac.cdriz": null, "drizzlepac.createMedian": "2.1.5", "drizzlepac.drizCR": "2.1.5", "drizzlepac.findobj": null, "drizzlepac.imageObject": "2.1.5", "drizzlepac.imagefindpars": "2.1.5", "drizzlepac.imgclasses": null, "drizzlepac.irData": null, "drizzlepac.linearfit": "0.4.0", "drizzlepac.mapreg": "0.1", "drizzlepac.mdzhandler": null, "drizzlepac.minmed": "2.1.5", "drizzlepac.nicmosData": null, "drizzlepac.outputimage": null, "drizzlepac.photeq": "0.2", "drizzlepac.pixreplace": "0.1", "drizzlepac.pixtopix": "0.1", "drizzlepac.pixtosky": "0.1", "drizzlepac.processInput": null, "drizzlepac.quickDeriv": "2.1.5", "drizzlepac.refimagefindpars": "2.1.5", "drizzlepac.regfilter": "0.1", "drizzlepac.resetbits": "1.0.0", "drizzlepac.runastrodriz": "1.5.2", "drizzlepac.sky": "2.1.5", "drizzlepac.skytopix": "0.1", "drizzlepac.staticMask": null, "drizzlepac.stisData": null, "drizzlepac.tests": null, "drizzlepac.tweakback": "0.4.0", "drizzlepac.tweakreg": "1.4.3", "drizzlepac.tweakutils": null, "drizzlepac.updatehdr": "0.2.0", "drizzlepac.updatenpol": "1.1.0", "drizzlepac.util": "2.1.5", "drizzlepac.version": "2.1.5", "drizzlepac.wcs_functions": null, "drizzlepac.wfc3Data": null, "drizzlepac.wfpc2Data": null}
```

###  Importing JSON data (Python 3.x)

```python
import json

with open('drizzle.json') as infile:
    data = json.load(infile)

for module, version in sorted(data.items()):
    print('{0:.<30s}: {1}'.format(module, version))
```

#### Outputs

```bash
drizzlepac....................: 2.1.5
drizzlepac.ablot..............: 2.1.5
drizzlepac.acsData............: None
drizzlepac.adrizzle...........: 2.1.5
drizzlepac.astrodrizzle.......: 2.1.5
drizzlepac.buildmask..........: None
drizzlepac.buildwcs...........: 0.1.0
drizzlepac.catalogs...........: None
drizzlepac.cdriz..............: None
drizzlepac.createMedian.......: 2.1.5
drizzlepac.drizCR.............: 2.1.5
drizzlepac.findobj............: None
drizzlepac.imageObject........: 2.1.5
drizzlepac.imagefindpars......: 2.1.5
drizzlepac.imgclasses.........: None
drizzlepac.irData.............: None
drizzlepac.linearfit..........: 0.4.0
drizzlepac.mapreg.............: 0.1
drizzlepac.mdzhandler.........: None
drizzlepac.minmed.............: 2.1.5
drizzlepac.nicmosData.........: None
drizzlepac.outputimage........: None
drizzlepac.photeq.............: 0.2
drizzlepac.pixreplace.........: 0.1
drizzlepac.pixtopix...........: 0.1
drizzlepac.pixtosky...........: 0.1
drizzlepac.processInput.......: None
drizzlepac.quickDeriv.........: 2.1.5
drizzlepac.refimagefindpars...: 2.1.5
drizzlepac.regfilter..........: 0.1
drizzlepac.resetbits..........: 1.0.0
drizzlepac.runastrodriz.......: 1.5.2
drizzlepac.sky................: 2.1.5
drizzlepac.skytopix...........: 0.1
drizzlepac.staticMask.........: None
drizzlepac.stisData...........: None
drizzlepac.tests..............: None
drizzlepac.tweakback..........: 0.4.0
drizzlepac.tweakreg...........: 1.4.3
drizzlepac.tweakutils.........: None
drizzlepac.updatehdr..........: 0.2.0
drizzlepac.updatenpol.........: 1.1.0
drizzlepac.util...............: 2.1.5
drizzlepac.version............: 2.1.5
drizzlepac.wcs_functions......: None
drizzlepac.wfc3Data...........: None
drizzlepac.wfpc2Data..........: None
```

# gnucash-portfolio-cli

Gnucash Portfolio CLI

If running a web UI (server + client) is problematic, here is a CLI interface to [GnuCash Portfolio](https://github.com/MisterY/gnucash-portfolio) functions, written in Python.

Initially, there well be simple scripts for accessing the basic features. This could grow into a full CLI application at a later stage.

## Tips

Set the log level using `-v` parameter.

In general, it should be possible to set the log level with `--log=DEBUG` but this does not work when using argparse.

## Distribution

### Test Site

```console
python setup.py sdist upload -r test
```

### Production Site

```console
python setup.py sdist upload -r pypi
```
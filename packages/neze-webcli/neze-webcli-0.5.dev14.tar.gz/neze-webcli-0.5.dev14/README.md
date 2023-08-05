# Configuration files

Every configuration should be ini-compatible, i.e., of the form `<section>.<key>=<value>`.

Usually, configuration has a name `<name>`. Configuration objects look for configuration files of `ini` format (no extension, `.ini` extension), `json` format (`.json`,`.js` extension) and `yaml` format (`.yaml`, `.yml` extension) in the following places:

* System in `$PREFIX/etc/<name><ext>`
* Global in `~/.<name><ext>`
* Local in `$(git rev-parse --git-dir)/<name><ext>`

Avoid having two configuration files with two different extensions in the same location. The choice of file will not be guaranteed. Configuration files are merged for reading, starting with System, then Global, followed by Local. This is the same priority order as with `git`. In the Configuration object, they are however kept separate which allows to modify separately the three configurations.

## Configuration formats

Here are short examples of configuration files in `ini`, `json` then `yaml` format. Remember that the `DEFAULT` section is not always available.

```ini
[DEFAULT]
foo=bar
[server]
name=example.com
```

```json
{
  "DEFAULT": {
    "foo": "bar"
  },
  "server": {
    "name": "example.com"
  }
}
```

```yaml
DEFAULT:
  foo: bar
server:
  name: example.com
```

## Configuration content

When there is a `DEFAULT` section in the configuration, you are usually allowed to have a section with any name and the same structure as the `DEFAULT` one.

When available, the `@secrets` key is parsed into a `<protocol>://<entry>` to fetch secrets. Right now, the only supported secrets holder is `pass`.

# Available binaries:

## Transmission

Help is available via `transmission -h`.

Configuration structure:

```ini
[DEFAULT]
;Required if url, username or password is not provided.
@secrets=pass://my-pass-entry
url=https://torrent.example.com/transmission/rpc
username=john
password=b278cdbd95e67b27
;Defaults to the hostname of the url
host=ssh.example.com
;Defaults to none
volume=/srv/torrent/data:/downloads
;Defaults to $PWD
downloads=/media/john/drive/Downloads
```

## Git Piptag

Help is available via `git piptag -h`.

There is no configuration. Git Piptag parses the tags of the git tree to get the latest version tag, and try to apply the given new version tag or to suggest a version tag.

The best way to get used to it is to actually test it weth `git piptag -n` (dry run mode) in several situations.

## Gitlab

Right now only `gitlab me` is available. Try `gitlab -h`, though.

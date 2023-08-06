# animeplanet CLI

## Installation

```console
pip3 install animeplanet
```

## Usage

### CLI

```console
animeplanet set-episodes elfen-lied 2
```

The CLI uses credentials stored in `~/.animeplanet.conf` in form `USERNAME,PASSWORD`.

### python module

```python
from animeplanet import AnimePlanetSession

session = AnimePlanetSession()
session.login('user', 'password')

session.set_episodes('elfen-lied', 2)

session.logout()
```

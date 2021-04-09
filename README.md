![GitHub](https://img.shields.io/github/license/adamjenkins1/MyTurnCADiscordBot) 
[![Unit tests](https://img.shields.io/github/workflow/status/adamjenkins1/DiscordUserDownDetector/Unit%20tests?label=unit%20tests)](https://github.com/adamjenkins1/DiscordUserDownDetector/actions/workflows/unit-tests.yml)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/adamjenkins1/DiscordUserDownDetector/Docker%20Build%20and%20Push%20on%20release)](https://github.com/adamjenkins1/DiscordUserDownDetector/actions/workflows/docker-build-and-push-on-release.yml)
[![Requires.io](https://img.shields.io/requires/github/adamjenkins1/DiscordUserDownDetector/main)](https://requires.io/github/adamjenkins1/DiscordUserDownDetector/requirements/?branch=main)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/adamjenkins1/DiscordUserDownDetector?sort=semver)

## DiscordUserDownDetector
### A small flask API to check if a particular user is online in a given Discord guild (server)

#### Usage
Use any HTTP client to send a `GET` request to `/guild/<GUILD_ID>/username/<USERNAME>`

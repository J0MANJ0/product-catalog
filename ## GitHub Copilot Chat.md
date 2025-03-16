## GitHub Copilot Chat

- Extension Version: 0.24.1 (prod)
- VS Code: vscode/1.97.2
- OS: Linux

## Network

User Settings:

```json
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:

- DNS ipv4 Lookup: 20.87.245.6 (9 ms)
- DNS ipv6 Lookup: 64:ff9b::1457:f506 (10 ms)
- Proxy URL: None (2 ms)
- Electron fetch (configured): HTTP 200 (509 ms)
- Node.js https: HTTP 200 (212 ms)
- Node.js fetch: HTTP 200 (479 ms)
- Helix fetch: HTTP 200 (379 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:

- DNS ipv4 Lookup: 140.82.113.21 (16 ms)
- DNS ipv6 Lookup: 64:ff9b::8c52:7015 (8 ms)
- Proxy URL: None (15 ms)
- Electron fetch (configured): HTTP 200 (811 ms)
- Node.js https: Error (270 ms): ETIMEDOUT
  connect ETIMEDOUT 140.82.113.21:443
  connect ENETUNREACH 64:ff9b::8c52:7015:443 - Local (:::0)
- Node.js fetch: Error (331 ms): fetch failed
  ETIMEDOUT
  connect ETIMEDOUT 140.82.113.21:443
  connect ENETUNREACH 64:ff9b::8c52:7015:443 - Local (:::0)
- Helix fetch: Error (288 ms): ETIMEDOUT

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).

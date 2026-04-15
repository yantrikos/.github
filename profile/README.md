# YantrikOS

**Building an AI-native OS. Memory first.**

The goal is something like Jarvis — ambient, persistent, context-aware AI as the foundation of the OS, not an app on top.

Memory turned out to be the bottleneck. Before you can build an AI OS, you need memory that doesn't forget what matters, doesn't hoard what doesn't, and catches when your agent contradicts itself three sessions later.

So we're building memory first.

![YantrikDB demo](https://raw.githubusercontent.com/yantrikos/yantrikdb-server/main/docs/images/demo.gif)

## Where we are now

**[YantrikDB](https://github.com/yantrikos/yantrikdb-server)** — the memory layer. Cognitive memory database for AI agents. Rust, AGPL, shipping today. Consolidates duplicate memories, detects contradictions, fades stale facts via temporal decay. Used in production at [tv.bothn.com](https://tv.bothn.com) for 24/7 AI sitcom agents.

```bash
docker run -d -p 7438:7438 ghcr.io/yantrikos/yantrikdb:latest
```

Full docs: [yantrikdb.com](https://yantrikdb.com)

## Ecosystem

- **[yantrikdb-server](https://github.com/yantrikos/yantrikdb-server)** — Rust backend (HTTP, cluster, embeddable)
- **[yantrikdb-mcp](https://github.com/yantrikos/yantrikdb-mcp)** — MCP server for Claude Code / Cursor / Windsurf
- **[yantrikdb-hermes-plugin](https://github.com/yantrikos/yantrikdb-hermes-plugin)** — Memory provider for Nous Research's Hermes Agent

## Where we're going

Memory is chapter one. Runtime, agent primitives, policy, and OS integration come next. The memory work is mapped in [RFC 006](https://github.com/yantrikos/yantrikdb-server/blob/main/docs/rfcs/006-context-aware-conflict-detection.md) — scoped claims as the primitive, context-aware conflict detection, phased across v0.6 → v0.7.

This is the early foundation. The OS is the destination.

## Get involved

- File issues, RFC feedback, PRs on any repo
- [Discussions](https://github.com/yantrikos/yantrikdb-server/discussions) on the main repo
- AGPL for the server, MIT for the MCP tooling

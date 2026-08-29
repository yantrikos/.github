<p align="center">
  <a href="https://yantrikdb.com">
    <img src="https://raw.githubusercontent.com/yantrikos/yantrikdb-web/main/public/icon.png" width="104" alt="YantrikDB Memory Mechanism logo">
  </a>
</p>

<h1 align="center">YantrikDB</h1>
<p align="center"><strong>Memory that just works.</strong></p>
<p align="center">
  Open-source cognitive memory for AI agents. Local when you want it, shared when you need it.
</p>

<p align="center">
  <a href="https://yantrikdb.com">Website</a> ·
  <a href="https://yantrikdb.com/guides/quickstart/">Quick start</a> ·
  <a href="https://yantrikdb.com/guides/mcp/">MCP setup</a> ·
  <a href="https://yantrikdb.com/research/benchmarks/">Benchmarks</a> ·
  <a href="https://github.com/yantrikos/yantrikdb-server/discussions">Discussions</a>
</p>

Your agent does not need another place to dump text. It needs memory that can
notice when facts changed, explain why something was recalled, keep tenants and
workspaces isolated, and remain useful after thousands of writes.

YantrikDB manages that full lifecycle: hybrid recall, temporal decay,
consolidation, contradiction tracking, entities and relations, provenance,
procedural memory, skills, and explicit maintenance. The core is Rust and the
same engine runs embedded, behind MCP, or as a replicated network database.

## Get an agent remembering in 60 seconds

```bash
pip install yantrikdb-mcp
```

For Codex:

```bash
codex mcp add yantrikdb -- yantrikdb-mcp
```

For Claude Code, Cursor, Windsurf, and other MCP clients:

```json
{
  "mcpServers": {
    "yantrikdb": {
      "command": "yantrikdb-mcp"
    }
  }
}
```

No cloud account is required. The default store is a local SQLite file and the
bundled embedder works without an external model service.

## Pick the shape that fits

| Run mode | Start here | Best for |
|---|---|---|
| **Embedded** | [`pip install yantrikdb`](https://pypi.org/project/yantrikdb/) or [`cargo add yantrikdb`](https://crates.io/crates/yantrikdb) | One application owning its memory in-process |
| **MCP** | [`pip install yantrikdb-mcp`](https://pypi.org/project/yantrikdb-mcp/) | Giving an existing coding agent memory across sessions |
| **Network** | [`docker pull ghcr.io/yantrikos/yantrikdb`](https://github.com/yantrikos/yantrikdb-server/pkgs/container/yantrikdb) | Shared memory, authenticated tenants, replication, and failover |

## What makes it cognitive

- **Memory can be wrong.** Contradictory structured claims remain visible and disputed until an operator resolves them.
- **Memory changes with time.** Recall supports decay, first-mention ordering, revision history, temporal ranges, and point-in-time queries.
- **Recall is inspectable.** Results include scores and retrieval reasons instead of asking you to trust an opaque top-k list.
- **Structure survives sessions.** Entities, typed relations, tasks, procedures, triggers, conversations, and skill outcomes live beside semantic memory.
- **Isolation is a primitive.** Namespaces scope records and cognitive state; the network server adds authenticated tenant databases.
- **The deployment path is real.** Start with one local file, then move to a server or YRP-replicated cluster without replacing the memory model.

## The ecosystem

| Project | Role |
|---|---|
| [`yantrikdb`](https://github.com/yantrikos/yantrikdb) | Apache-2.0 Rust engine and Python bindings |
| [`yantrikdb-mcp`](https://github.com/yantrikos/yantrikdb-mcp) | Drop-in MCP server and portable Agent Skill |
| [`yantrikdb-server`](https://github.com/yantrikos/yantrikdb-server) | Authenticated HTTP and wire APIs, tenancy, replication, and operations |
| [`yantrikdb-hermes-plugin`](https://github.com/yantrikos/yantrikdb-hermes-plugin) | Self-maintaining memory provider for Hermes Agent |
| [`openclaw-memory-yantrikdb`](https://github.com/yantrikos/openclaw-memory-yantrikdb) | Conflict-aware OpenClaw memory-slot plugin |
| [`langchain-yantrikdb`](https://github.com/yantrikos/langchain-yantrikdb) | LangChain VectorStore and ChatMessageHistory integration |
| [`yantrikdb-client`](https://github.com/yantrikos/yantrikdb-client) | Typed Python client for the network server |
| [`yantrikdb-web`](https://github.com/yantrikos/yantrikdb-web) | Documentation, live browser Memory Lab, and reproducible showcases |

Experimental work lives in [`yantrik-mind`](https://github.com/yantrikos/yantrik-mind).
It explores what a companion can become when typed beliefs, reflection,
delegation, and safety all share the same durable substrate.

## Inspect the evidence

We publish the awkward results as well as the wins. The benchmark pages include
commands, fixtures, caveats, and corrections so claims can be rerun rather than
repeated.

- [Run the browser Memory Lab](https://yantrikdb.com/#memory-lab)
- [Read the benchmark ledger](https://yantrikdb.com/research/benchmarks/)
- [Whose Memory, Whose Model?](https://yantrikdb.com/papers/beam-frozen-context/)
- [Skill as Memory, Not Document](https://doi.org/10.5281/zenodo.20128887)
- [See multi-agent memory handle a stale belief](https://yantrikdb.com/showcase/multi-agent/)

## Build with us

Use [Discussions](https://github.com/yantrikos/yantrikdb-server/discussions)
for architecture and product questions. File engine issues in
[`yantrikdb`](https://github.com/yantrikos/yantrikdb/issues), MCP issues in
[`yantrikdb-mcp`](https://github.com/yantrikos/yantrikdb-mcp/issues), and
server or cluster issues in
[`yantrikdb-server`](https://github.com/yantrikos/yantrikdb-server/issues).

The useful feedback is concrete: a memory your agent should have recalled, a
stale fact it should have downgraded, a conflict it failed to surface, or a
workflow that still takes too much ceremony.

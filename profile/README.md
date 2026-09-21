<p align="center">
  <a href="https://yantrikdb.com">
    <img src="https://raw.githubusercontent.com/yantrikos/.github/main/profile/logo.png" width="104" alt="YantrikDB logo">
  </a>
</p>

<h1 align="center">YantrikDB — memory for AI agents</h1>

<p align="center">
  <strong>Your agent forgets your project between sessions. This is the database that remembers.</strong>
</p>

<p align="center">
  Open source, local-first, and inspectable. Works with Claude Code, Cursor, Codex,
  Windsurf, and anything else that speaks MCP.
</p>

<p align="center">
  <a href="https://pypi.org/project/yantrikdb/"><img src="https://img.shields.io/pypi/v/yantrikdb?label=pypi&color=E8A33D" alt="PyPI version"></a>
  <a href="https://pypi.org/project/yantrikdb/"><img src="https://img.shields.io/pypi/dm/yantrikdb?label=installs%2Fmonth&color=E8A33D" alt="PyPI downloads per month"></a>
  <a href="https://crates.io/crates/yantrikdb"><img src="https://img.shields.io/crates/v/yantrikdb?label=crates.io&color=E8A33D" alt="crates.io version"></a>
  <a href="https://github.com/yantrikos/yantrikdb/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0"></a>
</p>

<p align="center">
  <a href="https://yantrikdb.com/guides/quickstart/">Quick start</a> ·
  <a href="https://yantrikdb.com/guides/mcp/">MCP setup</a> ·
  <a href="https://yantrikdb.com/research/benchmarks/">Benchmarks</a> ·
  <a href="https://yantrikdb.com/guides/memory-atlas/">Memory Atlas</a> ·
  <a href="https://github.com/yantrikos/yantrikdb-server/discussions">Discussions</a>
</p>

---

## Why not just a markdown file?

That is the right first question, and for a week of notes a `CLAUDE.md` is genuinely
fine. It stops being fine when the file gets long enough that everything in it is
loaded every turn, when two lines in it disagree and nothing notices, and when you
cannot tell why the agent brought up something from March.

|  | A notes file | A vector store | YantrikDB |
|---|---|---|---|
| Recalls only what is relevant | ✗ loads everything | ✓ | ✓ |
| Notices a fact changed | ✗ | ✗ keeps both | ✓ closes the old one and keeps the history |
| Surfaces contradictions | ✗ | ✗ | ✓ flags them for you to resolve |
| Tells you *why* it recalled something | ✗ | ✗ opaque top-k | ✓ scores and retrieval reasons |
| Answers "what did you believe in March?" | ✗ | ✗ | ✓ point-in-time recall |
| Still usable after 10,000 writes | ✗ becomes a junk drawer | partly | ✓ consolidation and decay |

## Get an agent remembering in 60 seconds

No account, no API key, no cloud. Memory lives in one SQLite file on your machine.

**Claude Code, Cursor, Windsurf, or any MCP client:**

```json
{
  "mcpServers": {
    "yantrikdb": {
      "command": "uvx",
      "args": ["yantrikdb-mcp"]
    }
  }
}
```

**Codex:**

```bash
codex mcp add yantrikdb -- uvx yantrikdb-mcp
```

**In your own Python or Rust:**

```bash
pip install yantrikdb        # or: cargo add yantrikdb
```

Your agent starts recalling prior context, recording decisions, and flagging
contradictions on its own — no prompting required.

## You can see everything it remembers

Memory you cannot inspect is memory you cannot trust. Every record carries where it
came from and why it was retrieved. You can read the store, correct a fact and keep
the old version, delete anything, or open the whole graph in your browser with
[Memory Atlas](https://yantrikdb.com/guides/memory-atlas/) — one command, no upload.

## Pick the shape that fits

| Run mode | Start here | Best for |
|---|---|---|
| **Embedded** | [`pip install yantrikdb`](https://pypi.org/project/yantrikdb/) · [`cargo add yantrikdb`](https://crates.io/crates/yantrikdb) | One application owning its memory in-process |
| **MCP server** | [`uvx yantrikdb-mcp`](https://pypi.org/project/yantrikdb-mcp/) | Giving a coding agent memory across sessions |
| **Self-hosted cluster** | [`docker pull ghcr.io/yantrikos/yantrikdb`](https://github.com/yantrikos/yantrikdb-server/pkgs/container/yantrikdb) | Shared memory, tenants, replication, failover |

The same engine runs in all three. Start with one local file and move to a server
later without changing the memory model.

## What it does that a vector index does not

- **Corrections keep receipts.** Tell it that it was wrong and the old belief becomes
  history rather than disappearing — you can still ask what it used to think.
- **Conflicting facts stay visible.** Contradictions are surfaced and marked disputed
  until someone resolves them, instead of both being served as true.
- **Time is a first-class dimension.** Decay, first-mention ordering, revision history,
  temporal ranges, and point-in-time queries.
- **Structure survives sessions.** Entities, typed relations, tasks, procedures,
  triggers, and skills live beside semantic memory.
- **Isolation is built in.** Namespaces scope every record; the server adds
  authenticated per-tenant databases.

## The projects

| Project | What it is |
|---|---|
| [`yantrikdb`](https://github.com/yantrikos/yantrikdb) | The engine — Rust core with Python bindings (Apache-2.0) |
| [`yantrikdb-mcp`](https://github.com/yantrikos/yantrikdb-mcp) | MCP server for Claude Code, Cursor, Codex, Windsurf, and friends |
| [`yantrikdb-server`](https://github.com/yantrikos/yantrikdb-server) | Self-hosted HTTP and wire APIs, tenancy, replication, operations |
| [`yantrikdb-hermes-plugin`](https://github.com/yantrikos/yantrikdb-hermes-plugin) | Memory provider for Hermes Agent |
| [`openclaw-memory-yantrikdb`](https://github.com/yantrikos/openclaw-memory-yantrikdb) | Memory slot plugin for OpenClaw |
| [`langchain-yantrikdb`](https://github.com/yantrikos/langchain-yantrikdb) | LangChain VectorStore and chat history |
| [`yantrikdb-client`](https://github.com/yantrikos/yantrikdb-client) | Typed Python client for the server |

## The evidence, including the parts that did not work

Benchmark pages ship with commands, fixtures, and caveats, so you can rerun them
rather than take our word for it — and the failed experiments stay published too.

- [LongMemEval retrieval](https://yantrikdb.com/papers/longmemeval-retrieval/) — 98.7% of queries retrieve every gold session at k=40 (479 of 500 queries, shipped defaults), with the command to rerun it and a section on why "recall@5" alone is not a number
- [Benchmark ledger](https://yantrikdb.com/research/benchmarks/) — token cost against file-based memory, with the script
- [Memory Lab in your browser](https://yantrikdb.com/#memory-lab) — no install
- [Multi-agent memory handling a stale belief](https://yantrikdb.com/showcase/multi-agent/)
- [Whose Memory, Whose Model?](https://yantrikdb.com/papers/beam-frozen-context/) · [Skill as Memory, Not Document](https://doi.org/10.5281/zenodo.20128887)

## Build with us

Questions and architecture discussion go in
[Discussions](https://github.com/yantrikos/yantrikdb-server/discussions). Bugs go to
the repo they belong to: [engine](https://github.com/yantrikos/yantrikdb/issues),
[MCP](https://github.com/yantrikos/yantrikdb-mcp/issues),
[server](https://github.com/yantrikos/yantrikdb-server/issues).

The most useful report is a concrete one: a memory your agent should have recalled
and did not, a stale fact it kept serving, a contradiction it missed, or a workflow
that still takes too much ceremony.

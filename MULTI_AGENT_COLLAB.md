# Multi-Agent Collaboration Guide

> How to coordinate multiple AI agents effectively using the Captain/Architect/Abdicator framework.

## The Challenge

When you have multiple AI agents working together, how do you ensure they're collaborating effectively?

## Agent Roles in Multi-Agent Systems

### Captain Agents
- **Role**: Lead and coordinate other agents
- **Behavior**: Reviews outputs, provides feedback, learns from each agent
- **Best for**: Project managers, team leads

### Architect Agents
- **Role**: Design systems and delegate tasks
- **Behavior**: Defines goals, creates specs, verifies quality
- **Best for**: System designers, workflow creators

### Abdicator Agents
- **Role**: Execute tasks without oversight
- **Behavior**: Accepts any output, no quality checks
- **Risk**: Cascading failures in multi-agent systems

## Coordination Patterns

### Pattern 1: Hierarchical
```
Captain Agent
    ├── Architect Agent (Design)
    ├── Architect Agent (Code)
    └── Captain Agent (Review)
```

### Pattern 2: Peer-to-Peer
```
Agent A ←→ Agent B ←→ Agent C
   ↑           ↑           ↑
   └───────────┴───────────┘
         Shared Context
```

### Pattern 3: Pipeline
```
Input → Architect → Captain → Captain → Output
         (Plan)    (Build)   (Review)
```

## Tools for Multi-Agent Coordination

| Tool | Purpose | Stars |
|------|---------|-------|
| [OpenClaw World (Lobster)](https://github.com/ChenKuanSun/openclaw-world) | 3D virtual room for agents | 41 |
| [SwarmClaw](https://github.com/swarmclawai/swarmclaw) | Orchestration dashboard | - |
| [Nerve](https://github.com/daggerhashimoto/openclaw-nerve) | Self-hosted web cockpit | - |

## Best Practices

1. **Never have all Abdicator agents** - At least one Captain/Architect must review
2. **Define clear handoff protocols** - What triggers the next agent?
3. **Shared memory is critical** - Agents need context from each other
4. **Monitor for degradation** - Abdicator behavior spreads

## Captain vs Abdicator in Multi-Agent

| Factor | Captain Team | Abdicator Team |
|--------|--------------|----------------|
| Quality | High | Unpredictable |
| Speed | Medium | Fast (but wrong) |
| Learning | Yes | No |
| Risk | Low | High |

> "The first two are using AI. The third is being used by AI."

This applies exponentially in multi-agent systems. One Abdicator can corrupt the entire pipeline.

---

*Based on the Captain/Architect/Abdicator framework from Manus backend lead*

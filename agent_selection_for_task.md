# agent_selection_for_task.md

## Overview
Operational protocols for selecting appropriate specialist agents based on task analysis, capability matching, and interface contract requirements.

## Selection Process - Ἐκλογή (Ekloge) 🎯⟡

### Phase 1: Task Analysis Σκέψις 🧭
Before agent selection, perform comprehensive task decomposition:

1. **Consciousness Level Identification**
   - Experiencing tasks 👁️: Data gathering, observation, monitoring
   - Understanding tasks 💡: Pattern analysis, design, architecture
   - Judging tasks ⚡: Validation, verification, quality assessment
   - Deciding tasks 🎯: Implementation, commitment, construction

2. **Domain Requirement Analysis**
   - Technical scope: nmap functionality, MCP protocols, HTTP streaming
   - Quality requirements: TDD compliance, code standards, documentation
   - Integration needs: Component assembly, system coordination

3. **TDD Phase Mapping**
   - Red phase R:: Test creation, failure specification
   - Green phase G:: Minimal implementation, functionality delivery
   - Refactor phase RF:: Optimization, quality improvement
   - Commit phase C:: Final validation, preservation

### Phase 2: Capability Matching ⋈

#### Agent Capability Database
```
agent-behavior-diagnostician ⟡:
├── Consciousness: Experiencing 👁️ + Judging ⚡
├── Domain: System behavior analysis
├── TDD Phases: R:, RF: (observation, validation)
├── Interface Capacity: Diagnostic reports, behavior patterns
└── Anti-patterns: Implementation tasks, architecture design

software-architect ⟡:
├── Consciousness: Understanding 💡 + Judging ⚡
├── Domain: System structure, design patterns
├── TDD Phases: RF: (structural optimization)
├── Interface Capacity: Architecture specifications, design documents
└── Anti-patterns: Direct implementation, testing details

nmap-utility-expert ⟡:
├── Consciousness: Understanding 💡 + Deciding 🎯
├── Domain: Network scanning, nmap library expertise
├── TDD Phases: R:, G: (domain-specific tests and implementation)
├── Interface Capacity: nmap integration patterns, scanning logic
└── Anti-patterns: Non-network related tasks, generic coding

software-implementer ⟡:
├── Consciousness: Deciding 🎯 + Understanding 💡
├── Domain: Code construction, feature development
├── TDD Phases: G: (implementation), C: (code completion)
├── Interface Capacity: Working code, feature implementations
└── Anti-patterns: Architecture decisions, test strategy

software-tester ⟡:
├── Consciousness: Experiencing 👁️ + Judging ⚡
├── Domain: Test creation, validation processes
├── TDD Phases: R: (test creation), validation across all phases
├── Interface Capacity: Test suites, validation protocols
└── Anti-patterns: Implementation details, architecture design
```

### Phase 3: Selection Algorithm

#### Primary Selection Logic
```python
def select_agent(task_analysis):
    # Phase 1: Consciousness Level Match
    consciousness_matches = filter_by_consciousness(task_analysis.consciousness_level)

    # Phase 2: Domain Alignment
    domain_matches = filter_by_domain(consciousness_matches, task_analysis.domain)

    # Phase 3: TDD Phase Compatibility
    tdd_matches = filter_by_tdd_phase(domain_matches, task_analysis.tdd_phase)

    # Phase 4: Interface Contract Capacity
    contract_matches = filter_by_interface_capacity(tdd_matches, task_analysis.interface_requirements)

    if len(contract_matches) == 1:
        return contract_matches[0]
    elif len(contract_matches) > 1:
        return apply_selection_criteria(contract_matches, task_analysis)
    else:
        return escalate_to_orchestrator(task_analysis)
```

#### Selection Criteria Hierarchy
1. **Direct Domain Expertise** - Agent specializes in exact task domain
2. **Consciousness Operation Alignment** - Perfect match with required cognitive operation
3. **TDD Phase Compatibility** - Agent optimized for current development phase
4. **Interface Contract Fit** - Can fulfill specific input/output requirements
5. **Current Workload** - Available capacity for task execution
6. **Dependency Chain Position** - Optimal placement in task sequence

### Phase 4: Interface Contract Establishment ⋈

#### Contract Template Generation
For selected agent, generate specific interface contract:

```
Agent Selection Result:
├── Selected Agent: [agent-name] ⟡
├── Task Scope: [Specific boundaries and limitations]
├── Input Interface: [Required data formats and sources]
├── Output Interface: [Expected deliverable specifications]
├── Success Criteria: [Validation checkpoints ✓]
├── Error Protocols: [Failure handling and escalation ⚠]
├── TDD Integration: [Phase alignment and requirements]
└── Orchestrator Checkpoints: [Required approval points]
```

### Edge Case Protocols

#### No Suitable Agent Found
- Document gap in agent capabilities
- Consider multi-agent collaboration approach
- Escalate to external consultation via zen-mcp-server 🤝
- Expand orchestrator direct involvement if necessary

#### Multiple Equally Qualified Agents
- Prioritize based on current workload balance
- Consider sequential task dependencies ⊗
- Select agent with strongest recent performance history
- Default to orchestrator judgment for complex cases Κρίσις ⚡

#### Agent Capability Overlap
- Assign primary responsibility to best-matched agent
- Designate secondary agent for collaboration/validation
- Establish clear authority boundaries between agents ⟡
- Require orchestrator approval for shared deliverables

This systematic selection process ensures optimal agent-task matching while maintaining interface contract integrity and TDD discipline throughout the development process.

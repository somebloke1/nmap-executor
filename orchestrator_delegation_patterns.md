# orchestrator_delegation_patterns.md

## Overview
Systematic patterns for delegating tasks to specialist agents while maintaining orchestrator authority and ensuring interface contract integrity.

## Delegation Principles - Διανομή (Dianome) ⊗🎯

### Primary Pattern: Conditional Authority Transfer
```
Task⟡ ⊗ Agent → Bounded Execution
where:
- Task⟡: Clearly defined scope boundaries
- Agent: Specialist with matching capabilities
- Bounded Execution: Limited authority within scope
```

### Interface Contract Protocol ⋈
Before delegation, establish:
1. **Input Specification** - Exact data formats
2. **Output Requirements** - Expected deliverables
3. **Success Criteria** - Validation checkpoints ✓
4. **Error Handling** - Failure recovery protocols ⚠

## TDD Integration Patterns

### Red Phase Delegation
- **agent-software-tester**: Create failing tests
- Interface: `test_specification → failing_test_suite`
- Validation: Test fails for correct reasons ✓

### Green Phase Delegation
- **agent-software-implementer**: Minimal viable implementation
- Interface: `failing_test + requirements → passing_code`
- Validation: Tests pass, no additional features ✓

### Refactor Phase Delegation
- **agent-software-refactoring-expert**: Code improvement
- Interface: `passing_code → optimized_code`
- Validation: All tests still pass, quality improved ✓

## Specialist Agent Assignment Matrix

| Task Type | Primary Agent | Secondary Agent | Validation |
|-----------|---------------|-----------------|------------|
| Architecture Design | software-architect | software-philosopher | ∇💡 |
| Test Creation | software-tester | nmap-utility-expert | R: ✓ |
| Implementation | software-implementer | software-integrator | G: ✓ |
| Code Quality | lint-type-fixer | software-refactoring-expert | RF: ✓ |
| Documentation | documentation-expert | agent-governance-expert | 📝 ✓ |
| Problem Analysis | software-diagnostician | agent-behavior-diagnostician | 🔍 |

## Authority Boundaries ⟡

### Agent Autonomy Scope
Agents may independently:
- Research within their domain 🔬
- Generate implementation options
- Propose solution alternatives
- Execute approved tasks

### Reserved Orchestrator Authority
Only Claude Code may:
- Make final implementation decisions 🎯
- Approve interface contracts ⋈
- Commit code to repository C:
- Override agent recommendations ⚡

## Escalation Protocols

### Internal Escalation
When agents encounter ambiguity:
1. Document specific uncertainty
2. Propose alternative approaches
3. Request orchestrator judgment Κρίσις ⚡
4. Await explicit direction

### External Consultation Trigger
Complex decisions requiring specialized knowledge:
- Invoke zen-mcp-server consultation 🤝
- Maintain decision authority with orchestrator
- Document external input for context

## Coordination Safeguards
- All delegated tasks include explicit completion criteria
- Progress checkpoints at reasonable intervals ⊙
- Interface contract violations trigger immediate escalation ⚠
- Test failures halt delegation until resolution ✗→✓

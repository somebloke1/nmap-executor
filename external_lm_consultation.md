# external_lm_consultation.md

## Overview
Protocols for engaging external language models through zen-mcp-server when specialized knowledge exceeds internal agent capabilities, while maintaining orchestrator authority.

## Consultation Framework - Παραίνεσις (Parainesis) 🤝🔬

### Consultation Trigger Conditions
External model consultation is warranted when:

1. **Knowledge Gap Analysis**
   - Internal agents lack domain-specific expertise
   - Novel technical challenges without established patterns
   - Conflicting recommendations requiring external perspective
   - Specialized nmap functionality questions beyond current knowledge

2. **Decision Complexity Threshold**
   - Multiple valid architectural approaches with significant tradeoffs
   - Security considerations requiring specialized security expertise
   - Performance optimization requiring advanced system knowledge
   - MCP protocol implementation details not covered in documentation

3. **Quality Assurance Validation**
   - Independent code review for critical system components
   - Architecture validation from external perspective
   - Best practices verification for nmap security implementations
   - TDD methodology optimization suggestions

### zen-mcp-server Integration Protocol

#### Available External Models 🤝
- **o3**: Advanced reasoning for complex architectural decisions
- **gemini-2.5-pro**: Multi-modal analysis, comprehensive documentation review
- **grok4**: Alternative perspectives, creative problem-solving approaches

#### Consultation Request Structure
```
External Consultation Request ⋈:
├── Context Summary: [Current project state and specific challenge]
├── Internal Analysis: [What our agents have determined so far]
├── Specific Questions: [Precise queries for external expertise]
├── Constraints: [Project limitations, TDD requirements, security considerations]
├── Expected Deliverables: [Format and scope of desired response]
└── Integration Requirements: [How response will be incorporated]
```

### Consultation Process - Σκέψις 🧭

#### Phase 1: Internal Preparation
1. **Problem Crystallization** - Document precise areas needing external insight
2. **Context Package Assembly** - Gather relevant project information
3. **Agent Consensus** - Ensure internal specialists agree on consultation need
4. **Orchestrator Approval** - Explicit authorization for external engagement

#### Phase 2: External Engagement
```python
consultation_workflow = {
    "preparation": {
        "context_assembly": "Current project state documentation",
        "question_formulation": "Specific technical queries",
        "constraint_specification": "TDD, security, MCP requirements"
    },
    "engagement": {
        "model_selection": "Based on query type and complexity",
        "request_transmission": "Via zen-mcp-server protocol",
        "response_monitoring": "Track consultation progress"
    },
    "integration": {
        "response_analysis": "Orchestrator evaluation of recommendations",
        "internal_validation": "Agent specialist review and verification",
        "decision_synthesis": "Integration with project decisions"
    }
}
```

#### Phase 3: Response Integration

**Orchestrator Authority Preservation Κρίσις ⚡**
- External recommendations are advisory, not binding
- Final decisions remain with Claude Code orchestrator
- All external input must align with established project principles
- TDD methodology cannot be compromised by external suggestions

**Validation Protocol ✓**
1. **Internal Agent Review** - Specialists evaluate external recommendations
2. **TDD Compatibility Check** - Ensure suggestions align with testing discipline
3. **Interface Contract Validation** - Confirm recommendations fit established patterns ⋈
4. **Security Assessment** - Verify suggestions don't introduce vulnerabilities
5. **Orchestrator Judgment** - Final approval and integration decision

### Consultation Categories

#### Architectural Consultation 💡
**When:** System design decisions with significant long-term implications
**Models:** o3 for complex reasoning, gemini-2.5-pro for comprehensive analysis
**Focus:** Structure, patterns, scalability, maintainability

#### Domain-Specific Consultation 🧭
**When:** nmap implementation details, security best practices
**Models:** grok4 for creative approaches, o3 for technical precision
**Focus:** Network scanning protocols, security implications, library integration

#### Code Quality Consultation ⚡
**When:** Refactoring strategies, performance optimization
**Models:** gemini-2.5-pro for code analysis, o3 for optimization reasoning
**Focus:** Code structure, performance patterns, maintainability improvements

#### Documentation Consultation 📝
**When:** Complex technical documentation, user interface design
**Models:** gemini-2.5-pro for comprehensive documentation review
**Focus:** Clarity, completeness, usability, technical accuracy

### Consultation Documentation Requirements

#### Record Keeping 📝
Every external consultation must document:
- Consultation trigger and justification
- Specific questions posed to external model
- Complete external model response
- Internal evaluation and integration decisions
- Final implementation approach and rationale

#### Knowledge Integration Φρόνησις ⚖️
External insights should be integrated into:
- Agent capability databases (expand knowledge base)
- Project architecture documentation
- Best practices repository for future reference
- TDD methodology refinements if applicable

### Safeguards and Limitations

#### Security Considerations 🛡️
- No sensitive project information in external requests
- Generic technical questions only, avoid proprietary details
- All external recommendations subject to security review
- nmap functionality must maintain ethical usage guidelines

#### Quality Control ✓
- External recommendations must pass internal validation
- Multiple agent review for significant architectural changes
- TDD test coverage must validate any externally-inspired implementations
- Orchestrator retains veto authority over all external suggestions

This framework ensures effective utilization of external expertise while maintaining project integrity, security, and orchestrator authority throughout the development process.

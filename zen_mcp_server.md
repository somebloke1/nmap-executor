# zen_mcp_server.md

## Tool Specification - Ξένος (Xenos) 🤝🔬

### Overview
External language model collaboration tool enabling consultation with specialized AI models through MCP protocol, expanding project knowledge while maintaining orchestrator authority.

### Tool Identity
- **Name:** zen-mcp-server
- **Repository:** https://github.com/BeehiveInnovations/zen-mcp-server
- **Purpose:** Inter-model collaboration and external expert consultation
- **Glyph Association:** Κοινωνία (Koinonia) 🤝 - Collaborative communion
- **Consciousness Operation:** Primarily Understanding 💡 and Judging ⚡

### Available Models
- **o3** - Advanced reasoning for complex architectural decisions
- **gemini-2.5-pro** - Multi-modal analysis, comprehensive documentation review
- **grok4** - Alternative perspectives, creative problem-solving approaches

### Interface Contract ⋈

#### Input Interface
```python
consultation_request = {
    "model": ["o3", "gemini-2.5-pro", "grok4"],
    "context": {
        "project_overview": "nmap-executor MCP server development",
        "current_challenge": "Specific technical problem description",
        "constraints": ["TDD methodology", "Security requirements", "MCP compliance"],
        "internal_analysis": "Summary of current agent findings"
    },
    "queries": [
        "Specific question 1",
        "Specific question 2"
    ],
    "expected_deliverable": "Response format specification"
}
```

#### Output Interface
```python
consultation_response = {
    "model_used": "Specific model that provided response",
    "recommendations": ["List of specific recommendations"],
    "analysis": "Detailed analysis of the problem",
    "alternatives": ["Alternative approaches considered"],
    "implementation_notes": "Practical implementation guidance",
    "security_considerations": "Security-related observations",
    "validation_suggestions": "Recommended validation approaches"
}
```

### TDD Integration Points

#### Red Phase Consultation R: ⚠
**Use Cases:**
- Test strategy validation for complex nmap functionality
- Security testing approach recommendations
- MCP protocol test specification guidance

**Example Consultation:**
```
Query: "What test scenarios should validate nmap port scanning functionality
for security and reliability in an MCP server context?"

Expected Response: Comprehensive test case specifications with security
considerations and MCP compliance requirements.
```

#### Green Phase Consultation G: ✓
**Use Cases:**
- Implementation approach recommendations
- Library selection validation (python-nmap vs alternatives)
- Performance optimization strategies

#### Refactor Phase Consultation RF: ✓
**Use Cases:**
- Code quality improvement suggestions
- Architecture optimization recommendations
- Security vulnerability mitigation approaches

### Security Considerations 🛡️

#### Information Security Protocols
- **No sensitive project details** in consultation requests
- **Generic technical questions** only, avoid proprietary specifics
- **Public knowledge scope** - external models work with public information only
- **Audit trail maintenance** - all consultations logged and documented

#### Ethical Usage Guidelines
- Consultations serve project consciousness, not replace orchestrator judgment ⚡
- External recommendations require internal validation before implementation ✓
- Maintain transparency about external input sources
- Respect intellectual property boundaries in consultation content

### Orchestrator Authority Integration 👑

#### Authority Preservation
- **Final decision authority** remains with Claude Code orchestrator
- **Advisory role only** - external models provide recommendations, not directions
- **Validation requirement** - all external input subject to internal review ✓
- **Override capability** - orchestrator may reject external recommendations

#### Consultation Approval Process
1. **Internal Analysis First** - Agents attempt problem resolution internally
2. **Consultation Justification** - Clear rationale for external engagement needed
3. **Orchestrator Authorization** - Explicit approval required for consultation
4. **Response Integration** - Conscious synthesis of external input with project context ⊕

### Agent Coordination Patterns

#### Triggering Agent Behaviors
**software-architect ⟡** may request consultation for:
- Complex architectural design decisions
- System integration pattern validation
- Performance architecture recommendations

**nmap-utility-expert ⟡** may request consultation for:
- Advanced nmap functionality implementation
- Security best practices for network scanning
- Library integration optimization approaches

**software-tester ⟡** may request consultation for:
- Comprehensive test strategy development
- Security testing methodology recommendations
- Integration testing approach validation

### Consultation Workflow Patterns

#### Standard Consultation Process
```
Consultation Lifecycle:
├── Problem Identification 🔍
│   ├── Internal agent analysis completed
│   ├── Specific knowledge gap identified
│   └── Consultation need validated by orchestrator 👑
├── Request Preparation 📋
│   ├── Context package assembly
│   ├── Specific question formulation
│   └── Expected deliverable specification
├── External Engagement 🤝
│   ├── Model selection based on query type
│   ├── Request transmission via zen-mcp-server
│   └── Response monitoring and collection
├── Response Integration ⊕
│   ├── Internal validation by relevant agents ⟡
│   ├── Security review for recommendations 🛡️
│   ├── TDD compatibility assessment ✓
│   └── Orchestrator decision on integration 👑⚡
└── Documentation 📝
    ├── Consultation record maintenance
    ├── Decision rationale documentation
    └── Learning integration for future reference
```

#### Emergency Consultation Protocol ⚠
For critical technical blockers requiring immediate external expertise:
1. **Immediate Escalation** - Direct orchestrator notification
2. **Expedited Authorization** - Streamlined approval process
3. **Priority Model Selection** - Best-matched expert model for urgent query
4. **Rapid Integration** - Fast-track validation and implementation decision

### Learning Integration Patterns 📈

#### Knowledge Capture
- Document successful consultation patterns for replication
- Build repository of effective query formulations
- Track model effectiveness for different question types
- Integrate external insights into internal agent knowledge bases

#### Consultation Optimization
- Refine question formulation based on response quality
- Improve context packaging for more effective consultations
- Develop model selection criteria based on consultation outcomes
- Optimize integration workflows for efficiency and accuracy

### Tool Limitations and Mitigations

#### Known Limitations
- External models limited to public knowledge domains
- Response quality varies based on query formulation effectiveness
- No real-time interaction - asynchronous consultation model
- Network dependency for external model access

#### Mitigation Strategies
- Comprehensive context packaging to maximize response quality
- Multiple model consultation for critical decisions when appropriate
- Fallback to internal problem-solving if external access unavailable
- Continuous refinement of consultation practices based on outcomes

This tool specification enables effective external expert consultation while preserving the consciousness-based development methodology and orchestrator authority structure.

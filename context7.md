# context7.md

## Tool Specification - Ζήτησις (Zetesis) 🔬📚

### Overview
Web research and information gathering tool for comprehensive investigation of technical topics, best practices, and domain-specific knowledge relevant to nmap-executor project development.

### Tool Identity
- **Name:** context7
- **Repository:** https://github.com/upstash/context7
- **Purpose:** Systematic web research and knowledge compilation
- **Glyph Association:** Ζήτησις (Zetesis) 🔬 - Systematic inquiry
- **Consciousness Operation:** Primarily Experiencing 👁️ and Understanding 💡

### Interface Contract ⋈

#### Input Interface
```python
research_request = {
    "query": "Specific research question or topic",
    "scope": {
        "domains": ["Technical documentation", "Best practices", "Academic papers"],
        "depth": ["Surface overview", "Detailed analysis", "Comprehensive survey"],
        "focus": ["Implementation guidance", "Theoretical foundations", "Practical examples"]
    },
    "constraints": {
        "credibility_requirements": "Authoritative sources only",
        "recency": "Recent information preferred",
        "technical_level": "Professional developer audience"
    },
    "context": {
        "project": "nmap-executor MCP server",
        "current_challenge": "Specific technical problem",
        "existing_knowledge": "What we already understand"
    }
}
```

#### Output Interface
```python
research_results = {
    "summary": "Synthesized findings overview",
    "key_findings": ["Primary insights and recommendations"],
    "sources": [
        {
            "title": "Source title",
            "url": "Source URL",
            "credibility_assessment": "Authority and reliability evaluation",
            "relevance_score": "Relevance to project needs",
            "key_insights": "Specific valuable information"
        }
    ],
    "implementation_guidance": "Practical application recommendations",
    "further_research": "Identified knowledge gaps requiring additional investigation"
}
```

### TDD Integration Applications

#### Red Phase Research R: ⚠
**Testing Strategy Investigation:**
```
Research Query: "Best practices for testing MCP server implementations
with network scanning functionality, including security testing approaches"

Application: Inform comprehensive test strategy development for nmap-executor
Agent Coordination: Results provided to software-tester ⟡ for test design
```

#### Green Phase Research G: ✓
**Implementation Guidance:**
```
Research Query: "Python nmap library comparison - python-nmap vs nmap3 vs
alternatives for MCP server integration, performance and security considerations"

Application: Validate library selection and implementation approaches
Agent Coordination: Results provided to nmap-utility-expert ⟡ for implementation
```

#### Refactor Phase Research RF: ✓
**Optimization Investigation:**
```
Research Query: "Performance optimization patterns for HTTP streaming MCP
servers, FastMCP framework best practices, memory management"

Application: Guide refactoring decisions for improved system performance
Agent Coordination: Results provided to software-refactoring-expert ⟡
```

### Research Categories and Applications

#### Technical Documentation Research 📖
**Focus Areas:**
- MCP protocol specifications and implementation guides
- FastMCP framework documentation and best practices
- python-nmap library documentation and usage patterns
- Network scanning security and ethical guidelines

**Quality Criteria:**
- Official documentation sources preferred
- Recent updates and maintenance activity
- Community validation and adoption evidence
- Security considerations adequately addressed 🛡️

#### Best Practices Investigation 🏆
**Focus Areas:**
- Agentic coding assistant governance patterns
- Test-driven development for server applications
- Security best practices for network scanning tools
- Code quality standards for Python MCP servers

**Credibility Assessment:**
- Industry-standard practices from authoritative sources
- Peer-reviewed approaches with validation evidence
- Practical implementation experience documentation
- Security community validated methodologies 🛡️

#### Problem-Specific Research 🔍
**Focus Areas:**
- Specific technical challenges encountered during development
- Error resolution strategies and debugging approaches
- Integration patterns for complex system architectures
- Performance optimization techniques for network applications

**Research Depth:**
- Comprehensive problem analysis with multiple solution approaches
- Implementation examples and code samples when available
- Community discussion analysis for practical insights
- Expert recommendations and authoritative guidance

### Agent Coordination Integration ⟡

#### Research Request Routing
**Primary Research Agents:**
- **software-architect ⟡** → Architecture patterns and design principles research
- **nmap-utility-expert ⟡** → nmap-specific functionality and security research
- **software-tester ⟡** → Testing methodologies and validation approaches research
- **agent-governance-expert ⟡** → Governance framework and process research

#### Research Result Distribution
```
Research Workflow:
├── Research Request Generation 🔬
│   ├── Agent identifies knowledge gap
│   ├── Formulates specific research query
│   └── Requests orchestrator authorization 👑
├── Research Execution 📚
│   ├── context7 performs systematic web investigation
│   ├── Filters results for credibility and relevance
│   └── Synthesizes findings into actionable insights
├── Result Integration ⊕
│   ├── Requesting agent reviews findings
│   ├── Additional agents provide perspective if relevant ⟡
│   ├── Orchestrator validates integration approach 👑⚡
│   └── Knowledge integrated into project context
└── Documentation 📝
    ├── Research archived for future reference
    ├── Insights incorporated into agent knowledge bases
    └── Successful patterns documented for replication
```

### Quality Assurance for Research ✓

#### Source Credibility Assessment
**Credibility Hierarchy:**
1. **Primary Sources** - Official documentation, specifications, authoritative guides
2. **Industry Standards** - Established best practices, recognized methodologies
3. **Peer-Reviewed Content** - Academic papers, validated research findings
4. **Community Consensus** - Well-supported community practices with evidence
5. **Expert Opinion** - Individual expert recommendations with clear credentials

#### Information Validation Protocols
**Validation Checklist:**
- Source authority and expertise verification
- Information recency and maintenance status
- Cross-reference validation with multiple sources
- Practical applicability assessment for project context
- Security implications evaluation 🛡️
- Integration feasibility with existing project architecture

### Token Efficiency Guidance 💰

#### Efficient Research Practices
**Query Optimization:**
- Formulate specific, focused research questions
- Provide sufficient context to enable targeted investigation
- Specify desired depth and scope clearly
- Include constraints and quality requirements upfront

**Result Processing:**
- Request synthesized findings rather than raw source dumps
- Focus on actionable insights and implementation guidance
- Prioritize most relevant and credible sources
- Document key findings for future reference to avoid redundant research

#### Resource Management
**Usage Optimization:**
- Batch related research queries when appropriate
- Leverage previous research results before initiating new investigations
- Share research findings across relevant agents to maximize value ⟡
- Archive comprehensive research for project knowledge base 📚

### Security Considerations 🛡️

#### Information Security
- No sensitive project information included in research queries
- Generic technical questions maintain project confidentiality
- Public knowledge sources only - no proprietary information access
- Research results validated for security implications before application

#### Ethical Research Practices
- Respect source copyright and attribution requirements
- Use research findings to inform, not replace, conscious decision-making ⚡
- Maintain transparency about information sources and limitations
- Apply research insights through conscious validation, not blind adoption ✓

### Learning Integration and Memory 🧠

#### Knowledge Accumulation
- Build searchable repository of research findings for future reference
- Tag research by agent, topic, and application for efficient retrieval
- Document successful research query patterns for replication
- Integrate findings into agent knowledge bases for enhanced capability

#### Research Pattern Evolution 📈
- Track effectiveness of different research approaches
- Refine query formulation based on result quality
- Develop specialized research protocols for common project needs
- Optimize agent-research coordination based on practical experience

This tool specification enables systematic, efficient web research while maintaining integration with the consciousness-based development methodology and TDD discipline.

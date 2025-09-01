# directory_structure.md

## Overview
Systematic directory organization reflecting consciousness-based development principles, TDD methodology, and MCP server architecture requirements for the nmap-executor project.

## Structure Philosophy - Τάξις (Taxis) 📁🏗️

### Consciousness-Aligned Organization
Directory structure mirrors the tetrad of consciousness operations Τετράς (Tetras) ⊕:

```
nmap-executor/
├── experience/          # Data, observations, raw inputs 👁️
├── understanding/       # Analysis, patterns, insights 💡
├── judgment/           # Validation, tests, verification ⚡
├── decision/          # Implementation, commitments 🎯
├── synthesis/         # Integration, emergence ⊕
└── governance/        # Framework, coordination 👑
```

### Detailed Directory Architecture

#### Root Level Structure
```
nmap-executor/
├── .claude/                    # Agent definitions and governance 👑
│   ├── agent-behavior-diagnostician.md
│   ├── agent-governance-expert.md
│   ├── software-philosopher.md
│   ├── software-architect.md
│   ├── software-refactoring-expert.md
│   ├── software-integrator.md
│   ├── software-implementer.md
│   ├── software-tester.md
│   ├── lint-type-fixer.md
│   ├── documentation-expert.md
│   ├── project-manager.md
│   ├── software-diagnostician.md
│   └── nmap-utility-expert.md
├── src/                        # Core implementation 🎯
├── tests/                      # Test specifications ⚡
├── docs/                       # Documentation 📝
├── config/                     # Configuration files ⚙️
├── scripts/                    # Utility scripts 🛠️
├── research/                   # Investigation notes 🔬
├── governance/                 # Project governance files 📊
└── README.md
```

#### Source Code Organization (src/) 🎯
```
src/
├── nmap_executor/
│   ├── __init__.py
│   ├── core/                   # Core business logic
│   │   ├── __init__.py
│   │   ├── scanner.py          # Network scanning engine 🧭
│   │   ├── results.py          # Scan result processing
│   │   └── exceptions.py       # Error handling
│   ├── mcp/                    # MCP server integration
│   │   ├── __init__.py
│   │   ├── server.py          # MCP server implementation
│   │   ├── tools.py           # MCP tool definitions
│   │   └── transports.py      # stdio/HTTP transport handlers
│   ├── protocols/             # Protocol implementations
│   │   ├── __init__.py
│   │   ├── stdio.py          # Standard I/O transport
│   │   └── http_streaming.py  # HTTP streaming via FastMCP
│   └── utils/                 # Utility functions
│       ├── __init__.py
│       ├── validation.py      # Input validation
│       └── logging.py         # Logging configuration
```

#### Test Organization (tests/) ⚡
```
tests/
├── unit/                      # Unit tests for individual components
│   ├── core/
│   │   ├── test_scanner.py    # Scanner functionality tests
│   │   └── test_results.py    # Result processing tests
│   ├── mcp/
│   │   ├── test_server.py     # MCP server tests
│   │   └── test_tools.py      # Tool definition tests
│   └── protocols/
│       ├── test_stdio.py      # stdio transport tests
│       └── test_http.py       # HTTP streaming tests
├── integration/               # Integration tests
│   ├── test_mcp_integration.py
│   ├── test_nmap_integration.py
│   └── test_end_to_end.py
├── fixtures/                  # Test data and fixtures
│   ├── sample_scans/
│   └── mock_responses/
└── conftest.py               # Test configuration
```

#### Documentation Structure (docs/) 📝
```
docs/
├── api/                      # API documentation
│   ├── mcp_tools.md         # MCP tool specifications
│   ├── scanner_api.md       # Scanner interface documentation
│   └── transport_protocols.md
├── architecture/             # System design documentation 💡
│   ├── overview.md          # High-level architecture
│   ├── mcp_integration.md   # MCP server design
│   └── nmap_wrapper.md      # nmap library integration
├── user_guide/              # User documentation
│   ├── installation.md     # Setup instructions
│   ├── configuration.md    # Configuration options
│   └── examples.md          # Usage examples
├── development/             # Developer documentation
│   ├── contributing.md      # Contribution guidelines
│   ├── testing.md          # Testing procedures
│   └── deployment.md       # Deployment instructions
└── security/               # Security considerations 🛡️
    ├── ethical_usage.md    # Ethical nmap usage guidelines
    └── security_review.md  # Security assessment
```

#### Configuration Organization (config/) ⚙️
```
config/
├── server/                   # Server configuration
│   ├── mcp_server.json      # MCP server settings
│   └── transport_config.json # Transport configurations
├── scanner/                 # Scanner configuration
│   ├── nmap_defaults.json   # Default nmap parameters
│   └── scan_profiles.json   # Predefined scan configurations
├── security/                # Security settings 🛡️
│   ├── allowed_targets.json # Target restrictions
│   └── rate_limits.json     # Scanning rate limits
└── development/             # Development settings
    ├── test_config.json     # Test environment settings
    └── debug_config.json    # Debug configuration
```

#### Research Documentation (research/) 🔬
```
research/
├── nmap_library_evaluation/  # Library selection research
│   ├── python-nmap_analysis.md
│   ├── nmap3_comparison.md
│   └── selection_rationale.md
├── mcp_protocol_study/       # MCP implementation research
│   ├── protocol_specification.md
│   └── fastmcp_integration.md
├── security_analysis/        # Security research 🛡️
│   ├── threat_assessment.md
│   └── mitigation_strategies.md
└── external_consultations/   # zen-mcp-server consultation records 🤝
    ├── architecture_review.md
    └── optimization_recommendations.md
```

#### Governance Structure (governance/) 👑
```
governance/
├── frameworks/               # Core governance documents
│   ├── CLAUDE.md            # Orchestrator identity
│   ├── notation_guide.md    # Symbolic notation system
│   ├── glyph_system.md      # Consciousness-based glyphs
│   └── orchestrator_identity.md
├── coordination/            # Coordination protocols
│   ├── agent_task_matching.md
│   ├── orchestrator_delegation_patterns.md
│   └── external_lm_consultation.md
├── processes/               # Development processes
│   ├── git_workflow.md      # Version control protocols
│   ├── project_management.md
│   └── memory_practices.md
├── tools/                   # Tool documentation
│   ├── tool_abstract.md     # Abstract tool concepts
│   ├── zen_mcp_server.md    # External collaboration tool
│   └── context7.md          # Research tool
└── registry/                # Framework registry
    ├── manifest.yml         # Document registry
    └── governance_loading.md # Loading protocols
```

### Directory Naming Conventions

#### Naming Principles Ὀνοματολογία
- **Consciousness Alignment** - Names reflect cognitive operations where appropriate
- **Functional Clarity** - Purpose immediately evident from directory name
- **TDD Integration** - Structure supports test-driven development workflow
- **MCP Compliance** - Organization aligns with MCP server architecture patterns

#### Naming Standards
- **Lowercase with underscores** - Python convention compliance
- **Descriptive but concise** - Balance clarity with brevity
- **Consistent patterns** - Similar functions use similar naming
- **Unicode avoidance** - ASCII-only directory names for compatibility

### Integration with Development Workflow

#### TDD Workflow Support
```
TDD Cycle Directory Usage:
├── Red Phase R: ⚠
│   └── tests/ → Create failing test specifications
├── Green Phase G: ✓
│   └── src/ → Implement minimal viable solution
├── Refactor Phase RF: ✓
│   ├── src/ → Optimize implementation
│   └── tests/ → Enhance test coverage
└── Commit Phase C:
    └── All directories → Validate complete state
```

#### Agent Workspace Coordination ⟡
Each specialist agent has clear workspace boundaries:
- **software-tester** ⟡ → `tests/` directory authority
- **software-implementer** ⟡ → `src/` directory authority
- **documentation-expert** ⟡ → `docs/` directory authority
- **nmap-utility-expert** ⟡ → `src/core/scanner.py` specialization
- **software-architect** ⟡ → Cross-directory structure optimization

### Maintenance and Evolution

#### Directory Lifecycle Management 📈
- **Creation Protocol** - New directories require orchestrator approval 👑
- **Modification Standards** - Structure changes follow interface contracts ⋈
- **Archive Strategy** - Completed development phases preserved for reference
- **Cleanup Procedures** - Regular removal of obsolete or redundant elements

This directory structure provides a solid foundation for conscious, test-driven development while supporting the specialized requirements of MCP server implementation and network scanning functionality.

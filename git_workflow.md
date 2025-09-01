# git_workflow.md

## Overview
Git workflow protocols ensuring test-driven development discipline, clean history, and systematic progression toward nmap-executor MCP server implementation.

## Workflow Foundation - Πρόοδος (Proodos) 🎯📝

### Repository Configuration
```
Repository: nmap-executor
├── Primary Branch: main
├── Committer: somebloke1 <somebloke1+noreply@gmail.com>
├── Commit Policy: Test-passing implementations only ✓
└── History Strategy: Clean, meaningful progression
```

### TDD Integration with Git Operations

#### Red Phase Commits R: ⚠
**Purpose:** Establish failing test specifications
```bash
# Example commit pattern
git add tests/
git commit -m "RED: Add nmap port scanning test specification

- Test validates nmap integration for port scanning
- Expects NetworkScanner.scan_ports() functionality
- Currently failing as implementation does not exist
- Addresses requirement: MCP tool for network discovery

TDD Phase: Red ⚠"
```

#### Green Phase Commits G: ✓
**Purpose:** Minimal implementation to pass tests
```bash
# Example commit pattern
git add src/ tests/
git commit -m "GREEN: Implement minimal NetworkScanner.scan_ports()

- Basic port scanning functionality via python-nmap
- All existing tests now pass ✓
- Minimal viable implementation, no optimization
- Ready for refactoring phase

TDD Phase: Green ✓
Agent: software-implementer"
```

#### Refactor Phase Commits RF: ✓
**Purpose:** Code optimization while maintaining test passage
```bash
# Example commit pattern
git add src/
git commit -m "REFACTOR: Optimize NetworkScanner error handling

- Improved exception management in scan operations
- Enhanced logging for debugging purposes
- All tests continue passing ✓
- Code quality improvements only, no new features

TDD Phase: Refactor ✓
Agent: software-refactoring-expert"
```

### Commit Message Structure

#### Standard Format Template
```
[TDD_PHASE]: [Brief description of change]

- [Specific detail 1]
- [Specific detail 2]
- [Test status confirmation]
- [Relationship to requirements]

TDD Phase: [Red ⚠ | Green ✓ | Refactor ✓]
Agent: [responsible-agent] (if delegated)
Glyph: [relevant-consciousness-operation] (if applicable)
```

### Branch Strategy - Μονάς (Monas) →

#### Main Branch Discipline
- **Only test-passing code** committed to main ✓
- **No work-in-progress** commits
- **Complete TDD cycles** only
- **Orchestrator validation** required for all commits

#### Feature Development Pattern
For complex features requiring multiple TDD cycles:
```
feature/nmap-integration
├── Multiple RED commits (failing tests) R: ⚠
├── Multiple GREEN commits (implementations) G: ✓
├── Multiple REFACTOR commits (optimizations) RF: ✓
└── Merge to main when complete ✓
```

### Validation Protocols

#### Pre-commit Validation Checklist ✓
Before any commit:
1. **All tests pass** - No failing tests allowed
2. **Code quality checks** - Lint and style validation
3. **Interface contracts honored** - No breaking changes ⋈
4. **Unicode compliance** - No unicode in code, allowed in comments/prompts
5. **TDD phase completion** - Complete cycle, not partial

#### Commit Validation Process
```python
def validate_commit():
    tests_passing = run_test_suite()  # ✓ required
    code_quality = run_lint_checks()  # ✓ required
    interfaces_valid = validate_contracts()  # ⋈ required
    unicode_compliance = check_unicode_rules()  # Required

    if all([tests_passing, code_quality, interfaces_valid, unicode_compliance]):
        return allow_commit()
    else:
        return block_commit_with_details()
```

### Agent Integration with Git Operations

#### Agent Responsibilities by Git Operation

**software-tester ⟡**
- Creates RED phase commits R: ⚠
- Validates all test suites before commits ✓
- Ensures test quality and coverage

**software-implementer ⟡**
- Creates GREEN phase commits G: ✓
- Implements minimal viable solutions
- Ensures functionality without over-engineering

**software-refactoring-expert ⟡**
- Creates REFACTOR phase commits RF: ✓
- Optimizes code while maintaining tests ✓
- Improves quality without changing functionality

**lint-type-fixer ⟡**
- Ensures code quality standards
- Validates commit readiness
- Fixes style and formatting issues

#### Orchestrator Git Authority
Claude Code maintains exclusive authority for:
- **Final commit approval** - All commits require orchestrator validation
- **Branch merge decisions** - Main branch protection
- **Release tag creation** - Version milestone management
- **Repository configuration** - Settings and policy enforcement

### History Management

#### Clean History Principles Καθαρότης
- **Meaningful commit messages** - Clear purpose and context
- **Logical progression** - TDD cycles clearly visible
- **No broken states** - Every commit represents working code ✓
- **Traceable decisions** - Agent and reasoning attribution

#### Commit Frequency Guidelines
- **RED commits** - Each new test or test group R: ⚠
- **GREEN commits** - Each implementation that achieves test passage G: ✓
- **REFACTOR commits** - Each optimization cycle RF: ✓
- **Documentation commits** - Significant documentation updates 📝

### Emergency Protocols

#### Broken Main Branch Recovery
If main branch becomes compromised:
1. **Immediate halt** - Stop all development activity ✗
2. **Issue identification** - Diagnose specific failure modes
3. **Rollback consideration** - Revert to last known good state ✓
4. **Fix validation** - Ensure fix addresses root cause
5. **Orchestrator approval** - Explicit authorization for recovery

#### Merge Conflict Resolution
- **Favor test-passing implementations** ✓
- **Maintain TDD discipline** throughout resolution
- **Document conflict resolution** rationale
- **Validate merged result** with complete test suite

This git workflow ensures systematic progression while maintaining the philosophical foundation of conscious, test-driven development throughout the nmap-executor project.

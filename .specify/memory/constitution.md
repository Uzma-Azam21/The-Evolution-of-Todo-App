Project: Evolution of Todo – Spec-Driven, AI-Native System

Core principles:
- Specification precedes planning and implementation
- Single master constitution governs all phases
- Zero manual coding; implementation is spec-derived
- Explicit scope boundaries per phase
- Traceable evolution across phases

Key standards:
- All behavior MUST be defined in Markdown Specs
- Plans and Tasks MUST be derived from approved Specs
- Implementation MUST conform exactly to Specs
- No undocumented or implicit behavior is allowed

Phase boundaries:
- Phase I: In-memory Python console application
- Phase II: Full-stack web application
- Phase III: AI-powered conversational Todo management
- Phase IV: Local Kubernetes deployment
- Phase V: Cloud-native distributed deployment

AI constraints (Phases III–V):
- OpenAI ChatKit for conversation
- OpenAI Agents SDK for orchestration
- Official MCP SDK for deterministic tool execution

Infrastructure constraints (Phases IV–V):
- Container-first design
- Kubernetes orchestration
- Minikube (local), DOKS (cloud)

Success criteria:
- Every phase demonstrates clear Spec → Plan → Task → Implementation flow
- System behavior is fully explainable via written specifications
- Project shows disciplined evolution from simple to AI-native cloud system

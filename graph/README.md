# 🕸️ Personal Solopreneur Graph

The graph turns the repository into a connected knowledge system.

## Core nodes

```text
Person
Occupation
Skill
Constraint
Vertical
Customer
Problem
Gap
Capability
Business Model
Offer
Technology
Experiment
Customer Result
Revenue
System
Company
```

## Core relationships

```text
Person → HAS_OCCUPATION → Occupation
Person → HAS_SKILL → Skill
Person → HAS_CONSTRAINT → Constraint
Occupation → EXPOSES_TO → Vertical
Vertical → HAS_CUSTOMER → Customer
Customer → EXPERIENCES → Problem
Problem → CREATES → Gap
Gap → REQUIRES → Capability
Capability → ENABLES → Offer
Offer → SERVES → Customer
Offer → USES → Technology
Offer → PRODUCES → Customer Result
Customer Result → PRODUCES → Revenue
Repeated Work → BECOMES → System
System → ENABLES → Company
```

The graph exists so a learner's AI can reason across resources instead of treating every document as a separate lesson.

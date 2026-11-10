# Test strategy

## Scope

Which kinds of tests a project needs, chosen by **what you are building** and **how users interface with it**. For rules on writing any test, see [testing](testing.md).

## Guidelines

### Start with unit and integration tests

Every project, whatever it is, should have unit tests and integration tests. They sit closest to the code, are fastest to run and diagnose, and should be colocated with the code when the language and repository allow. Add other kinds only for what these cannot show.

### Test internal modules as libraries

Code structured as libraries ([architecture](../structure/architecture.md#build-most-code-as-libraries)) is tested like one: unit and integration tests, plus tests of its public interface. This applies to every module, including unpublished ones. The application-level tests then cover only what the application adds: composition, wiring, configuration, and the entry points.

### Choose extra kinds by product and interface

Use the [matrix](#matrix) to pick the additional kinds for what you build and how it is used. Do not add a kind because it exists; add it because a risk needs it.

### Test through the interface users actually use

The top-level tests should drive the same interface real users or callers use (screen, command line, API), so they catch what lower levels cannot: wiring, packaging, and configuration.

### Keep the top thin

Keep higher-level tests few, for critical paths only. The reason and the method are in [test at the lowest level](testing.md#test-at-the-lowest-level-that-gives-confidence).

### Name tests by what they exercise

Projects name test kinds differently. Classify by what a test exercises, not its label. If the repository has its own names, map them to the levels and kinds below and use the repository's names in code.

## Test levels

| Level | Exercises | Also called | Best for | Cost |
| --- | --- | --- | --- | --- |
| **Unit** | One function, type, or small group in isolation; collaborators replaced or absent. | Small test, isolated test | Logic, branches, edge cases, error paths. | Lowest. |
| **Integration** | Several real parts together, or a unit with a real collaborator. | Medium test, slice test, component test (in some orgs) | Persistence, serialization, wiring, configuration, framework behavior. | Moderate. |
| **Service** | One running service through its public interface, with dependencies real, faked, or stubbed. | API test, service-level test, component test (in some orgs), black-box test | A service's contract and behavior without the rest of the system. | Moderate to high. |
| **Contract** | The agreement between a provider and its consumers, checked at the boundary. | Interface test, consumer-driven contract test, compatibility test | Compatibility between separately changing components. | Low to moderate. |
| **End-to-end** | The whole system through its real entry points, as a user or caller would. | E2E, system test, functional test, acceptance test, journey test, large test | A few critical journeys and deployment wiring. | Highest. |

Notes:

- **Service versus end-to-end.** If a service's product is an API, testing that API through its public interface is that product's end-to-end test. Many projects still separate them: service tests cover one service; end-to-end tests span several. Follow the repository's split and name it.
- **"Component test" is ambiguous.** It means a service in isolation in some projects and a group of integrated parts in others. Check what the repository means.

## Matrix

Unit and integration tests apply to every cell and are not repeated. Cells list the additional kinds.

**Interface** is how users reach the product:
- **GUI:** a graphical or web interface.
- **CLI:** a command line.
- **API:** any programmatic interface, such as a network protocol, messages, or a library's public interface.

| Building ↓ / Interface → | GUI | CLI | API |
| --- | --- | --- | --- |
| **Library or package** | n/a | n/a | Contract (public interface stays compatible), property or fuzz (for parsers and algorithms), examples as tests, supported-environment checks |
| **Service or backend** | n/a | Service (run the command; assert output, exit code, side effects) | Service, contract, smoke after deploy |
| **Application or product** | End-to-end on critical journeys; snapshot or golden only for stable output | End-to-end on full command flows; smoke on the packaged build | End-to-end across services; contract at each service boundary |
| **Data pipeline or job** | n/a | End-to-end on sample data; golden output | Contract (schemas); data-quality checks; golden output |
| **Infrastructure or configuration** | n/a | Smoke (applies cleanly) | Smoke; validation or plan checks |

The **library** row applies to every internal module as well as to published packages. The **application** row then covers only the composition layer, which is why its top-level tests can stay few.

Where a product has several interfaces, combine its cells. A library that also ships a CLI follows both rows.

## Cross-cutting kinds

Added by risk, not by cell.

| Kind | Purpose | Also called |
| --- | --- | --- |
| **Regression** | Keep a fixed bug fixed. A purpose, not a level: write it at the lowest level that reproduces the bug. | |
| **Smoke** | Quick check that the system starts and basics work. | Sanity test, build verification test |
| **Property-based or fuzz** | Check invariants over many generated inputs. | Generative test, randomized test |
| **Snapshot or golden** | Compare output, including rendered or visual output, to stored expected output. Use for stable, reviewed output only. | Approval test, characterization test, visual test |
| **Examples as tests** | Run every documented example and check its stated result. | Doctest, documentation test |
| **Supported-environment** | Check it works on each supported runtime, platform, or version. | Compatibility matrix, cross-platform test |
| **Data-quality** | Check data meets expectations: completeness, ranges, uniqueness, referential integrity. | Data validation, expectation test |
| **Validation or plan checks** | Check configuration or infrastructure is valid and shows the expected changes before applying. | Dry run, policy check, lint, plan test |
| **Performance or load** | Check speed, throughput, or resource limits. | Benchmark, stress test, soak test |
| **Security** | Check abuse and failure cases for access, input, and data handling. For high-tier changes. | Penetration test, abuse-case test |
| **Manual or exploratory** | Human verification where automation is impractical or insufficient. | Ad hoc testing |

## Examples

### Library

Building a parsing library whose public interface is a set of functions.

| Kind | What it verifies |
| --- | --- |
| Unit (colocated) | Each function's logic and edge cases, including invalid input. |
| Integration | Real file or stream input, and behavior with real dependencies. |
| Contract | The public interface (names, signatures, documented behavior) has not changed incompatibly. |
| Property or fuzz | Round-trip and no-crash invariants over generated inputs. |
| Examples as tests | Every example in the documentation runs and gives the stated result. |
| Supported-environment checks | It works on each supported runtime or platform version. |

No end-to-end tests are needed. The library has no user journey of its own, and tests of the consuming application cover that.

### Service with an API

| Kind | What it verifies |
| --- | --- |
| Unit | Business rules. |
| Integration | Persistence and message handling with real or faithful dependencies. |
| Service | Requests and responses through the public interface, with other services stubbed. |
| Contract | Response shape against each consumer's expectations. |
| Smoke | After deploy, the service is up and answers basics. |

### Application with a GUI

| Kind | What it verifies |
| --- | --- |
| Unit and integration | Logic, state, and wiring in code. |
| End-to-end | A few critical journeys (sign in, check out) in the real interface. |
| Snapshot or golden | Stable rendered output, where worth the upkeep. |

### Where behaviors are tested

| Behavior | Where |
| --- | --- |
| Discount calculation rules | Unit. |
| Order is saved and read back with the right fields | Integration, with a real or faithful database. |
| Service A's response shape matches what service B parses | Contract. |
| Customer can check out | End-to-end, one critical path. |
| Orders API returns 404 for an unknown order | Service. |
| Bug: leap-day dates rejected | Unit regression, if the bug is in date logic. |

## Exceptions

Throwaway or exploratory code may skip this. Small projects may combine unit and integration tests in one suite when separating them adds cost with no benefit; state the choice. The tests must still cover both.

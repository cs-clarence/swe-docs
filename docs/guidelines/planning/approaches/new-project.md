# New project

## Scope

Starting a system, service, or product with no existing code or users to preserve. Once it exists and is in use, later work follows the small, medium, and large approaches.

## Guidelines

### Settle purpose, users, and success before technology

Write down who it is for, what problem it solves, and how you will know it works. Technology chosen first constrains the answers.

### Test the riskiest assumptions with a prototype

List what must be true for the project to work, and test the shakiest items with throwaway prototypes. Label or discard the prototype so it does not become the product by accident.

### Choose proven tools unless a need says otherwise

Pick well-understood tools and record the choice and the reasons ([decision records](../../core/decision-records.md)). Novelty costs time that does not go into the product.

### Build a thin end-to-end slice first

Get one minimal path working through every layer, including build, test, release, and monitoring, before adding features. It exposes integration problems when they are cheap.

### Set up verification before the features

Put automated checks and a repeatable build in place first, so every later change is verified the same way. Retrofitting them is harder than starting with them.

### Decide early what is costly to change later

Settle the data model, public contracts, and trust boundaries early, and leave cheap choices open. These are the decisions that cannot be revised cheaply.

### Keep the structure as simple as the need

Start with the fewest parts that work and split where clear boundaries emerge. Structure built for needs that do not exist yet is cost with no return.

### Define a small first version

State what is in the first version and what is not. A project with no edge never finishes.

### Write the conventions down early

Record the code style, layout, and workflow conventions while there are few files. Later contributors copy what exists.

## Exceptions

A throwaway prototype or experiment may skip most of these. Mark it as throwaway, and do not build on it.

# Contribution Guidelines

Thanks for helping make this list better. By contributing you agree to follow the [Code of Conduct](code-of-conduct.md).

## What belongs here

Resources that help people **build with Jev**, TypeSafe's System One model:

- Projects, libraries, integrations, and tools that call Jev or the TypeSafe API.
- Tutorials, articles, talks, and videos that teach something concrete.
- Recipes and examples that show a use of Jev that is not already covered.
- Benchmarks and comparisons that publish their method.

What does not belong here:

- General LLM resources that do not involve Jev.
- Marketing pages with no technical content.
- Anything that leaks API keys, private data, or copyrighted material.

## Quality bar

The ecosystem is young, so there is no star minimum. Instead, a resource should:

- Work today with a current Jev model, or say clearly which version it targets.
- Have a README or write-up that explains what it does and how to run it.
- Have had at least one update after its first release, or be a finished article or talk.
- Be in English, or have an English summary.

## How to add something

1. Search the list and the open pull requests to make sure it is not already there.
2. Either [open a suggestion issue](https://github.com/Li-Evan/awesome-jev/issues/new/choose), or edit `README.md` directly and open a pull request.
3. Add **one resource per pull request**, at the bottom of the most fitting section.
4. Use this format:

   ```md
   - [Name](https://link) - Description.
   ```

5. Write the description in your own words:
   - Start with a capital letter and end with a period.
   - Say what it does and why it is useful, not just its name again.
   - Mention the primitive or pattern it uses when that helps (Choice, Score, Noul, fan-out, reranking).
   - Keep numbers you quote identical to the source.
6. Link to the canonical page. For GitHub projects, link the repository, not a mirror.
7. Tag affiliation honestly. If you work on the project, say so in the pull request.

## Updating or removing

If a link is broken, a project is abandoned, or a description is outdated, open an issue or a pull request with a short explanation.

## Pull request checklist

- [ ] One resource per pull request.
- [ ] The link works and points to the canonical page.
- [ ] The description is clear, starts with a capital letter, and ends with a period.
- [ ] I checked that the resource is not already listed.
- [ ] `npx awesome-lint` passes locally, or CI is green.

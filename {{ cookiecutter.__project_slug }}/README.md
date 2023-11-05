# {{ cookiecutter.project_name }}

A Python web application based on Flask and the VITE stack (Vue, Inertia, TailwindCSS and Vite).

## Installation

Clone the repo locally:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_slug }}.git
cd {{ cookiecutter.__project_slug }}
```

Install dependencies:

```bash
poetry install
poetry shell
poe init
```

Run development server:

```bash
poe dev
```

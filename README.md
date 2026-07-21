# Task CLI

A simple command-line task manager written in Python.

Task CLI allows you to create, update, organize, and track tasks directly from your terminal. Tasks are stored locally in a JSON file, making the application lightweight and easy to use without requiring a database or external services.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as **todo**
- Mark tasks as **in-progress**
- Mark tasks as **done**
- List all tasks
- Filter tasks by status
- Persist tasks between executions using a JSON file

## Requirements

- Python 3.10 or newer

## Clone the repository

```bash
git clone https://github.com/<your-username>/task_manager_cli.git
cd task_manager_cli
```

## Install

If using `uv`:

```bash
uv sync
```

or install in editable mode with pip:

```bash
pip install -e .
```

## Running the application

After installation you can use:

```bash
task-cli <command>
```

or

```bash
python -m task_cli <command>
```

## Usage

### Add a task

```bash
task-cli add "Finish Boot.dev project"
```

### Update a task

```bash
task-cli update 1 "Finish README"
```

### Delete a task

```bash
task-cli delete 1
```

### Mark a task as in progress

```bash
task-cli mark-in-progress 2
```

### Mark a task as done

```bash
task-cli mark-done 2
```

### List every task

```bash
task-cli list
```

### List only completed tasks

```bash
task-cli list done
```

### List only tasks in progress

```bash
task-cli list in-progress
```

### List only todo tasks

```bash
task-cli list todo
```

## Project Structure

```
task_manager_cli/
├── task_cli/
│   ├── __main__.py
│   ├── task_manager.py
│   └── __init__.py
├── pyproject.toml
├── README.md
└── LICENSE
```

## Data Storage

Tasks are automatically stored in a local file named:

```
task_objects.json
```

Each task contains:

- Unique ID
- Description
- Status
- Creation timestamp
- Last updated timestamp

## Technologies Used

- Python 3
- argparse
- JSON
- Object-Oriented Programming
- Standard Library

## License

This project is licensed under the MIT License.

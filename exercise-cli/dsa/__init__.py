#!/usr/bin/env python3
"""DSA Exercises CLI - Manage data structures and algorithms exercises."""
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

EXERCISES = [
    # Arrays & Strings
    ("packet_parser", "Arrays & Strings", "Easy", "Parse network packet headers"),
    ("url_encoder", "Arrays & Strings", "Medium", "URL encode/decode strings"),
    # Linked Lists
    ("network_flow", "Linked Lists", "Medium", "Flow tracking using linked list"),
    ("lru_cache_ll", "Linked Lists", "Medium-Hard", "LRU cache using doubly linked list"),
    # Stacks & Queues
    ("request_queue", "Stacks & Queues", "Easy-Medium", "Network request queuing"),
    ("bracket_validator", "Stacks & Queues", "Medium", "Validate nested network configs"),
    # Hash Tables
    ("dns_cache", "Hash Tables", "Medium", "DNS caching with TTL"),
    ("ip_classifier", "Hash Tables", "Medium", "IP address classification"),
    ("rate_limiter", "Hash Tables", "Medium-Hard", "Token bucket rate limiter"),
    # Trees
    ("network_topology", "Trees", "Medium", "Tree-based network representation"),
    ("spanning_tree", "Trees", "Hard", "Minimum spanning tree"),
    # Graphs
    ("network_router", "Graphs", "Medium-Hard", "Shortest path routing"),
    ("network_flow_graph", "Graphs", "Hard", "Max flow problem"),
    # Heaps
    ("packet_scheduler", "Heaps", "Medium", "Priority-based packet scheduling"),
    # Recursion & DP
    ("path_finder", "Recursion & DP", "Medium", "Network path backtracking"),
    ("network_optimization", "Recursion & DP", "Hard", "DP for bandwidth allocation"),
    # Sorting & Searching
    ("log_analyzer", "Sorting & Searching", "Medium", "Binary search in time-series logs"),
    # General DSA - Arrays & Strings
    ("valid_palindrome", "Arrays & Strings", "Easy", "Check if string is palindrome"),
    ("best_time_buy_sell", "Arrays & Strings", "Easy", "Best time to buy/sell stock"),
    ("remove_duplicates", "Arrays & Strings", "Easy", "Remove duplicates from sorted array"),
    # General DSA - Hash Maps & Sets
    ("two_sum", "Hash Maps & Sets", "Easy", "Find two numbers that sum to target"),
    ("contains_duplicate", "Hash Maps & Sets", "Easy", "Check if array contains duplicates"),
    ("group_anagrams", "Hash Maps & Sets", "Medium", "Group strings that are anagrams"),
    ("top_k_frequent", "Hash Maps & Sets", "Medium", "Find k most frequent elements"),
    ("longest_consecutive", "Hash Maps & Sets", "Medium", "Longest consecutive sequence"),
    # General DSA - Sorting & Searching
    ("find_first_last", "Sorting & Searching", "Medium", "Find first/last position in sorted array"),
    ("merge_intervals", "Sorting & Searching", "Medium", "Merge overlapping intervals"),
    ("product_except_self", "Sorting & Searching", "Medium", "Product of array except self"),
    ("maximum_subarray", "Sorting & Searching", "Medium", "Maximum subarray sum"),
]

def get_exercises_dir() -> Path:
    """Get the exercises directory."""
    return Path(__file__).parent.parent.parent / "exercises"

def get_solutions_dir() -> Path:
    return Path(__file__).parent.parent.parent / "solutions"

def get_hints_dir() -> Path:
    return Path(__file__).parent.parent.parent / "hints"

def find_exercise_dir(exercise_name: str) -> Path | None:
    """Find exercise directory in any subdirectory."""
    exercises_dir = get_exercises_dir()
    
    # Check direct path first
    direct_path = exercises_dir / exercise_name
    if direct_path.exists():
        return direct_path
    
    # Search in subdirectories
    for topic_dir in exercises_dir.iterdir():
        if topic_dir.is_dir():
            exercise_path = topic_dir / exercise_name
            if exercise_path.exists():
                return exercise_path
    
    return None

def is_completed(exercise_name: str) -> bool:
    """Check if an exercise is completed."""
    exercise_dir = find_exercise_dir(exercise_name)
    if exercise_dir is None:
        return False
    main_file = exercise_dir / "main.py"
    if not main_file.exists():
        return False
    content = main_file.read_text()
    return "TODO" not in content

@click.group()
def cli():
    """DSA Exercises - Practice for Meta Network Production Engineer interviews."""
    pass

@cli.command()
def list():
    """List all exercises with their completion status."""
    table = Table(title="DSA Exercises", show_header=True, header_style="bold cyan")
    table.add_column("#", style="dim", width=3)
    table.add_column("Exercise", style="bold white")
    table.add_column("Topic", style="cyan")
    table.add_column("Difficulty", style="yellow")
    table.add_column("Description", style="green")
    table.add_column("Status", width=6)

    for i, (name, topic, difficulty, description) in enumerate(EXERCISES, 1):
        completed = is_completed(name)
        status = "[green]✓[/green]" if completed else "[dim]○[/dim]"
        table.add_row(str(i), name, topic, difficulty, description, status)

    console.print(table)
    console.print("\n[green]✓[/green] = Completed  [dim]○[/dim] = Not started\n")

@cli.command()
@click.argument("exercise")
def start(exercise: str):
    """Start working on an exercise."""
    exercise_dir = find_exercise_dir(exercise)
    
    if exercise_dir is None:
        console.print(f"[red]Error: Exercise '{exercise}' not found![/red]")
        list()
        return
    
    readme_file = exercise_dir / "README.md"

    console.print(Panel(f"[bold green]Starting Exercise: {exercise}[/bold green]"))
    
    if readme_file.exists():
        console.print(f"\n[bold cyan]Instructions:[/bold cyan]")
        console.print(readme_file.read_text())
    else:
        console.print(f"[yellow]No README.md found for {exercise}[/yellow]")

@cli.command()
@click.argument("exercise")
@click.option("--level", type=click.IntRange(1, 3), default=1, help="Hint level (1-3)")
def hint(exercise: str, level: int):
    """Show hints for an exercise."""
    hints_file = get_hints_dir() / f"{exercise}.txt"

    if not hints_file.exists():
        console.print(f"[yellow]No hints available for '{exercise}'[/yellow]")
        return

    content = hints_file.read_text()
    hint_levels = content.split("=== HINT LEVEL ===")
    
    if level > len(hint_levels) - 1:
        console.print(f"[yellow]Only {len(hint_levels) - 1} hint levels available[/yellow]")
        return

    hint_text = hint_levels[level].strip()
    console.print(Panel(f"[bold cyan]Hint Level {level}[/bold cyan]\n\n{hint_text}"))

@cli.command()
@click.argument("exercise")
def test(exercise: str):
    """Run tests for an exercise."""
    import subprocess
    import sys

    exercise_dir = find_exercise_dir(exercise)
    
    if exercise_dir is None:
        console.print(f"[red]Error: Exercise '{exercise}' not found![/red]")
        return
    
    test_file = exercise_dir / "test_main.py"

    if not test_file.exists():
        console.print(f"[yellow]No test file found for '{exercise}'[/yellow]")
        return

    console.print(f"[bold cyan]Running tests for {exercise}...[/bold cyan]\n")
    
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=short"],
        cwd=str(exercise_dir),
        capture_output=False,
    )

    if result.returncode == 0:
        console.print(f"\n[bold green]✓ All tests passed![/bold green]")
    else:
        console.print(f"\n[red]✗ Some tests failed[/red]")

@cli.command()
@click.argument("exercise")
def solution(exercise: str):
    """Show the reference solution for an exercise."""
    solutions = {
        "packet_parser": "packet_parser.py",
        "url_encoder": "url_encoder.py",
        "network_flow": "network_flow.py",
        "lru_cache_ll": "lru_cache_ll.py",
        "request_queue": "request_queue.py",
        "bracket_validator": "bracket_validator.py",
        "dns_cache": "dns_cache.py",
        "ip_classifier": "ip_classifier.py",
        "rate_limiter": "rate_limiter.py",
        "network_topology": "network_topology.py",
        "spanning_tree": "spanning_tree.py",
        "network_router": "network_router.py",
        "network_flow_graph": "network_flow_graph.py",
        "packet_scheduler": "packet_scheduler.py",
        "path_finder": "path_finder.py",
        "network_optimization": "network_optimization.py",
        "log_analyzer": "log_analyzer.py",
    }

    solution_file = get_solutions_dir() / solutions.get(exercise, f"{exercise}.py")

    if not solution_file.exists():
        console.print(f"[yellow]No solution found for '{exercise}'[/yellow]")
        return

    console.print(Panel(f"[bold cyan]Reference Solution: {exercise}[/bold cyan]"))
    console.print(solution_file.read_text())

@cli.command()
@click.argument("exercise")
@click.option("--force", is_flag=True, help="Force reset without confirmation")
def reset(exercise: str, force: bool):
    """Reset an exercise to its initial state."""
    import shutil

    exercise_dir = get_exercises_dir() / exercise

    if not exercise_dir.exists():
        console.print(f"[red]Error: Exercise '{exercise}' not found![/red]")
        return

    if not force:
        if not click.confirm(f"Are you sure you want to reset '{exercise}'? This will delete all your changes."):
            console.print("[yellow]Reset cancelled[/yellow]")
            return

    console.print(f"[yellow]Warning: Reset functionality coming soon. For now, manually restore from backups.[/yellow]")

if __name__ == "__main__":
    cli()
